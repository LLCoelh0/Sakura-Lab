import customtkinter as ctk
from PIL import Image

class InitialSelection:
    def __init__(self, sk, creds):
        self.sk = sk
        self.creds = creds
        self.selection_setup_window()
        self.grid_setup()
        self.create_widgets()

    def selection_setup_window(self):
        self.sk.title("Sakura Lab")
        self.sk.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        #Icon Setup
        self.sk.iconbitmap(r"resources\images\sk_icon.ico")

    def grid_setup(self):
        #Grid setup
        self.sk.rowconfigure(0, weight=1)
        self.sk.columnconfigure(0, weight=1)
        self.sk.columnconfigure(1, weight=1)

    def create_widgets(self):
        #create left frame
        self.download_frame = ctk.CTkFrame(self.sk, corner_radius=10)
        self.download_frame.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")
        self.download_frame.grid_rowconfigure(0, weight=1)
        self.download_frame.grid_columnconfigure(0, weight=1)
        #Import download icon
        download_path = r"resources\images\download_icon.png"
        download_icon = Image.open(download_path)
        self.sk_download_icon = ctk.CTkImage(download_icon, size=(200, 200))
        #Download Button
        self.download_button = ctk.CTkButton(self.download_frame, corner_radius=0, height=40, border_spacing=10, text="Download Files", 
                                           fg_color="transparent", text_color=("gray10","gray90"), hover_color=("gray70","gray30"),
                                           image=self.sk_download_icon, compound="top", font=ctk.CTkFont(size=30), command=self.on_click_download_button)
        self.download_button.grid(row=0, column=0, pady=5, sticky="nsew")

        #create right frame
        self.upload_frame = ctk.CTkFrame(self.sk, corner_radius=10)
        self.upload_frame.grid(row=0, column=1, padx=50, pady=50, sticky="nsew")
        self.upload_frame.grid_rowconfigure(0, weight=1)
        self.upload_frame.grid_columnconfigure(0, weight=1)
        #Import upload icon
        upload_path = r"resources\images\upload_icon.png"
        upload_icon = Image.open(upload_path)
        self.sk_upload_icon = ctk.CTkImage(upload_icon, size=(200, 200))
        #Download Button
        self.upload_button = ctk.CTkButton(self.upload_frame, corner_radius=0, height=40, border_spacing=10, text="Upload Files", 
                                           fg_color="transparent", text_color=("gray10","gray90"), hover_color=("gray70","gray30"),
                                           image=self.sk_upload_icon, compound="top", font=ctk.CTkFont(size=30), command=self.on_click_upload_button)
        self.upload_button.grid(row=0, column=0, pady=5, sticky="nsew")

    def on_click_download_button(self):
        #self.clear_window()
        from download_files import DownloadFiles
        self.download_files = DownloadFiles(sk=self.sk, creds=self.creds)

    def on_click_upload_button(self):
        #self.clear_window()
        from upload_files import UploadFiles
        self.download_files = UploadFiles(sk=self.sk, creds=self.creds)