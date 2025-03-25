// Test Runner for Game Functionality
document.addEventListener('DOMContentLoaded', function() {
    console.log("Running tests for game functionality...");
    
    // Test TOO CURIOUS counter
    if (verifyTooCuriousCounter()) {
        console.log("✓ TOO CURIOUS counter exists");
    } else {
        console.error("✗ TOO CURIOUS counter test failed");
    }
    
    // Test patch selection limit
    if (verifyPatchSelectionLimit()) {
        console.log("✓ Patch selection limit working correctly");
    } else {
        console.error("✗ Patch selection limit test failed");
    }
    
    // Test page down button creation
    setTimeout(function() {
        const pageDownButton = document.querySelector('.page-down-button');
        if (pageDownButton) {
            console.log("✓ Page down button created successfully");
        } else {
            console.error("✗ Page down button creation failed");
        }
        
        // Test tooltip creation
        const infoTooltip = document.querySelector('.info-tooltip');
        if (infoTooltip) {
            console.log("✓ Info tooltip created successfully");
        } else {
            console.error("✗ Info tooltip creation failed");
        }
    }, 1000);
});
