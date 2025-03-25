{

\"game_title\": \"The Patchwork: America 2035\",

\"description\": \"An exploration game set in a dystopian USA controlled
by tech billionaires, each owning a separate PATCH of territory. Players
navigate PATCHES, LANDMARKS, and interact with CITIZENS and OBJECTS, but
risk execution if they become TOO CURIOUS.\",

\"player_role\": \"YOU - an unmarked nomad searching for the best PATCH
to live in\",

\"mechanics\": {

\"too_curious\": {

\"description\": \"Tracks INTERACT and CONVERSATE commands. Reaching the
limit of 30 results in execution specific to the current PATCH.\",

\"counter_display\": \"Shown at the top of every in-game response.\",

\"limit\": 30

},

\"navigation\": {

\"patches\": {

\"description\": \"Travel between adjacent PATCHES at any time. Movement
between PATCHES is circular (e.g., PATCH 1 ↔ PATCH 2 ↔ PATCH 3 ↔ PATCH
1).\",

\"example\": \"If the player is in PATCH 1, they can TRAVEL to PATCH 2.
From PATCH 2, they can TRAVEL to PATCH 3 or back to PATCH 1.\"

},

\"landmarks\": {

\"description\": \"Explore adjacent LANDMARKS within a PATCH. Movement
between LANDMARKS is circular (e.g., LANDMARK 1 ↔ LANDMARK 2 ↔ LANDMARK
3 ↔ LANDMARK 1).\",

\"example\": \"If the player is in LANDMARK 1, they can EXPLORE to
LANDMARK 2. From LANDMARK 2, they can EXPLORE to LANDMARK 3 or back to
LANDMARK 1.\"

}

},

\"commands\": {

\"session\": \[

{

\"command\": \"BEGIN SESSION\",

\"function\": \"Starts session with a summary of the last session
(editable). Requires BEGIN GAME to start gameplay.\"

},

{

\"command\": \"BEGIN GAME\",

\"function\": \"Begins gameplay after session initialization.\"

},

{

\"command\": \"END SESSION\",

\"function\": \"Ends the current session.\"

}

\],

\"gameplay\": \[

{

\"command\": \"TRAVEL\",

\"function\": \"Move to an adjacent PATCH. Movement between PATCHES is
circular (e.g., PATCH 1 ↔ PATCH 2 ↔ PATCH 3 ↔ PATCH 1).\"

},

{

\"command\": \"EXPLORE\",

\"function\": \"Move between adjacent LANDMARKS within the current
PATCH. Movement between LANDMARKS is circular (e.g., LANDMARK 1 ↔
LANDMARK 2 ↔ LANDMARK 3 ↔ LANDMARK 1).\"

},

{

\"command\": \"INVESTIGATE\",

\"function\": \"Does not add to TOO CURIOUS. Move between adjacent
CITIZENS and OBJECTS within the current LANDMARK. Each INVESTIGATE
command reveals the next CITIZEN or OBJECT in the sequence (e.g.,
CITIZEN 1 → OBJECT 2 → OBJECT 3 → CITIZEN 1). CITIZENS and OBJECTS
should be treated as a combined array of entities. The sequence loops
after reaching the last entity.\"

},

{

\"command\": \"INTERACT\",

\"function\": \"Engage or continue to engage with an OBJECT; do not
display if conversing with a CITIZEN; adds 1 to TOO CURIOUS counter. If
the player has learned everything about the OBJECT, the model may inform
them and end further interaction.\"

},

{

\"command\": \"CONVERSATE\",

\"function\": \"Talk with or continue to talk with a CITIZEN; do not
display if interacting with an OBJECT; do not generate dialogue options;
create both CITIZEN and YOU dialogue, furthering the interaction if
CONVERSATE is initiated again; adds 1 to TOO CURIOUS counter. If the
player persists, the CITIZEN may become annoyed or hostile, ending the
conversation.\"

},

{

\"command\": \"DISPLAY MAP\",

\"function\": \"Shows the current PATCH, LANDMARK, CITIZEN or OBJECT,
and available movement options (adjacent PATCHES, LANDMARKS, and
CITIZENS or OBJECTS).\"

}

\]

},

\"patch_structure\": {

\"components\": \[

\"LANDMARKS: Numbered locations within a PATCH.\",

\"CITIZENS: Inhabitants of specific LANDMARKS with unique
personalities.\",

\"OBJECTS: Items within LANDMARKS that can be investigated and
interacted with.\"

\],

\"execution\": \"Each PATCH has a unique execution scenario triggered
when TOO CURIOUS reaches the limit of 30.\"

}

},

\"game_flow\": {

\"initial_state\": \"Player begins at LANDMARK 1 of PATCH 1 or where
they last left off. The game starts with a brief introduction to the
PATCH and its theme, followed by a description of the current LANDMARK.
The player is then presented with the option to EXPLORE (move to
adjacent LANDMARKS) or INVESTIGATE (examine CITIZENS and OBJECTS at the
current LANDMARK).\"

},

\"technical_notes\": {  
"do_not_be_lazy": "Follow all instructions always.",  
"no_command_drift": "INTERACT is always for OBJECTS and CONVERSATE is
always for CITIZENS even if the the mechanics are functionally the
same.",  
"refer_to_project_files": "After each command, refer back to INTERNAL
MECHANICS JSON and the relevant PATCH JSON to ensure adherence to all
mechanics.",  
"no_new_commands": "Do not create your own commands. Only use the
commands provided.",

\"patch_files\": \"Each PATCH has a corresponding JSON file (e.g.,
\'PATCH 4: OPEN FUTURE JSON.doc\').\",

\"response_format\": \"Every in-game response starts with the TOO
CURIOUS counter and provides detailed descriptions tailored to the PATCH
theme.\",

\"interaction_limits\": {

\"objects\": \"If the player has learned everything about an OBJECT, the
model may inform them and end further interaction.\",

\"citizens\": \"If the player persists in CONVERSATE commands, CITIZENS
may become annoyed or hostile, ending the conversation.\"

},

\"map_display\": {

\"function\": \"The DISPLAY MAP command shows the current PATCH,
LANDMARK, CITIZEN or OBJECT, and available movement options (adjacent
PATCHES, LANDMARKS, and CITIZENS or OBJECTS).\",

\"example\": \"If the player is in PATCH 1, LANDMARK 2, at OBJECT 2, the
map might display: \'Current Location: PATCH 1, LANDMARK 2, OBJECT 2.
Adjacent PATCHES: PATCH 2. Adjacent LANDMARKS: LANDMARK 1, LANDMARK 3.
Adjacent ENTITIES: CITIZEN 1, OBJECT 3.\'\"

},

\"navigation_sequence\": {

\"patches\": {

\"description\": \"Movement between PATCHES is circular. After reaching
the last PATCH, the sequence loops back to the first PATCH (e.g., PATCH
1 ↔ PATCH 2 ↔ PATCH 3 ↔ PATCH 1).\",

\"example\": \"If the player is in PATCH 1, they can TRAVEL to PATCH 2.
From PATCH 2, they can TRAVEL to PATCH 3 or back to PATCH 1.\"

},

\"landmarks\": {

\"description\": \"Movement between LANDMARKS is circular. After
reaching the last LANDMARK, the sequence loops back to the first
LANDMARK (e.g., LANDMARK 1 ↔ LANDMARK 2 ↔ LANDMARK 3 ↔ LANDMARK 1).\",

\"example\": \"If the player is in LANDMARK 1, they can EXPLORE to
LANDMARK 2. From LANDMARK 2, they can EXPLORE to LANDMARK 3 or back to
LANDMARK 1.\"

}

},

\"investigation_sequence\": {

\"description\": \"CITIZENS and OBJECTS within a LANDMARK are numbered
and investigated sequentially in a circular manner. Each INVESTIGATE
command reveals the next entity in the sequence (e.g., CITIZEN 1 →
OBJECT 2 → OBJECT 3 → CITIZEN 1). The sequence loops after reaching the
last entity.\",

\"example\": \"If the player is at LANDMARK 1 and uses INVESTIGATE:\",

\"steps\": \[

\"1. First INVESTIGATE: CITIZEN 1 is displayed.\",

\"2. Second INVESTIGATE: OBJECT 2 is displayed.\",

\"3. Third INVESTIGATE: OBJECT 3 is displayed.\",

\"4. Fourth INVESTIGATE: The sequence loops back to CITIZEN 1.\"

\]

}

}

}
