import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import os

from src.settings.settings_window import SettingsWindow
from src.recognition.zbar_scanner import decode as zbar_decode
from src.recognition.zxing_scanner import decode as zxing_decode

# Choose the default recognition library
DEFAULT_SCANNER = "zbar"
CURRENT_SCANNER = DEFAULT_SCANNER

try:
    # Try importing zxing
    from recognition.zxing_scanner import decode as zxing_decode
    CURRENT_SCANNER = "zxing"
except ImportError:
    pass

class ScannerApp:
    def __init__(self, window, window_title, video_size=(640, 480), qr_window_size=(320, 240)):
        self.window = window
        self.window.title(window_title)
        self.video_size = video_size
        self.qr_window_size = qr_window_size

        os.environ['ZBAR_CAM_PDF417'] = '0'

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size[1])

        self.canvas = tk.Canvas(window, width=self.qr_window_size[0], height=self.qr_window_size[1])
        self.canvas.pack()

        self.settings_button = tk.Button(window, text="Settings", command=self.open_settings)
        self.settings_button.pack()

        self.close_button = tk.Button(window, text="Close", command=self.close)
        self.close_button.pack()

        self.message_label = tk.Label(window, text="")
        self.message_label.pack()

        self.video_loop()

    def video_loop(self):
        try:
            ret, frame = self.cap.read()

            if ret:
                frame = cv2.resize(frame, self.qr_window_size)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Use the selected recognition library
                if CURRENT_SCANNER == "zxing":
                    decoded_objects = zxing_decode(gray)
                else:
                    decoded_objects = zbar_decode(gray)

                for obj in decoded_objects:
                    barcode_data = obj.data.decode('utf-8')
                    barcode_type = obj.type

                    try:
                        barcode_data_as_int = int(barcode_data)
                        print(f"Barcode Data as Integer: {barcode_data_as_int}")
                    except ValueError:
                        print("Barcode Data is not numeric.")

                    rect_points = obj.polygon
                    if rect_points:
                        pts = np.array(rect_points, dtype=int)
                        pts = pts.reshape((-1, 1, 2))
                        cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

                    barcode_info = f"Type: {barcode_type}, Data: {barcode_data}"
                    self.message_label.config(text=barcode_info)

                self.photo = self.convert_image(frame)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            self.window.after(10, self.video_loop)

        except Exception as e:
            print(f"Error in video loop: {e}")

    def open_settings(self):
        SettingsWindow(self)

    def close(self):
        self.cap.release()
        self.window.destroy()

    def convert_image(self, cv_image):
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb_image)
        return ImageTk.PhotoImage(image=img)
