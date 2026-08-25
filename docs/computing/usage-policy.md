# Usage policy

!!! info "Additional information"
    [General Terms of Use for CSC's Services for Research and
    Education](https://research.csc.fi/general-terms-of-use)

## Login nodes

When you login to the CSC supercomputer, you end up on one of the login nodes of
the cluster. These login nodes are shared by all users and they are **not**
intended for heavy computing.

The login nodes should be used only for:

* code editing and code compilation
* managing batch jobs
* moving data
* light pre- and postprocessing

Here **light** means **one-core jobs** that finish in **minutes** and require
**less than 1 GiB** of memory at maximum. All other tasks are to be done in
compute nodes either as normal [batch jobs](running/getting-started.md) or as
[interactive batch jobs](running/interactive-usage.md). Programs not adhering
to these rules will be terminated without warning.

!!! warning "Important"
    The login nodes are not meant for long or heavy processes.

## Agentic AI tools on Roihu

Agentic AI tools, such as Claude Code, OpenAI Codex and OpenCode, are
LLM-based assistants that can autonomously run commands, edit files and
submit jobs on your behalf. They are typically used for tasks like coding
assistance or managing Slurm jobs. AI agents should be used
carefully, as they can introduce security risks and performance problems
for all Roihu users, including yourself.

!!! warning "Responsibility for running AI agents"
    You are always responsible for the actions of your AI agents. Any
    command run by your agent is executed under your personal user account,
    and you are bound by the
    [General Terms of Use](https://research.csc.fi/general-terms-of-use)
    regardless of whether you or your agent typed the command.
    

Key rules for using AI agent tools on Roihu:

1. *Use up-to-date [csc-skills](https://github.com/CSCfi/csc-skills).*
   These skills provide guidance for the tools on how to use the system
   without causing disruptions, and help with the other points in this list.

2. *Control the agent's access to files on the system.* Do not give the
   agent access to files that contain your secrets, or any other
   information that you do not want to provide to it. Typical examples are
   your SSH keys in `~/.ssh` and Allas credentials in
   [`rclone.conf`](../data/Allas/using_allas/rclone.md). A good method is to run
   the agentic tool in an [Apptainer container](containers/overview.md),
   only bind mounting what you need on the system (e.g. your scratch
   directory). CSC is preparing a supported container for this use case.
   One can also use the sandboxing features of the tools, but not all
   methods are supported on Roihu. See for example
   [Claude Code sandbox environments](https://code.claude.com/docs/en/sandbox-environments).

3. *Control the agent's access to tools on the system.* Be mindful of
   what tools you allow the agent to execute without confirmation. The
   more isolated the sandbox, the more permissive you can afford to be
   with auto-approved tools. See the tool documentation on how to
   configure this, for example
   [Claude Code permissions](https://code.claude.com/docs/en/permissions)
   and [Codex sandbox and approval policies](https://learn.chatgpt.com/docs/sandboxing).

4. *Prefer running the agent on your own computer.* If possible, run
   the tool on your own laptop or workstation and not on the
   supercomputer. The agent can then run commands and manage jobs
   through the [FirecREST API](firecrest/index.md). Keep the FirecREST
   token in an environment variable (e.g. `FIRECREST_TOKEN`), let the
   agent refer to it by name only, never paste it into a prompt and do
   not let the agent print it. CSC is preparing a FirecREST MCP server
   that keeps the token outside the agent's reach. Roihu can also be
   accessed over [SSH](connecting/index.md).


5. *Do not overload the login node!* As an exception to the login node
   rules above, running the interactive session of an agent on a login
   node is allowed, provided that you supervise it and that the agent
   itself only does light work.  All heavy computation must be
   submitted as normal [batch jobs](running/getting-started.md) or
   [interactive batch jobs](running/interactive-usage.md).

6. *Do not overload Lustre and Slurm!* If you run the agent on Roihu, instruct
   it that `home`, `projappl` and `scratch` are on a
   [Lustre filesystem](roihu-disk.md) and that it should use the
   [local disk under `$TMPDIR`](roihu-disk.md#temporary-local-disk-areas)
   for temporary files. Avoid excessive amounts of Slurm jobs and heavy
   tool calling: no tight polling loops of `squeue` or `sacct`, no
   recursive `find` or `grep` over large directories on Lustre, and no
   bursts of test jobs. 

7. *Never give your CSC credentials to an agent running on a third-party
   service.* Do not give your CSC password, SSH keys or FirecREST tokens
   to an agent hosted on a system that you do not control, such as a
   web-based chatbot with tool calling or a cloud-based AI-assisted IDE.
   Under the
   [General Terms of Use](https://research.csc.fi/general-terms-of-use)
   you agree not to share your credentials or leave them for others to
   see, and this includes handing them to a service you do not control.
   It is permitted to run an agent on your own computer where your SSH
   keys are stored.

8. *Do not open Roihu to an agent running on a third-party service.* Do
   not start an MCP server, a reverse tunnel or a similar service on Roihu
   that lets an agent running on a system you do not control execute
   commands on Roihu. This gives that service the same access to your
   account as sharing your credentials would.
   

9. *Do not expose other users' data to the agent.* On a shared system
   you can see information about other users that is not yours to pass
   on: their user names, jobs and processes on login nodes. Everything
   the agent reads may be sent to an external LLM provider, so
   restrict the agent to your own data. For example, always list only
   your own jobs (`squeue --me`) and processes (`ps -u $USER`), and do
   not let the agent run commands like `squeue`, `sacct -a`, `who`,
   `top` or `ps aux` without restriction.

For a more extensive list of common problems with AI agents and how to
avoid them, see the
[LUMI AI agent guide](https://docs.lumi-supercomputer.eu/development/ai-tools/ai-agent-guide/#common-problems-with-ai-agents-and-how-to-avoid-them).
The same principles apply on Roihu.

## Disk cleaning

Each project has disk space in the directory `/scratch/<project>`. This fast
parallel scratch space is intended for data that is in active use. To ensure
that the parallel disk system does not run out of storage space and to keep
performance acceptable,
[CSC automatically removes files in Puhti scratch](../support/tutorials/clean-up-data.md#automatic-removal-of-files)
that have not been accessed in a long time. The performance of a parallel file
system starts to degrade when it fills up, and the more it fills up, the slower
the performance will get.

This cleaning will happen regularly, and each time users are informed at least
1 month in advance. CSC also provides lists of files that are about to be
removed and instructions for how one can transfer important files to more
suitable disk systems.

**The cleaning is stricter for projects with larger quotas**:

* For projects that have a **scratch quota of 5 TiB or more**, files that have
  not been accessed (opened, read, modified) in the last **90 days** will be
  deleted.
* For other projects with **smaller scratch quotas**, files that have not been
  accessed (opened, read, modified) in the last **180 days** will be deleted.

You can use the `csc-workspaces` command to see which cleaning cycle your
projects are subject to.

**Mahti:** A similar procedure will be introduced on Mahti if the disk usage
grows enough to warrant it. The policy is still that users should keep only
actively used data in scratch.

## GPU nodes

Puhti and Mahti GPUs should only be used for workloads that greatly benefit
from GPU capacity compared to using CPUs or which can't be run on CPUs. In
particular AI/ML workloads are prioritized, since many of them cannot be done
at all on CPUs. A good rule of thumb is to compare the
[Billing Unit (BU)](../accounts/billing.md) usage (_e.g._ with
[`seff`](./performance.md#quick-start-efficiency-report-with-seff) or the
[Billing Unit calculator](https://research.csc.fi/resources/#buc))
of the job on GPUs against CPUs and select the one using less. One CPU BU and one 
GPU BU are equal in terms of cost.

For Puhti and Mahti, this means that a full node of CPU cores roughly equals
one GPU. However, since Puhti and Mahti have more CPU capacity than GPU, you
might get access to CPUs with less queuing. Note that
[LUMI has a lot of GPU capacity](https://docs.lumi-supercomputer.eu/hardware/lumig/)
which is also "cheaper" as measured in BUs, and on LUMI it's better to use GPUs
if possible for your research. In any case, always make sure you use resources
efficiently.

## Conda installations

Due to performance issues of Conda-based environments on parallel file systems,
CSC has deprecated the _direct_ usage of Conda installations. This means that
any Conda environments you intend to use must be installed within a container.
See [Conda best practices](../support/tutorials/conda.md) for more information.

!!! info "Tykky"
    Please consider the [Tykky container wrapper](containers/tykky.md) for easy
    containerization of Conda and pip environments.

## Running out of Billing Units

When a project runs out of Billing Units, the ability to use
the service will be limited in three phases.  If you are still
actively using the project you can lift the limitations by
[applying](../accounts/how-to-apply-for-billing-units.md) for more
Billing Units.

In the first phase the ability to submit new jobs is limited:

* If you run out of Storage BUs, no new jobs can be submitted to any
partition 
* If you run out of CPU BUs, no new jobs can be submitted to CPU partitions
* If you run out of GPU BUs, no new jobs can be submitted to GPU partitions

In other words, running out of CPU or GPU BUs only affects the
corresponding partition type, while Storage BUs affect all. Jobs that
are running are not interrupted and will run until completion/timeout.


In the second step data access is limited. When you run out of storage
BUs a 30-day grace period starts, after which access to `/projappl`
and `/scratch` folders is disabled. No data is deleted, it is only
access that is disabled. Data will, however, still be removed from
`/scratch` during the [normal cleaning process](#disk-cleaning). Note that
having negative balance for CPU or GPU BUs does not trigger this step,
only a negative Storage BU balance.


If you are not using a project actively we encourage you to migrate any data
that you still need within the 30-day grace period and then
[close the project](../accounts/how-to-manage-your-project.md#project-closure)
in MyCSC. 

In the third phase the project is closed after a 60-day grace period
if you have run out of BUs of any type. If the project still has a
negative amount of Billing Units of any type after 60 days, it will be
closed.



## Slurm job management by CSC

* CSC will not change job parameters like length or priority. 
* CSC can terminate jobs if they are misusing resources. E.g., if resources
  (CPU cores, GPUs, memory) are severely underutilized or IO is overloading
  the storage system.
