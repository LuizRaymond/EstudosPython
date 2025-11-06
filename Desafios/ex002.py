import cv2
img = cv2.imread("teclas_de_piano.png")
inverted_img = cv2.bitwise_not(img)
cv2.imwrite("teclas_invertidas.png", inverted_img)  