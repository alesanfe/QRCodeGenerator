import base64
from io import BytesIO

import qrcode


def generate_qr_code(absolute_url: str):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(absolute_url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    buffered = BytesIO()
    qr_image.save(buffered)  # Specify the format as "PNG"
    qr_code_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return qr_code_base64

def generate_qr_code_and_save(absolute_url: str, output_path: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(absolute_url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Guardar el código QR en un archivo de salida
    qr_image.save(output_path)

if __name__ == '__main__':
    # Ejemplo de uso
    absolute_url_example = 'https://www.cuevana3.eu/'
    output_path_example = 'qr_code.png'

    generate_qr_code_and_save(absolute_url_example, output_path_example)

