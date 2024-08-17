# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "21661450"))
    API_HASH = os.environ.get("API_HASH", "79612bc71908f95372808520a7eeee74")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7211200915:AAHYmpFqwjyhvVqdXZzjQuBBn7HaJna1gfs")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 2021408974))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "2021408974").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Madhan:N0password@cluster0.y0vtta6.mongodb.net/?retryWrites=true&w=majority")
    FORCE_SUB = os.environ.get("FORCE_SUB", "beta_bot_updates")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002233706633"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
