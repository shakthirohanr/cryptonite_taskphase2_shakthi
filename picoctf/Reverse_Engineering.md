# Reverse Engineering

This module is about reverse engineering.

- [Reverse Engineering](#reverse-engineering)
	- [GDB baby step 1](#gdb-baby-step-1)
		- [Thought process and approach](#thought-process-and-approach)
		- [Resources used](#resources-used)
		- [Concepts and knowledge gained](#concepts-and-knowledge-gained)
		- [The FLAG:](#the-flag)
	- [ARMssembly 1](#armssembly-1)
		- [Thought process and approach](#thought-process-and-approach-1)
		- [Resources used](#resources-used-1)
		- [Concepts learnt and knowledge gained](#concepts-learnt-and-knowledge-gained)
		- [Incorrect tangents](#incorrect-tangents)
		- [The FLAG](#the-flag-1)
	- [Vault door 3](#vault-door-3)
		- [Thought process and approach](#thought-process-and-approach-2)
		- [Resources used](#resources-used-2)
		- [Concepts and knowledge gained](#concepts-and-knowledge-gained-1)
		- [The FLAG](#the-flag-2)

## GDB baby step 1

### Thought process and approach

Firstly I downloaded the `debugger0_a` file from the website. I used the `file` command to check what kind of a file it is.

```
debugger0_a: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=15a10290db2cd2ec0c123cf80b88ed7d7f5cf9ff, for GNU/Linux 3.2.0, not stripped

```

I saw that it was an executable so I made the file executable using `chmod u+x ./debugger0_a` and tried to run it but it didn't do anything.

The challenge obviously hints us to use `gdb` but I have had no experience with using it and also the challenge statement asks us to disassemble the file so I googled gdb disassembly guide and came upon this [gist](https://gist.github.com/jarun/ea47cc31f1b482d5586138472139d090).

In the guide, he had used `info functions` to list out the functions in the file so I did the same:

```
0x0000000000001000  _init
0x0000000000001030  __cxa_finalize@plt
0x0000000000001040  _start
0x0000000000001070  deregister_tm_clones
0x00000000000010a0  register_tm_clones
0x00000000000010e0  __do_global_dtors_aux
0x0000000000001120  frame_dummy
0x0000000000001129  main
0x0000000000001140  __libc_csu_init
0x00000000000011b0  __libc_csu_fini
0x00000000000011b8  _fini
```

The challenge statement asks to look into the main function so I referred to the gist again and noticed the `disassemble` command. So I ran `disassemble main` which returned:

```
Dump of assembler code for function main:
   0x0000000000001129 <+0>:	endbr64
   0x000000000000112d <+4>:	push   %rbp
   0x000000000000112e <+5>:	mov    %rsp,%rbp
   0x0000000000001131 <+8>:	mov    %edi,-0x4(%rbp)
   0x0000000000001134 <+11>:	mov    %rsi,-0x10(%rbp)
   0x0000000000001138 <+15>:	mov    $0x86342,%eax
   0x000000000000113d <+20>:	pop    %rbp
   0x000000000000113e <+21>:	ret
```
 
Finally I see the mention of `eax` but I didn't know what an `eax register` was so I googled it.

![](https://i.imgur.com/8x0QdRf.png)

So I learnt that registers are used to store values and are like built-in variables for the computer.Also I got to know that when you disassemble something using gdb, the returned code is in assembly so I researched about the `mov` instruction in assembly.

After going through some websites, I learnt that the `mov` instruction copies the data item referred to by its second operand into the location referred to by its first operand. So in our case, whatever is being stored in the `eax` register is being copied to `0x86342`. 

The website expects us to give the answer in decimal and memory addresses are in hexadecimal so I used an online hexadecimal to decimal converted and got the resulting value:

![](https://i.imgur.com/HjGn51F.png)


### Resources used

- https://gist.github.com/jarun/ea47cc31f1b482d5586138472139d090 - Very Useful
- https://www.eecg.utoronto.ca/~amza/www.mindsec.com/files/x86regs.html
- https://www.cs.virginia.edu/~evans/cs216/guides/x86.html#:~:text=The%20mov%20instruction%20copies%20the,to%2Dmemory%20moves%20are%20not

### Concepts and knowledge gained

- Learnt about the basic usage of `gdb`.
- Got an idea of what registers are and their uses.
- Instructions in assembly (mov)


### The FLAG:

I followed the flag format of PicoCTF and got the flag:

```
picoCTF{549698}
```

## ARMssembly 1

### Thought process and approach

Firstly I donwloaded the file the website and then ran the `file` command to see what kind of a file is. 

```
./chall_1.S: assembler source, ASCII text
```

I use `cat` to print out the contents of the file.

```
	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 79
	str	w0, [sp, 16]
	mov	w0, 7
	str	w0, [sp, 20]
	mov	w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 20]
	ldr	w1, [sp, 16]
	lsl	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 24]
	sdiv	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	sub	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w0, [sp, 28]
	add	sp, sp, 32
	ret
	.size	func, .-func
	.section	.rodata
	.align	3
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function	.file	"chall_1.c"
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func
	cmp	w0, 0
	bne	.L4
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

I read through the assembly code and noticed the line - `	.file	"chall_1.c"`. I don't  exactly understand what it means but I think that this assembly code was generated from a c program namely - `chall_1.c`.

I found a an [ARM instruction set online](https://iitd-plos.github.io/col718/ref/arm-instructionset.pdf) and found out what each command does.

The program essentially calls a function with an argument and prints out `win` if the value returned by the function is equal to `0` otherwise prits `lose`. So we need to find out the argument that would make the function return 0.

I look at the function code and try to understand what it does:

```	str	w0, [sp, 12]```

This line stores the argument passed by the main program in the location `[sp, 12]`.

```
mov	w0, 79
str	w0, [sp, 16]
mov	w0, 7
str	w0, [sp, 20]
mov	w0, 3
str	w0, [sp, 24]
```

In this snippet of code, 79, 7 and 3 are getting stored in [sp, 16], [sp, 20] and [sp, 24] respectively. They first store the value in the `w0` register and then use `str` to copy it into the memory.

```
ldr	w0, [sp, 20]
ldr	w1, [sp, 16]
lsl	w0, w1, w0
str	w0, [sp, 28]

```
In this snippet of code, `7` is being loaded into `w0` from `[sp, 20]` and `79` is being loaded into `w1` from `[sp, 16]`. Then a left shift operation is being performed - `79 << 7` and the result - `10112` is stored in `w1` which is then stored in `[sp, 28]`.

```
    ldr	w1, [sp, 28]
    ldr	w0, [sp, 24]
    sdiv	w0, w1, w0
    str	w0, [sp, 28]
```
In this snippet of code, the result from the previous operation is being loaded into `w1` from `[sp, 28]` and `3` is being loaded into `w0` from `[sp, 24]`. Then division is performed - `10112 / 3` and the result - `3370` is being stored in `w0` which is then stored in `[sp, 28]`

```
ldr	w1, [sp, 28]
ldr	w0, [sp, 12]
sub	w0, w1, w0
str	w0, [sp, 28]
ldr	w0, [sp, 28]
add	sp, sp, 32
ret
```
In this snippet of code, the result from the previous operation is being loaded into `w1` from `[sp, 28]` and the argument passed onto the function is loaded into `w0` from `[sp, 12]`. Then subraction is performed - `3370 - X` and stores it into `w0` which is then returned by the function. 

The return value should be 0 so `3370 - X = 0` therefore `X = 3370`. The argument should be `3370`. I convert it to hexadecimal using an online editor

![](https://i.imgur.com/WqHbKPE.png)

### Resources used

- https://iitd-plos.github.io/col718/ref/arm-instructionset.pdf
- google 

### Concepts learnt and knowledge gained

- Learnt more about assembly and it's instructions.
- Learnt about arithmetic operations in assembly.
  
### Incorrect tangents 

I was trying to find ways to convert the assembly code into C for better understanding but I don't think there's any way to do that


### The FLAG

Following the flag format of picoCTF and the instructions provided, the flag is:

``` 
picoCTF{00000d2a}
```

## Vault door 3

### Thought process and approach

Firstly I downloaded the `VaultDoor3.java` file from the website. Then I opened it in VSC to analyze it. 

```
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
    }
}

```
I understood that the input we provide should be equal to `jU5t_a_sna_3lpm18gb41_u_4_mfr340` after all the substitutions performed by the program. We can just reverse the substitutions performed on the string to get our flag so I wrote a python script to do this:

```
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
```

Running the script gave me the flag.


### Resources used

- Python

### Concepts and knowledge gained

- Learnt about the basic syntax of Java. 
- Learnt basic python syntax.

### The FLAG

Following the flag format of picoCTF, I got the following flag:

```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
```