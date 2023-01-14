from PIL import Image

def readImage(path):
    img = image = Image.open("./assets/red.png")
    return img

def imageToFreq(image):
    pass



if __name__ == '__main__':
    image = readImage('./assets/red.png')
    print(image)

    parser = argparse.ArgumentParser(
                    prog = 'LimitlessKnowledge',
                    description = 'Parser for blind people',
                    epilog = 'Thanks buddy')
    parser.add_argument()
