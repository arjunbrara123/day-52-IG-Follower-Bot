from time import sleep
from InstaFollower import InstaFollower

ig_bot = InstaFollower()

ig_bot.login()

ig_bot.find_followers()

ig_bot.follow()
