import tkinter as tk
from tkinter import ttk

class SettingsWindow:
    def __init__(self, parent):
        self.parent = parent
        self.settings_window = tk.Toplevel(self.parent.window)
        self.settings_window.title("Settings")

        # Resolution
        self.resolution_label = tk.Label(self.settings_window, text="Resolution:")
        self.resolution_label.pack()

        self.resolution_var = tk.StringVar(value=f"{self.parent.video_size[0]}x{self.parent.video_size[1]}")
        self.resolution_dropdown = ttk.Combobox(self.settings_window, textvariable=self.resolution_var)
        self.resolution_dropdown['values'] = ["640x480", "1280x720", "1920x1080"]
        self.resolution_dropdown.pack()

        # Barcode Types
        self.code_types_label = tk.Label(self.settings_window, text="Barcode Types:")
        self.code_types_label.pack()

        self.pdf417_var = tk.BooleanVar(value=True)
        self.pdf417_checkbox = tk.Checkbutton(self.settings_window, text="PDF417", variable=self.pdf417_var)
        self.pdf417_checkbox.pack()

        self.qr_code_var = tk.BooleanVar(value=True)
        self.qr_code_checkbox = tk.Checkbutton(self.settings_window, text="QR Code", variable=self.qr_code_var)
        self.qr_code_checkbox.pack()

        # Lighting Conditions
        self.lighting_label = tk.Label(self.settings_window, text="Lighting Conditions:")
        self.lighting_label.pack()

        self.bright_light_var = tk.BooleanVar(value=True)
        self.bright_light_checkbox = tk.Checkbutton(self.settings_window, text="Bright Light", variable=self.bright_light_var)
        self.bright_light_checkbox.pack()

        self.apply_button = tk.Button(self.settings_window, text="Apply", command=self.apply_settings)
        self.apply_button.pack()

    def apply_settings(self):
        # Apply resolution and barcode type settings
        selected_resolution = self.resolution_var.get().split("x")
        self.parent.video_size = (int(selected_resolution[0]), int(selected_resolution[1]))

        # Update barcode types based on checkboxes
        barcode_types = []
        if self.pdf417_var.get():
            barcode_types.append("PDF417")
        if self.qr_code_var.get():
            barcode_types.append("QR Code")

        # Consider lighting conditions
        if self.bright_light_var.get():
            print("Bright Light selected")

        # Close the settings window
        self.settings_window.destroy()
