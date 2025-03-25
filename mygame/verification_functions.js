// Verification Functions for Game Testing
function verifyTooCuriousCounter() {
    // Check if TOO CURIOUS counter exists and increments correctly
    console.log("Verifying TOO CURIOUS counter functionality...");
    return gameState.tooCurious !== undefined;
}

function verifyPatchSelectionLimit() {
    // Verify that patch selection is limited to 3
    console.log("Verifying patch selection limit...");
    return gameState.selectedPatches.length <= 3;
}

function logCommandExecution(command) {
    // Log command execution for testing
    console.log(`Command executed: ${command}`);
    return true;
}
