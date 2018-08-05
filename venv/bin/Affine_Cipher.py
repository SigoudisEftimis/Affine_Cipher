




 # The function str2lst accepts a string  and returns its arithmetic coding to ASCI

def str2lst(string):

    return [ord(x) - 65 for x in string]


# The function lst2str receives a list of numbers and returns an alphanumeric

def lst2str(list):

    return ''.join([chr(x+65) for x in list])

# This function returns the greatest common divisor (gcd) of two  integers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# This functions returns true if  two integers are relatively prime
def coprime(a, b):
    return gcd(a, b) == 1

# This function implements the extendes Euclidean algorithm .

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# This function returns  a modular multiplicative inverse of an integer a
def inverse(a,n):
    d,s,t = egcd(a,n)
    if d == 1:
        return s %n
    else: print(a, "in not in 26* group")
    return False

# Encryption with Affine cipher algorithm

def affine_enc(message,key1,key2):
    plaintextList = str2lst(message)
    ciphertextList = [(key1 *x+key2) % 26 for x in plaintextList]
    ciphertext = lst2str(ciphertextList)
    return ciphertext

# Decryption with Affine cipher algorithm

def affine_dec(ciphertext,key1,key2):
    key1_inverse = inverse(key1,26)
    ciphertextList = str2lst(ciphertext)
    plaintextList = [(key1_inverse *(x-key2)) % 26 for x in ciphertextList]
    plaintext = lst2str(plaintextList)
    return plaintext


if __name__ == '__main__':

    k1 , k2 = 11 , 4
    message = "UNIVERSITY"
    ciphertext = affine_enc(message, k1, k2)
    print ("The plaintext message: " + message + " becomes --> " + ciphertext)

    print("The ciphertext message: " + ciphertext + " becomes --> " + affine_dec(ciphertext, k1, k2))