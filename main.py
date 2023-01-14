import colour
import numpy as np
import matplotlib.pyplot as plot
from PIL import Image

'''
Description
'''
def readImage(path):
    return Image.open(path)

'''
Description
'''
def imageToParts(image):
    w, h = image.size
    
    parts = [.2, .1, .4, .1, .2]
    dominant_colors = list()
    last_width = 0
    for part_percent in parts:
        pixels = w * part_percent
        cropped_image = image.crop((last_width, 0, last_width + pixels, h))
        last_width += pixels
        dominant_colors.append(getDominantColor(cropped_image))
    return dominant_colors

'''
Description
'''
def getDominantColor(image):
    width, height = image.size
    image = image.resize((width, height),resample = 0)
    pixels = image.getcolors(width * height)
    sorted_pixels = sorted(pixels, key=lambda t: t[0])
    dominant_color = sorted_pixels[-1][1]
    return dominant_color

'''
Description
'''
def RGBToWaveLength(r,g,b):
    RGB_f = np.array([r,g,b]) / 255

    RGB_l = colour.models.eotf_sRGB(RGB_f)
    XYZ = colour.RGB_to_XYZ(
        RGB_l,
        colour.models.RGB_COLOURSPACE_sRGB.whitepoint,
        colour.models.RGB_COLOURSPACE_sRGB.whitepoint,
        colour.models.RGB_COLOURSPACE_sRGB.matrix_RGB_to_XYZ,
    )
    xy = colour.XYZ_to_xy(XYZ)
    wl, xy_1, xy_2 = colour.dominant_wavelength(
        xy, colour.models.RGB_COLOURSPACE_sRGB.whitepoint
    )

    wl, xy_1, xy_2 = colour.convert(RGB_f, "Output-Referred RGB", "Dominant Wavelength")

    return wl, xy_1, xy_2

def wavelengthToFreq(wl):
    # freq  = speedOfLight/waveLength
    return 299792458//wl*10e9    # This is returned in HZ
    # return 299792458//wl    # This is returned in GHZ

if __name__ == '__main__':
    image = readImage('./assets/green_blue.png')

    dominant_colors = imageToParts(image)
    wave_lengths = [RGBToWaveLength(r,g,b) for r,g,b in dominant_colors]
    print("Dominant colors", dominant_colors)

    #Wave lengths in nano m.
    print("Wave lengths", wave_lengths)
    # print("Wave lengths[0]", wave_lengths[0][0])
    print(wavelengthToFreq(wave_lengths[0][0]))

    # parser = argparse.ArgumentParser(
    #                 prog = 'LimitlessKnowledge',
    #                 description = 'Parser for blind people',
    #                 epilog = 'Thanks buddy')
    # parser.add_argument()
