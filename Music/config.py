##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'BAApuxTZYI8HiX5e8_GcBOF9btoe5_qyPp_Y_NSdiuzDg5457urWg5aX2ZK8QZ6_uYEeOni9W4rLTnjnXCGHS4g5pYtbae1sD__zY7137qp9JA3y8UdZQvnD9Vb1vn2Y-UzSb5u_ZgV6797ZcCQWaRxYx7_8P7KcldEFn9M_n9rMOXF1iAMhEnEGfQLy-k76XMvnDcue5vME7f_2bln7prfqAqZuvjKbnOdDFHhzfqn2BydJPYldzeecbtQGqwGGJaVaXjoyk3k3qS2ucn-E3ArMnr80Ta_LIhKc78uxadl_n1FuaR8a2HNaCrKm_6t9ZrrOHVeg8QN-5ByFXnerAKSTdaqVbgA')
BOT_TOKEN = getenv('2027063729:AAExwlLJF2OO2LFse1C3dhM4yKgICoy9p7c')
API_ID = int(getenv('API_ID', "10067699"))
API_HASH = getenv('4314073203822c14efeafbae0f8a72d3')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("mongodb+srv://juicessh:juicesshg@cluster0.mkcuc7e.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1974113646').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001446828143'))
ASS_ID = int(getenv("ASS_ID", '1692445304'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1974113646').split()))
GROUP = getenv("B_A_7_R", None)
CHANNEL = getenv("a_s_g_ki", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muhammadrizky16/KyyMusic")
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# KALO FORK/CLONE JAN DI HAPUS KENTOD
OWNER_ID.append(1663258664)
OWNER_ID.append(1607338903)
