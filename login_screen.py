import customtkinter as ctk
from PIL import Image

class SakuraLabLoginScreen:
    def __init__(self, sk):
        self.sk = sk
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.sk.title("Sakura Lab")
        self.sk.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        #Icon Setup
        self.sk.iconbitmap(r"E:\OneDrive\Vscode\Sakura-Lab\resources\images\sk_icon.ico")
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
        image_path = r"E:\OneDrive\Vscode\Sakura-Lab\resources\images\sk_logo.png"
        image = Image.open(image_path)
        sk_logo = ctk.CTkImage(image, size=(300, 300))
        #Image position
        logo_label = ctk.CTkLabel(self.sk, image=sk_logo, text="")
        logo_label.grid(row=0, column=1, pady=10, sticky="s")
        #Email field setup
        entry_email = ctk.CTkEntry(self.sk, placeholder_text="E-mail")
        entry_email.grid(row=1, column=1, padx=10, pady=10, sticky="sew")
        #Password field setup
        entry_password = ctk.CTkEntry(self.sk, placeholder_text="Password")
        entry_password.grid(row=2, column=1, padx=10, pady=10, sticky="new")
        #Login Button Stup
        submit_button = ctk.CTkButton(self.sk, text="Login")
        submit_button.grid(row=3, column=1, sticky="n")

sk = ctk.CTk()
app = SakuraLabLoginScreen(sk)
sk.mainloop()