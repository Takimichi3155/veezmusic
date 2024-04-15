import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "Seista02)
BOT_TOKEN = getenv("BOT_TOKEN", "6891505280:AAHC-b3eZuYgqw2ZgbWFC1afLYGPZ8bS9xY")
BOT_NAME = getenv("BOT_NAME", "Seista")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/d91623e9cefcef8fb3aa8.png")
admins = {}
API_ID = int(getenv("API_ID", "26977508"))
API_HASH = getenv("API_HASH", "396589629e6705c592bc7fe891dc6e37")
BOT_USERNAME = getenv("BOT_USERNAME", "SiestaProX_Robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Seista02")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Dare_Devils_01")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Seista_Updates")
OWNER_NAME = getenv("OWNER_NAME", "aye_ujjwal") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "aye_ujjwal")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
