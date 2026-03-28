import config
print(f"Token present: {bool(config.BOT_TOKEN)}")
print(f"Token length: {len(config.BOT_TOKEN) if config.BOT_TOKEN else 0}")
