import customtkinter as ctk
from PIL import Image

class TemplateWindow:

    def __init__(self, sk):
        self.sk = sk
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.sk.title("Sakura Lab")
        self.sk.geometry("1280x720")
        #Icon Setup
        self.sk.iconbitmap(r"E:\OneDrive\Vscode\Sakura-Lab\resources\images\sk_icon.ico")
        #Grid setup
        self.sk.columnconfigure(0, weight=1)
        self.sk.columnconfigure(1, weight=20)
        self.sk.columnconfigure(2, weight=1)
        self.sk.rowconfigure(0, weight=200)
        self.sk.rowconfigure(1, weight=1)

    def create_widgets(self):
        #import logo
        logo_path = r"E:\OneDrive\Vscode\Sakura-Lab\resources\images\sk_logo.png"
        logo = Image.open(logo_path)
        self.sk_logo = ctk.CTkImage(logo, size=(45, 45))

        #import update icon
        update_path = r"E:\OneDrive\Vscode\Sakura-Lab\resources\images\update_icon.png"
        update_icon = Image.open(update_path)
        self.sk_update_icon = ctk.CTkImage(update_icon, size=(30, 30))

        #import folder icon
        files_path = r"E:\OneDrive\Vscode\Sakura-Lab\resources\images\folder_icon.png"
        files_icon = Image.open(files_path)
        self.sk_files_icon = ctk.CTkImage(files_icon, size=(30, 30))

        #create left frame
        self.navigation_frame = ctk.CTkFrame(self.sk, corner_radius=10)
        self.navigation_frame.grid(row=0, column=0, rowspan=2, padx=5, pady=5, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(0, weight=1)
        self.navigation_frame.grid_rowconfigure(4, weight=5)

        #title
        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Sakura Lab",
                                                   image=self.sk_logo, compound="left", 
                                                   font=ctk.CTkFont(size=30, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=5, pady=15, sticky="n")

        #first button
        self.update_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Update Project", 
                                           fg_color="transparent", text_color=("gray10","gray90"), hover_color=("gray70","gray30"),
                                           image=self.sk_update_icon, anchor="w", font=ctk.CTkFont(size=20))
        self.update_button.grid(row=2, column=0, pady=5, sticky="ew")

        #second button
        self.files_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Files Explorer", 
                                           fg_color="transparent", text_color=("gray10","gray90"), hover_color=("gray70","gray30"),
                                           image=self.sk_files_icon, anchor="w", font=ctk.CTkFont(size=20))
        self.files_button.grid(row=3, column=0, pady=5, sticky="ew")

        #create right frame
        self.description_frame = ctk.CTkFrame(self.sk, corner_radius=10)
        self.description_frame.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky="nsew")
        self.description_frame.grid_rowconfigure(4, weight=1)

        #create lower frame
        self.options_frame = ctk.CTkFrame(self.sk, corner_radius=10, height=100)
        self.options_frame.grid(row=1, column=1, sticky="new")
        self.options_frame.grid_rowconfigure(4, weight=1)

        #create upper frame
        self.content_frame = ctk.CTkFrame(self.sk, corner_radius=10)
        self.content_frame.grid(row=0, column=1,pady=5, sticky="nsew")
        self.content_frame.grid_rowconfigure(4, weight=1)

sk = ctk.CTk()
app = TemplateWindow(sk)
sk.mainloop()