# FirecREST HPC API

The FirecREST HPC API provides a standardized RESTful HTTP interface for accessing computing resources on Roihu. It offers APIs for managing jobs through Slurm scheduler, performing file system operations over personal and project data, and for transferring large amounts of data to or from the system.

It is an ideal solution for building automated access to computing resources, as well as for creating and running personal web-based client applications that consume computing resources.

## How to get access to the API?

All Roihu users can use the FirecREST HPC API using time-limited personal access tokens. This effectively allows using the REST API as an alternative to a direct SSH connection, as all API operations are executed on Roihu using your CSC identity and privileges. Personal access tokens can be generated at `TODO: MyCSC token interface link`.

In order to use the REST API for building more serious integrations, such as CI pipelines or building web applications, you can request for a [machine-to-machine robot account](../../accounts/how-to-create-new-user-account.md#getting-a-machine-to-machine-robot-account) to be created for your project.

!!! info "About robot accounts"
    Robot accounts are tied to a specific project. They have access to the same computing resources, and consume your project's resource allocations, as any regular project member would.

    FirecREST HPC API does not impose any additional restrictions for robot account. It can schedule any Slurm job, or perform any data transfer or file system operation within the scope of your project.

    If a robot account is used to provide a HPC backend for a web application intended for humans, please be mindful of having sufficient guardrails, input validation and user authorization in the application itself to prevent unauthorized workloads or commands being run under your project's privileges.

## Getting started

Check out the following documentation to get started with FirecREST HPC API on Roihu:

1. [Connect to FirecREST HPC API](connecting.md)
2. [FirecREST API documentation](https://api.roihu.csc.fi/v1/docs/)
3. [Transfer data with FirecREST](data-transfer-s3.md)
4. [Set up PyFirecREST](pyfirecrest.md) for use with Python applications
