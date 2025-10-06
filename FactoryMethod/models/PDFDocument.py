# Concrete Products
from FactoryMethod.models.Document import Document


class PDFDocument(Document):
    """Concrete implementation for PDF documents"""

    def __init__(self, encryption=False, compression_level=5):
        # PDF-specific properties
        self.encryption = encryption
        self.compression_level = compression_level
        self.pages = []

    def create(self):
        return "Creating PDF document"

    def open(self):
        return "Opening PDF document with PDF viewer"

    def save(self):
        return "Saving PDF document"

    # PDF-specific method (not in interface)
    def add_watermark(self, text):
        return f"Adding watermark '{text}' to PDF"

    def set_permissions(self, permissions):
        return f"Setting PDF permissions: {permissions}"