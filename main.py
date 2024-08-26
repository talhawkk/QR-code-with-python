try:
    import qrcode as qr
    data = input("Please enter the data you want to encode in the QR code: \n")
    name = input("kindly enter name for QR code (without extentsion) :\n")
    img=qr.make(data)
    img.save(name+".png")
    print(f"your QR code has been saved with name {name}.png")
except Exception as e:
    print(f"An error is occured {e}")

    
