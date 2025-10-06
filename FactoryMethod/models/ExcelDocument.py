from FactoryMethod.models.Document import Document


class ExcelDocument(Document):
    """Concrete implementation for Excel documents"""

    def __init__(self, num_sheets=1, enable_macros=False):
        # Excel-specific properties
        self.num_sheets = num_sheets
        self.enable_macros = enable_macros
        self.formulas = []

    def create(self):
        return "Creating Excel spreadsheet"

    def open(self):
        return "Opening Excel spreadsheet with Excel"

    def save(self):
        return "Saving Excel spreadsheet"

    # Excel-specific methods (not in interface)
    def add_formula(self, cell, formula):
        self.formulas.append((cell, formula))
        return f"Added formula to {cell}: {formula}"

    def create_pivot_table(self, data_range):
        return f"Creating pivot table from range {data_range}"