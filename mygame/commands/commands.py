# mygame/commands/commands.py
from evennia import Command, CmdSet
from evennia.utils import search
from typeclasses.patches import Patch, Landmark

class CmdTravel(Command):
    """
    Travel to an adjacent Patch.
    Usage:
      travel
    """
    key = "travel"
    help_category = "General"
    def func(self):
        caller = self.caller
        current_patch = caller.location.location #Double check
        if not isinstance(current_patch, Patch):
            caller.msg("You can't travel from here.")
            return
        # Get adjacent patches (circular navigation)
        all_patches = search.typeclass_search("typeclasses.patches.Patch")
        all_patches.sort(key=lambda x: x.db.patch_number)  # Ensure correct order
        current_index = -1
        for i, patch in enumerate(all_patches):
            if patch == current_patch:
                current_index = i
                break
        if current_index == -1:
            caller.msg("|rERROR: Current patch not found in patch list.|n")
            return
        next_patch_index = (current_index + 1) % len(all_patches)
        prev_patch_index = (current_index - 1) % len(all_patches)
        #Offer choices
        caller.msg("Adjacent Patches:")
        caller.msg(f"  1. {all_patches[next_patch_index].get_display_name(caller)}")
        caller.msg(f"  2. {all_patches[prev_patch_index].get_display_name(caller)}")
        try:
            choice = int(self.args.strip())
        except ValueError:
            caller.msg("Enter 1 or 2 to choose your destination.")
            return
        if choice == 1:
            target_patch = all_patches[next_patch_index]
        elif choice == 2:
            target_patch = all_patches[prev_patch_index]
        else:
            caller.msg("Invalid choice. Enter 1 or 2.")
            return
        # Move the player to Landmark 1 of the target patch
        target_landmark = search.objects(f"{target_patch.key}_Landmark_1", typeclass=Landmark)
        if target_landmark:
            caller.move_to(target_landmark[0])
        else:
            caller.msg(f"|rERROR: Could not find Landmark 1 in {target_patch.db.patch_name}.|n")

class CmdExplore(Command):
    """
    Explore to an adjacent Landmark within the current Patch.
    Usage:
      explore
    """
    key = "explore"
    help_category = "General"
    def func(self):
        caller = self.caller
        current_landmark = caller.location
        if not isinstance(current_landmark, Landmark):
                caller.msg("You can't explore from here.")
                return
        current_patch = current_landmark.location
        if not isinstance(current_patch, Patch):
            caller.msg("You can't explore from here.")
            return
        # Get adjacent landmarks (circular navigation)
        all_landmarks = [search.objects(f"{current_patch.key}_Landmark_{x+1}", typeclass=Landmark)[0] for x in range(len(current_patch.db.landmarks))]
        all_landmarks.sort(key=lambda x: x.db.landmark_number)
        current_index = -1
        for i, landmark in enumerate(all_landmarks):
            if landmark == current_landmark:
                current_index = i
                break
        if current_index == -1:
            caller.msg("Error: Could not find landmark index")
            return
        next_landmark_index = (current_index + 1) % len(all_landmarks)
        prev_landmark_index = (current_index - 1) % len(all_landmarks)
        #Offer choices
        caller.msg("Adjacent Landmarks:")
        caller.msg(f"  1. {all_landmarks[next_landmark_index].get_display_name(caller)}")
        caller.msg(f"  2. {all_landmarks[prev_landmark_index].get_display_name(caller)}")
        try:
            choice = int(self.args.strip())
        except ValueError:
            caller.msg("Enter 1 or 2 to choose your destination.")
            return
        if choice == 1:
            target_landmark = all_landmarks[next_landmark_index]
        elif choice == 2:
            target_landmark = all_landmarks[prev_landmark_index]
        else:
            caller.msg("Invalid choice. Enter 1 or 2.")
            return
        caller.move_to(target_landmark)

class CmdInvestigate(Command):
    """
    Investigate the next Citizen or Object in the current Landmark.
    Usage:
      investigate
    """
    key = "investigate"
    help_category = "General"
    def func(self):
        caller = self.caller
        current_landmark = caller.location
        if not isinstance(current_landmark, Landmark):
            caller.msg("You are not in a Landmark.")
            return
        #Get objects and citizens
        all_entities = [search.objects(f"{current_landmark.key}_{x['type']}_{x['entity_number']}")[0] for x in current_landmark.db.entities]
        #Find current entity
        current_entity = None
        for obj in caller.contents:
            if obj.db.type == "CITIZEN" or obj.db.type == "OBJECT":
                current_entity = obj
                break;
        current_index = -1
        for i, entity in enumerate(all_entities):
            if entity == current_entity:
                current_index = i
                break
        #If no current entity, start at the beginning
        next_entity_index = 0
        if(current_index != -1):
            next_entity_index = (current_index + 1) % len(all_entities)
        next_entity = all_entities[next_entity_index]
        #Move object to player
        if next_entity:
            next_entity.move_to(caller, quiet=True)
            caller.msg(next_entity.return_appearance(caller))
        else:
            caller.msg("There is nothing to investigate.")

class CmdInteract(Command):
    """
    Interact with an Object.
    Usage:
      interact
    """
    key = "interact"
    aliases = ["touch", "examine"]
    help_category = "General"
    def func(self):
        caller = self.caller
        # Find the object the player is currently "with"
        current_object = None
        for obj in caller.contents:
            if obj.db.type == "OBJECT":
                current_object = obj
                break
        if not current_object:
            caller.msg("You must first INVESTIGATE an object to interact with.")
            return
        # Increment TOO CURIOUS counter
        caller.db.too_curious = (caller.db.too_curious or 0) + 1
        caller.msg(f"|rTOO CURIOUS: {caller.db.too_curious}/30|n")
        # Check for execution
        if caller.db.too_curious >= 30:
            self.execute_player(caller)
            return
        # --- Object-Specific Interactions ---
        # Instead of a generic message, we'll call a method on the object.
        if not current_object.at_interact(caller): #If at_interact returns false
            caller.msg(f"You interact with {current_object.key}.") #Default message
            caller.msg("|r[Object interaction not yet fully implemented]|n")
    
    def execute_player(self, caller):
        current_patch = caller.location.location
        if isinstance(current_patch, Patch):
            execution_sequence = current_patch.db.execution_sequence
            caller.msg(execution_sequence.get("description", "You are executed!"))
            for step in execution_sequence.get("steps", []):
                caller.msg(step)
        else:
            caller.msg("You are executed!")
        # Placeholder for actual execution (e.g., deleting the character)
        caller.msg("|rGAME OVER|n")
        caller.delete()

class CmdConversate(Command):
    """
    Converse with a Citizen.
    Usage:
      conversate
    """
    key = "conversate"
    aliases = ["talk", "speak"]
    help_category = "General"
    def func(self):
        caller = self.caller
        current_citizen = None
        for obj in caller.contents:
            if obj.db.type == "CITIZEN":
                current_citizen = obj
                break
        if not current_citizen:
            caller.msg("You must INVESTIGATE a citizen to talk with them.")
            return
        # Increment TOO CURIOUS counter
        caller.db.too_curious = (caller.db.too_curious or 0) + 1
        caller.msg(f"|rTOO CURIOUS: {caller.db.too_curious}/30|n")
        # Check for execution
        if caller.db.too_curious >= 30:
            CmdInteract.execute_player(self, caller)
            return
        # --- Citizen-Specific Dialogue ---
        # Instead of a generic message, we'll call a method on the citizen.
        if not current_citizen.at_conversate(caller): #If at_conversate returns false
            caller.msg(f"You talk with {current_citizen.key}.") #Default message
            caller.msg("|r[Dialogue not yet fully implemented]|n")

class GameCmdSet(CmdSet):
    """
    Command set for the game.
    """
    key = "GameCmdSet"
    def at_cmdset_creation(self):
        self.add(CmdTravel())
        self.add(CmdExplore())
        self.add(CmdInvestigate())
        self.add(CmdInteract())
        self.add(CmdConversate())

class PatchCmdSet(CmdSet):
    """
    Command set for Patches.
    """
    key = "PatchCmdSet"
    def at_cmdset_creation(self):
        self.add(CmdExplore())

class LandmarkCmdSet(CmdSet):
    """
    Command set for Landmarks.
    """
    key = "LandmarkCmdSet"
    def at_cmdset_creation(self):
        self.add(CmdInvestigate())
