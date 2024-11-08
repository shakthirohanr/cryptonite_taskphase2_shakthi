import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""
prev = 0

for char in chars:
 cur = lookup2.index(char)
 out += lookup1[(cur + prev) % 40]
 prev = (cur+prev) % 40

sys.stdout.write(out)
