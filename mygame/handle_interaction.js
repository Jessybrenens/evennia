// Function to handle player's interaction choice
function handleInteractionChoice(choice) {
    // Convert choice to number and validate
    const choiceNum = parseInt(choice);
    
    if (isNaN(choiceNum) || choiceNum < 1 || choiceNum > gameState.interactionOptions.length) {
        print('Invalid choice. Please enter a valid number.', 'red');
        return;
    }
    
    // Get the selected interaction/conversation
    const selected = gameState.interactionOptions[choiceNum - 1];
    
    if (gameState.interactionMode === 'object') {
        // Handle object interaction
        print(`\nYou ${selected.action.toLowerCase()}.`, 'cyan');
        print(selected.result, 'white');
    } else if (gameState.interactionMode === 'citizen') {
        // Handle citizen conversation
        print(`\nYou: "${selected.prompt}"`, 'cyan');
        print(`${gameState.currentEntity.name}: "${selected.response}"`, 'yellow');
    }
    
    // Reset interaction mode
    gameState.interactionMode = null;
    gameState.interactionOptions = null;
}
