# <img width="32" height="32" alt="image" src="https://github.com/user-attachments/assets/033acf25-7748-4ea3-a04f-b4c0b54bed0e" /> AI Sports Commentator & News Anchor 


<p align="center">
   <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
   <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-green.svg" alt="Platform">
   <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
   <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status">
   <img src="https://img.shields.io/badge/Streamlit-Enabled-red.svg" alt="Streamlit">
</p>

<p align="center">
  <b>An AI-powered virtual sports commentator and news anchor that brings your sports updates to life!</b>
</p>

---

<p align="center">
  <a href="https://www.youtube.com/watch?v=KXMh7-ApLBg" target="_blank">
    <img src="https://img.shields.io/badge/Watch%20on-YouTube-red?logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=KXMh7-ApLBg" target="_blank">
    <img src="https://github.com/user-attachments/assets/837fd679-4163-43e2-af0e-31fdb0e4a65f" 
         alt="Ansh Singh Sonkhia on News" 
         width="2816" height="1536"/
    >
  </a>
</p>

## 🌟 Overview

Transform sports news and live commentary into engaging video content with our AI-powered virtual anchor system. This cutting-edge application automatically fetches sports news, converts text to natural speech, and generates realistic lip-synced videos featuring an AI avatar - perfect for sports commentary, match updates, and news broadcasting.

## ✨ Key Features

- 🎮 **Interactive GUI Interface** - User-friendly Tkinter-based control panel
- 🌐 **Streamlit Web App** - Run the project in your browser with a modern Streamlit interface
- 📰 **Smart News Fetching** - Automatically retrieves the latest sports news from Google News  
-- 🗣️ **Flexible Text-to-Speech** - Choose between Google's gTTS (online) and pyttsx3 (offline, multi-voice)
- 🎤 **Voice Selection** - Select from available system voices when using pyttsx3
- 👄 **Advanced Lip-Sync Technology** - Wav2Lip integration for perfect mouth movements
- 🎬 **Professional Video Output** - Seamlessly merged audio-video with background effects
- 🏆 **Sports-Focused Content** - Specialized in sports commentary and match analysis

## 🆕 New Features (Aug, 2025)

- Select TTS method: Choose between gTTS (online), pyttsx3 (offline) or coqui ai (offline)
- Voice selection: Pick from available system voices when using pyttsx3 or coqui-tts
- All features accessible via the GUI
- Streamlit web app: Run `streamlit run streamlit-app.py` for a browser-based experience

## 📁 Project Structure

```
AI-Sports-Commentator/
│
├── gui.py                                  # GUI interface built with Tkinter for user interaction and news input
├── main.py                                 # Main controller script that integrates all modules and triggers the complete pipeline
├── boundary_box_detection.py               # Script to detect bounding box coordinates for lips, chin, and cheeks of the avatar image
├── avatar4.png                             # Static avatar image used to generate the lip-synced talking head
├── project GUI screenshot.png              # Screenshot of the GUI to provide a visual preview of the interface
│
├── Wav2Lip/                                # Deep Learning model, that generate the lip-sync video from the image given by the user
│   └── inference.py                        # Lip-sync video generation module using Wav2Lip model
│
├── modules/
│   ├── text_generation.py                  # Automatically fetches and generates news content using web scraping and APIs
│   ├── text_to_speech.py                   # Converts news text into speech using gTTS (online) or pyttsx3 (offline, multi-voice)
│   └── avatar_generation.py                # Coordinates the avatar image and speech audio to generate the final video
│
├── output/
│   └── result_voice.mp4                    # Final output video of the AI avatar reading the news with lip-sync
│
├── click.wav                               # MP3 file containing button sounds used in GUI
├── requirements.txt                        # List of required Python libraries and packages to run the project
└── README.md                               # Project documentation file with setup instructions and project details
```

## ⚙️ Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AnshSinghSonkhia/AI-Commentator-Avatar
   cd AI-Sports-Commentator
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate    # On Windows
   # or
   source venv/bin/activate  # On Linux/Mac
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Pre-trained & Setup:**
    - Windows
    ```bash
    python setup.py
    ```
    - Linux / MacOS
    ```bash
    python3 setup.py
    ```

5. **Run the Project:**
    - **Tkinter GUI:**
       ```bash
       python gui.py
       ```
       Use the GUI to:
       - Enter a topic and news count, or type your own news text
       - Select TTS method (gTTS or pyttsx3) and voice (if using pyttsx3)
       - Click "Generate Video" to create a lip-synced news anchor video

    - **Streamlit Web App:**
       ```bash
       streamlit run streamlit-app.py
       ```
       Use the browser-based interface for a modern experience. All major features are available in both GUI and Streamlit modes.

## 🎥 Output

The final output video will be saved as `output/result_voice.mp4`, showcasing the AI avatar delivering sports commentary in a realistic, lip-synced video format.

## 📜 Dependencies

- Python 3.7+
- gTTS
- pyttsx3
- moviepy
- OpenCV
- numpy
- requests
- newspaper3k
- GoogleNews
- tqdm
- torch, torchvision
- ffmpeg (installed and added to system path)
- Pillow (for image processing in GUI)
- streamlit (for web app)
- coqui-tts

## 📬 Contact

For any queries or issues, please contact via GitHub issues or open a pull request.

---

<p align="center">
  <i>Brought to you by Ansh Singh Sonkhia, B.Tech in CSE (Artificial Intelligence and Machine Learning)</i>
</p>
