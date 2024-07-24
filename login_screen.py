import customtkinter as ctk
from PIL import Image

class LoginScreen:
    def __init__(self, sk, authenticate_func):
        self.sk = sk
        self.login_setup_window()
        self.create_widgets()
        self.setup_grid()
        self.authenticate_func = authenticate_func

    def login_setup_window(self):
        self.sk.title("Sakura Lab")
        self.sk.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        #Icon Setup
        self.sk.iconbitmap(r"resources\images\sk_icon.ico")

    def setup_grid(self):
        #Setup of the of the grid
        self.sk.columnconfigure(0, weight=3)
        self.sk.columnconfigure(1, weight=1)
        self.sk.columnconfigure(2, weight=3)
        self.sk.rowconfigure(0, weight=2)
        self.sk.rowconfigure(1, weight=1)
        self.sk.rowconfigure(2, weight=1)
        self.sk.rowconfigure(3, weight=1)

    def create_widgets(self):
        #Image import
        image_path = r"resources\images\sk_logo.png"
        image = Image.open(image_path)
        self.sk_logo = ctk.CTkImage(image, size=(300, 300))
        #Image position
        self.logo_label = ctk.CTkLabel(self.sk, image=self.sk_logo, text="")
        self.logo_label.grid(row=0, column=1, pady=10, sticky="s")
        #Title label
        self.title_label = ctk.CTkLabel(self.sk, text="Sakura Lab", font=ctk.CTkFont(size=40, weight="bold"))
        self.title_label.grid(row=1, column=1)
        #Login button
        self.login_button = ctk.CTkButton(self.sk, text="Login", command=self.on_login_button_click)
        self.login_button.grid(row=3, column=1, sticky="n")

    def on_login_button_click(self):
        self.authenticate_func()
