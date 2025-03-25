# mygame/typeclasses/__init__.py
"""
Typeclasses package module.
"""
from typeclasses.patches import Patch, Landmark
from typeclasses.entities import Entity, Citizen, Game_Object

def register_all_typeclasses():
    """
    Register all typeclasses.
    """
    return {
        "Patch": Patch,
        "Landmark": Landmark,
        "Entity": Entity,
        "Citizen": Citizen,
        "Game_Object": Game_Object
    }
