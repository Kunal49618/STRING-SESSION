from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("7158227205:AAGSk3bpEyLGxcQASpZxpqQs_LCC6VF9l6U")
OWNER_ID = int(getenv("7173620352"))

MONGO_DB_URI = getenv("mongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("https://t.me/KNOW_ABOUT_KUNAL", None)
