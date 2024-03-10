from urllib.parse import quote

import customtkinter as ctk

from qrgenerator import generate_qr_code_and_save


class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Generador de Códigos QR")

        # Etiqueta para la entrada de texto
        self.label = ctk.CTkLabel(master, text="Ingresa la URL:")
        self.label.pack(pady=5)

        # Campo de entrada de texto
        self.entry = ctk.CTkEntry(master)
        self.entry.pack(pady=10, ipadx=20)

        # Botón para generar el código QR
        self.button = ctk.CTkButton(master, text="Generar QR", command=self.generate_qr)
        self.button.pack(pady=10)

    def generate_qr(self):
        user_input = self.entry.get()

        # Convertir la URL a un nombre de archivo válido
        filename = quote(user_input, safe='')

        # Generar el código QR y guardarlo con el nombre de archivo válido
        generate_qr_code_and_save(user_input, f"{filename}.png")

        # Ventana de resultado
        result_window = ctk.CTkToplevel(self.master)
        result_window.title("Resultado")

        # Etiqueta en la ventana de resultado
        label = ctk.CTkLabel(result_window, text=f"QR generado para: {user_input}")
        label.pack(pady=10)

if __name__ == "__main__":
    root = ctk.CTk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

