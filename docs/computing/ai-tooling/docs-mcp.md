# CSC Documentation MCP Server

Model Context Protocol (MCP) is a standardized way for AI agents to access a large variety of tools. It is hosted by the Linux Foundation. See the [MCP documentation](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) for a general introduction.

The CSC Documentation MCP server lets agents search the CSC User Guide for up-to-date information about HPC, Roihu, and other CSC services. It indexes the documentation as snippets and returns the snippets that best match a query. The search is *semantic*, so the agent does not have to guess the exact keywords used in the documentation. A query phrased in the agent's own words is enough to find the relevant passages.

The server is public and requires no authentication.

## How it works

The server exposes a single tool, `retrieve_docs`, which takes a search query and returns the closest matching documentation snippets. The agent decides when to call it and what to search for.

| Parameter | Description | Values |
| --- | --- | --- |
| `query` | The search query, in natural language. | Text, up to 100 characters. |
| `k` | How many of the best matching snippets to return. | An integer from 1 to 10. Default is 4. |

The indexed documentation is kept up-to-date automatically, so the snippets reflect the current CSC User Guide without any action on your part.

!!! info "Authoritative source"
    Because the User Guide changes over time, the documentation returned by this server is more reliable than the model's own training data. It is worth instructing your agent to treat these results as the authoritative source, for example in a AGENTS.md.

## Usage

The endpoint is `https://mcp.docs.csc.fi` and it uses streamable HTTP.

How you add an MCP server depends on the client, so check the documentation of your agent. Instructions for two common clients are below.

For **Claude Code**, add it by running:

```bash
claude mcp add --transport http csc-docs https://mcp.docs.csc.fi
```

For **OpenCode**, run the following command and follow the prompts:

```bash
opencode mcp add
```