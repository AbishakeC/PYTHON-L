from QR.qr_generator import qr_generator
from QR.qr_LogoEmbeded import add_logo
from QR.CLI import run_cli

# QR generation
data=input("Enter the Url: ")
filename=input("Enter the FileName: ")
result = qr_generator(data,filename)
print(result)

#QR Logo Embedding
QR_path=input("enter the QR path: ")
QR_Logo=input("enter the Logo Detail: ")
destination=input("Enter the destination path: ")
result=add_logo(qr_path=QR_path,logo_path=QR_Logo,destination_path=destination)
print(f"logo edited.....{destination}")

#CLI interface
print("to be run in CLI......")
run_cli()



