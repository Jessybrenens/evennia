// Conversation data from citizen_conversations.md
const conversationData = {
    // PATCH 1: "X" Citizens
    patch1: {
        citizen1: {
            greeting: "Citizen, your presence has been noted. State your purpose.",
            conversations: [
                { prompt: "What is your role here?", response: "I monitor productivity metrics to ensure optimal efficiency. All citizens must contribute at maximum capacity with minimal resource expenditure. Inefficiency is waste. Waste is prohibited." },
                { prompt: "Tell me about X.", response: "X is the optimal social structure. We have eliminated the inefficiency of choice. All decisions are calculated by our algorithms to maximize output. The absence of choice eliminates anxiety, indecision, and error." },
                { prompt: "Do you ever miss having choices?", response: "Your question contains a logical fallacy. One cannot 'miss' what is demonstrably inefficient. Studies show decision fatigue reduces productivity by 27.4%. The elimination of choice has increased our efficiency by 42.8%. The data is conclusive." },
                { prompt: "What happens to people who don't follow the rules?", response: "Non-compliance is a system error. System errors are corrected. Repeat errors are eliminated. This is not punishment. It is maintenance. The system must function optimally." }
            ]
        },
        citizen2: {
            greeting: "Hello. You are not from Block A. Your jumpsuit is non-standard.",
            conversations: [
                { prompt: "What's it like living here?", response: "Living conditions are optimal. My housing unit provides 27.3 square meters of space, which is sufficient. Meals are nutritionally complete. Sleep is uninterrupted. Work is assigned according to aptitude. There is no inefficiency." },
                { prompt: "Do you have a name besides your number?", response: "Names are inefficient identifiers. They contain unnecessary syllables and create ambiguity. Numbers are precise. I am Resident 1729. The number is sufficient." },
                { prompt: "Are you happy here?", response: "Happiness is an imprecise metric. I am productive. My health indicators are within optimal parameters. My assigned tasks are completed with 98.7% efficiency. These are the relevant measurements." },
                { prompt: "What do you do for fun?", response: "Fun is an inefficient allocation of time. I have 42 minutes of designated leisure activity daily, during which I engage in approved physical movement to maintain optimal body function. Entertainment is unnecessary." }
            ]
        },
        citizen3: {
            greeting: "Technician XM-42 reporting. This area is operating at 99.8% efficiency. State your purpose.",
            conversations: [
                { prompt: "What do you maintain here?", response: "I maintain the automation systems that produce all necessary goods. The robots require minimal intervention. My primary function is preventative maintenance to ensure zero downtime. Downtime is inefficiency. Inefficiency is waste." },
                { prompt: "Have you ever been outside X?", response: "Negative. External environments are inefficient. They contain variables that cannot be controlled. Variables reduce predictability. Unpredictability reduces efficiency. I remain where I am optimally useful." },
                { prompt: "Do the robots ever malfunction?", response: "Malfunctions occur at a rate of 0.02%. This is within acceptable parameters. When malfunctions occur, the unit is immediately replaced. Repair is less efficient than replacement for units below threshold value." },
                { prompt: "What do you think about the other patches?", response: "Other patches operate at sub-optimal efficiency. Their retention of choice architecture creates waste. Their diversity of output is unnecessary. Their emotional attachments to inefficient systems is illogical. They will eventually optimize or become obsolete." }
            ]
        }
    },
    
    // PATCH 2: "PRIME" Citizens
    patch2: {
        citizen1: {
            greeting: "Fascinating! Your arrival has a 0.0034% probability. I must recalibrate my models.",
            conversations: [
                { prompt: "What are you working on?", response: "I'm analyzing pattern fluctuations in social interaction matrices. The equations reveal beautiful symmetries when properly mapped. Every human behavior can be reduced to elegant mathematical expressions. The universe speaks in numbers, and I am merely translating." },
                { prompt: "Tell me about PRIME.", response: "PRIME is the natural evolution of society. We've stripped away the messy irrationality of human systems and rebuilt based on pure mathematical principles. Our resource allocation algorithms operate at 99.97% efficiency. Our social harmony index is at an all-time high of 94.3. The numbers don't lie." },
                { prompt: "Is everything here based on math?", response: "Of course! Math is the only objective truth. Our buildings follow Fibonacci sequences. Our work schedules align with prime number intervals to maximize productivity. Even our dating system pairs individuals based on complementary equation sets. Love is simply chemistry expressed as mathematics." },
                { prompt: "What about art and creativity?", response: "Art is pattern recognition. Creativity is novel pattern generation. We've developed algorithms that produce music with perfect mathematical harmony, visual art with ideal proportions, and literature with optimal narrative structures. The results are objectively superior to chaotic human creation." }
            ]
        },
        citizen2: {
            greeting: "Welcome, observer! Your presence has collapsed several interesting probability waves.",
            conversations: [
                { prompt: "What does your quantum computer do?", response: "Our quantum systems operate in superposition, exploring all possible solutions simultaneously. We're currently modeling societal outcomes for the next 200 years with 89.7% accuracy. The multiverse is just mathematics in motion, and we're mapping every branch." },
                { prompt: "How does PRIME govern itself?", response: "Governance is an optimization problem. Our quantum systems calculate the most efficient resource allocation and policy decisions. Human oversight exists only to verify the elegance of the solutions. The most beautiful equation always yields the most just outcome." },
                { prompt: "Do you ever make mistakes?", response: "Mistakes are simply iterations toward optimization. When our predictions deviate from outcomes, we don't see failure—we see data. Each discrepancy refines our models. Even chaos follows mathematical principles when viewed at sufficient scale." },
                { prompt: "What do you think of the other patches?", response: "Other patches are operating with incomplete datasets and inferior algorithms. BALAJISTAN's chaos is merely unrecognized pattern. X's minimalism lacks mathematical elegance. The JEFFERSONIAN's democracy is inefficient without proper weighting functions. They'll all converge on our methods eventually—it's mathematically inevitable." }
            ]
        },
        citizen3: {
            greeting: "Ah, a new variable in my garden equation! Welcome to the Fibonacci Gardens.",
            conversations: [
                { prompt: "What makes these gardens special?", response: "Every aspect follows mathematical principles. The spiral patterns of our plantings follow the golden ratio. The height differentials create perfect harmonic progressions. Even the color distribution follows optimal contrast equations. Nature itself is mathematics made visible." },
                { prompt: "Do you enjoy working here?", response: "Enjoyment is the recognition of pattern harmony. When I trim these hedges to maintain perfect proportions, I'm not just gardening—I'm solving equations in physical form. There's profound satisfaction in bringing the abstract into material reality." },
                { prompt: "What's your favorite mathematical concept?", response: "I'm particularly fond of the Mandelbrot Set. Infinite complexity emerging from simple recursive equations. That's what we're building here in PRIME—a society of beautiful complexity emerging from elegant foundational principles. The mathematics of human potential is boundless." },
                { prompt: "Do visitors appreciate the mathematical design?", response: "Some see only pretty flowers. Others glimpse the underlying patterns. The most enlightened visitors understand that the aesthetic beauty and the mathematical precision are one and the same. Beauty is truth, truth beauty—that is all ye know on earth, and all ye need to know. Keats was a mathematician at heart." }
            ]
        }
    },
    
    // PATCH 3: "BALAJISTAN" Citizens
    patch3: {
        citizen1: {
            greeting: "Hey! Perfect timing! I'm pivoting my business model and you could be my first customer! Or investor? Or co-founder?",
            conversations: [
                { prompt: "What's your current startup?", response: "I'm disrupting the disruption industry! It's a platform that helps startups pivot faster by randomly generating new business models every 72 hours. We've pivoted 17 times this month alone! Our burn rate is astronomical but our optionality quotient is off the charts!" },
                { prompt: "Tell me about BALAJISTAN.", response: "BALAJISTAN is creative destruction incarnate! We tear down yesterday's innovations to build tomorrow's obsolescence! Nothing lasts more than a quarter here—buildings, relationships, identities—it's all fluid! Permanence is death! Change is the only constant! Move fast and break EVERYTHING!" },
                { prompt: "Isn't all this change exhausting?", response: "Exhaustion is just disruption of the energy sector! I sleep in 15-minute micronaps between pivots. I've had 12 different jobs this week! My personal identity has pivoted from crypto-maximalist to AI-skeptic to bio-optimist since breakfast! It's exhilarating! Want some nootropics? They're new! Brand new! Newer than new!" },
                { prompt: "What happens to people who can't keep up?", response: "They become cautionary tales! Or case studies! Or vintage! Some people are still running business models from LAST MONTH if you can believe it! Dinosaurs! But even failure is just pre-success here! I've failed 143 times! Each failure adds to my founder story! My TED talk is going to be EPIC! Want to invest in my next pivot?" }
            ]
        },
        citizen2: {
            greeting: "I just disrupted the greeting industry with this revolutionary new hello! Want to join my cap table?",
            conversations: [
                { prompt: "How many companies have you started?", response: "I'm currently CEO of 17 startups simultaneously! Sleep is for people without vision! I've founded 143 companies in the last year alone! Most failed spectacularly, which makes my founder journey even more compelling! Failure is just pre-unicorn status! My portfolio of pivots is unmatched in the ecosystem!" },
                { prompt: "How do you make money here?", response: "Revenue is an outdated metric! We measure success in TAM, burn rate, and narrative potential! I've raised $50M for a company with no product, $100M for a product with no market, and $200M for a market with no problem! The key is storytelling! Reality is just another variable to optimize! Want to see my pitch deck? It has 347 slides!" },
                { prompt: "Is there any stability in BALAJISTAN?", response: "Stability is stagnation! Our buildings are modular and reconfigure weekly! Our relationships are term-limited with renewal options! Even our physical appearances change constantly—I've had seven different biotech enhancements installed this month alone! My blood is 30% experimental compounds! I've never felt better! Or worse! It's impossible to tell! Isn't that EXCITING?" },
                { prompt: "What's your long-term plan?", response: "Long-term? That's dinosaur thinking! I plan in nano-epochs! By this afternoon, I'll have pivoted to an entirely new industry! By tomorrow, I'll have disrupted that industry! By next week, I'll have made that disruption obsolete! The only constant is acceleration! The only strategy is optionality! The only reality is narrative! Want to join my next venture? It's going to change EVERYTHING for at least 72 hours!" }
            ]
        },
        citizen3: {
            greeting: "You're just in time for my ICO! We're tokenizing the concept of tokenization itself! Meta-tokens! Revolutionary!",
            conversations: [
                { prompt: "What does your company actually do?", response: "Do? DO? That's such a Web2 question! We don't DO anything—we ENABLE everything! We're a platform for platforms! A protocol for protocols! We're building the infrastructure for the infrastructure of the future! Our whitepaper has 347 pages but zero technical specifications because we're THAT disruptive!" },
                { prompt: "How is BALAJISTAN governed?", response: "Governance is a DAO of DAOs! Every decision requires a token-weighted vote that can be instantly overturned by a counter-vote with more tokens! Leadership changes hourly! Laws are smart contracts with built-in expiration dates! Nothing persists! Everything is contestable! It's pure liquid democracy accelerated to the point of quantum uncertainty!" },
                { prompt: "Is there anything permanent here?", response: "Only our commitment to impermanence! Even our physical infrastructure is designed to be obsolete within months! Our buildings have planned demolition dates! Our roads automatically reconfigure! Our identities are fluid! I've been seven different people since breakfast! Each identity has its own token! Want to buy some? The price is incredibly volatile!" },
                { prompt: "What happens when people get older?", response: "Aging is just a disruption opportunity! We have longevity startups competing to reverse, accelerate, pause, or gamify the aging process! I'm chronologically 37 but biologically somewhere between 25 and 62 depending on which experimental treatment is currently active in my system! Consistency is death! Homeostasis is for the unambitious! Live fast, pivot young, leave a confusing legacy!" }
            ]
        }
    },
    
    // PATCH 4: "PRAXIA" Citizens
    patch4: {
        citizen1: {
            greeting: "I notice you took an inefficient path to this location. I can help optimize your movement patterns.",
            conversations: [
                { prompt: "What do you do here?", response: "I measure, analyze, and improve practical workflows. Every motion should have purpose. Every system should produce tangible results. In PRAXIA, we don't theorize—we optimize. Last month, I reduced the average citizen's daily walking distance by 0.7 miles while increasing productivity by 12%. That's not a concept. That's a result." },
                { prompt: "Tell me about PRAXIA.", response: "PRAXIA is where ideas meet implementation. Other patches debate philosophies or chase disruption. We build solutions that work. Our buildings are functional. Our systems are tested. Our society produces measurable outcomes. We don't have time for abstractions that don't improve real lives." },
                { prompt: "Do you value creativity?", response: "We value practical creativity. A beautiful idea that solves no problems is just mental decoration. Show me creativity that reduces suffering, increases efficiency, or solves tangible problems. In PRAXIA, your imagination is judged by what it produces, not what it envisions." },
                { prompt: "What's wrong with the other patches?", response: "X sacrifices humanity for efficiency. PRIME mistakes equations for reality. BALAJISTAN confuses movement with progress. JEFFERSONIAN wastes time debating what should be tested. THE WALLED GARDEN solves problems by pretending they don't exist. None of them ask the only question that matters: Does it work in practice, not just in theory?" }
            ]
        },
        citizen2: {
            greeting: "You look like you have a problem that needs solving. Specific parameters would help me assist you better.",
            conversations: [
                { prompt: "What kinds of problems do you solve?", response: "I specialize in tangible challenges with measurable outcomes. Water purification systems for outlying communities. Modular housing that can be assembled in hours. Agricultural techniques that increase yield while reducing resource use. I don't write papers—I build prototypes. I don't debate solutions—I implement and refine them." },
                { prompt: "How does PRAXIA approach education?", response: "We teach by doing. Our children spend mornings learning fundamentals and afternoons applying them to real projects. A ten-year-old here can build a solar circuit, grow food, and repair basic machinery. Theory without application is just trivia. In PRAXIA, knowledge is measured by what you can create with it." },
                { prompt: "Do you ever relax or have fun?", response: "Recreation in PRAXIA is purposeful. We play games that build skills. We create art that serves functions. Even our celebrations include community improvement projects. This doesn't mean we don't enjoy ourselves—we simply find satisfaction in utility. The joy of solving real problems is profound." },
                { prompt: "What's your biggest challenge here?", response: "Resource constraints always limit implementation. We must constantly balance immediate needs against long-term solutions. Sometimes a quick fix now prevents a better solution later. The hardest part is knowing when to patch a system and when to rebuild it entirely. Theory is infinite—materials, time, and energy are not." }
            ]
        },
        citizen3: {
            greeting: "Welcome to Results Park. Would you like me to quantify the impact of our implementations?",
            conversations: [
                { prompt: "What results are you most proud of?", response: "Our water reclamation system reduced consumption by 47% while improving quality metrics. Our modular housing initiative decreased construction waste by 82% and homelessness by 94%. Our distributed healthcare model increased access by 73% while reducing costs by 31%. These aren't projections or promises—they're measured outcomes from implemented solutions." },
                { prompt: "How do you measure success?", response: "Success has specific metrics: Lives improved. Resources conserved. Problems solved. Suffering reduced. Time saved. We establish baselines before implementation and measure outcomes after. The data doesn't lie. A solution either works or it doesn't. If it doesn't work, we modify or abandon it. No attachment to failed approaches, no matter how elegant they seemed in theory." },
                { prompt: "Do you share your solutions with other patches?", response: "We freely share proven implementations. Our designs, methods, and results are open-source. Some patches adopt our solutions; others are too attached to their ideologies to implement practical fixes. We don't force our approaches on anyone, but we document everything. Reality is the ultimate arbiter of what works." },
                { prompt: "What's your next big project?", response: "We're implementing a closed-loop manufacturing system that reduces waste to near-zero levels. Initial tests show 96% resource recovery with minimal energy input. The prototype is running now, and we're gathering data on durability and maintenance requirements. If the real-world results match our projections, we'll scale it across PRAXIA within six months." }
            ]
        }
    }
};

// Object interaction data
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
        ],
        object3: [
            { action: "Observe the robot's work", result: "The robot arm moves with hypnotic precision, assembling components at a rate of one unit every 4.7 seconds. Each movement is identical to the last, with no wasted motion. A small display shows its efficiency rating: 99.97%." },
            { action: "Try to interrupt the robot's sequence", result: "As your hand approaches, a red light activates. A voice states: 'Interference with optimization processes is prohibited. Step back to avoid injury.' The robot continues its work, unaffected by your presence." }
        ]
    },
    patch2: {
        object1: [
            { action: "Study the changing symbols", result: "As you watch, complex equations flow across the surface of the pillar. You recognize elements of calculus, quantum mechanics, and number theory, but they're integrated in ways you've never seen before." },
            { action: "Touch the pillar", result: "When your fingers contact the surface, the equations respond to your touch, swirling around your hand. You feel a slight tingling sensation as the pillar samples your bioelectrical field." }
        ],
        object2: [
            { action: "Observe the quantum core", result: "The cube exists in a state of quantum superposition, simultaneously solid and transparent. Within it, you glimpse what appear to be multiple realities overlapping—the same space with different configurations." },
            { action: "Ask about its function", result: "A nearby terminal activates: 'The Quantum Core processes calculations across multiple probability states simultaneously. Current processing capacity: 10^86 operations per second.'" }
        ],
        object3: [
            { action: "Study the sculpture's proportions", result: "The sculpture spirals with perfect mathematical precision, each segment relating to the next by exactly 1.618033988749895... (φ). As you observe its proportions, you feel a strange sense of satisfaction." },
            { action: "Touch the sculpture", result: "The metal is warm to the touch. As your fingers trace the spiral, small lights activate along the path, highlighting the Fibonacci sequence embedded in the design. A soft harmonic tone plays." }
        ]
    },
    patch3: {
        object1: [
            { action: "Press the generate button", result: "The machine whirs dramatically and displays: 'BLOCKCHAIN PET FOOD DELIVERY FOR THE METAVERSE!' A small ticker at the bottom shows this is idea #7,392,418 generated today." },
            { action: "Request a different idea", result: "The machine spins even more dramatically than before, emitting unnecessary smoke effects. New text appears: 'AI-POWERED SUBSCRIPTION BOXES FOR QUANTUM COMPUTING!'" }
        ],
        object2: [
            { action: "Submit a business plan", result: "The terminal scans your plan for exactly 3.7 seconds before responding: 'FUNDING APPROVED! $2.3M SEED ROUND AT $45M VALUATION!' Money instantly transfers to a newly created company account." },
            { action: "Ask about the evaluation criteria", result: "The terminal displays: 'Primary funding criteria: 1) Buzzword density (37%), 2) Founder narrative arc (26%), 3) Disruptive potential (22%), 4) Actual viability (4%), 5) Random chance (11%).'" }
        ],
        object3: [
            { action: "Insert your failing business concept", result: "The Pivot Machine absorbs your business details and immediately begins transforming them. Finally, it presents your pivoted concept: your same product, but now 'powered by AI' and 'built for the metaverse.'" },
            { action: "Check the pivot history", result: "The machine displays famous pivots: 'Twitter: SMS service → social network. Slack: game company → business chat. PIVOT-O-MATIC 3000: toilet paper dispenser → blockchain authentication → pet psychiatry → finally, the Pivot Machine itself!'" }
        ]
    },
    patch4: {
        object1: [
            { action: "Test the prototype", result: "You activate the water purification system. It hums quietly, processing contaminated water through a series of filters and membranes. Within moments, clean water flows from the output pipe. A display shows: '99.7% contaminant removal, 0.3kWh energy used.'" },
            { action: "Examine the design", result: "The system is elegantly practical. Every component serves a clear purpose. The materials are durable but affordable. Maintenance access points are clearly marked. Instructions are engraved directly into the casing—no manual to lose. This was designed to work reliably for years with minimal intervention." }
        ],
        object2: [
            { action: "Open the toolkit", result: "The compact case unfolds to reveal dozens of precisely organized tools. Each has multiple functions. The hammer head detaches to reveal screwdriver bits. The wrench handles contain measuring devices. Everything is durable, practical, and arranged for maximum efficiency." },
            { action: "Read the usage log", result: "The toolkit's digital log shows it has been used to build 47 structures, repair 239 devices, and teach 184 students. Each use is documented with outcomes and improvements. This isn't just a collection of tools—it's an evolving system refined through practical application." }
        ],
        object3: [
            { action: "Review the data dashboard", result: "The screen displays real-time metrics from across PRAXIA. Energy usage, resource allocation, project completion rates, health outcomes—all visualized clearly. Unlike other patches' abstract or financial metrics, every number here connects directly to tangible quality-of-life improvements." },
            { action: "Input a problem scenario", result: "You describe a theoretical resource shortage. The system processes this and displays three potential solutions, ranked by implementation difficulty, resource requirements, and expected outcomes. Each solution includes prototype designs and test results from similar scenarios. Theory immediately translated to practical action." }
        ]
    }
};
