# Price-Drop Alert Bot

A flexible, extensible Discord bot that DMs you whenever a product’s price drops below your set threshold
usuable as a clean template you can easily customize and build new features onto

---

Features

- `!track <URL> <price>` – begin watching  
- `!list` – view active watches  
- `!untrack <#>` – stop watching  
- Checks prices hourly and DMs on drops  

---

Stack & Dependencies

- Python 3.8+  
- discord.py  
- aiohttp  
- beautifulsoup4  
- python-dotenv  

---

Usage

1. **Clone & enter repo**
   ```bash
   git clone https://github.com/your-username/price-drop-bot.git
   cd price-drop-bot
2.  Create a .env file and add your dsicord bot token in the form: DISCORD_BOT_TOKEN = (paste token here)
3.  ```bash
    python bot.py
