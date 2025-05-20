import os
import logging
from flask import Flask
from app import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    # debug_mode = os.getenv("FLASK_ENV")
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        logging.error(f"Failed to start server: {e}", exc_info=True)
        raise