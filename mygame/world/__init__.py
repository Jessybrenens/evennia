# mygame/world/__init__.py
"""
World package module.
"""
from world.utils import logger
from world.data_loader import load_game_data

def initialize_world():
    """
    Initialize the game world.
    """
    logger.log_info("Initializing game world...")
    load_game_data()
    logger.log_info("Game world initialized.")
