To use OpenSpec in Qoder, follow these steps based on the OpenSpec documentation:

1. **Install OpenSpec CLI**:
```bash
npm install -g @fission-ai/openspec@latest
```

2. **Initialize in your project**:
```bash
cd your-project
openspec init
```
- This creates `openspec/specs/` (current specs) and `openspec/changes/` (proposed changes)

3. **Create a change proposal**:
- Use natural language prompt: *"Create an OpenSpec change proposal for [your feature]"`
- Or use CLI: 
```bash
openspec new "Add profile search filters"
```

4. **Review and refine**:
```bash
openspec show <change-name>  # View proposal
openspec validate <change-name>  # Check specs
```

5. **Implement with Qoder**:
- When Qoder recognizes the OpenSpec workflow (via AGENTS.md convention), use:
```text
@openspec-apply <change-name>
```
- Or follow natural language instructions in your AI chat

6. **Archive completed changes**:
```bash
openspec archive <change-name> --yes
```

**For AGENTS.md compatibility**:
1. Create `openspec/AGENTS.md` with your workflow instructions
2. Qoder will automatically follow the documented workflow

**Example workflow**:
```text
You: Create an OpenSpec proposal for adding dark mode toggle
AI:  I'll create a change proposal for dark mode
    *Generates openspec/changes/dark-mode/...*
You: @openspec-apply dark-mode
AI:  Implementing dark-mode change from OpenSpec
    *Follows tasks in openspec/changes/dark-mode/tasks.md*
```

Check Qoder's documentation for specific OpenSpec integration details if not automatically supported.