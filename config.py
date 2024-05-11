import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "26026658"))
API_HASH = getenv("API_HASH", "7573b1e004f6da153dba07bf5c1a2a6a")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6999969950:AAGIwlgqnDowSBew4yBuvbpDOeIEuaxPLBg")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mukundsrajput:lFRam73ZwE2D4snZ@cluster0.bmxejth.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002078575375"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002078575375")) 

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6584789596"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/VG-TEAM/VIP-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FleX_Support_Chat")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Emxes_Community")

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "100"))
# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = False

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "3")
)  # Remember to give value in Seconds

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds

# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQGNIqIAqrS_USl6MT1NSoC6ZvluBr284hgYI8EaFjaIpFnrvNArjtR0Fas212V1_rmH4_aUNc4PNDJxM880G_iOcnEMfCOFLBUXfeFMZ6X9v8lKKeV4CH4BX3319yXQV6OW3FjhquSNZLfDvKwD8XYm2lJTyU6_9acUhqvfib_p4c68kylPM2Ur7FoRvIclPuTwv88Ny5kFi1hflPQZdTZ1VJRxhRLZoiOD25-4OCKDz7_65dgUmCBUh8LL5zfisV-BVWG-rzOO5rYedrRBbHRPTqHMrm_aA2WsAe0YxPqVXMOQPLQiLU_7tGimjJ6o2YzmzN4_cmaSnNCVyJLAOgBv2xjZ8AAAAAF7SiUgAA")
STRING2 = getenv("STRING_SESSION2", "BQGNIqIAYKGDNUWeAcOT0W9mUj8NxM5bSY0CPF4V7IvYdOsTf_0BcBqKtqHbQzSKFBesMiDe2lrqLp5FF5XqoxkYcp98V0COZBp5ssSBBjAFGhccdz_4R7fJWQrwuRrZQSo16iWZWB71PLU2VR5fMpLUW7Y0mDWaimIxdT0danEV3HF-0zoIJV-hOod9HjzOML-lI4ZRcYvtMC_CJ2eeBclOnwxgMDgcB37kDZcXmNBPZDYWl50ZxSs-Au45nEOz3MYdIBpt3xmorelYSWtM0F6k_YwK_KUWjIm6DoutGrs7mUIX7B-zruwfbtpbhNGUo9qJ9PBhWp9kuCT-JyvtC5pcaJz6WAAAAAF7SiUgAA")
STRING3 = getenv("STRING_SESSION3", "BQGNIqIAS2gpYIBsf2YVukOrAFj6uQn2WuCD9CVnotJBbYsRX9SXyWO1bKdTCo3GH_n0lquT6Bk6aKh-R4d_7_ZWG2aXGbPrkE8uPuQzpI6uAflg9GfpojXQfta7LRmcMg7OpwosLVKpj2nS3-At5vuQQVE7-_2I94Z_mT7CmrSSVmPFtwpl0mQZXhEQjcWtmoU5kllJcKWw2wgjqni5la20h9uLjl-vva1jGk6TZhXrcSgAjlEtWMg0WttnQybykur5sJfzUZcq-BGOCqHAMFwGzGtkHzBYhILKETmuvhQpAdhyay_21X-hvah1tbaQg36oJ36Prg4pfsIFfn0rIHTHnAAAAAF7SiUgAA")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#    __      _______ _____    ___  __ _    _  _____ _____ _____   _____   ____ _______
#    \ \    / /_   _|  __ \   |  \/  | |  | |/ ____|_   _/ ____|  |  _ \ / __ \__   __|
#     \ \  / /  | | | |__) |  | \  / | |  | | (___   | || |       | |_) | |  | | | |
#      \ \/ /   | | |  ___/   | |\/| | |  | |\___ \  | || |       |  _ <| |  | | | |
#       \  /   _| |_| |       | |  | | |__| |____) |_| || |____   | |_) | |__| | | |
#        \/   |_____|_|       |_|  |_|\____/|_____/|_____\_____|  |____/ \____/  |_|


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/af76565ecb93f1763a9fd.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
STATS_IMG_URL = "https://graph.org/file/527daa229a210ec5b901f.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
STREAM_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/5abc92f2c2367baf29fa3.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
