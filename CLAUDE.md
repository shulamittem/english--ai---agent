# CLAUDE.md

Conventions this project follows, based on the Google ADK (Python) Quickstart
(https://google.github.io/adk-docs/, now hosted at https://adk.dev/get-started/python/).

## Requirements

- Python **>= 3.10** (required by the `google-adk` package).
- Package: `google-adk` (installed via pip).

## Project structure

ADK expects the agent to live in its own package directory:

```
first agent/
    my_agent/            # the agent package (name = whatever the agent is called)
        __init__.py      # makes the directory a Python package
        agent.py          # defines root_agent
        .env              # API keys / project config (never commit this)
```

- `__init__.py` marks the folder as an importable Python package. ADK's CLI
  tools (`adk run`, `adk web`, `adk api_server`) discover agents by looking
  for a package with this structure.
- `agent.py` holds the agent logic and must expose the `root_agent` variable.
- `.env` holds credentials and is gitignored (already covered by this repo's
  `.gitignore`).

## Defining `root_agent`

`agent.py` must define a module-level variable named exactly `root_agent`.
This is the only required element of an ADK agent:

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-flash-latest",
    name="root_agent",
    description="...",
    instruction="...",
    tools=[...],
)
```

- The variable **must** be named `root_agent` — ADK's CLI looks for this
  exact name when it imports the package.
- `tools` is a list of callables/tool objects; omit or leave empty if the
  agent doesn't need tools.

## Required environment variables

Set these in `my_agent/.env` (never commit this file):

```
GOOGLE_API_KEY="YOUR_API_KEY"
```

- Obtain the key from Google AI Studio's API Keys page (for Gemini models).
- If a different model provider is used instead of Gemini, different
  auth env vars apply — see ADK's Models & Authentication docs.

## Running the agent locally

Run these from the **parent directory** that contains the agent package
(e.g. from `first agent/`, not from inside `my_agent/`):

```bash
# Interactive terminal chat
adk run my_agent

# Browser-based Dev UI (default http://localhost:8000)
adk web --port 8000

# Expose the agent as a REST API
adk api_server
```

## Setup checklist

```bash
python3 -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install google-adk
```

No agent code exists in this repo yet — this file documents the conventions
to follow once it's written.
