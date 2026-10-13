# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

# One == Physics Wallah (PW)
# Two == ClassPlus (CP)
# Three == Appx

import os

api_id = int(os.environ.get("API_ID", "22114233"))
api_hash = os.environ.get("API_HASH", "d7abcec5c967414fadb1d438fa05ebea")
bot_token = os.environ.get("BOT_TOKEN", "8595771992:AAFnAiGV12oVL6j39OTAZqnewDWhEYPdDuA")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "1403488629").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")

# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
