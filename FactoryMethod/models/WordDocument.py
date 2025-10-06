from FactoryMethod.models.Document import Document


class WordDocument(Document):
    """Concrete implementation for Word documents"""

    def __init__(self, template=None, track_changes=False):
        # Word-specific properties
        self.template = template
        self.track_changes = track_changes
        self.revision_count = 0

    def create(self):
        return "Creating Word document"

    def open(self):
        return "Opening Word document with Word processor"

    def save(self):
        return "Saving Word document"

    # Word-specific methods (not in interface)
    def enable_track_changes(self):
        self.track_changes = True
        return "Track changes enabled"

    def accept_all_changes(self):
        self.revision_count = 0
        return "All changes accepted"