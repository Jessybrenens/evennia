# mygame/commands/initiate_chat.py
import json
from evennia import Command, CmdSet
from evennia.utils import search
from typeclasses.patches import Patch, Landmark
from typeclasses.entities import Citizen, Game_Object

class CmdBeginSession(Command):
    """
    Start a new game session.
    
    Usage:
      BEGIN SESSION
    """
    key = "BEGIN SESSION"
    help_category = "Session"
    
    def func(self):
        caller = self.caller
        caller.msg("|c=== THE PATCHWORK: AMERICA 2035 ===|n")
        caller.msg("|yWelcome to THE PATCHWORK - a fragmented vision of America in 2035, where tech billionaires have carved the nation into corporate PATCHES.|n")
        caller.msg("|yYou are an unmarked nomad, searching for a place to call home.|n")
        caller.msg("|yIn The Patchwork, you move between PATCHES using TRAVEL and navigate between LANDMARKS inside a PATCH using EXPLORE.|n")
        caller.msg("\nType |wBEGIN GAME|n to start your journey through The Patchwork.")

class CmdBeginGame(Command):
    """
    Start gameplay after session initialization.
    
    Usage:
      BEGIN GAME
    """
    key = "BEGIN GAME"
    help_category = "Session"
    
    def func(self):
        caller = self.caller
        # Initialize TOO CURIOUS counter
        caller.db.too_curious = 0
        
        # Find Patch 1
        patches = search.typeclass_search("typeclasses.patches.Patch")
        patch_1 = None
        for patch in patches:
            if patch.db.patch_number == 1:
                patch_1 = patch
                break
        
        if not patch_1:
            caller.msg("|rError: Could not find Patch 1. Please contact an administrator.|n")
            return
        
        # Find Landmark 1 in Patch 1
        landmark_1 = search.objects(f"{patch_1.key}_Landmark_1", typeclass=Landmark)
        if not landmark_1:
            caller.msg("|rError: Could not find Landmark 1 in Patch 1. Please contact an administrator.|n")
            return
        
        # Move player to Landmark 1
        caller.move_to(landmark_1[0], quiet=True)
        
        # Display introduction to Patch 1
        caller.msg(f"|c=== {patch_1.get_display_name(caller)} ===|n")
        caller.msg(f"|wMotto:|n {patch_1.db.motto}")
        caller.msg(f"|wLocation:|n {patch_1.db.location}")
        caller.msg(f"|wOverview:|n {patch_1.db.overview}")
        
        # Display current landmark
        caller.msg(f"\n{landmark_1[0].get_display_name(caller)}")
        caller.msg(landmark_1[0].db.description)
        
        # Display available commands
        caller.msg("\n|yAvailable commands:|n")
        caller.msg("  |wTRAVEL|n - Move to an adjacent PATCH")
        caller.msg("  |wEXPLORE|n - Move to an adjacent LANDMARK within the current PATCH")
        caller.msg("  |wINVESTIGATE|n - Examine an OBJECT or CITIZEN in the current LANDMARK")
        caller.msg("  |wDISPLAY MAP|n - Show your current location and movement options")
        
        # Display TOO CURIOUS counter
        caller.msg(f"\n|rTOO CURIOUS: {caller.db.too_curious}/30|n")

class CmdEndSession(Command):
    """
    End the current game session.
    
    Usage:
      END SESSION
    """
    key = "END SESSION"
    help_category = "Session"
    
    def func(self):
        caller = self.caller
        caller.msg("|cEnding your session in The Patchwork. Your progress has been saved.|n")
        caller.msg("|yType |wBEGIN SESSION|n to continue your journey.|n")

class CmdDisplayMap(Command):
    """
    Show current PATCH, LANDMARK, and movement options.
    
    Usage:
      DISPLAY MAP
    """
    key = "DISPLAY MAP"
    aliases = ["MAP"]
    help_category = "General"
    
    def func(self):
        caller = self.caller
        current_landmark = caller.location
        
        if not isinstance(current_landmark, Landmark):
            caller.msg("You are not in a valid location. Please contact an administrator.")
            return
        
        current_patch = current_landmark.location
        
        if not isinstance(current_patch, Patch):
            caller.msg("You are not in a valid location. Please contact an administrator.")
            return
        
        # Display TOO CURIOUS counter
        caller.msg(f"|rTOO CURIOUS: {caller.db.too_curious}/30|n")
        
        # Display current location
        caller.msg(f"\n|cYou are currently in:|n")
        caller.msg(f"  {current_patch.get_display_name(caller)}")
        caller.msg(f"  {current_landmark.get_display_name(caller)}")
        
        # Display ASCII map if available
        if current_patch.db.ascii_map:
            caller.msg("\n|cPATCH MAP:|n")
            caller.msg(current_patch.db.ascii_map)
        
        if current_landmark.db.ascii_map:
            caller.msg("\n|cLANDMARK MAP:|n")
            caller.msg(current_landmark.db.ascii_map)
        
        # Display adjacent patches
        all_patches = search.typeclass_search("typeclasses.patches.Patch")
        all_patches.sort(key=lambda x: x.db.patch_number)
        current_index = -1
        for i, patch in enumerate(all_patches):
            if patch == current_patch:
                current_index = i
                break
        
        if current_index != -1:
            next_patch_index = (current_index + 1) % len(all_patches)
            prev_patch_index = (current_index - 1) % len(all_patches)
            
            caller.msg("\n|cAdjacent PATCHES (use TRAVEL to move):|n")
            caller.msg(f"  1. {all_patches[next_patch_index].get_display_name(caller)}")
            caller.msg(f"  2. {all_patches[prev_patch_index].get_display_name(caller)}")
        
        # Display adjacent landmarks
        all_landmarks = [search.objects(f"{current_patch.key}_Landmark_{x+1}", typeclass=Landmark)[0] 
                         for x in range(len(current_patch.db.landmarks))]
        all_landmarks.sort(key=lambda x: x.db.landmark_number)
        current_index = -1
        for i, landmark in enumerate(all_landmarks):
            if landmark == current_landmark:
                current_index = i
                break
        
        if current_index != -1:
            next_landmark_index = (current_index + 1) % len(all_landmarks)
            prev_landmark_index = (current_index - 1) % len(all_landmarks)
            
            caller.msg("\n|cAdjacent LANDMARKS (use EXPLORE to move):|n")
            caller.msg(f"  1. {all_landmarks[next_landmark_index].get_display_name(caller)}")
            caller.msg(f"  2. {all_landmarks[prev_landmark_index].get_display_name(caller)}")
        
        # Display entities in current landmark
        caller.msg("\n|cEntities in this LANDMARK (use INVESTIGATE to examine):|n")
        if current_landmark.db.entities:
            for i, entity_data in enumerate(current_landmark.db.entities):
                entity_type = entity_data["type"]
                entity_number = entity_data["entity_number"]
                entity = search.objects(f"{current_landmark.key}_{entity_type}_{entity_number}")
                if entity:
                    caller.msg(f"  - {entity[0].get_display_name(caller)}")
        else:
            caller.msg("  None")

class InitiateChatCmdSet(CmdSet):
    """
    Command set for the initiate chat functionality.
    """
    key = "InitiateChatCmdSet"
    
    def at_cmdset_creation(self):
        self.add(CmdBeginSession())
        self.add(CmdBeginGame())
        self.add(CmdEndSession())
        self.add(CmdDisplayMap())
