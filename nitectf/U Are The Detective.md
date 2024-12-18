# U Are The Detective

When I first downloaded the `signal.sr` file from the website, I did not know what kind of a file it was. I ran `file` and it returned: 

![](https://cdn.discordapp.com/attachments/1146471180858048532/1318587033576538172/image.png?ex=6762dd5e&is=67618bde&hm=4edc1eaf6ed3229f2a994edacc9ebb0649c1c392019ee8d53aeedb7b67285098&)

I renamed the file to `signal.zip` and extracted it. I went through the `metadata` file and read that it was a sigrok file. So after doing some research, I found out that you can use Pulseview to open these files. I downloaded Pulseview and opened the file. 

There was a signal in the D1 channel. Zooming in, I saw that the signal it was a square waveform.

![](https://i.imgur.com/ZlLyXcO.png)

When I image searched the waveform, I found out that it was a UART waveform. I went to youtube to learn how UART signals work and found this [video](https://www.youtube.com/watch?v=sTHckUyxwp8). Pulseview has a built in decoder for UART signals. But when I tried to decode the signal using the decoder, I kept getting a `frame` error. After researching how to fix it, I learnt that we need the baud rate of the signal in order to decode it correctly. 

![](https://cdn.discordapp.com/attachments/1146471180858048532/1318759656968949780/image.png?ex=67637e23&is=67622ca3&hm=a9acd33c43f0a59280e1f531e908976e39243c908751aa9b21a09c86ce6b13ae&)

To find the baud rate, we should find the bitrate of the smallest bit. Using Pulseview's built in baud rate guesser, I found that the baud rate is 5333333.

![](../resources/U%20Are%20The%20Detective/image.png)

Using the UART signal and inputting the correct baud rate, I was getting data but it was in hex format. Changing it to ascii, I started to see the flag.

![alt text](../resources/U%20Are%20The%20Detective/image2.png)

I exported the data to a file and I could get the flag.

## Flag 

The flag is `nite{n0n_std_b4ud_r4t3s_ftw}`