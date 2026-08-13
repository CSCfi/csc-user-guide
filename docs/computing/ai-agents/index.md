# AI Agent infrastructure

some preamble

## Agent environment

A containerized coding agent is provided on Roihu. Containerization gives more control over what the agent can access. which makes its use more secure. Currently the environment includes the open-source teminal-based [OpenCode agent](https://opencode.ai/).

!!! warning "Responsibility"
    The user is **always** responsible for the actions of the agent, and every command run by your agent is executed under your personal account.


### Must read

- **Data privacy**: By default, OpenCode is configured with the model provider OpenCode Zen, which is hosted by [Anomaly Innovations](https://anoma.ly/), who maintain OpenCode. They provide a certain amount of use for free, but all of the data you enter or is read by the agent will be sent to Anomaly Innovations. We recommend you use models hosted on [Aitta, a CSC service](https://aitta.csc.fi). Currently users with a Lumi project are able to use Aitta, but we are working on getting access for everyone with a Roihu project. See [Configuring the Agent](#configuring-the-agent) on how to use Aitta. You can also use whatever other endpoint you have access to.
- **Security**: The agent has access to the directory you launch it from, all of its subdirectories, and certain subdirectories in your $HOME. $HOME itself is not accessible by default.
- **Tool use**: By default, the agent has permission to use many read-only tools without permission, but asks for permission for any write-operations.
- **Experimental status**: The agent environment is still experimental and rapid changes are possible.

### How to use

Make sure you understand the Must read section before using OpenCode.

To use OpenCode in your project directory, navigate to the directory and run the following commands:

```bash
module load opencode

opencode
```

You can add directories to the environment by adding them to the `AGENT_BIND_PATHS` environment variable before launching OpenCode:
```bash
# Bind mount additional directories (optional)
export AGENT_BIND_PATHS=/path/to/dir1,/path/to/dir2
```

### Configuring the Agent

If you want to change tool permissions, add MCP servers, or add a model provider, you can add your configuration to `~/.config/opencode/opencode.json`, or the `opencode.json` to your project directory. You can find instructions for custom configurations in the [OpenCode documentation](https://opencode.ai/docs/config/).

Aitta is included in the default configuration. You need to get your API key from [here](https://aitta-auth.csc.fi/myToken), and save it to the $AITTA_KEY env variable before you start the agent.
```bash
export AITTA_KEY=<YOUR_KEY_HERE>
```
It is easiest to add this line to your `~/.bashrc ` to avoid setting it every login.

## MCP servers

The MCP servers in the default enviroment are one to run Slurm commands, and CSC-docs for providing the agent access to the CSC User Guide.

### Slurm

The Slurm MCP provides a controlled way for the agent to access Slurm commands, as the agent has no access to Slurm commands without the MCP. Results are cached, so the agent cannot stressing the Slurm database by repeated and redundant calls.

MCP provides the following tools - listed with which underlying command it runs:

- MyJobs - "squeue --me"
- JobHistory - "sacct"
- Sinfo - "sinfo"
- BatchScript - "scontrol write batch_script JOBID -" or "sacct -B -j JOBID"
- slurm-config - "scontrol show config"
- reservations - "scontrol show reservations"
- launchJobs - "sbatch"
- cancelJobs - "scancel"

The default configuration allows the agent to call all except launchJobs and cancelJobs without authorization, the latter two require permission from the user each time.

### CSC-docs

The MCP gives the agent ability to search the CSC User Guide semantically, which allows the agent to effectively find information even with non-exact search terms. The AGENTS.MD included in the environment instructs the agent to use this MCP as an authoritative source. 

The MCP also keeps the documentation up-to-date automatically.

## Skills

### Job efficiency

### Software environments

### Slurm scripts