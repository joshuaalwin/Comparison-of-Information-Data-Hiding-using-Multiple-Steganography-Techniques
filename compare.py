import math

from skimage.metrics import structural_similarity as structSim
import matplotlib.pyplot as plot
import numpy
import cv2



def meanSquareError(im1, im2):
    error = numpy.sum((im1.astype('float') - im2.astype('float')) ** 2)
    error /= float(im1.shape[0] * im1.shape[1])

    # Returns the MSE, Lower the error the more similar
    return error


def calculate_psnr(img1, img2):
    # img1 and img2 have range[0, 255]
    img1 = img1.astype(numpy.float64)
    img2 = img2.astype(numpy.float64)
    mse = numpy.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')
    return 20 * math.log10(255.0 / math.sqrt(mse))


def compareImages(im1, im2, title):
    mse = meanSquareError(im1, im2)
    ss = structSim(im1, im2, multichannel=True)
    psn1=calculate_psnr(im1,im2)

    # make figure
    fig = plot.figure(title)
    plot.suptitle('MSE: %.2f, SSIM: %.2f PSNR: %.2f' % (mse, ss,psn1))

    # Plotting the first figure
    ax = fig.add_subplot(1, 2, 1)
    plot.imshow(im1, cmap=plot.cm.gray)
    plot.axis('off')

    # Plotting the second figure
    ax = fig.add_subplot(1, 2, 2)
    plot.imshow(im2, cmap=plot.cm.gray)
    plot.axis('off')

    plot.show()


def main():
    original = cv2.imread('D:\Stego_Project\lenna.png')
    lsbEncoded = cv2.imread('D:\Stego_Project\lsb_lenna.png')
    dctEncoded = cv2.imread('D:\Stego_Project\dct_lenna.png')

    # Converting to RGB
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    lsbEncoded = cv2.cvtColor(lsbEncoded, cv2.COLOR_BGR2RGB)
    dctEncoded = cv2.cvtColor(dctEncoded, cv2.COLOR_BGR2RGB)

    # Initializing the figure
    fig = plot.figure("Images")
    images = ('Original', original), ('LSB', lsbEncoded), ('DCT', dctEncoded)

    # Looping over the images
    for (i, (name, image)) in enumerate(images):
        ax = fig.add_subplot(1, 3, i + 1)
        ax.set_title(name)
        plot.imshow(image, cmap=plot.cm.gray)
        plot.axis('off')

    plot.show()

    # Compare all the images
    compareImages(original, original, "Original vs Original")
    compareImages(original, lsbEncoded, "Original vs LSB")
    compareImages(original, dctEncoded, "Original vs DCT")


if __name__ == '__main__':
    main()
