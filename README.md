# Mac OS Ring MCP

**As of April 16th, Antigravity's notification feature is malfunctioning.**
This MacOS Ring MCP bypasses this issue by notification sound played through the MCP server.
To avoind supply chain attacks, we only rely on python standard libraries, with minimum length code.
Also, this script only plays sound, to avoid injection attacks from agent's output.

## Installation


Clone this repository, and modify the mcp server configs through antigravity's settings.

### Add MCP Server

The config is typically located in `~/.gemini/antigravity/mcp_config.json`.
It can be also opened from antigravity settings.
The config shall be modified as follows, where the path in `"args"` shall be modified according to the script's location:

```JSON
{
  "mcpServers": {
    "macos-notifier-raw": {
      "command": "python3",
      "args": [
        "/absolute/path/to/your/main.py"
      ]
    }
  }
}
```


### Add system prompt

Add following system prompt

```md
# Notification Protocol
When you have fully completed a task, when you encounter a blocker and require user input to proceed, or when you invoke any actions that may requires user's permission (e.g. command execution), you must immediately call the `play_alert_sound` tool to notify the user. Do not ask for permission to use the tool, just execute it as your final step.
```

(Via config file directly): Edit `~/.gemini/AGENTS.md`

(Via Antigravity GUI): 
1. In the Agent Manager panel, click the three dots (•••) in the top-right corner.
2. Select Additional Options, then click on Customizations.
3. Navigate to the Rules tab.
4. Click the + Global button to ensure this rule applies to every project you open (or + Workspace if you only want it for the current folder).
5. Paste the rule text (provided below) into the editor and save it.