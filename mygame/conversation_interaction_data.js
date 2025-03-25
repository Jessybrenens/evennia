// Conversation and Interaction Data
const conversationData = {
    // Citizen conversations for each patch
    patch1: {
        citizen1: [
            { prompt: "What is your role here?", response: "I monitor efficiency metrics for this sector. All activities must maintain optimal resource utilization." },
            { prompt: "How do you like living in X?", response: "Preference is irrelevant. I function at 98.7% efficiency in this environment, which is satisfactory." },
            { prompt: "Do you ever wish for more color or variety?", response: "Such desires would be inefficient. Uniformity eliminates decision fatigue and maximizes cognitive resources for productive tasks." }
        ],
        citizen2: [
            { prompt: "What's your name?", response: "I am Resident 1729. Names are inefficient identifiers compared to numerical designations." },
            { prompt: "What do you do for fun?", response: "Recreation is scheduled for 30 minutes daily. I optimize this time by engaging in approved cognitive exercises that improve processing efficiency." },
            { prompt: "Do you ever leave X?", response: "Travel outside our optimization zone would introduce unnecessary variables and reduce efficiency. I remain here." }
        ]
    }
};

const interactionData = {
    // Object interactions for each patch
    patch1: {
        object1: [
            { action: "Press the button", result: "The terminal activates, displaying a stream of efficiency metrics for various sectors of X. Every process has been optimized to use minimal resources." },
            { action: "Examine the terminal", result: "The terminal is designed with absolute minimalism—a single white button on a white surface. No decorative elements exist." }
        ],
        object2: [
            { action: "Request food", result: "The dispenser produces a precisely measured portion of gray nutrient paste. It contains exactly the calories and nutrients required for optimal human function." },
            { action: "Examine the dispenser", result: "The nutrition dispenser is a white cube with a single dispensing slot. No controls are visible—it automatically provides the optimal nutrition at designated times." }
        ]
    }
};
