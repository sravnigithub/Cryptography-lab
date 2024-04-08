#1.sh1 digest

import hashlib

def calculate_sha1(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    return sha1.hexdigest()

if __name__ == "__main__":
    text = input("Enter the text to calculate SHA-1 digest: ")
    sha1_digest = calculate_sha1(text)
    print("SHA-1 digest:", sha1_digest)



#2.mds digest

import hashlib

def calculate_md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

if __name__ == "__main__":
    text = input("Enter the text to calculate MD5 digest: ")
    md5_digest = calculate_md5(text)
    print("MD5 digest:", md5_digest)
