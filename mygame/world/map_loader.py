# mygame/world/map_loader.py
"""
Module for loading ASCII maps into the game.
"""
from evennia.utils import search
from typeclasses.patches import Patch, Landmark

def load_ascii_maps():
    """
    Load ASCII maps for all patches and landmarks.
    """
    # Patch 1: X
    patch_1_map = """
+------------------------------+
|            PATCH 1           |
|             "X"              |
|                              |
|    [L1]----[L2]              |
|     |                        |
|    [L3]                      |
|                              |
+------------------------------+
"""

    # Patch 2: PRIME
    patch_2_map = """
+------------------------------+
|            PATCH 2           |
|           "PRIME"            |
|                              |
|    [L1]----[L2]----[L3]      |
|                              |
|                              |
|                              |
+------------------------------+
"""

    # Patch 3: BALAJISTAN
    patch_3_map = """
+------------------------------+
|            PATCH 3           |
|         "BALAJISTAN"         |
|                              |
|    [L1]                      |
|     |                        |
|    [L2]----[L3]              |
|                              |
+------------------------------+
"""

    # Patch 4: PRAXIA
    patch_4_map = """
+------------------------------+
|            PATCH 4           |
|           "PRAXIA"           |
|                              |
|    [L1]----[L3]              |
|     |                        |
|    [L2]                      |
|                              |
+------------------------------+
"""

    # Patch 5: JEFFERSONIAN
    patch_5_map = """
+------------------------------+
|            PATCH 5           |
|        "JEFFERSONIAN"        |
|                              |
|    [L1]----[L2]              |
|             |                |
|            [L3]              |
|                              |
+------------------------------+
"""

    # Patch 6: THE WALLED GARDEN
    patch_6_map = """
+------------------------------+
|            PATCH 6           |
|      "THE WALLED GARDEN"     |
|                              |
|    [L1]                      |
|     |                        |
|    [L2]----[L3]              |
|                              |
+------------------------------+
"""

    # Landmark maps
    landmark_map = """
+------------------------------+
|           LANDMARK           |
|                              |
|    [C1]    [O1]              |
|                              |
|    [O2]    [C2]              |
|                              |
+------------------------------+
"""

    # Find all patches and assign maps
    patches = search.typeclass_search("typeclasses.patches.Patch")
    for patch in patches:
        if patch.db.patch_number == 1:
            patch.db.ascii_map = patch_1_map
        elif patch.db.patch_number == 2:
            patch.db.ascii_map = patch_2_map
        elif patch.db.patch_number == 3:
            patch.db.ascii_map = patch_3_map
        elif patch.db.patch_number == 4:
            patch.db.ascii_map = patch_4_map
        elif patch.db.patch_number == 5:
            patch.db.ascii_map = patch_5_map
        elif patch.db.patch_number == 6:
            patch.db.ascii_map = patch_6_map
        
        # Assign maps to landmarks in this patch
        for landmark_key in patch.db.landmarks:
            landmarks = search.objects(landmark_key, typeclass=Landmark)
            if landmarks:
                landmarks[0].db.ascii_map = landmark_map
    
    print("ASCII maps loaded successfully.")
