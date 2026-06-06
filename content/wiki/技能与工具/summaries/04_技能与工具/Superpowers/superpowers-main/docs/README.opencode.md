---
source: raw/04_技能与工具/Superpowers/superpowers-main/docs/README.opencode.md
raw_sha256: 62c1f6619d632d07a3c29c21758a15c3ecc97210a5baa65d41cba2d4a930c536
compiled_at: 2026-04-24T08:48:21.324Z
---
<wiki>
# Superpowers for OpenCode
## Summary
This is the official complete guide for installing, configuring, and using the **Superpowers** open-source plugin for [OpenCode.ai](https://opencode.ai). Superpowers extends OpenCode functionality with reusable skill management, custom workflow tools, context persistence across conversation compaction, and cross-compatibility with Claude Code skills.

---

## Installation
Superpowers can be installed either via automated quick setup or manual step-by-step installation.

### Quick Install (Automated)
Provide the following instruction directly to OpenCode to handle setup automatically:
```
Clone https://github.com/obra/superpowers to ~/.config/opencode/superpowers, then create directory ~/.config/opencode/plugin, then symlink ~/.config/opencode/superpowers/.opencode/plugin/superpowers.js to ~/.config/opencode/plugin/superpowers.js, then restart opencode.
```

### Manual Installation
#### Prerequisites
- [OpenCode.ai](https://opencode.ai) installed
- Node.js (with ES module support) installed
- Git installed

#### Installation Steps
1. **Install Superpowers Core Files**
   Create the required directory and clone the Superpowers repository:
   ```bash
   mkdir -p ~/.config/opencode/superpowers
   git clone https://github.com/obra/superpowers.git ~/.config/opencode/superpowers
   ```

2. **Register the Plugin**
   OpenCode loads plugins from the `~/.config/opencode/plugin/` directory (global, user-wide) or `.opencode/plugin/` directory (project-local). Create a symlink for your desired scope:
   - **Global installation (available for all projects):**
     ```bash
     mkdir -p ~/.config/opencode/plugin
     ln -sf ~/.config/opencode/superpowers/.opencode/plugin/superpowers.js ~/.config/opencode/plugin/superpowers.js
     ```
   - **Project-local installation (only available for current project):**
     ```bash
     # Run from your OpenCode project root
     mkdir -p .opencode/plugin
     ln -sf ~/.config/opencode/superpowers/.opencode/plugin/superpowers.js .opencode/plugin/superpowers.js
     ```

3. **Restart OpenCode**
   Restart your OpenCode instance to load the plugin; Superpowers will activate automatically.

---

## Usage
### Core Built-In Tools
Superpowers provides two custom tools for skill management:
1. **`find_skills`**: Lists all available registered skills across all enabled scopes.
   Usage: `use find_skills tool`
2. **`use_skill`**: Loads a specified skill into the conversation. Loaded skills persist across OpenCode context compaction.
   Usage: `use use_skill tool with skill_name: "superpowers:brainstorming"`

### Custom Skill Creation
Superpowers supports three scopes of custom skills, with hierarchical priority resolution. All skills follow the same structure: a dedicated directory containing a `SKILL.md` file with YAML frontmatter metadata.

#### Personal Skills (User-Wide)
Stored in `~/.config/opencode/skills/`, available across all projects for your user:
1. Create a dedicated directory for your skill:
   ```bash
   mkdir -p ~/.config/opencode/skills/[your-skill-name]
   ```
2. Create a `SKILL.md` file with the following structure:
   ```markdown
   ---
   name: [your-skill-name]
   description: Use when [trigger condition] - [brief summary of skill functionality]
   ---

   # [Your Skill Display Name]
   [Full skill implementation content here]
   ```

#### Project Skills (Project-Specific)
Stored in `.opencode/skills/` of your OpenCode project root, only available for that project:
1. Create a dedicated directory for your project skill:
   ```bash
   # Run from your OpenCode project root
   mkdir -p .opencode/skills/[your-project-skill-name]
   ```
2. Create a `SKILL.md` file following the same format as personal skills.

---

## Skill Priority Resolution
Skills are resolved in the following hierarchical order (highest priority to lowest) to handle name conflicts:
1. Project skills (`.opencode/skills/`)
2. Personal skills (`~/.config/opencode/skills/`)
3. Superpowers core skills (`~/.config/opencode/superpowers/skills/`)

You can force skill resolution to a specific scope by adding a prefix to the skill name:
- `project:[skill-name]`: Force use of the project-level version of the skill
- `[skill-name]`: Use the default priority search order
- `superpowers:[skill-name]`: Force use of the core Superpowers version of the skill

---

## Core Features
1. **Automatic Context Injection**: Core Superpowers context is automatically injected into every OpenCode session via the `chat.message` hook, requiring no manual user configuration.
2. **Skill Persistence**: Skills loaded via `use_skill` are inserted as user messages with the `noReply: true` flag, ensuring they remain available throughout long conversations, even after context compaction.
3. **Context Compaction Resilience**: The plugin listens for OpenCode's `session.compacted` events and automatically re-injects the core Superpowers bootstrap context to maintain full functionality after context compaction.
4. **Claude Code Skill Compatibility**: Skills written for Claude Code are automatically adapted for use with OpenCode via built-in tool mapping:
   - `TodoWrite` → OpenCode's `update_plan` tool
   - `Task` with subagents → OpenCode's `@mention` system
   - Claude Code `Skill` tool → Superpowers `use_skill` tool
   - File operations → Native OpenCode file tools

---

## Architecture
### Plugin Structure
- **File Path**: `~/.config/opencode/superpowers/.opencode/plugin/superpowers.js`
- **Core Components**:
  - Two custom tools: `use_skill`, `find_skills`
  - `chat.message` hook for initial context injection
  - `session.compacted` event handler for post-compaction context re-injection
  - Dependency on the shared `lib/skills-core.js` module

### Shared Core Module (`skills-core.js`)
- **File Path**: `~/.config/opencode/superpowers/lib/skills-core.js`
- A reusable module shared between OpenCode and Codex Superpowers implementations to reduce code duplication.
- Core functions:
  - `extractFrontmatter()`: Parse YAML frontmatter metadata from skill files
  - `stripFrontmatter()`: Remove metadata from skill content for display
  - `findSkillsInDir()`: Recursively discover skills in a specified directory
  - `resolveSkillPath()`: Handle skill path resolution with priority shadowing
  - `checkForUpdates()`: Detect available Git updates for the Superpowers repository

---

## Updating
To update Superpowers to the latest version:
```bash
cd ~/.config/opencode/superpowers
git pull
```
Restart OpenCode to load the updated plugin version.

---

## Troubleshooting
### Plugin Not Loading
1. Verify the plugin file exists: `ls ~/.config/opencode/superpowers/.opencode/plugin/superpowers.js`
2. Verify the symlink is correctly configured: `ls -l ~/.config/opencode/plugin/superpowers.js`
3. Check OpenCode debug logs: `opencode run "test" --print-logs --log-level DEBUG`
4. Confirm the plugin load log entry is present: `service=plugin path=file:///.../superpowers.js loading plugin`

### Skills Not Found
1. Verify the core skills directory exists and contains skill folders: `ls ~/.config/opencode/superpowers/skills`
2. Run the `find_skills` tool to list all skills discovered by Superpowers
3. Confirm each skill directory contains a valid `SKILL.md` file with required frontmatter

### Tools Not Working
1. Confirm the plugin loaded successfully via OpenCode logs
2. Verify your Node.js version supports ES modules (required for the plugin)
3. Test the plugin manually via Node.js:
   ```bash
   node --input-type=module -e "import('file://~/.config/opencode/plugin/superpowers.js').then(m => console.log(Object.keys(m)))"
   ```

### Context Not Injecting
1. Verify the `chat.message` hook is functioning correctly
2. Confirm the default `using-superpowers` core skill exists
3. Update OpenCode to a recent version with official plugin support

---

## Testing
Superpowers includes an automated test suite for the OpenCode implementation, located at `tests/opencode/` in the repository:
- Run all integration tests with verbose output:
  ```bash
  ./tests/opencode/run-tests.sh --integration --verbose
  ```
- Run a specific test file:
  ```bash
  ./tests/opencode/run-tests.sh
