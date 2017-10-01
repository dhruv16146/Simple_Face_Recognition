import numpy as np
import cv2
import sys

x=sys.argv[1] 
print x

try:
	test1 = cv2.imread(x)
	gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
	haar_face_cascade = cv2.CascadeClassifier('abcd.xml')
	faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

	for (x,y,w,h) in faces:
	    cv2.rectangle(test1,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow('img',test1)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

except:
	print "The image name you provided doesn't exit or the extension name you provided is incorrect"




#print('Faces found: ', len(faces))