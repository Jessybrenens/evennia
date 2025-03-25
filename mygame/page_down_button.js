// Page Down Button Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Find the game output element
    const gameOutput = document.querySelector('.output') || document.querySelector('#output');
    
    // Create button element
    const pageDownButton = document.createElement('div');
    pageDownButton.className = 'page-down-button';
    pageDownButton.innerHTML = '↓';
    pageDownButton.title = 'Page Down';
    
    // Create info tooltip
    const infoTooltip = document.createElement('div');
    infoTooltip.className = 'info-tooltip';
    infoTooltip.innerHTML = 'Click to scroll down. Double-click to return to your last action. Click this message to dismiss.';
    
    // Add elements to the document
    document.body.appendChild(pageDownButton);
    document.body.appendChild(infoTooltip);
    
    // Track if tooltip has been shown
    let tooltipShown = false; // Start with false to show on first use
    
    // Check if we should show the tooltip
    function shouldShowTooltip() {
        // Always show on first use in this session
        if (!tooltipShown) {
            return true;
        }
        return false;
    }
    
    // Track last action position
    let lastActionPosition = 0;
    let lastActionMarker = null;
    
    // Update last action position when game output changes
    if (gameOutput) {
        // Position the button relative to the game output
        function updateButtonPosition() {
            const commandsContainer = document.querySelector('#commands');
            if (commandsContainer) {
                const rect = commandsContainer.getBoundingClientRect();
                pageDownButton.style.top = (rect.top - 60) + 'px';
                infoTooltip.style.top = (rect.top - 60) + 'px';
            }
        }
        
        // Initial positioning
        setTimeout(updateButtonPosition, 500);
        
        // Update position on window resize
        window.addEventListener('resize', updateButtonPosition);
        
        const observer = new MutationObserver(function(mutations) {
            // Store the current scroll position as the last action position
            lastActionPosition = gameOutput.scrollTop;
            
            // Create or update a marker for the last action
            if (lastActionMarker) {
                lastActionMarker.remove();
            }
            
            // Create a hidden marker at the current position
            lastActionMarker = document.createElement('div');
            lastActionMarker.id = 'last-action-marker';
            lastActionMarker.style.position = 'absolute';
            lastActionMarker.style.height = '1px';
            lastActionMarker.style.width = '1px';
            lastActionMarker.style.opacity = '0';
            lastActionMarker.dataset.position = lastActionPosition;
            
            // Insert the marker
            gameOutput.appendChild(lastActionMarker);
            
            // Update button position in case layout changed
            updateButtonPosition();
        });
        
        observer.observe(gameOutput, { childList: true, subtree: true });
    }
    
    // Single click handler - scroll down
    pageDownButton.addEventListener('click', function(e) {
        // Prevent double click from triggering this twice
        if (e.detail === 1) {
            setTimeout(function() {
                if (!tooltipShown) {
                    infoTooltip.classList.add('visible');
                    tooltipShown = true;
                    
                    // Auto-hide tooltip after 10 seconds
                    setTimeout(function() {
                        infoTooltip.classList.remove('visible');
                    }, 10000);
                }
                
                // Scroll down logic
                if (gameOutput) {
                    // Get the last visible line position
                    const lineHeight = parseInt(window.getComputedStyle(gameOutput).lineHeight) || 20;
                    const visibleLines = Math.floor(gameOutput.clientHeight / lineHeight);
                    const scrollAmount = lineHeight * visibleLines;
                    
                    // Scroll so the last visible line becomes the top line
                    gameOutput.scrollBy({
                        top: scrollAmount,
                        behavior: 'smooth'
                    });
                } else {
                    // Fallback for general page scrolling
                    const lineHeight = 20; // Estimate line height
                    const visibleLines = Math.floor(window.innerHeight / lineHeight);
                    const scrollAmount = lineHeight * visibleLines;
                    
                    window.scrollBy({
                        top: scrollAmount,
                        behavior: 'smooth'
                    });
                }
            }, 200); // Small delay to allow for double click detection
        }
    });
    
    // Double click handler - return to last action
    pageDownButton.addEventListener('dblclick', function() {
        if (gameOutput) {
            // Find the marker if it exists
            const marker = document.getElementById('last-action-marker');
            if (marker && marker.dataset.position) {
                // Scroll to the stored position
                gameOutput.scrollTop = parseInt(marker.dataset.position);
            } else {
                // Fallback to the tracked position
                gameOutput.scrollTop = lastActionPosition;
            }
            
            // Visual feedback for double-click action
            pageDownButton.style.backgroundColor = '#00aa00';
            setTimeout(() => {
                pageDownButton.style.backgroundColor = '';
            }, 300);
        }
    });
    
    // Hide tooltip when clicked
    infoTooltip.addEventListener('click', function() {
        infoTooltip.classList.remove('visible');
    });
});
