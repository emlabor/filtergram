from PIL import Image
from filters import *

# gets an image from the user
def get_img():
    while True:
        filename = input("Enter an image file name: ")
        try:
            img = load_img(filename)
            if img:
                break
        except IOError:
            print("Error: file not found")
    return img

# user selects a filter
# returns index of the desired filter in filters list
def ask_for_filter(filters):
    print("Filters: ", end=" ")
    print(filters)
    filter = ""
    while (filter not in filters):
        filter = input("Choose a filter: ")
    return filters.index(filter)

def main():
    #list of function names
    filter_names = ["obamicon"]

    # list of functions
    filters = [obamicon]

    #choose an image
    img = get_img()

    #apply the chosen filter
    filter_num = ask_for_filter(filter_names)

    show_img(img)
    filters[filter_num](img)

    show_img(img)
    save_img(img, "newfoto.jpg")

if __name__ == "__main__":
	main()