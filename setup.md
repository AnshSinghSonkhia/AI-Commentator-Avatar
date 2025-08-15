# Steps to Run the "AI Virtual News Anchor" Project

1. **(Optional) Create a Virtual Environment**
   - Open PowerShell in your project folder.
   - Run:
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```

2. **Install Dependencies**
   - Run:
     ```powershell
     pip install -r requirements.txt
     ```
   - This installs all required Python packages (gTTS, moviepy, OpenCV, numpy, requests, newspaper3k, GoogleNews, tqdm, torch, torchvision, etc.).

3. **Install ffmpeg**
   - Download ffmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
   - Add ffmpeg to your system PATH.

4. **Download Wav2Lip Pretrained Model**
   - Download `Wav2Lip.pth` from [https://github.com/Rudrabha/Wav2Lip](https://github.com/Rudrabha/Wav2Lip)
   - Place `Wav2Lip.pth` in the project directory or inside the `Wav2Lip` folder.

5. **Download espeak-ng** 

    - https://github.com/espeak-ng/espeak-ng/releases/tag/1.52.0

6. **Run the Project**
   - Start the GUI:
     ```powershell
     python gui.py
     ```
   - Use the GUI to enter a news topic and number of news items, then click "Generate News Video".

7. **Output**
   - The final video will be saved as `output/result_voice.mp4`.

---

If you encounter any errors during these steps, let me know the error message and I will help you resolve them.

## Temporarily removing

```numba==0.48```

from Wav2Lip/requirements.txt

---

# Sample input

Former Reserve Bank of India (RBI) Governor Raghuram Rajan has warned that US President Donald Trump’s decision to impose a 50 per cent tariff on Indian exports could have severe political repercussions if it forces New Delhi to halt its purchases of Russian oil.

Speaking to International Valor, Rajan said the economic impact of stopping Russian oil imports would not be catastrophic, since current prices for non-Russian crude are not much higher. “Stopping purchases of Russian oil wouldn’t be a disaster for India, since current prices aren’t much higher than for Russian crude,” he explained according to a ET report.

However, Rajan stressed that the political consequences could be far more damaging. “The bigger issue is political , publicly bowing to US demands would be deeply unpopular domestically,” he said. According to him, if India had quietly reduced its purchases without public pressure, it might have been politically manageable. Trump’s public announcement and tariff threats have now made that path much more difficult.

“It’s hard to negotiate with a gun to your head,” Rajan warned, adding that coercive tactics rarely yield long-term diplomatic goodwill.

The 50% tariff, announced last week, is aimed at compelling India to cut ties with Russia’s oil sector. Rajan acknowledged Washington’s strategic concerns but criticised the blunt approach. He suggested that a behind-the-scenes diplomatic push could have been more effective than a public ultimatum that corners India’s leadership.


# Sample input 2

“They need to understand what is important and what is not. This is as simple as that. For me, humare desh ka wo jawan jo sarhad par khada hua hai, unki families jo kayi baar unko nahi dekh paati hain, unki shahadat ho jaati hai, wo ghar wapas nahi laut paate hain — unki itni badi sacrifice hoti hai hum sabke liye. Toh ye to bahut chhoti si baat hai ki hum ek cricket match na chhod sakein. For me, the soldier who stands on the border, whose family often doesn’t get to see him, who sometimes sacrifices his life and never returns home — their sacrifice is so immense for all of us. Compared to that, this is a very small thing — that we can’t even skip playing one cricket match. It’s a very small matter," Harbhajan Singh was quoted as saying to the Times of India.

The Men in Blue are the reigning champions and the initial host of this tournament, as it will now be held in the UAE, so that the Men in Green don't have to cross their borders and come to India.