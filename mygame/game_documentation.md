# THE PATCHWORK: AMERICA 2035
## Game Documentation

### Introduction

Welcome to **THE PATCHWORK: AMERICA 2035** - a text-based adventure game set in a fragmented America of 2035, where tech billionaires have carved the nation into territories known as PATCHES. You play as an unmarked nomad, searching for a place to call home while exploring these diverse corporate territories.

### Accessing the Game

The game is available on the Manus webpage at: https://pages.manus.im/?sId=JFidTNlKh0a8Kkl3vXQDYn

To access the game:
1. Visit the URL above
2. Create an account or log in if you already have one
3. Connect to the game using the web client

### Getting Started

When you first connect to the game, you'll see the connection screen with basic information about the game. To begin playing:

1. Type `BEGIN SESSION` to start a new game session
2. Read the introduction to the game
3. Type `BEGIN GAME` to start gameplay
4. You'll be placed in Patch 1, Landmark 1 to begin your journey

### Command System

The game uses a simple command system to navigate and interact with the world:

#### Session Commands

- `BEGIN SESSION` - Start a new game session
- `BEGIN GAME` - Start gameplay after session initialization
- `END SESSION` - End the current game session

#### Gameplay Commands

- `TRAVEL` - Move between PATCHES (territories)
- `EXPLORE` - Move between LANDMARKS within the current PATCH
- `INVESTIGATE` - Examine CITIZENS and OBJECTS in the current LANDMARK
- `INTERACT` - Engage with an OBJECT (increases TOO CURIOUS counter)
- `CONVERSATE` - Talk with a CITIZEN (increases TOO CURIOUS counter)
- `DISPLAY MAP` - Show your current location and movement options

### Game Mechanics

#### World Structure

The game world is organized hierarchically:
- **PATCHES** - Distinct corporate-controlled territories, each ruled by a different billionaire
- **LANDMARKS** - Specific locations within a PATCH (cities, industrial sites, outposts)
- **CITIZENS** - Characters you can talk to within LANDMARKS
- **OBJECTS** - Items you can interact with within LANDMARKS

#### Navigation

- Use `TRAVEL` to move between adjacent PATCHES in a circular pattern (e.g., PATCH 1 ↔ PATCH 2 ↔ PATCH 3 ↔ PATCH 1)
- Use `EXPLORE` to move between LANDMARKS within the current PATCH in a circular pattern (e.g., LANDMARK 1 ↔ LANDMARK 2 ↔ LANDMARK 3 ↔ LANDMARK 1)

#### Interaction

- Use `INVESTIGATE` to examine CITIZENS and OBJECTS in the current LANDMARK
- Use `INTERACT` to engage with OBJECTS
- Use `CONVERSATE` to talk with CITIZENS

#### TOO CURIOUS Counter

- The TOO CURIOUS counter starts at 0 and increases by 1 each time you use `INTERACT` or `CONVERSATE`
- The counter is displayed at the top of each in-game response
- If the counter reaches 30, you will be "executed" according to the current PATCH's execution sequence
- Each PATCH has its own unique execution sequence

#### Maps

- Use `DISPLAY MAP` to see an ASCII representation of your current location
- Maps show the current PATCH, LANDMARK, and available movement options

### PATCHES Overview

The game features six unique PATCHES, each with its own theme and governance style:

1. **X** - The first PATCH you'll encounter
2. **PRIME** - A mathematically-oriented society
3. **BALAJISTAN** - A territory with unique cultural elements
4. **PRAXIA** - A pragmatic, efficiency-focused community
5. **JEFFERSONIAN** - A territory inspired by historical American ideals
6. **THE WALLED GARDEN** - A highly controlled and isolated community

Each PATCH contains multiple LANDMARKS to explore, and each LANDMARK contains CITIZENS to talk with and OBJECTS to interact with.

### Tips for Playing

- Take your time to explore each PATCH thoroughly
- Talk to CITIZENS to learn about the world and its history
- Be cautious with your curiosity - remember that the TOO CURIOUS counter increases with each interaction
- Use `DISPLAY MAP` frequently to understand your location and movement options
- If you get stuck, try investigating different entities or moving to a different LANDMARK or PATCH

### Troubleshooting

If you encounter any issues while playing:
- Refresh the web client
- Try reconnecting to the game
- Clear your browser cache
- Contact support at support@manus.ai

### Credits

Game developed by Jessybrenens using the Evennia MUD framework.
Deployed and hosted on Manus.ai.
