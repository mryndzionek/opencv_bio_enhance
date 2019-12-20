import cv2 as cv

inputImage = cv.imread("images/input.JPG", -1)
retina = cv.bioinspired_Retina.create((inputImage.shape[1], inputImage.shape[0]))

#retina.write('retinaParams.xml')
retina.setup('retinaParams.xml')

retina.run(inputImage)

#grab retina outputs
retinaOut_parvo = retina.getParvo()
retinaOut_magno = retina.getMagno()

#draw retina outputs
cv.imwrite('parvo.jpg', retinaOut_parvo)
cv.imwrite('magno.jpg', retinaOut_magno)
