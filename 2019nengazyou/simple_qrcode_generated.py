import qrcode

img = qrcode.make('https://yokoemon99.github.io/test_ar/')
img.save('img/simple_qrcode.png')
