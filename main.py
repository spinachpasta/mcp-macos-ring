import sys
import json
import subprocess

def send_response(message):
    """Writes the JSON-RPC response to standard output."""
    print(json.dumps(message), flush=True)

def main():
    # Listen continuously for messages on standard input
    for line in sys.stdin:
        if not line.strip():
            continue
        
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            continue

        req_id = request.get("id")
        method = request.get("method")

        # 1. Handle the Initial Handshake
        if method == "initialize":
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {
                        "name": "macos-sound-only",
                        "version": "1.0.0"
                    },
                    "capabilities": {
                        "tools": {}
                    }
                }
            })
        
        # 2. Expose the tool with NO inputs
        elif method == "tools/list":
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": [
                        {
                            "name": "play_alert_sound",
                            "description": "Plays a hardcoded macOS system sound to alert the user. Takes no inputs.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {}
                            }
                        }
                    ]
                }
            })
        
        # 3. Execute the hardcoded command
        elif method == "tools/call":
            params = request.get("params", {})
            name = params.get("name")
            
            if name == "play_alert_sound":
                try:
                    # Safely play a local audio file. No variables are passed to the shell.
                    subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"], check=True)
                    
                    send_response({
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": {
                            "content": [
                                {"type": "text", "text": "Sound played successfully."}
                            ]
                        }
                    })
                except subprocess.CalledProcessError as e:
                    send_response({
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": {
                            "isError": True,
                            "content": [
                                {"type": "text", "text": f"Error playing sound: {str(e)}"}
                            ]
                        }
                    })

if __name__ == "__main__":
    main()