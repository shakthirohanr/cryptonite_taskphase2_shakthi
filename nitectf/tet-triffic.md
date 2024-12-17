# tet-triffic!

![](https://i.imgur.com/aLecoHm.png)

I downloaded the files and found a `pcap` file and a python file. 

On insepecting the python file, I found that it was an implementation of the game tetris. The game had predefined blocks and had different coloured blocks aswell. I thought that completed game would have the written out flag.

I moved on to check out the `pcap` file in Wireshark and found that it was a capture of USB packets. I figured out that we must replay the keystrokes found in the caputre file on the tetris game. I did some research and went through this [youtube video](https://www.youtube.com/watch?v=EnOgRyio_9Q&t=124s) to exract the keystrokes from the pcap files and saved it in [keystrokes.txt](../resources/tet-triffic/keystrokes.txt)

![](https://i.imgur.com/s0C2PZw.png)

Then I moved onto the emulating keystokes on the fame part. I used Gemini to modify to the python file to read the keystrokes from the file and then replay them on the game. I also increased the fps to 165 to make the process faster. The code I used is at [tetris.py](../resources/tet-triffic/tetris.py)

![cool animation](https://i.imgur.com/Sj38iMp.gif)

After working on this for 2 hours. It turned out that the QR code was broken. Then I got stuck on reparing the QR code for hours. Whatever I tried to do didn't seem to work. I remembered a [video](https://www.youtube.com/watch?v=w5ebcowAJD8) from Versatium on how QR codes worked. After painstakingly placing pixel after pixel on a pixel art website, I ended up with this:

![](https://cdn.discordapp.com/attachments/1314927157310656555/1317444229525667901/1734173581374.png?ex=6762a98d&is=6761580d&hm=5ced38ced2e442b0f51734132511699c92e6d2744331ba628a66a3a999cae43e&)

But even now I couldn't scan the QR code. As a last resort I googled qr code related ctf challenges and found a writeup that mentioned a webite called [Qrazybox](https://merri.cx/qrazybox/). I uploaded the image there and finally got the flag.


## Flag

![](https://cdn.discordapp.com/attachments/1146471180858048532/1318569263803404328/image.png?ex=6762ccd2&is=67617b52&hm=56337ebbf95d4d02f324c7c3927040b6af51db1382ff91f069b9a950d33afc58&)