# `mutnav` - README

The `mutnav` repository contains a demo MCP server that can be configured
with Claude Code to query simple somatic mutation data provided by ICGC-Argo.

## Installation
Clone the repository and use `uv` to install the dependencies.
```
git clone --recursive git@github.com:richard-dnastack/mutnav.git
cd mutnav
uv pip install -r pyproject.toml
```


## Download data
A copy of simple somatic mutations can be found in a DNAstack bucket
(`dnastack-bioinformatics`):
```
mkdir data
gcloud storage cp gs://richard_dev/ssm.tsv ssm.tsv data/ssm.tsv
```

## Usage
To integrate the MCP server with the Claude desktop app, edit the
desktop configuration app JSON file.  On macOS, edit the following
file:
```
/Users/<username>Library/Application\ Support/Claude/claude_desktop_config.json
```

Add the following entry under `mcpServers`:
```
"mutnav": {
   "command": "uv",
   "args": [
       "--directory",
       "/Users/richard.deborja/.local/projects/mcp/mutnav",
       "run",
       "main.py"
   ]
}
```

## License
MIT


#### Copyright (c) 2025 Richard de Borja, DNAstack.  All rights reserved.

