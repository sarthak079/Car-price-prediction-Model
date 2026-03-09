import os
import sys
import uvicorn

print(f"DEBUG: Current Working Directory: {os.getcwd()}")
print(f"DEBUG: Files in directory: {os.listdir('.')}")

try:
    from main import app
    print("DEBUG: Successfully imported 'app' from 'main'")
except Exception as e:
    print(f"DEBUG: Failed to import 'app': {e}")
    sys.exit(1) # This will force a clear error message in your Render logs

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"DEBUG: Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)