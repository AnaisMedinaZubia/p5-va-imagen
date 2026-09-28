import cv2
# Leer la imagen con cv2 = computer vision
img = cv2.imread('hamster.jpg')
# determinar tipo de imagen numpy.ndarry
print(type(img))
# mostrar pixeles (279, 464, 3)
print(img.shape)
# mostrando imagen en ventana barra de titulo hamster 0099
cv2.imshow('hamster 0099', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()
