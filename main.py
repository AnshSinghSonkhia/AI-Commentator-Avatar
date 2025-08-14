import sys
import os
import logging
import subprocess
import platform
from modules.text_to_speech import text_to_speech
from modules.avatar_generation import generate_lip_synced_video
from modules.text_generation import fetch_latest_news_with_content
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_avatar(avatar_path):
    """Validate the avatar image file"""
    logger.info(f"Checking avatar at: {os.path.abspath(avatar_path)}")
    logger.info(f"File exists: {os.path.exists(avatar_path)}")

    if not os.path.exists(avatar_path):
        raise FileNotFoundError(f"Avatar file not found at {avatar_path}")

    logger.info(f"File size: {os.path.getsize(avatar_path)} bytes")
    logger.info("Running image diagnostic...")

    try:
        img = Image.open(avatar_path)
        img.verify()
        img.close()
        logger.info("✅ Image verification passed - file is valid")
        
        return True
    except Exception as e:
        logger.error(f"❌ IMAGE VALIDATION FAILED: {str(e)}")
        logger.error("The avatar image file is corrupted or invalid. Please:")
        logger.error("1. Re-save the image using Paint or Photoshop")
        logger.error("2. Try using a different image file")
        logger.error("3. Check file permissions")
        
        return False


def play_video(video_path):
    """Automatically play the video using the default media player."""
    logger.info("🔁 Attempting to play the generated video...")
    
    try:
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', video_path))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(video_path)
        else:  # Linux and others
            subprocess.call(('xdg-open', video_path))
        logger.info("📽️ Video playback started.")
    except Exception as e:
        logger.error(f"❌ Failed to play video: {str(e)}")

def main():
    logger.info("🐍 Python in use: %s", sys.executable)

    # Example news text
    news_text = "Good evening, and welcome to the Daily Update – your trusted source for the latest headlines from around the globe. I’m your virtual anchor, bringing you today’s top stories."
    #news_text = fetch_latest_news_with_content("INDIA", 1)

    if not news_text:
        logger.error("⚠️ No news content to generate speech.")
        return

    try:
        # Step 1: Generate TTS audio
        logger.info("Generating speech from text...")
        audio_path = text_to_speech(news_text)
        logger.info(f"Audio generated: {audio_path}")

        # Step 2: Validate avatar
        avatar_path = os.path.join(os.path.dirname(__file__), "assets/avatars/avatar-tech.png")
        if not validate_avatar(avatar_path):
            return

        # Step 3: Generate video using Wav2Lip
        logger.info("Generating lip-synced AI avatar video...")
        video_path = generate_lip_synced_video(audio_path, avatar_path)

        if video_path and os.path.exists(video_path):
            logger.info(f"🎉 Project completed successfully! Video ready at: {video_path}")

            # Step 4: Automatically play the video
            play_video(video_path)

        else:
            logger.error("⚠️ Video generation failed. Check logs for details.")

    except Exception as e:
        logger.error(f"❌ Fatal error in main execution: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()