from typing import cast
from os import getenv


BOT_TOKEN = cast(str, getenv('BOT_TOKEN'))
assert BOT_TOKEN is not None
