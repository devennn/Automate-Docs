import cv2


def run_selector(img_filename):
    imageread = cv2.imread(img_filename)
    imagedraw = cv2.selectROI(imageread)
    croppedimage = imageread[int(imagedraw[1]):int(imagedraw[1] + imagedraw[3]),
                   int(imagedraw[0]):int(imagedraw[0] + imagedraw[2])]
    print(int(imagedraw[1]), int(imagedraw[1] + imagedraw[3]), int(imagedraw[0]), int(imagedraw[0] + imagedraw[2]))
    cv2.imshow('Cropped_image', croppedimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
