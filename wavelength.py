import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class WavelengthApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Wavelength")
        self.geometry("400x240")


if __name__ == "__main__":
    app = WavelengthApp()
    app.minsize(width=400, height=240)
    app.mainloop()
