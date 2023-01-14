from PIL import Image
import colour
import numpy as np
import matplotlib.pyplot as plot

def readImage(path):
    return Image.open(path)

def imageToFreq(image):
    rgb_im = image.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))

    RGB_f = np.array([r,g,b]) / 255

    # Using the individual definitions:
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

    # Using the automatic colour conversion graph:
    wl, xy_1, xy_2 = colour.convert(RGB_f, "Output-Referred RGB", "Dominant Wavelength")

    print(wl, xy_1, xy_2)
    return wl, xy_1, xy_2


if __name__ == '__main__':
    image = readImage('./assets/red.png')
    wl, xy1, xy2 = imageToFreq(image)

    # Get x values of the sine wave

    time        = np.arange(0, 100, 10)
    amplitude   = 1 # np.sin(time)

    plot.plot(time, amplitude)
    plot.title('Sine wave')
    plot.xlabel('Time')
    plot.ylabel('Amplitude = sin(time)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show()

    # parser = argparse.ArgumentParser(
    #                 prog = 'LimitlessKnowledge',
    #                 description = 'Parser for blind people',
    #                 epilog = 'Thanks buddy')
    # parser.add_argument()
