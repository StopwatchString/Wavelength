import sys
import os
import tkinter
import customtkinter
from utils import program_path
import views

class WavelengthApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Wavelength")

        self.configured_columns = [0, 1, 2, 3]
        self.configured_rows = [0]

        self.grid_columnconfigure(0, weight=1, minsize=220)
        self.grid_columnconfigure([1, 2], weight=3, minsize=400)
        self.grid_columnconfigure(3, weight=1, minsize=220)

        self.grid_rowconfigure(0, weight=1, minsize=400)

        self.workspace_list_frame = views.WorkspaceListFrame(self)
        self.workspace_list_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.workspace_list_frame.grid_rowconfigure(4, weight=1)

        self.right_sidebar_frame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.right_sidebar_frame.grid_rowconfigure(4, weight=1)

        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.workspace_list_frame,
                                                                      values=["System", "Light", "Dark"],
                                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = WavelengthApp()
    app.minsize(1000, 400)
    app.iconbitmap(os.path.join(program_path(), "res/wavelength.ico"))
    app.mainloop()
