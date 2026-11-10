# Workload Security

Kubernetes constrains what a pod may request through [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-admission/), applied per namespace with the `pod-security.kubernetes.io/enforce` label. On Rahti, this label is set to restricted for all user workloads. Containers must run as non-root, drop all Linux capabilities except `NET_BIND_SERVICE`, disallow privilege escalation, use an allowed seccomp profile, and avoid host namespaces. Pods that violate these rules are rejected at admission time rather than failing later at runtime. In OKD, other mechanisms are implemented to harden the platform further. See below section.

## What SecurityContextConstraints are

SecurityContextConstraints (SCC) are a mechanism implemented in OKD to control the permissions a pod can request at runtime. An SCC acts as an admission-level policy: when a pod is created, OKD checks it against the SCCs available to the requesting user or service account, and either rejects the pod or admits it after applying defaults from the matching SCC.

An SCC governs things such as:

* whether a container may run as privileged
* which user and group IDs the container may run as
* which Linux capabilities may be requested or are dropped
* whether privilege escalation is allowed
* which volume types may be mounted
* access to host resources (host network, host ports, host PID/IPC namespaces, host paths)
* the SELinux context and the seccomp profile applied to the pod

### SCCs in Rahti

Rahti sets restrictive policies for the workloads its users run and does not grant permissive SCCs by default, because Rahti is a multi-tenant container platform.

The SCC available to Rahti users is `rahti-restricted-v2`. Under this policy:

* Containers cannot run as privileged.
* Containers must run with a UID allocated from the project’s assigned UID range; running as root (UID 0) is not permitted.
* An SELinux context and an fsGroup are assigned automatically from the project’s ranges.
* All Linux capabilities are dropped; only `NET_BIND_SERVICE` may be added back.
* Privilege escalation is disabled by default (`allowPrivilegeEscalation: false`).
* Host namespaces, host networking and host ports are not available.

In addition to the above, `rahti-restricted-v2` sets the default seccomp profile for user workloads to `{"type": "Localhost", "localhostProfile": "rahti-custom-seccomp.json"}`.

### What seccomp is and what to set

Seccomp (secure computing mode) is a Linux kernel feature that restricts which system calls a process is allowed to make. A seccomp profile is a list of syscall rules.

Workloads in Rahti may explicitly set the seccomp profile so that it matches the one required by `rahti-restricted-v2`. This applies to all workload controllers that create pods, such as Deployment, StatefulSet, Job and CronJob. As a Rahti user, you either leave it unset and let the SCC apply the default, or set it to exactly the following value for `kind: Deployment, StatefulSet, Job, CronJob, etc.`.

The profile is ultimately set in the pod or container specifications in `securityContext`:

```yaml
securityContext:
  seccompProfile:
    type: Localhost
    localhostProfile: rahti-custom-seccomp.json
```
