from dotenv import load_dotenv
load_dotenv()
import os


BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
# Amazon needs a User-Agent header or it rejects requests
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    )
}

TRACKED_FILE = "data/tracked.json"
