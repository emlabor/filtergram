from PIL import Image

# returns an Image object
def load_img(filename):
    img = Image.open(filename)
    return img

def show_img(img):
    img.show("SIPstagram")

def save_img(img, filename):
    img.save(filename)

# returns an Image object w the filter
def obamicon(img):
    data = img.getdata()
    new = []
    for px in data:
        intensity = px[0] + px[1] + px[2]
        if (intensity < 182):
            new.append((0, 51, 76))
        elif (intensity >= 182 and intensity < 364):
            new.append((217, 26, 33))
        elif (intensity >= 364 and intensity < 546):
            new.append((112, 150, 158))
        elif (intensity >= 546):
            new.append((252, 227, 166))
    img.putdata(new)

