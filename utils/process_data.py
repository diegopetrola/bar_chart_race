import pandas as pd
from PIL import Image
import os
import glob


def autocrop_image(image, border=0) -> Image:
    """
    Crop a single image to their bounding box size 
    (removes transparent pixels surrounding the img)
    """
    # Get the bounding box
    bbox = image.getbbox()

    # Crop the image to the contents of the bounding box
    image = image.crop(bbox)

    # Determine the width and height of the cropped image
    (width, height) = image.size

    # Add border
    width += border * 2
    height += border * 2

    # Create a new image object for the output image
    cropped_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Paste the cropped image onto the new image
    cropped_image.paste(image, (border, border))

    # Done!
    return cropped_image


def process_data():
    """
    Script used to process the raw data and write a 'data.csv'
    which will avoid reprocessing in the future
    """
    # cols = 'chrstprot,chrstcat,chrstorth,chrstang,chrstothr,chrstgen,judorth,jdcons,judref,judothr,judgen,islmsun,islmshi,islmibd,islmnat,islmalw,islmahm,islmothr,,budmah,budthr,budothr,,,,,,,,,,,,,'
    cols = "year,chrstgen,judgen,islmgen,budgen,zorogen,hindgen,sikhgen,shntgen,bahgen,taogen,jaingen,confgen,syncgen,anmgen,nonrelig,othrgen"
    cols = cols.split(',')
    new_labels = {
        "chrstgen": "Christianity",
        "judgen": "Judaism",
        "islmgen": "Islam",
        "budgen": "Budhism",
        "zorogen": "Zoroastrian",
        "hindgen": "Hindu",
        "sikhgen": "Sikh",
        "shntgen": "Shinto",
        "bahgen": "Baha'i",
        "taogen": "Taoism",
        "jaingen": "Confucianism",
        "confgen": "Jain",
        "syncgen": "Syncretic Religions",
        "anmgen": "Animist Religions",
        "nonrelig": "Non. Religious",
        "othrgen": "Other Religions",
    }

    df = pd.read_csv('WRP_global.csv', thousands=',')
    df = df[cols]
    df.set_index('year', inplace=True)
    df.rename(columns=new_labels, inplace=True)
    df.to_csv('data.csv')


def process_images(path: str = '..\imgs'):
    """Crop images on imgs folder so they fit better on the plot"""
    img_paths = glob.glob(os.path.join("..", "imgs", "**"))
    for img_path in img_paths:
        img = Image.open(img_path)
        img = autocrop_image(img)
        img.save(img_path)


if __name__ == "__main__":
    process_images()
    # process_data()
    exit(0)
