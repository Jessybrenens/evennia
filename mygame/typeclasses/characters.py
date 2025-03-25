# mygame/typeclasses/characters.py
"""
Character typeclass for The Patchwork game.
"""
from evennia import DefaultCharacter
from commands.initiate_chat import InitiateChatCmdSet
from commands.commands import GameCmdSet

class Character(DefaultCharacter):
    """
    The Character typeclass for The Patchwork game.
    This class represents the player character in the game.
    """
    
    def at_object_creation(self):
        """
        Called when the character is first created.
        """
        super().at_object_creation()
        self.db.too_curious = 0
        
        # Add command sets
        self.cmdset.add(InitiateChatCmdSet, permanent=True)
        self.cmdset.add(GameCmdSet, permanent=True)
    
    def at_post_puppet(self, **kwargs):
        """
        Called just after puppeting has been completed.
        """
        super().at_post_puppet(**kwargs)
        
        # Display welcome message
        self.msg("|c=== THE PATCHWORK: AMERICA 2035 ===|n")
        self.msg("|yWelcome back to The Patchwork.|n")
        self.msg("|yType |wBEGIN SESSION|n to continue your journey.|n")
        
        # Display TOO CURIOUS counter
        self.msg(f"\n|rTOO CURIOUS: {self.db.too_curious}/30|n")
