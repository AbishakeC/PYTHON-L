import qrcode

def generate_QR_code(data,file_name="qr_password.png"):
    qr=qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black",back_color="white")
    img.save(file_name)
    return file_name