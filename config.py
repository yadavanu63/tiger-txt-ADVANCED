import os

API_ID = API_ID = 22609670

API_HASH = os.environ.get("API_HASH", "a98b5be0127986be1cc2553dbd99765e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7139260466:AAEHwNQrZnGb8fzuQhNxEvlAl6Ud5_T_ddU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7118905960))

LOG = -1002005269251

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6127347210").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


