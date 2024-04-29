import os

API_ID = API_ID = 24478182

API_HASH = os.environ.get("API_HASH", "a98b5be0127986be1cc2553dbd99765e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7088632591:AAEvdJBXacrQYmGqEUc1mpzdegX_5wRumw8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7118905960))

LOG = -1002068352431

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7097613157").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)

api_id = ""
api_hash = "a98b5be0127986be1cc2553dbd99765e"
bot_token = "7088632591:AAEvdJBXacrQYmGqEUc1mpzdegX_5wRumw8"
auth_groups = "-1002068352431"
