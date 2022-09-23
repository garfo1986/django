
import hashlib
from hashlib import md5, sha1


text= "Hello world"

encrypte = md5(text.encode("utf-8"))
encrypteread = encrypte.hexdigest()
#print (encrypteread)

encrypte1 = sha1(text.encode("utf-8"))
encrypteread1 = encrypte1.hexdigest()
#print (encrypteread1)

encrypted3 = (sha1(text.encode("utf-8")).hexdigest())

print(encrypte1)
print(encrypteread1)
print(encrypted3)

text2= input("type your password: ")
encrypte2 = sha1(text2.encode("utf-8"))
encrypteread2 = encrypte2.hexdigest()


if encrypteread1 ==encrypteread2:
    print ("passwords match")
else:
    print("passwords don't match")