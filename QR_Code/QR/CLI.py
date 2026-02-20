import argparse
from qr_generator import qr_generator

def run_cli():
    parser = argparse.ArgumentParser(description="QR generation in CLI interface")
    parser.add_argument("--data",required=True,help="add your QR data")
    parser.add_argument("--output",default="outputs/CLIoutput.png",help="destination to the output")
    parser.add_argument("--fill",default="black",help="fill color")
    parser.add_argument("--back",default="white",help="background color")
    args=parser.parse_args()


    qr_generator(
        data=args.data,
        filename=args.output,
        fill_color=args.fill,
        # back_color=args.back
    )


if __name__ == "__main__":
    run_cli()