import os

API_ID = API_ID = 24478182

API_HASH = os.environ.get("API_HASH", "a98b5be0127986be1cc2553dbd99765e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7109707094:AAGwjPkyO78A-7gX3vcQnA5T6zRTXUc1-Ik")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7118905960))

LOG = -1002054734777

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7097613157").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
