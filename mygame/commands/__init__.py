# mygame/commands/__init__.py
"""
Commands package module.
"""
from commands.commands import GameCmdSet, PatchCmdSet, LandmarkCmdSet
from commands.initiate_chat import InitiateChatCmdSet

def register_all_commands():
    """
    Register all command sets.
    """
    return {
        "GameCmdSet": GameCmdSet,
        "PatchCmdSet": PatchCmdSet,
        "LandmarkCmdSet": LandmarkCmdSet,
        "InitiateChatCmdSet": InitiateChatCmdSet
    }
