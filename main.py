from dotenv import load_dotenv

load_dotenv()

import os
import uvicorn
from app.api import app

PORT = os.environ.get("PORT", "8080")

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(PORT),
        log_level="info",
    )
