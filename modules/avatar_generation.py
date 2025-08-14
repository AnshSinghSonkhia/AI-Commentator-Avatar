import os
import subprocess
import cv2
import numpy as np
from pathlib import Path
import sys

def validate_image_file(filepath):
    """Thorough validation of image file using multiple methods"""
    try:
        # Method 1: Verify with PIL
        from PIL import Image
        with Image.open(filepath) as img:
            img.verify()
            if img.mode not in ('RGB', 'L'):
                img = img.convert('RGB')
        return True
    except Exception as e:
        print(f"❌ PIL validation failed: {str(e)}")
        return False

def load_avatar_image(filepath):
    """Robust image loading with multiple fallbacks"""
    # Try OpenCV first
    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    if img is not None:
        return img

    # Fallback 1: Direct file reading
    try:
        with open(filepath, 'rb') as f:
            img_array = np.frombuffer(f.read(), np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            if img is not None:
                return img
    except Exception as e:
        print(f"⚠️ Direct file reading failed: {str(e)}")

    # Fallback 2: PIL conversion
    try:
        from PIL import Image
        pil_img = Image.open(filepath)
        if pil_img.mode == 'RGBA':
            pil_img = pil_img.convert('RGB')
        return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    except Exception as e:
        print(f"⚠️ PIL conversion failed: {str(e)}")

    return None

def generate_lip_synced_video(audio_path, face_path=None, output_path="output/result_voice.mp4"):
    print("🎥 Generating lip-synced AI avatar video...")

    # Get the project root directory
    project_root = Path(__file__).parent.parent.absolute()

    # Set default face path if not provided
    if face_path is None:
        face_path = project_root / "assets/avatars/avatar-tech.png"

    # Convert all paths to absolute and string
    face_path = str(Path(face_path).absolute())
    audio_path = str(Path(audio_path).absolute())
    output_path = str(project_root / output_path)
    temp_dir = project_root / "temp"
    wav_audio_path = str(temp_dir / "temp.wav")
    temp_video_path = str(temp_dir / "avatar_video.mp4")

    # Ensure required directories exist
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"🔍 Looking for avatar at: {face_path}")

    # Validate image file first
    if not validate_image_file(face_path):
        print(f"❌ The image file at {face_path} is corrupted or invalid")
        print("ℹ️ Please try:")
        print("1. Opening and re-saving the image in an editor")
        print("2. Using a different image format (JPEG recommended)")
        print("3. Checking file permissions")
        return None

    # Load the image with multiple fallbacks
    print("🖼️ Loading avatar image with robust methods...")
    
    img = load_avatar_image(face_path)
    
    if img is None:
        print("❌ All image loading methods failed")
        return None

    print(f"✅ Image loaded successfully. Dimensions: {img.shape}")

    # Convert static image to video
    print("🔄 Converting avatar image to video...")
    
    try:
        height, width = img.shape[:2]

        # Adjust dimensions if needed
        if width % 2 != 0 or height % 2 != 0:
            width = width - 1 if width % 2 != 0 else width
            height = height - 1 if height % 2 != 0 else height
            img = cv2.resize(img, (width, height))
            print(f"⚠️ Adjusted dimensions to: {width}x{height}")

        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(temp_video_path, fourcc, 25.0, (width, height))

        # Write multiple frames
        for _ in range(25):
            out.write(img)
        out.release()
        
        print(f"✅ Temporary video created at: {temp_video_path}")
    except Exception as e:
        print(f"❌ Video creation failed: {str(e)}")
        return None

    # Audio conversion - using list format for subprocess to handle spaces
    print("🔄 Converting audio to WAV format...")
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", audio_path,
            "-ar", "16000", "-ac", "1", "-vn",
            wav_audio_path
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Audio conversion failed: {str(e)}")
        return None

    # Wav2Lip execution - using list format for subprocess
    wav2lip_dir = project_root / "Wav2Lip"
    command = [
        sys.executable, str(wav2lip_dir / "inference.py"),
        # "python", str(wav2lip_dir / "inference.py"),
        "--checkpoint_path", str(wav2lip_dir / "checkpoints" / "wav2lip_gan.pth"),
        "--face", temp_video_path,
        "--audio", wav_audio_path,
        "--outfile", output_path,
        "--static", "True"
        #"--pads", "0", "20", "0", "0",  # Adjust padding (top, bottom, left, right)
        #"--box", "250", "650", "200", "600"  # Manually set face position (y1, y2, x1, x2)
    ]

    print("🎬 Running Wav2Lip...")
    try:
        subprocess.run(command, check=True, cwd=str(wav2lip_dir))
    except subprocess.CalledProcessError as e:
        print(f"❌ Wav2Lip failed: {str(e)}")
        return None

    # Verify output
    if os.path.exists(output_path):
        print(f"✅ Success! Video generated at: {output_path}")
        return output_path
    else:
        print("❌ Final video not created")
        return None