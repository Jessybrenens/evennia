# mygame/world/data_loader.py
import json
from evennia import create_object
from typeclasses.patches import Patch, Landmark
from typeclasses.entities import Citizen, Game_Object
from evennia.utils import search

def load_game_data():
    """
    Loads game data from JSON files and creates the game world.
    """
    #Helper function to create objects
    def create_entity(landmark, entity_data):
        entity_type = entity_data['type']
        entity_name = entity_data['name']
        entity_key = f"{landmark.key}_{entity_type}_{entity_data['entity_number']}"

        if(entity_type == "CITIZEN"):
            entity = create_object(Citizen, key=entity_key)
        else:
            entity = create_object(Game_Object, key=entity_key)

        entity.db.entity_number = entity_data['entity_number']
        entity.db.description = entity_data['description']
        entity.move_to(landmark, quiet=True)
        return ({"type": entity_type, "entity_number": entity.db.entity_number})

    # Load Patches
    patch_files = [
        "PATCH 1- X JSON [MConverter.eu].md",
        "PATCH 2- PRIME JSON [MConverter.eu].md",
        "PATCH 3- BALAJISTAN JSON [MConverter.eu].md",
        "PATCH 1- PRAXIA JSON.md",
        "PATCH 2- JEFFERSONIAN JSON [MConverter.eu].md",
        "PATCH 3- THE WALLED GARDEN JSON [MConverter.eu].md"
    ]

    for patch_file in patch_files:
        with open(f"world/data/{patch_file}", "r", encoding="utf-8") as f:
            data = json.load(f)

            # Create Patch
            patch_key = f"Patch_{data['patch_number']}"
            patch = create_object(Patch, key=patch_key)
            patch.db.patch_number = data['patch_number']
            patch.db.patch_name = data['patch_name']
            patch.db.motto = data['motto']
            patch.db.location = data['location']
            patch.db.governance_style = data['governance_style']
            patch.db.leader_title = data['leader_title']
            patch.db.citizenship_requirements = data['citizenship_requirements']
            patch.db.overview = data['overview']
            patch.db.execution_sequence = data['execution_sequence']
            patch.cmdset.add_default(PatchCmdSet, permanent=True) #Add commands

            # Create Landmarks
            for landmark_data in data['landmarks']:
                landmark_key = f"{patch_key}_Landmark_{landmark_data['landmark_number']}"
                landmark = create_object(Landmark, key=landmark_key)
                landmark.db.landmark_number = landmark_data['landmark_number']
                landmark.db.landmark_name = landmark_data['landmark_name']
                landmark.db.description = landmark_data['description']
                landmark.cmdset.add_default(LandmarkCmdSet, permanent=True) #Add commands
                landmark.move_to(patch)  # Place Landmark inside Patch

                #Create entities
                landmark.db.entities = [create_entity(landmark, entity) for entity in landmark_data['entities']]

            #Add landmarks to patch
            patch.db.landmarks = [f"{patch_key}_Landmark_{x+1}" for x in range(len(data['landmarks']))]

    print("Game world created from JSON data.")
