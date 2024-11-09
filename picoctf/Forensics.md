# Forensics

This module is about forensics.

- [Forensics](#forensics)
  - [Trivial Flag Transfer Protocol](#trivial-flag-transfer-protocol)
    - [Thought process and approach](#thought-process-and-approach)
    - [Resources used](#resources-used)
    - [Concept and knowledge gained](#concept-and-knowledge-gained)
    - [The FLAG:](#the-flag)

## Trivial Flag Transfer Protocol

### Thought process and approach 

I downloaded the `tftp.pcapng` from the website. I was familiar with `pcap` files but wasn't sure what `pcapng` meant so I googled it. It turns out thats its an upgrade to the `pcap` format. I worked with `pcap` files in KernelCTF so I opened it in Wireshark.

![](https://i.imgur.com/Q9EKkri.png)

There seems to be an `instructions.txt` file being transmitted but it was all in the format of data packets so I looked for a tool to recover the files. I went through the resources provided in the pdf and came across [Network Miner](https://www.netresec.com/?page=NetworkMiner). I downloaded it and tried to import the `tftp.pcapng` file but it required premium to open so I converted the `pcapng` file into a `pcap` file using `editcap -F tftp.pcapng tftp1.pcap` and opened it in Network Miner.

![](../resources/Trivial_Flag/networkminer.png)

I downloaded all the files from Netork Miner into a folder. When I opened `instructions.txt`, I found it to be encrypted. I tried to decrypt it using different ciphers in `CyberChef` and found that it was encrypted using `ROT13`. Decrypting it gave:

```
TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN
```

There was also a `plan` file which was also encrypted using `ROT13`. Decrypting it gave:

```
I USED THE PROGRAM AND HID IT WITH - DUEDILIGENCE. CHECK OUT THE PHOTOS
```

There was a `program.deb` file which I tried to install, When trying to install, I found out that it was `steghide`:

![](https://i.imgur.com/6F43Y0A.png)

I have used `steghide` in a previous CTF so I knew that it's used to hide files in images. I tried to extract the different image files I got from Network Miner, providing the password as `DUEDILIGENCE`. In the `picture3.bmp` file, I got the file `flag.txt` which contained the flag:

![](https://i.imgur.com/RUDTxnf.png)

### Resources used

- [Wireshark](https://www.wireshark.org/)
- [Network Miner](https://www.netresec.com/?page=NetworkMiner)
- [CyberChef](https://gchq.github.io/CyberChef/)
- **Steghide**

### Concept and knowledge gained

- Learnt working with `pcap` files using `Wireshark`.
- Learnt using `Steghide` to extract files from images.
- Learnt about `Netork Miner` and how it can be used to extract files from `pcap` files.

### The FLAG:

The flag is:

```  
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```
