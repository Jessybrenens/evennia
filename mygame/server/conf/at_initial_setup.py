# mygame/server/conf/at_initial_setup.py
"""
Initial setup hooks for The Patchwork game.
"""
from evennia.utils import logger
from evennia import create_object
from typeclasses.patches import Patch, Landmark
from typeclasses.entities import Citizen, Game_Object

def at_initial_setup():
    """
    This is called the very first time the game starts up.
    """
    logger.log_info("Initial setup - creating default game objects...")
    
    # Create default admin character
    try:
        from evennia.objects.models import ObjectDB
        from django.conf import settings
        
        # Check if default character already exists
        default_char = ObjectDB.objects.filter(db_typeclass_path=settings.BASE_CHARACTER_TYPECLASS, 
                                              db_key="Admin").first()
        if not default_char:
            from typeclasses.characters import Character
            default_char = create_object(Character, key="Admin")
            default_char.db.desc = "The game administrator."
            default_char.db.too_curious = 0
            logger.log_info("Created default admin character.")
    except Exception as e:
        logger.log_err(f"Error creating default admin character: {e}")
    
    logger.log_info("Initial setup complete.")
