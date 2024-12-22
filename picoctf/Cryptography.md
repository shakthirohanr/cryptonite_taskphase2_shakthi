# Cryptography

This module is about cryptography.

- [Cryptography](#cryptography)
  - [C3](#c3)
    - [Thought process and approach](#thought-process-and-approach)
    - [Resources used](#resources-used)
    - [Concepts and knowledge gained](#concepts-and-knowledge-gained)
    - [Incorect tangents](#incorect-tangents)
    - [The FLAG](#the-flag)
  - [Custom Encryption](#custom-encryption)
    - [Thought process and approach](#thought-process-and-approach-1)
    - [The FLAG](#the-flag-1)
  - [miniRSA](#minirsa)
    - [Thought process and approach](#thought-process-and-approach-2)
    - [The Flag](#the-flag-2)

## C3

### Thought process and approach 

Firstly I downloaded `ciphertext` and `convert` from the website.

On inspecting the files, I found that `convert` is a python script that acts as a encoder and `ciphertext` is the encoded message.I tried reversing the things that `convert` does and wrote a `decoder.py` script.

```
import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

for char in chars:
 cur = lookup2.index(char)
 out += lookup1[(cur + prev) % 40]
 prev = (cur+prev) % 40

sys.stdout.write(out)
 
```

I ran the script passing in `ciphertext` as the input and it gave me the following code snippet:

```
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1
```

I tried to run this python script but it had a syntax error so I corrected it enclosing the print command with brackets:
```
- print chars[o] #prints
+ print(chars[0]) #prints
```
Initially I tried passing in `ciphertext` as the input for the script but it was not correct and then I tried passing in the script itself as the input and it printed out the following which turned out to be the flag.
```
a
d
l
i
b
s
```

### Resources used

- Python

### Concepts and knowledge gained

- Learnt basics of python syntax and how the `fileinput` package works.
- Learnt reversing ciphers.

### Incorect tangents 

After getting the decoded script, I ran the script passing in `ciphertext` as the input and got:
```
L
g
H
D
P
t
```
I thought that this was the flag but it was incorrect. I was stuck on this from a long time. Then I read the comments of script and noticed `#selfinput` so I passed the program itself as the text to be decoded and it worked.

### The FLAG

Following the picoCTF flag format I got the flag:

```
picoCTF{adlibs}
```

## Custom Encryption

### Thought process and approach

Looking at the given program, I noticed that the program has two parts of encryption. It first gets an semi cipher using an XOR shift and then it uses Diffie–Hellman key exchange to further encrypt it.
The python script I wrote to decrypt it is [here](../resources/custom_encryption/decrypt.py)

We know the following values:

```
a = 95
b = 21
p = 97
g = 31
cipher = [237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]
```

Since the values of `p` and `g` are fixed in the program, we can use the generator function to generate `u` and `v` in order to get the key. Because the program checks wheter the key and the shared key are equal and exits the program if not, we can find only `u` or `v`. In this case, I used the value of `v` to get the key.

```
def generator(g, x, p):
    return pow(g, x) % p

v = generator(g, b, p)
key = generator(v, a, p)

semi_cipher = ""
for c in cipher:
    semi_cipher += chr(c//311//key)
```

Now that I have the semi cipher, I need to perform the XOR shift to get the flag but the program reverses the plaintext before encrypting it so the key also reverses but since we know the key is `trudeau` and the flag will start with `picoCTF{`, we can get the key that will decrypt the semi cipher. Calling the function with semi cipher and the key as `picoCTF{`, I get the key as `aedurtu`. Using this key, I was able to decrypt the flag. 

```
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    k = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        k += key_char
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    print(f"key: {k}")
    return cipher_text
```

### The FLAG

The flag is:

``` 
picoCTF{custom_d2cr0pt6d_66778b34}
```

## miniRSA

### Thought process and approach

In RSA encryption the message is encrypted by using the formula:

```
ciphertext = message ^ e % n 
```

In this specific case, our `e` value is only 3 which is very small and therefore `message ^ 3` will also be a small number but the `n` value provided is very large. So the equation essentially changes to:

```
ciphertext = message ^ 3
```

Therefore, to get the message, we need to find the cube root of the ciphertext. I tried implementing this in python but I kept encountering errors due to the enormous size of `n`. I did some research on packages that can do this and found the `gmpy2` package which can handle large numbers. Using the package, I wrote this script in order to get the cube root:

```
import gmpy2
from Crypto.Util.number import *

ciphertext = 2205316413931134031074603746928247799030155221252519872650080519263755075355825243327515211479747536697517688468095325517209911688684309894900992899707504087647575997847717180766377832435022794675332132906451858990782325436498952049751141 
n = 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e = 3

cube_root, is_exact = gmpy2.iroot(ciphertext, 3)
message_bytes = long_to_bytes(cube_root)
message = message_bytes.decode("utf-8")
print(f"Message: {message}")
```

To convert the cube root to a string, I used the `long_to_bytes` function from the `Crypto.Util.number` package and then used the `decode` function to convert the bytes to a string. Doing this, I was able to get the flag.

### The Flag

The flag is:

```
picoCTF{n33d_a_lArg3r_e_d0cd6eae}
```