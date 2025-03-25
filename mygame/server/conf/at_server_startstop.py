# mygame/server/conf/at_server_startstop.py
"""
Server startstop hooks for The Patchwork game.
"""
from evennia.utils import logger
from world.map_loader import load_ascii_maps
from world.data_loader import load_game_data

def at_server_start():
    """
    This is called every time the server starts up.
    """
    logger.log_info("Server starting - initializing game world...")
    
    # Load game data
    try:
        load_game_data()
        logger.log_info("Game data loaded successfully.")
    except Exception as e:
        logger.log_err(f"Error loading game data: {e}")
    
    # Load ASCII maps
    try:
        load_ascii_maps()
        logger.log_info("ASCII maps loaded successfully.")
    except Exception as e:
        logger.log_err(f"Error loading ASCII maps: {e}")
    
    logger.log_info("Game world initialization complete.")

def at_server_stop():
    """
    This is called just before the server is shut down.
    """
    logger.log_info("Server shutting down - saving game state...")
