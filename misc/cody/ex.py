img = open('cadeau.jpeg', 'rb').read()
img = b'\xff\xd8\xfe\xe0' + img[4:]
open('flag.jpeg', 'wb').write(img)
