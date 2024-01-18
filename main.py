import tkinter as tk
from src.scanner_app import ScannerApp

try:
    root = tk.Tk()
    app = ScannerApp(root, "Barcode Scanner")
    root.mainloop()

except ImportError as import_error:
    print(f"Import error: {import_error}")
    print("Make sure the file and class exist, and the directory structure is correct.")

except tk.TclError as tcl_error:
    print(f"Tkinter error: {tcl_error}")
    print("Ensure that you have a valid Tkinter installation.")

except Exception as general_error:
    print(f"General error: {general_error}")
