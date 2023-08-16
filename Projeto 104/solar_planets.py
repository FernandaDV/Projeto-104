import cv2
img=cv2.imread('sistema solar.jpg')

cv2.putText(img,'Sol',(100,80),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,'Mercurio',(110,180),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,'Venus',(190,270),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,'Terra',(300,270),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,'Marte',(400,270),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,'Jupiter',(500,90),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,'Saturno',(720,110),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,'Urano',(950,130),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,'Netuno',(1080,130),cv2.FONT_ITALIC,0.5,(255,255,255))


cv2.imshow('resultado',img)
cv2.waitKey(0)



