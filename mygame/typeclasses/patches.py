# mygame/typeclasses/patches.py
from evennia import DefaultRoom
from evennia.utils import search

class Patch(DefaultRoom):
    def at_object_creation(self):
        self.db.patch_number = 0
        self.db.patch_name = ""
        self.db.motto = ""
        self.db.location = ""
        self.db.governance_style = ""
        self.db.leader_title = ""
        self.db.citizenship_requirements = ""
        self.db.overview = ""
        self.db.execution_sequence = {}
        self.db.landmarks = []  # List of Landmark keys
        self.db.ascii_map = ""

    def get_display_name(self, looker, **kwargs):
        return f"|cPATCH {self.db.patch_number}: {self.db.patch_name}|n"

    def return_appearance(self, looker, **kwargs):
        if not looker:
            return ""

        string = self.get_display_name(looker) + "\n"
        string += f"|wMotto:|n {self.db.motto}\n"
        string += f"|wLocation:|n {self.db.location}\n"
        string += f"|wOverview:|n {self.db.overview}\n"
        return string
class Landmark(DefaultRoom):
    def at_object_creation(self):
        self.db.landmark_number = 0
        self.db.landmark_name = ""
        self.db.description = ""
        self.db.entities = [] #List of strings that are object keys
        self.db.ascii_map = ""

    def get_display_name(self, looker, **kwargs):
        return f"|gLandmark {self.db.landmark_number}: {self.db.landmark_name}|n"

    def return_appearance(self, looker, **kwargs):
        if not looker:
            return ""

        string = self.get_display_name(looker) + "\n"
        string += self.db.description + "\n"
        return string
