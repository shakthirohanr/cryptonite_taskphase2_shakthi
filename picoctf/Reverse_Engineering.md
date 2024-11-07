# Reverse Engineering

This module is about reverse engineering.

- [Reverse Engineering](#reverse-engineering)
  - [GDB baby step 1](#gdb-baby-step-1)
    - [Thought process and approach:](#thought-process-and-approach)
    - [Resources used:](#resources-used)
    - [Concepts and knowledge gained:](#concepts-and-knowledge-gained)
    - [The FLAG:](#the-flag)

## GDB baby step 1

### Thought process and approach:

Firstly I donwloaded the `debugger0_a` file from the website. I used the `file` command to check what kind of a file it is.

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


### Resources used:

- https://gist.github.com/jarun/ea47cc31f1b482d5586138472139d090 - Very Useful
- https://www.eecg.utoronto.ca/~amza/www.mindsec.com/files/x86regs.html
- https://www.cs.virginia.edu/~evans/cs216/guides/x86.html#:~:text=The%20mov%20instruction%20copies%20the,to%2Dmemory%20moves%20are%20not

### Concepts and knowledge gained:

- Learnt about the basic usage of `gdb`.
- Got an idea of what registers are and their uses.
- Instructions in assembly (mov)


### The FLAG:

I followed the flag format of PicoCTF and got the flag:

**```picoCTF{549698}```**