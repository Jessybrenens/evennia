# Deployment Configuration for The Patchwork Game

This file contains the configuration for deploying The Patchwork game to a Manus webpage.

## Deployment Steps

1. Prepare the game files for deployment
2. Set up the Manus webpage
3. Deploy the game to the webpage
4. Test the deployed game

## Game Information

- Title: THE PATCHWORK: AMERICA 2035
- Description: A text-based adventure game set in a fragmented America of 2035, where tech billionaires have carved the nation into territories known as PATCHES.
- Game Type: MUD (Multi-User Dungeon)
- Technology: Evennia (Python-based MUD framework)

## Deployment Configuration

```python
# Deployment settings
GAME_NAME = "THE PATCHWORK: AMERICA 2035"
GAME_DESCRIPTION = "A text-based adventure game set in a fragmented America of 2035, where tech billionaires have carved the nation into territories known as PATCHES."
GAME_AUTHOR = "Jessybrenens"
GAME_VERSION = "1.0"
GAME_URL = "https://github.com/Jessybrenens/evennia"

# Web client settings
WEB_CLIENT_OPTIONS = {
    "theme": "dark",
    "font_size": "medium",
    "command_history_length": 50,
    "default_commands": [
        "BEGIN SESSION",
        "BEGIN GAME",
        "END SESSION",
        "TRAVEL",
        "EXPLORE",
        "INVESTIGATE",
        "INTERACT",
        "CONVERSATE",
        "DISPLAY MAP"
    ]
}

# Server settings for deployment
DEPLOYMENT_SERVER = {
    "host": "manus.ai",
    "port": 4000,
    "web_port": 4001,
    "ssl": True,
    "max_players": 100
}
```

## Manus Webpage Integration

The game will be integrated into a Manus webpage with the following features:

1. Game client embedded in the webpage
2. Game information and description
3. Command reference and help
4. User account management
5. Game statistics and leaderboards

## Post-Deployment Testing

After deployment, the following tests should be performed:

1. Connection test from the Manus webpage
2. Account creation and login
3. Game session initialization
4. Basic gameplay functionality
5. Multi-user interaction
6. Performance under load
