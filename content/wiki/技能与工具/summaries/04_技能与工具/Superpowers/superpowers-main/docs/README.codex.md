---
source: raw/04_技能与工具/Superpowers/superpowers-main/docs/README.codex.md
raw_sha256: 59681464372d0714d4b03e0eec112337b0e8514ccc6a6d84bfe8929d98fdae1c
compiled_at: 2026-04-24T08:46:15.538Z
---
# Superpowers for Codex

## Summary
This is the complete guide for using the Superpowers skill extension system with OpenAI Codex. Codex support for Superpowers is currently experimental and may be refined based on user feedback.

## Installation
### Quick Install
Instruct Codex to run the following to install automatically:
```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md
```

### Manual Installation
#### Prerequisites
- Active OpenAI Codex access
- Shell access to install required files

#### Installation Steps
1. **Clone the Superpowers repository**
    ```bash
    mkdir -p ~/.codex/superpowers
    git clone https://github.com/obra/superpowers.git ~/.codex/superpowers
    ```

2. **Install Bootstrap**
    The bootstrap file is included in the repository at `.codex/superpowers-bootstrap.md`, and Codex will automatically load it from the cloned installation path.

3. **Verify Installation**
    Instruct Codex to run the following command to confirm setup is complete:
    ```
    Run ~/.codex/superpowers/.codex/superpowers-codex find-skills to show available skills
    ```
    A successful installation will return a list of available skills with corresponding descriptions.

## Usage
### Find Available Skills
Instruct Codex to run:
```
Run ~/.codex/superpowers/.codex/superpowers-codex find-skills
```

### Load a Specific Skill
Instruct Codex to run, replacing `<skill-name>` with the target skill:
```
Run ~/.codex/superpowers/.codex/superpowers-codex use-skill <skill-name>
```
*Example: `Run ~/.codex/superpowers/.codex/superpowers-codex use-skill superpowers:brainstorming`*

### Bootstrap All Skills
Load the full bootstrap file containing all registered skill information by instructing Codex to run:
```
Run ~/.codex/superpowers/.codex/superpowers-codex bootstrap
```

### Create Custom Personal Skills
1. Create a dedicated directory for your custom skill:
    ```bash
    mkdir -p ~/.codex/skills/my-skill
    ```
2. Create a `SKILL.md` file in the skill directory following this template:
    ```markdown
    ---
    name: my-skill
    description: Use when [condition] - [what it does]
    ---

    # My Skill

    [Your skill content here]
    ```
Personal skills will override built-in Superpowers skills that share the same name.

## Architecture
### Superpowers Codex CLI Tool
- **File Location:** `~/.codex/superpowers/.codex/superpowers-codex`
- A Node.js command-line utility that provides 3 core skill management commands:
  1. `bootstrap`: Load the complete bootstrap dataset with all skill metadata
  2. `use-skill <name>`: Load and activate a single specified skill
  3. `find-skills`: List all available registered skills with descriptions

### Shared `skills-core` Module
- **File Location:** `~/.codex/superpowers/lib/skills-core.js`
- An ES format module that handles skill discovery and parsing logic. This module is shared between the Codex Superpowers integration and the OpenCode plugin to ensure consistent skill behavior across platforms.

### Claude Code to Codex Tool Mapping
Skills originally written for Claude Code are adapted for Codex compatibility via the following mappings:
- `TodoWrite` → `update_plan`
- `Task` with subagents → Directly perform requested work, with notification that subagents are not available
- `Skill` tool → `~/.codex/superpowers/.codex/superpowers-codex use-skill`
- File operations → Use native Codex file management tools

## Updating Superpowers for Codex
Run the following shell command to pull the latest version of the Superpowers repository:
```bash
cd ~/.codex/superpowers
git pull
```

## Troubleshooting
### Skills Not Found
1. Verify the skill directory exists and is populated: `ls ~/.codex/superpowers/skills`
2. Confirm the CLI tool is functional: `~/.codex/superpowers/.codex/superpowers-codex find-skills`
3. Check that all registered skills have a valid `SKILL.md` file in their directory

### CLI Script Not Executable
Run the following to grant execution permissions to the CLI tool:
```bash
chmod +x ~/.codex/superpowers/.codex/superpowers-codex
```

### Node.js Errors
The Superpowers Codex CLI tool requires Node.js. Verify your installed version with:
```bash
node --version
```
A minimum of Node.js v14 is required; Node.js v18+ is recommended for full ES module support.

## Getting Help
- Report bugs or issues: https://github.com/obra/superpowers/issues
- Main Superpowers documentation: https://github.com/obra/superpowers
- Official launch blog post: https://blog.fsck.com/2025/10/27/skills-for-openai-codex/
