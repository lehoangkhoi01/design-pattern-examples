# Client code
from FactoryMethod.DocumentCreator import DocumentCreator
from FactoryMethod.ExcelCreator import ExcelCreator
from FactoryMethod.PDFCreator import PDFCreator
from FactoryMethod.WordCreator import WordCreator


def client_code(creator: DocumentCreator):
    """
    Client code works with an instance of a concrete creator,
    but through its base interface
    """
    print(f"Client: Working with {creator.__class__.__name__}")
    print(creator.new_document())
    print()


# Example usage
if __name__ == "__main__":
    print("=== Factory Method Pattern Demo ===\n")

    # Create documents with different configurations
    print("Creating encrypted PDF:")
    client_code(PDFCreator(encrypted=True, compression=9))

    print("Creating Word document with template:")
    client_code(WordCreator(template="BusinessLetter.docx"))

    print("Creating Excel with multiple sheets:")
    client_code(ExcelCreator(sheets=3, macros=True))

    # Direct usage showing unique methods
    print("=== Using Product-Specific Features ===\n")

    pdf_factory = PDFCreator(encrypted=True)
    pdf_doc = pdf_factory.factory_method()
    print(pdf_doc.create())
    print(pdf_doc.add_watermark("CONFIDENTIAL"))  # PDF-specific method
    print(pdf_doc.set_permissions("read-only"))  # PDF-specific method
    print()

    word_factory = WordCreator()
    word_doc = word_factory.factory_method()
    print(word_doc.create())
    print(word_doc.enable_track_changes())  # Word-specific method
    print(word_doc.save())
    print()

    excel_factory = ExcelCreator(sheets=2, macros=True)
    excel_doc = excel_factory.factory_method()
    print(excel_doc.create())
    print(excel_doc.add_formula("A1", "=SUM(B1:B10)"))  # Excel-specific method
    print(excel_doc.create_pivot_table("A1:D100"))  # Excel-specific method
    print(excel_doc.save())