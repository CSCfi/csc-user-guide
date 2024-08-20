# How can I change which project is billed for my usage?

This depends on which CSC service you are using. In each service, you start by
selecting the project first.

* In supercomputer batch jobs, you specify the billing project in the batch job
  script. There is a separate documentation for
  [**Puhti**](../../computing/running/creating-job-scripts-puhti.md) and
  [**Mahti**](../../computing/running/creating-job-scripts-mahti.md).
* In **Allas**, the project to use is specified using the
  [`allas-conf` command](../../data/Allas/accessing_allas.md).
* In **cPouta** or **ePouta**, you
  [select the project from the dropdown menu of the OpenStack Horizon UI](../../cloud/pouta/launch-vm-from-web-gui.md#preparatory-steps).
* In **Rahti**,
  [OpenShift projects are mapped to CSC projects using the *Description* field](../../cloud/rahti2/usage/projects_and_quota.md)
  of the OpenShift project.
