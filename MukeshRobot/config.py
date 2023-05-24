class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 22850063
    API_HASH = "cf9724197b0d6e7d8a53e46763b34fd1"

    CASH_API_KEY = "Q9HM7GIY4OXW2VLW"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://othibonw:1FkVhmA4bMwDr6cfwJcQzqrlIiq8a7cu@horton.db.elephantsql.com/othibonw"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://sakilanowar78:atIAQ0iJ2bwlMig7@cluster0.1mqytch.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/c8510dc787aa503705ea1.jpg"

    SUPPORT_CHAT = "https://t.me/Its_Me_SakiL)"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6189174968:AAElY0tbbrBIj5ephVQGuLQ0TWPEdrrt8GQ"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "HUQ59MUZB00R"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6024212623  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
