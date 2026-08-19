# AI Tools

some preamble

## Agent environment

A containerized coding agent is provided on Roihu. Containerization gives more control over what the agent can access, which makes its use more secure. Currently the environment includes the open-source terminal-based [OpenCode agent](https://opencode.ai/), [Claude Code](https://claude.com/product/claude-code), and [Codex](https://openai.com/codex/). 

All users must follow the [CSC AI Agent Policy](WIP). In addition, you must understand the following:

!!! warning "Responsibility"
    The user is **always** responsible for the actions of the agent, and every command run by your agent is executed under your personal account.

!!! warning "Data privacy"
    By default, OpenCode is configured with the model provider OpenCode Zen, which is hosted by [Anomaly Innovations](https://anoma.ly/), who maintain OpenCode. They provide a certain amount of use for free, but all of the data you enter or is read by the agent will be sent to Anomaly Innovations.

- **Security**: The agent has access to the directory you launch it from, all of its subdirectories, and certain hidden subdirectories in your $HOME. $HOME itself is not accessible by default.
- **Tool use**: By default, the agent has permission to use many read-only tools without permission, but asks for permission for any write-operations.
- **Experimental status**: The agent environment is still experimental and rapid changes are possible.

### How to use

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

We recommend you use models hosted on [Aitta](https://aitta.csc.fi), a CSC service. Unfortunately, currently only users with a Lumi project are able to use Aitta. We are working on getting access for everyone with a Roihu project.

Aitta is included in the default configuration. You just need to get your API key from [Aitta](https://aitta.csc.fi) from the 'Generate token' button, and save it to the $AITTA_KEY env variable before you start the agent.
```bash
export AITTA_KEY=<YOUR_KEY_HERE>
```
It is easiest to add this line to your `~/.bashrc ` to avoid setting it every login.

If you want to use a different model provider, change tool permissions, or add MCP servers, you can add your configuration to `~/.config/opencode/opencode.json`, or add a `opencode.json` with the configuration to your project directory. You can find instructions for custom configurations in the [OpenCode documentation](https://opencode.ai/docs/config/).

## MCP servers

Model Context Protocol (MCP) is a standardized way for AI agents to access a large variety of tools. It is hosted by the Linux Foundation. See the [MCP documentation](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) for a general introduction.

The MCP servers in the default environment are one to run Slurm commands, and CSC-docs for providing the agent access to the CSC User Guide. You are free to add more.

### Slurm

The Slurm MCP provides a controlled way for the agent to access Slurm commands, as the agent has no access to Slurm commands without the MCP. Results are cached, so the agent cannot stressing the Slurm database by repeated and redundant calls.

The MCP provides the following tools, listed with the underlying command each one runs. By default the agent can call the read-only tools without asking, while `launchJobs` and `cancelJobs` require your permission each time.

| Tool | Command | Needs permission |
| --- | --- | --- |
| my_jobs | `squeue --me` | No |
| job_history | `sacct` | No |
| sinfo | `sinfo` | No |
| batch_script | `scontrol write batch_script` or `sacct -B` | No |
| slurm_config | `scontrol show config` | No |
| reservations | `scontrol show reservations` | No |
| launch_job | `sbatch` | Yes |
| cancel_job | `scancel` | Yes |

### CSC-docs

The agents come preconfigured with the CSC-docs MCP server. You can read more about it in the [Docs MCP](docs-mcp.md) page. You can also add the CSC-docs MCP to any local client you are using.

## Skills

Agent skills are an token-efficient way to give agents more context. They are markdown files, which the agent reads only when necessary. They can provide the agent with workflows to follow, additional context, or ready scripts for the agent to run. You can read more about agent skills in the [Agent Skills Documentation](https://agentskills.io/home). 

The Roihu agent environment contains three skills by default: Job efficiency, Software environments, and Slurm scripts. You can read more about them below.

### Job efficiency

Enables the agent to get job efficiency metrics. It gives the agent a script to run to fetch the metrics for a given job ID. Instructs the agent to figure out what job is meant if not explicitly stated by the user.

### Software environments

Helps with installing or using software on Roihu. It guides the agent on how to check if the software exists. If the software isn't preinstalled, the skill gives the agent the different methods of installation on Roihu, and tells it to the correct documentation using the CSC-docs MCP.

### Batch scripts

Helps with batch/Slurm script creation, debugging, and optimization. Guides the agent in what things to ask from the user, choosing a partition, and what to do in certain special cases (eg. I/O intensive tasks, MPI based jobs).