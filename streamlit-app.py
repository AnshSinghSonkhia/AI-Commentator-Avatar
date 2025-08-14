import streamlit as st
from modules.text_to_speech import text_to_speech
from modules import avatar_generation, text_generation
from main import validate_avatar, play_video
import os

st.title("AI Commentator Avatar")

st.sidebar.header("Options")

# Upload avatar image
guide_avatar = st.sidebar.file_uploader("Upload Avatar Image", type=["jpg", "png"])

# Enter text for commentary
commentary_text = st.text_area("Enter Commentary Text")

# Generate avatar (dummy example)
if st.button("Generate Avatar"):
    if guide_avatar is not None:
        st.image(guide_avatar, caption="Avatar Preview", use_container_width=True)
        st.success("Avatar uploaded!")
    else:
        st.warning("Please upload an avatar image.")

# Generate commentary audio
if st.button("Generate Commentary Audio"):
    if commentary_text:
        # Use your text_to_speech function directly
        audio_path = text_to_speech(commentary_text)
        st.audio(audio_path)
        st.success("Commentary audio generated!")
    else:
        st.warning("Please enter commentary text.")

# Generate full video (dummy example)
if st.button("Generate Avatar Video"):
    if commentary_text:
        st.info("Generating avatar video...")
        audio_path = text_to_speech(commentary_text)
        avatar_path = os.path.join(os.path.dirname(__file__), "avatar-tech.png")
        if validate_avatar(avatar_path):
            video_path = avatar_generation.generate_lip_synced_video(audio_path, avatar_path)
            if video_path and os.path.exists(video_path):
                st.success(f"Video generated: {video_path}")
                st.video(video_path)
                play_video(video_path)
            else:
                st.error("Video generation failed.")
        else:
            st.error("Avatar validation failed.")
    else:
        st.warning("Please enter commentary text.")

st.markdown("---")
st.markdown("Developed by AnshSinghSonkhia")
