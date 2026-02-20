import qrcode
from PIL import Image
import os

def qr_generator(data,filename,
              fill_color="black",
              box_color="white",
              box_size=18,
              border=2,
              error_correction=qrcode.constants.ERROR_CORRECT_H):

    qr=qrcode.QRCode(
        version=None,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )

    qr.add_data(data)
    qr.make(fit=True)

    img= qr.make_image(fill_color=fill_color,box_color=box_color)
    img.save(filename)
    return filename


# Testing block

# if __name__=="__main__":
#     data="www.example.com"
#     folder_name="D:\Python Projects\PYTHON-L\QR_Code"
#     filename=os.path.join(folder_name,"")
#
#     result=qr_generator(data,filename)
#     print(f"qr is generated {result}")