import sys
import os
import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('..'), relative_path)

class WavelengthApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Wavelength")

        self.configured_columns = [0, 1, 2, 3]

        self.grid_columnconfigure(0, weight=1, minsize=220)
        self.grid_columnconfigure((1, 2), weight=3, minsize=400)
        self.grid_columnconfigure(3, weight=1, minsize=220)

        total_min_size = 0
        for column in self.configured_columns:
            column_config = self.grid_columnconfigure(column)
            total_min_size += column_config['minsize']
        total_min_size += 40  # extra padding

        self.geometry(f"{total_min_size}x240")

        self.sidebar_frame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                      values=["System", "Light", "Dark"],
                                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = WavelengthApp()
    app.minsize(width=1280, height=240)
    app.iconbitmap(resource_path("res/wavelength.ico"))
    app.mainloop()
