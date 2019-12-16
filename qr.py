import qrcode
qr = qrcode.QRCode(
    version = 1,
    box_size = 20
)
qr.add_data('https://yokoemon99.github.io/test_ar/')
qr.make()
img = qr.make_image()
img.save('img/qrcode_test2.png')

