from PIL import Image

def add_logo(qr_path,logo_path,destination_path):

    qr=Image.open(qr_path)
    img = Image.open(logo_path)

    qr_width,qr_height=qr.size

    logo_size=qr_width//4
    logo = img.resize((logo_size,logo_size))

    position=(
    (qr_width-logo_size)//2,
    (qr_height-logo_size)//2
    )

    qr.paste(logo,position,mask=logo)

    qr.save(destination_path)