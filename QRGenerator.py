import qrcode

qr = qrcode.QRCode(
    version=5,  # from 1 - 40
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # L/M/Q/H or 7/15/25/30%
    box_size=10,  # how many pixels each “box” of the QR code is
    border=4,  # Default is 4
)

data = "https://www.linkedin.com/in/wisanggenipw/"  # fill with your data link

qr.add_data(data)  # Add your data
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('WisangLinkedIn-QR.png')  # save with your file name as you want
