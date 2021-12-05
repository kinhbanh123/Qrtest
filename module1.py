import cv2
detector = cv2.QRCodeDetector()
reval,point,s_qr = detector.detectAndDecode(cv2.imread('first.png'))
f = open("final.txt",'w+')
f.write(reval)
f.close()

