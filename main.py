import secrets
import time

def generate_number_sec(lower_bound,upper_bound,exl = set()):
    while True:
        number = secrets.randbelow(upper_bound - lower_bound + 1) + lower_bound
        if number not in exl:
            return number
            

        

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1 
    
    
def Miller_Robins_is_prime_one_iter(number_to_check,a):

    if not number_to_check % 2:
        return False

    if not number_to_check % 3:
        return False

    k = 0
    m = number_to_check - 1
    while m % 2 == 0:
        m//=2
        k += 1
    b = pow(a,int(m),number_to_check)
    if b == 1:
        return True
    elif b == number_to_check -1:
        return True
    
    
    b = pow(b,2,number_to_check)
    
    
    for _ in range(k):
        if b == 1:
            return False
        elif b == number_to_check -1:
            return True
        else:
            b = pow(b,2,number_to_check)
    return False 

def generate_prime(lower = 2 ** 1024, upper = 2 ** 2048, safety= 50):
    checked = set()
    while True:
        maybe_prime = generate_number_sec(lower,upper,checked)
        if is_prime_for_sure_aprox(maybe_prime,safety):
            return maybe_prime
        checked.add(maybe_prime)
        
        
def is_prime_for_sure_aprox(number_for_check,surenes = 50):  #surness 50
    excluded = set()
    for _ in range(surenes):
        a_to_test = generate_number_sec(2,number_for_check - 2,excluded)
        if not Miller_Robins_is_prime_one_iter(number_for_check,a_to_test):
            return False
        excluded.add(a_to_test)
    return True

class RSA:
    def __init__(self,public_key = None,private_key = None,e = 65537, prime_safety = 50, prime_lower = 2**1024, prime_upper = 2**2048):
        if not(private_key == None and public_key == None):
            self.n = public_key
            self.d = private_key
            self.e = e
        else:
            self.key_generation(prime_safety,prime_lower,prime_upper,e)      
        print(str(self.n) + " " + str(self.d) + " " + str(self.e))
    
    def key_generation(self,safetyer,lower_band,upper_band,eeler):
        p = generate_prime(lower_band,upper_band,safetyer)
        q = generate_prime(lower_band,upper_band,safetyer)
        while p == q:
            q = generate_prime(lower_band,upper_band,safetyer)
        r = (p-1)*(q-1)
        self.n = p * q
        self.d = mod_inverse(eeler,r)
        self.e = eeler
    
    
        
    
    def cypher_text(self,text):
        return pow(text, self.e, self.n)
    
    def decypher_text(self,cyphertext):
        return pow(cyphertext, self.d, self.n)    

    def sign_text(self, text):
        return pow(text, self.d, self.n)
        
    def decypher_sign(self, sign):
        return pow(sign, self.e, self.n)

    def validate(self, safety = 9999999999):
        cyphertext = secrets.randbelow(safety)
        signtext = secrets.randbelow(safety)
        cyphered = self.cypher_text(cyphertext)
        sign = self.sign_text(signtext)
        if self.decypher_text(cyphered) == cyphertext and self.decypher_sign(sign) == signtext:
            return True
        else:
            return False

rsa = RSA()
print(rsa.validate())

print(generate_number_sec(2 ** 2048,2 ** 4096)) 