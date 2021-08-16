import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import widgets


def onselect(eclick, erelease):
    if eclick.ydata > erelease.ydata:
        eclick.ydata, erelease.ydata = erelease.ydata, eclick.ydata
    if eclick.xdata > erelease.xdata:
        eclick.xdata, erelease.xdata = erelease.xdata, eclick.xdata
    print('startposition: (%f, %f)' % (eclick.xdata, eclick.ydata))
    print('endposition  : (%f, %f)' % (erelease.xdata, erelease.ydata))
    print('used button  : ', eclick.button)
    ax.set_ylim(erelease.ydata, eclick.ydata)
    ax.set_xlim(eclick.xdata, erelease.xdata)
    fig.canvas.draw()


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)
    filename = "../assets/examples/im1.jpg"
    im = Image.open(filename)
    arr = np.asarray(im)
    plt_image = plt.imshow(arr)
    rs = widgets.RectangleSelector(ax, onselect, drawtype='box',
                                   rectprops=dict(facecolor='red', edgecolor='black', alpha=0.5, fill=True))
    plt.show()
