import customtkinter as ctk
from login_screen import LoginScreen
from google_authenticator import GoogleAuthenticator

class SakuraMain:
    def __init__(self, sk):
        self.sk = sk
        self.authenticator = GoogleAuthenticator()
        self.login_screen = LoginScreen(sk, self.authenticate)

    def authenticate(self):
        creds = self.authenticator.get_credentials()
        if creds:
            print("Authentication successful!")
            # Aqui você pode adicionar lógica adicional para lidar com o usuário autenticado
        else:
            print("Authentication failed!")

if __name__ == "__main__":
    sk=ctk.CTk()
    app = SakuraMain(sk)
    sk.mainloop()