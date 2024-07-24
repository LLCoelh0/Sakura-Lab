from googleapiclient.discovery import build
import customtkinter as ctk
from PIL import Image


class DownloadFiles:
    def __init__(self, creds, sk):
        self.sk = sk
        self.creds = creds
        self.service = build('drive', 'v3', credentials=self.creds)
        self.list_files()
        self.download_window_setup()
        self.download_grid_setup()
        self.create_widgets()

    def download_window_setup(self):
        self.sk.title("Sakura Lab")
        self.sk.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        #Icon Setup
        self.sk.iconbitmap(r"resources\images\sk_icon.ico")

    def download_grid_setup(self):
        self.sk.columnconfigure(0, weight=1)
        self.sk.columnconfigure(1, weight=20)
        self.sk.columnconfigure(2, weight=1)
        self.sk.rowconfigure(0, weight=200)
        self.sk.rowconfigure(1, weight=1)

    def create_widgets(self):
        #import logo
        logo_path = r"resources\images\sk_logo.png"
        logo = Image.open(logo_path)
        self.sk_logo = ctk.CTkImage(logo, size=(45, 45))

        #import folder icon
        download_path = r"resources\images\download_icon.png"
        download_icon = Image.open(download_path)
        self.sk_download_icon = ctk.CTkImage(download_icon, size=(30, 30))

        #import update icon
        upload_path = r"resources\images\upload_icon.png"
        upload_icon = Image.open(upload_path)
        self.sk_upload_icon = ctk.CTkImage(upload_icon, size=(30, 30))

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
        self.download_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Download Project", 
                                           fg_color="transparent", text_color=("gray10","gray90"), hover_color=("gray70","gray30"),
                                           image=self.sk_download_icon, anchor="w", font=ctk.CTkFont(size=20), command=self.on_click_download_button)
        self.download_button.grid(row=2, column=0, pady=5, sticky="ew")

        #second button
        self.upload_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Upload Project", 
                                           fg_color="transparent", text_color=("gray10","gray90"), hover_color=("gray70","gray30"),
                                           image=self.sk_upload_icon, anchor="w", font=ctk.CTkFont(size=20), command=self.on_click_upload_button)
        self.upload_button.grid(row=3, column=0, pady=5, sticky="ew")

        #create right frame
        self.description_frame = ctk.CTkFrame(self.sk, corner_radius=10)
        self.description_frame.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky="nsew")
        self.description_frame.grid_rowconfigure(0, weight=1)
        self.navigation_frame.grid_rowconfigure(4, weight=5)
        #description
        self.description_frame_label = ctk.CTkLabel(self.description_frame, text="Download")
        self.description_frame_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        #create lower frame
        self.options_frame = ctk.CTkFrame(self.sk, corner_radius=10, height=100)
        self.options_frame.grid(row=1, column=1, sticky="new")
        self.options_frame.grid_columnconfigure(0, weight=1)
        self.options_frame.grid_rowconfigure(4, weight=1)

        #create upper frame
        self.content_frame = ctk.CTkFrame(self.sk, corner_radius=10)
        self.content_frame.grid(row=0, column=1,pady=5, sticky="nsew")
        self.content_frame.grid_rowconfigure(4, weight=1)

    def list_files(self, page_size=10):
        try:
            # Query to list all items in "My Drive"
            query = "'root' in parents and trashed=false"
            results = self.service.files().list(
                q=query,
                pageSize=page_size,
                fields="nextPageToken, files(id, name, mimeType)"
            ).execute()
            print("API Response:", results)  # Print the entire response for debugging
            items = results.get('files', [])

            if not items:
                print('No files found.')
            else:
                print('Files and Folders in My Drive:')
                for item in items:
                    print(f"{item['name']} ({item['id']}) - {item['mimeType']}")
            return items
        except Exception as e:
            print(f"An error occurred: {e}")

    def on_click_download_button(self):
        #self.clear_window()
        from download_files import DownloadFiles
        self.download_files = DownloadFiles(sk=self.sk, creds=self.creds)

    def on_click_upload_button(self):
        #self.clear_window()
        from upload_files import UploadFiles
        self.download_files = UploadFiles(sk=self.sk, creds=self.creds)