from PIL import Image
img = Image.open('C:\\Users\\richa\\Pictures\\emrakul.jpg')
print(img.size)
print(img.info)
print(img.getexif)
img.show()
r,g,b = img.split()
len (r.histogram())
print (r.histogram())
