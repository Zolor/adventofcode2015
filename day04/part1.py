import hashlib

data = open("input.txt").read()
secret = 0

while True:
    tmp_hash = hashlib.md5((data + str(secret)).encode('utf-8')).hexdigest()
    if str(tmp_hash).startswith("00000"):
        print(secret)
        break
    secret += 1