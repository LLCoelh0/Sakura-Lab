import customtkinter as ctk
from login_screen import LoginScreen
from google_authenticator import GoogleAuthenticator
from initial_selection import InitialSelection
from upload_files import UploadFiles

class SakuraMain:
    def __init__(self, sk):
        self.sk = sk
        self.creds = None
        self.authenticator = GoogleAuthenticator()
        self.login_screen = LoginScreen(sk, self.authenticate)

    def authenticate(self):
        self.creds = self.authenticator.get_credentials()
        if self.creds:
            print("Authentication successful!")
            self.upload_files_window = UploadFiles(self.sk, self.creds)
            self.clear_window()
            self.initial_selection = InitialSelection(self.sk, self.creds)

        else:
            print("Authentication failed!")

    def clear_window(self):
        # Destroys all widgets in the main window
        for widget in self.sk.winfo_children():
            widget.destroy()
        for i in range(self.sk.grid_size()[0]):  # Reset column configurations
            self.sk.grid_columnconfigure(i, weight=0)
        for i in range(self.sk.grid_size()[1]):  # Reset row configurations
            self.sk.grid_rowconfigure(i, weight=0)

    def get_creds(self):
        return self.creds

if __name__ == "__main__":
    sk=ctk.CTk()
    app = SakuraMain(sk)
    sk.mainloop()