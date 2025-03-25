# mygame/typeclasses/entities.py
from evennia import DefaultObject
from evennia.utils import search

class Entity(DefaultObject):
    """
    Base class for Citizens and Objects.
    """
    def at_object_creation(self):
        self.db.entity_number = 0
        self.db.description = ""
        self.db.type = "" #CITIZEN or OBJECT
        self.locks.add(";".join([
            "puppet:perm(Immortals)", #Immortals can puppet
            "edit:false()", #No one can edit
            "view:all()", #Everyone can view,
            "call:false()" #No one can call
        ]))

    def at_interact(self, caller):
        """
        Called when a player uses the INTERACT command on this object.
        Returns True if a custom interaction occurred, False otherwise.
        """
        return False  # Default: no custom interaction

    def at_conversate(self, caller):
        """
        Called when a player uses the CONVERSATE command on this entity.
        Returns True if a custom interaction occurred, False otherwise.
        """
        return False  # Default: no custom interaction

    def get_display_name(self, looker, **kwargs):
        if self.db.type == "CITIZEN":
            return f"|yCitizen: {self.key}|n"
        elif self.db.type == "OBJECT":
                return f"|mObject: {self.key}|n"
        else:
            return f"|rEntity: {self.key}|n" #Error case

    def return_appearance(self, looker, **kwargs):
        if not looker:
            return ""
        string = self.get_display_name(looker) + "\n"
        string += self.db.description + "\n"
        return string

class Citizen(Entity):
    """
    Represents a Citizen.
    """
    def at_object_creation(self):
        super().at_object_creation()
        self.db.type = "CITIZEN"
        self.db.dialogue = "" #Optional, for future use
        self.db.dialogue_state = "start"  # Initial dialogue state

    def at_conversate(self, caller):
        # Example of a VERY simple state machine for dialogue.
        if self.db.dialogue_state == "start":
            caller.msg(f"{self.key} says: 'Hello there.'")
            self.db.dialogue_state = "greeted"
            return True  # We handled the interaction
        elif self.db.dialogue_state == "greeted":
            caller.msg(f"{self.key} says: 'I don't have much to say.'")
            self.db.dialogue_state = "end"
            return True
        elif self.db.dialogue_state == "end":
            caller.msg(f"{self.key} says: 'I've said all I have to say.'")
            return True
        return False  # No interaction occurred

class Game_Object(Entity):
    """
    Represents a game object.
    """
    def at_object_creation(self):
        super().at_object_creation()
        self.db.type = "OBJECT"
        self.db.interaction_state = "default"  # Initial interaction state

    def at_interact(self, caller):
        # Example of a VERY simple state machine for interaction.
        if self.db.interaction_state == "default":
            caller.msg(f"You interact with {self.key}.")
            self.db.interaction_state = "interacted"
            return True  # We handled the interaction
        elif self.db.interaction_state == "interacted":
            caller.msg(f"You've already interacted with {self.key}.")
            return True
        return False  # No interaction occurred
