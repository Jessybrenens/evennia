# Test Script for The Patchwork Game

This script outlines the testing procedures for verifying the functionality of The Patchwork game.

## 1. Server Startup Test

```bash
# Navigate to the evennia directory
cd /home/ubuntu/evennia

# Start the evennia server
evennia start
```

Expected result: Server starts successfully, initializing the game world and loading ASCII maps.

## 2. Connection Test

Connect to the game using a MUD client or the web client at http://localhost:4001.

Expected result: Connection screen displays with welcome message and basic commands.

## 3. Character Creation Test

Create a new character or use the default Admin character.

Expected result: Character is created successfully and can be controlled.

## 4. Session Command Tests

Test the following session commands:
- BEGIN SESSION
- BEGIN GAME
- END SESSION

Expected result: 
- BEGIN SESSION displays introduction to the game
- BEGIN GAME starts gameplay and places character in Patch 1, Landmark 1
- END SESSION ends the current game session

## 5. Navigation Tests

Test the following navigation commands:
- TRAVEL (to move between patches)
- EXPLORE (to move between landmarks)

Expected result:
- TRAVEL allows movement between adjacent patches in a circular pattern
- EXPLORE allows movement between landmarks within a patch in a circular pattern
- Current location is correctly updated and displayed

## 6. Interaction Tests

Test the following interaction commands:
- INVESTIGATE (to examine citizens and objects)
- INTERACT (to engage with objects)
- CONVERSATE (to talk with citizens)

Expected result:
- INVESTIGATE allows examination of citizens and objects in the current landmark
- INTERACT allows engagement with objects and increases TOO CURIOUS counter
- CONVERSATE allows conversation with citizens and increases TOO CURIOUS counter

## 7. Display Map Test

Test the DISPLAY MAP command.

Expected result: ASCII map of current patch and landmark is displayed correctly, showing current location and movement options.

## 8. TOO CURIOUS Counter Test

Test the TOO CURIOUS counter by repeatedly using INTERACT and CONVERSATE commands.

Expected result:
- Counter increases by 1 for each use of INTERACT or CONVERSATE
- Counter is displayed at the top of each in-game response
- When counter reaches 30, character is executed according to the current patch's execution sequence

## 9. Error Handling Tests

Test error handling by:
- Using commands in invalid contexts
- Providing invalid arguments to commands
- Attempting to access non-existent locations

Expected result: Appropriate error messages are displayed, and the game continues to function correctly.

## 10. Performance Tests

Test performance by:
- Running multiple client connections simultaneously
- Executing commands rapidly
- Navigating quickly between different patches and landmarks

Expected result: Game responds promptly to commands and maintains stability under load.
