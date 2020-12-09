import qrcode



qr = qrcode.QRCode(

version = 2,

error_correction = qrcode.constants.ERROR_CORRECT_H,

box_size = 2,

border = 2

)



url = 'http://192.168.45.56:7777/gibo'

qr.add_data(url)

qr.make()

img = qr.make_image(fill_color="black", back_color="white")

img.save('acronet.png')