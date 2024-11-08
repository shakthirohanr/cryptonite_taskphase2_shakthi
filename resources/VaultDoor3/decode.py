string = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
output = [''] * 32

for i in range(8):
    output[i] = string[i]
for i in range(8, 16):
    output[i] = string[23 - i]
for i in range(16, 32, 2):
    output[i] = string[46 - i]
for i in range(31, 16, -2):
    output[i] = string[i]

output = ''.join(output)
print(f"picoCTF{{{output}}}")