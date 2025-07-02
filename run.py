from app.bootstrap import bootstrap
from app.main import launch_server_or_gui

if __name__ == "__main__":
    print("🚀 Launching David AI 2B...")
    bootstrap()  # Downloads all models if not already
    launch_server_or_gui()  # Starts GUI or API server
