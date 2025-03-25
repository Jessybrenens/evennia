# mygame/server/conf/settings.py
"""
Settings file for The Patchwork game.
"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "THE PATCHWORK: AMERICA 2035"

# Path to the game directory
GAME_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# This is a security setting protecting against host poisoning
# attacks. It defaults to allowing all. In production, make
# sure to change this to your actual host addresses/IPs.
ALLOWED_HOSTS = ['*']

# The path that contains the root 'typeclasses' directory.
TYPECLASS_PATHS = ["mygame.typeclasses"]

# Command sets
CMDSET_PATHS = ["mygame.commands"]

# Add custom handlers for the game
INLINEFUNC_ENABLED = True

# Configure default command sets
COMMAND_DEFAULT_CLASS = "mygame.commands.commands.GameCmdSet"
CMDSET_CHARACTER = "mygame.commands.commands.GameCmdSet"
CMDSET_ACCOUNT = "mygame.commands.initiate_chat.InitiateChatCmdSet"

# Configure default typeclass paths
BASE_CHARACTER_TYPECLASS = "mygame.typeclasses.characters.Character"
BASE_ROOM_TYPECLASS = "mygame.typeclasses.patches.Patch"
BASE_EXIT_TYPECLASS = "evennia.objects.objects.DefaultExit"
BASE_OBJECT_TYPECLASS = "mygame.typeclasses.entities.Entity"

# Configure game settings
TOO_CURIOUS_LIMIT = 30
