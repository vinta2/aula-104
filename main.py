import cv2

img=cv2.imread("poster.jpg")
foguete=img[120:360,400:500]
img[100:340,500:600]=foguete

text="oi meu nome e vitor"
cv2.putText(img,text,(20,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.imshow("poster",img)
cv2.waitKey(0)