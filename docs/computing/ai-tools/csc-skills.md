# Using the CSC computing environment with LLM coding agents

LLM coding agents such as Claude Code, Codex and GitHub Copilot CLI know
general tools like Slurm, S3 and Kubernetes well, but not CSC's hostnames,
quotas, billing units or local rules. Without that context they often guess
plausible but wrong values. [csc-skills](https://github.com/CSCfi/csc-skills)
is a collection of [agent skills](https://agentskills.io/home) that gives
agents this CSC-specific knowledge, based on this user guide.

!!! warning "Responsibility"
    You are always responsible for what your agent does. Every command it
    runs is executed under your own account and CSC project. Read the
    [CSC AI Agent Policy](../usage-policy.md) before using
    agents on CSC systems.

## Available skills

| Skill | Service |
|---|---|
| `csc-roihu` | [Roihu](../systems-roihu.md) supercomputer: batch jobs, SSH certificates, disk areas, billing |
| `csc-allas` | [Allas](../../data/Allas/index.md) object storage |
| `csc-pouta` | [Pouta](../../cloud/pouta/index.md) IaaS cloud |
| `csc-rahti` | [Rahti](../../cloud/rahti/index.md) container cloud |
| `csc-satama` | [Satama](../../cloud/satama/index.md) container image registry |

An agent loads a skill only when your request concerns that service, so
installing all of them costs nothing for the ones you don't use.

## What the skills let the agent do

The skills mainly help the agent write code and commands for you to review
and run. By default:

* Read-only inspection (listing resources, checking quotas and usage) is
  done on request.
* Creating new resources, such as a VM or a batch job, is done only after the
  agent tells you the cost in billing units and any network exposure.
* Modifying or deleting existing resources or data is never done on the
  agent's own initiative. The agent writes a script and explains what it
  does, and runs it only after you explicitly confirm. Remember that a CSC
  project is shared, so mistakes can affect all its members.
* Credentials are never written into code, logs or commits.

## Installing

The repository is a plugin marketplace containing one plugin, `csc-skills`.
After installing, start a new agent session to load the skills.

### Claude Code and GitHub Copilot CLI

Inside an agent session, add the marketplace and install the plugin:

```
/plugin marketplace add CSCfi/csc-skills
/plugin install csc-skills@csc-skills
```

In Copilot CLI you can also run the same commands from the shell as
`copilot plugin marketplace add …` and `copilot plugin install …`.

### Codex

Add the marketplace from the shell:

```bash
codex plugin marketplace add CSCfi/csc-skills
```

Then open the plugin browser with `/plugins` in Codex and install
`csc-skills`.

### OpenCode and other agents

Agents without plugin support can load the skills from a directory. Clone
the repository and link the skills into `~/.agents/skills`, which OpenCode
and many other agents search:

```bash
git clone https://github.com/CSCfi/csc-skills.git
mkdir -p ~/.agents/skills
ln -s "$PWD"/csc-skills/skills/csc-* ~/.agents/skills/
```

Update the skills with `git pull` in the clone.

### On Roihu

The [Roihu agent environment](agent-env.md) provides
Claude Code, Codex and OpenCode with HPC-specific skills already set up. You
can add csc-skills to it as described in
[Adding your own skills](agent-env.md#adding-your-own-skills).

## Using the skills

Ask the agent about the task in your own words, for example "write a batch
job that runs this script on one GPU in Roihu" or "upload my results to an
Allas bucket". The agent picks the matching skill automatically.

For questions the skills don't cover, the
[CSC Documentation MCP server](docs-mcp.md) lets the
agent search this user guide directly.

Feedback and contributions are welcome in the
[GitHub repository](https://github.com/CSCfi/csc-skills).
