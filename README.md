# RSA Implementation in Python

## Overview
This is a Python implementation of the RSA cryptographic algorithm, including key generation, encryption, decryption, signing, and verification. The implementation uses the Miller-Rabin primality test to generate large prime numbers securely.

## Features
- Secure random prime generation using Miller-Rabin primality test
- RSA key generation with customizable bit sizes
- Encryption and decryption of messages
- Basic RSA validation function

## Installation
No external dependencies are required as this implementation uses Python's built-in libraries. Ensure you are using **Python 3.6+**.

## Usage
### Generating RSA Keys
```python
rsa = RSA()
print(f"Public Key (n): {rsa.n}")
print(f"Private Key (d): {rsa.d}")
```

You can also initialize an RSA object with your own keys:
```python
rsa = RSA(public_key=your_n, private_key=your_d, e=your_e)
```

### Encrypting and Decrypting
```python
message = 123456  # Must be an integer
ciphertext = rsa.cypher_text(message)
plaintext = rsa.decypher_text(ciphertext)
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted message: {plaintext}")
```

### Signing and Verifying Signatures
```python
message = 7890  # Must be an integer
signature = rsa.sign_text(message)
verified_message = rsa.decypher_sign(signature)
print(f"Signature: {signature}")
print(f"Verified message: {verified_message}")
```

### Validating the RSA Implementation
```python
print("RSA Validation Result:", rsa.validate())
```


## Disclaimer
This implementation is for educational purposes only and **should not be used in production systems**. For secure cryptographic applications, consider using established libraries like PyCryptodome or OpenSSL.


