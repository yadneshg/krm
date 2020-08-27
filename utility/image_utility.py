import PIL
from PIL import Image
from io import BytesIO
import io
from flask import flash


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# for resizing images to be uploaded in static folder
def resizeImage(image):
    img = Image.open(image)
    basewidth = 2000
    per=(basewidth / float(img.size[0]))
    size= int((float(img.size[1]) * float(per)))
    img=img.resize((basewidth, size), PIL.Image.ANTIALIAS)
    img.save(image)

def resize_image(image, width, height, max_allowed_size, need_to_resize):
    image_data = image.read()  # convert to binary
    image_size = len(image_data) / (1000 * 1000)  # image size in mb
    if image_size > max_allowed_size:
        flash("Too Large Image. Image Size should be less than 3 mb!")
    else:
        if image_size > need_to_resize:
            # pdb.set_trace()
            new_image = Image.open(image)
            new_resized_image = new_image.resize((width, height))
            return convert_to_byte(new_resized_image)
        else:
            return image_data

    #             try:
    #                     image_to_save = ImageContents(name=image_name, data=image_data)
    #                     save_to_database(db, image_to_save)
    #                 except OSError:
    #                     flash("Failed to Save in Database!")
    #             else:
    #                 flash("Invalid File Type!")
    #             flash("saved " + image_name + " to the Database!")
    # else:
    #     flash("Maximum Limit Achieved!")

def convert_to_byte(image):
    byteArr = io.BytesIO()
    image.save(byteArr, format="JPEG")
    return byteArr.getvalue()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS