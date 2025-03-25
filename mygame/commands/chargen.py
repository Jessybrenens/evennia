# mygame/commands/chargen.py
"""
Character generation module for The Patchwork game.
"""
from evennia import Command, CmdSet
from evennia.utils import create

class CmdCreateCharacter(Command):
    """
    Create a new character for The Patchwork game.
    
    Usage:
      createcharacter <name>
    """
    key = "createcharacter"
    locks = "cmd:pperm(Players)"
    help_category = "Character Generation"
    
    def func(self):
        caller = self.caller
        
        if not self.args:
            caller.msg("Usage: createcharacter <name>")
            return
            
        name = self.args.strip()
        
        # Create the character
        try:
            default_home = caller.db.home or "#2"
            permissions = ["Player"]
            typeclass = "typeclasses.characters.Character"
            
            new_character = create.create_object(
                typeclass, 
                key=name,
                location=default_home,
                home=default_home,
                permissions=permissions,
                locks=None,
                report_to=caller
            )
            
            # Set up character attributes
            new_character.db.too_curious = 0
            
            # Connect the character to the account
            caller.puppet_object(caller.sessions.get()[0], new_character)
            
            caller.msg(f"Character '{name}' created and connected.")
            
        except Exception as e:
            caller.msg(f"Error creating character: {e}")

class CharGenCmdSet(CmdSet):
    """
    Command set for character generation.
    """
    key = "CharGenCmdSet"
    
    def at_cmdset_creation(self):
        self.add(CmdCreateCharacter())
