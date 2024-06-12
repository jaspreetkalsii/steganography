import cv2
import os
import string

img=cv2.imread("flower.jpg")
msg=input("Enter secret message:")
password=input("Enter password:")

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)

n=0
m=0
z=0

for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite("encryptedImage.jpg",img)
os.startfile("encryptedImage.jpg")
decryptedMsg=""
n=0
m=0
z=0

decryptionPassword=input("Enter password:")
if(password==decryptionPassword):
    for i in range(len(msg)):
        decryptedMsg=decryptedMsg+c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
        print("Decrypted message is",decryptedMsg)
else:
    print("Authentication denied")
