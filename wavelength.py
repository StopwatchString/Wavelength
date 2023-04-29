import sys
import os
import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

class WavelengthApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Wavelength")
        self.geometry("400x240")


if __name__ == "__main__":
    app = WavelengthApp()
    app.minsize(width=400, height=240)
    app.iconbitmap(resource_path("res/wavelength.ico"))
    app.mainloop()
