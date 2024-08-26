import qrcode as qr
import tkinter as tk
from tkinter import filedialog
try:
    root = tk.Tk()
    root.withdraw()
    data = input("Please enter the data you want to encode in the QR code: \n")
    name = input("kindly enter name for QR code (without extentsion) :\n")
    img=qr.make(data)
    savepath=filedialog.asksaveasfilename(defaultextension=".png",initialfile=name,filetypes=[("PNG files","*.png")])
    # img.save(name+".png")

    if savepath:
        img.save(savepath)
        print(f"your QR code has been saved with name {name}.png")
    else:
        print("operation failed")
except Exception as e:
    print(f"An error is occured {e}")

    
