from Chizuru.Helper.core.bot import Chizuru
from Chizuru.Helper.core.dir import dirr
from Chizuru.Helper.core.git import git
from Chizuru.Helper.core.userbot import Userbot
from Chizuru.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Chizuru()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
