import tkinter

import customtkinter


class SettingsWindow(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.transient(parent)
        self.grab_set()