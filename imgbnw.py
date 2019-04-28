import os
from PIL import Image

path = 'c:\\mapimages\\'
newpath = 'c:\\mapimages\\gray\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            files.append(os.path.join(r, file))

for f in files:
    #print(f)
    words = f.split("\\")  
    fname = words[-1]
    justnamearr = fname.split(".")
    justname = justnamearr[0]
    print('c:\\mapimages\\gray\\' + justname + ".png")
    img = Image.open('c:\\mapimages\\' + justname + ".png").convert('L')
    img.save("c:\\mapimages\\gray\\" + justname + ".png" , "png")
    