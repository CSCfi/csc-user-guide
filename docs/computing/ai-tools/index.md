# AI tools

CSC provides tools for working with AI agents in an HPC environment. This page
describes the containerized agent environment on Roihu, together with the MCP servers
and skills included in it. The CSC-docs MCP server is not limited to Roihu: you can
add it to an AI client running on your own computer as well.

These tools are meant for HPC-specific work such as managing and debugging Slurm
jobs, writing batch scripts, and setting up software environments. General code
development is **not** an intended use case.

## Agent environment

A containerized environment that hosts coding agents is provided on Roihu.
Containerization limits what files the agent can access, and the virtual filesystem
lowers the I/O load the agent can cause on Lustre. Currently the environment includes
the open-source [OpenCode agent](https://opencode.ai/) and [Claude Code](https://claude.com/product/claude-code).

All users must follow the TODO: [CSC AI Agent Policy](WIP). In addition, you must
understand the following:

!!! warning "Responsibility"
    You are **always** responsible for the actions of the agent, and every
    command run by your agent is executed under your personal account.

!!! warning "Data privacy"
    By default, OpenCode is configured with the model provider OpenCode Zen, which
    is hosted by [Anomaly Innovations](https://anoma.ly/), who maintain OpenCode.
    They provide a certain amount of use for free, but everything you type or
    the agent reads is sent to Anomaly Innovations and used according to their
    terms of service.

    Claude Code sends your prompts and the files the agent reads to [Anthropic](https://www.anthropic.com/).
    How that data is retained, and whether it may be used for model training, depends
    on the terms of the account you sign in with. CSC does not provide the endpoint
    and cannot determine this for you, so check the terms that apply to your own
    subscription before using Claude Code with confidential material.

TODO: List directories in a smart way. Link to public repo?
- **Security**: The agent has access to the directory you launch it from, all of its
subdirectories, and certain hidden subdirectories in your `$HOME`. `$HOME` itself is
not accessible by default.
TODO: Link to repo for tool permissions?
- **Tool use**: By default, the agent can use many read-only tools
without permission, but asks for confirmation for any write operations.
- **Experimental status**: The agent environment is still experimental and may
change without notice.

### How to use

To use OpenCode or Claude in your project directory, navigate to the directory and run the
following commands:

TODO: Update to real commands
```bash
module load roihu-agent-env

opencode
# or
claude
```

You can make additional directories visible in the environment by adding them to the
`AGENT_BIND_PATHS` environment variable before launching the agents:

```bash
export AGENT_BIND_PATHS=/path/to/dir1,/path/to/dir2
```

### How to configure the agents

#### OpenCode
We recommend you use models hosted on [Aitta](https://aitta.csc.fi), a CSC service.

!!! info
    Only users with a LUMI project are able to access Aitta. We are working on
    providing access to everyone with a Roihu project.

Aitta is included in the default OpenCode configuration. You just need to get your API key
from [Aitta](https://aitta.csc.fi) from the *Generate token* button, and save it to
the `$AITTA_KEY` environment variable before you start the agent.
```bash
export AITTA_KEY=<YOUR_KEY_HERE>
```
It is easiest to add this line to your `~/.bashrc` so you don't have to set it
every login.

If you want to use a different model provider, change tool permissions, or add MCP
servers, you can add your configuration to `~/.config/opencode/opencode.json`, or
add an `opencode.json` with the configuration to your project directory. You can find
instructions for custom configurations in the [OpenCode documentation](https://opencode.ai/docs/config/).

#### Claude Code
Aitta does not provide an Anthropic-compatible endpoint, so you cannot
use it as an endpoint for Claude Code. 

As with OpenCode, you can change settings with
a JSON file, which you place at `$HOME/roihu-claude/settings.json`. Note that this path
differs from the official path of `$HOME/.claude/settings.json`. This is due to some
problems with binding the directory to the agent container. Alternatively you can
change settings in Claude Code and the file will be auto-generated.

For the format and other details regarding settings and the configuration file, see the
[Claude Code documentation](https://code.claude.com/docs/en/model-config).

## MCP servers

Model Context Protocol (MCP) is a standardized way for AI agents to access many
different tools. See the [MCP documentation](https://modelcontextprotocol.io/docs/getting-started/intro)
for a general introduction.

The agent environment includes two MCP servers: one to run Slurm commands, and CSC-docs
to search the CSC User Guide. You are free to add more.

### Slurm

The agents are not able to run Slurm commands from within the container, the
Slurm MCP server is the only route. It exposes a fixed set of commands and caches
results, so repeated or redundant calls do not stress the Slurm database.

The MCP provides the following tools, listed with the underlying command each one
runs. By default the agent can call the read-only tools without asking, while
`launch_job` and `cancel_job` require your permission each time.

| Tool | Command | Needs permission |
| --- | --- | --- |
| `my_jobs` | `squeue --me` | No |
| `job_history` | `sacct` | No |
| `sinfo` | `sinfo` | No |
| `batch_script` | `scontrol write batch_script` or `sacct -B` | No |
| `slurm_config` | `scontrol show config` | No |
| `reservations` | `scontrol show reservations` | No |
| `launch_job` | `sbatch` | Yes |
| `cancel_job` | `scancel` | Yes |

### CSC-docs

The agents come preconfigured with the CSC-docs MCP server. You can read more about
it in the TODO: Check if link exists: [CSC-docs MCP](docs-mcp.md) page. You can also
add the MCP to any local client you are using.

## Skills

Agent skills are markdown files which give an agent more context. They can provide
the agents with workflows to follow, additional information, or ready-made scripts.

Skills are automatically invoked by the agent in situations it deems fit, which makes
them token-efficient as they aren't read except the situations when they are needed.
You can also manually invoke them by typing `/<skill-name>` at the start of your
prompt for both OpenCode and Claude Code. You can read more about agent skills in the
[agent skills documentation](https://agentskills.io/home).

The Roihu agent environment contains three skills by default: `job-efficiency`,
`software-environments`, and `batch-scripts`. You can read more about them below.

### Job efficiency

Fetches efficiency metrics for a job. If you don't give a Job ID, the agent works
out which job you mean.

### Software environments

Helps with installing or using software on Roihu. Checks whether something is already
installed on Roihu, how to access it if it is, and what options for installation there
are if it is not.

### Batch scripts

Helps with batch/Slurm script creation, debugging, and optimization. Makes sure
the script contains the necessary parts, takes into account some common cases
(High I/O, MPI jobs, etc.) and what changes they require in the batch/Slurm script.

### Adding your own skills

You can add your own skills for the agents. Create a skill according to the standards
in the [agent skills documentation](https://agentskills.io/home), and add it to
`$HOME/.agents/skills` for OpenCode, and to `$HOME/roihu-claude/skills` for Claude Code.
Alternatively you can add the skills to the directory you launch the agents from
in a `.claude/skills` folder instead of the aforementioned directories. Both Claude
Code and OpenCode will check this directory. Skills placed in other locations than
`$HOME/.agents` or `$HOME/roihu-claude` will only be accessible to agents launched in
the directory with the `.claude` directory.

You can find more skills created by CSC from our [Github](https://github.com/CSCfi/csc-skills),
which can help in the use other CSC services.