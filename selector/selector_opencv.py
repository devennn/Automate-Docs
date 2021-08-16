import cv2

if __name__ == '__main__':
    imageread = cv2.imread('../assets/examples/im1.jpg')
    imagedraw = cv2.selectROI(imageread)
    croppedimage = imageread[int(imagedraw[1]):int(imagedraw[1] + imagedraw[3]),
                   int(imagedraw[0]):int(imagedraw[0] + imagedraw[2])]
    print(int(imagedraw[1]), int(imagedraw[1] + imagedraw[3]), int(imagedraw[0]), int(imagedraw[0] + imagedraw[2]))
    cv2.imshow('Cropped_image', croppedimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
