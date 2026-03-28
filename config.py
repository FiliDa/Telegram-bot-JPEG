import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
_admin_id = os.getenv("ADMIN_ID")
ADMIN_ID = int(_admin_id) if _admin_id and _admin_id.strip() else None
_channels = os.getenv("CHANNELS", "")
CHANNELS = [int(x.strip()) for x in _channels.split(",") if x.strip()]

# Mapping button text to folder names
CATEGORIES = {
    "🔥 ТопВайфу": "media/top_waifu",
    "💫 Гифки": "media/gifs",
    "🐱 Ушки": "media/ears",
    "🦎 Хвосты": "media/tails",
    "👗 Повседневная": "media/casual",
    "👕 Спорт": "media/sport",
    "🌸 Милые": "media/cute",
    "😎 Крутые": "media/cool",
    "🖤 Дарк гёрл": "media/dark_girl",
    "✨ Магическая": "media/magic",
    "😈 Демоны": "media/demons",
    "😇 Ангелы": "media/angels",
    "💛 Блондинки": "media/blondes",
    "🔥 Рыжие": "media/redheads",
    "🖤 Брюнетки": "media/brunettes",
    "⚔️ Воительницы": "media/warriors"
}
