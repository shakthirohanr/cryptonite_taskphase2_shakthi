# Cryptography

This module is about cryptography.

- [Cryptography](#cryptography)
  - [C3](#c3)
    - [Thought process and approach](#thought-process-and-approach)
    - [Resources used](#resources-used)
    - [Concepts and knowledge gained](#concepts-and-knowledge-gained)
    - [Incorect tangents](#incorect-tangents)
    - [The FLAG](#the-flag)

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