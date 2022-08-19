from PIL import Image, ImageFilter

img = Image.open('./GRU.jpeg')
img.thumbnail((200, 200))
img.save('Gru.jpg')

img = Image.open('./Kevin.png')
img.thumbnail((200, 200))
img.save('Kevin_1.png')

img = Image.open('./Stuart.jpeg')
img.thumbnail((200, 200))
img.save('Stuart_1.jpg')