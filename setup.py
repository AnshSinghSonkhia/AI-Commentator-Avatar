import os
import requests
from pathlib import Path

if not os.path.exists("temp/"):
    os.makedirs("temp")

if not os.path.exists("output/"):
    os.makedirs("output")
    
try:
    save_dir = Path("Wav2Lip/checkpoints")
    save_dir.mkdir(parents=True, exist_ok=True)
    
    urls = [
        {
            "link": "https://huggingface.co/numz/wav2lip_studio/resolve/main/Wav2lip/wav2lip.pth?download=true",
            "fname": "wav2lip.pth"
        },
        {
            "link": "https://huggingface.co/numz/wav2lip_studio/resolve/main/Wav2lip/wav2lip_gan.pth?download=true",
            "fname": "wav2lip_gan.pth"
        }
    ]
    
    for url in urls:
        filename = url["fname"]
        file_path = f'{save_dir}\\{filename}'

        print(f"Downloading {url['link']} to {file_path}...")

        response = requests.get(url["link"])
        response.raise_for_status()
        
        with open(file_path, "wb") as f:
            f.write(response.content)

    print("✅ Download complete.")
except Exception as e:
    print(f"❌ An error occurred: {e}")