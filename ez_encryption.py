from hashlib import sha512

def passwordEncryption(password):
    ePassword = sha512(str(password).encode('utf8'))
    return ePassword.hexdigest()

pw = input("Enter password: ")
print("Encrypted password:",passwordEncryption(pw))