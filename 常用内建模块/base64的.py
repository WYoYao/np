import base64,os

with open("./src/pic/txt.txt","rb") as target:
    t=target.read()
    print(base64.b64encode(t))
    print(base64.b64decode(base64.b64encode(t)))
    # 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
    print(base64.urlsafe_b64decode(base64.urlsafe_b64encode(t)))