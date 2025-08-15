import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk
from PIL import Image, ImageTk
import os
import threading
import pygame

from modules.text_to_speech import text_to_speech
from modules.text_generation import fetch_latest_news_with_content
from modules.avatar_generation import generate_lip_synced_video
from modules.voice_data import get_voice_array, get_voice_data
from main import validate_avatar, play_video

class NewsAnchorApp:
    def __init__(self, root):
        pygame.mixer.init()
        self.root = root
        self.root.title("🎙️AI Virtual News Anchor ")
        self.root.attributes("-fullscreen", True)

        self.news_content = ""

        # Load and place background image
        bg_image_path = "assets/studio.png"
        bg_image = Image.open(bg_image_path)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.setup_ui()

        # Typing animation for title
        self.title_text = "🎙️AI Virtual News Anchor"
        self.title_label.after(100, self.type_text, 0)
        self.root.after(100, self.show_welcome_popup)  # 👈 This shows the popup after the GUI loads
        
    def _on_voice_menu_change(self, event):
        value = self.voice_menu.get()

        voice_data = get_voice_data(value)
        if voice_data:
            self.voice_data = voice_data

    def _populate_voice_menu(self):
        try:
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            
            self.voice_choices = get_voice_array()
            
            if self.voice_menu:
                self.voice_menu.destroy()
                
            self.voice_menu = ttk.Combobox(self.root, textvariable=self.voice_var, values=self.voice_choices, state="readonly", width=30)
            self.voice_menu.bind("<<ComboboxSelected>>", self._on_voice_menu_change)
            self.voice_menu.place(relx=0.40, rely=0.25, anchor="center")
            self.voice_menu.set(self.voice_choices[0] if self.voice_choices else "")
        except Exception:
            self.voice_choices = []
            
            if self.voice_menu:
                self.voice_menu.destroy()
                
            self.voice_menu = None

    def setup_ui(self):
        # TTS Method Option
        self.voice_var = tk.StringVar(value="David")
        
        tts_voice_label = tk.Label(self.root, text="Select Voice:", fg="white", font=("Times New Roman", 14), bg="#001638")
        tts_voice_label.place(relx=0.27, rely=0.25, anchor="center")

        self.voice_var = tk.StringVar(value="")
        self.voice_menu = None
        
        self._populate_voice_menu()
        
        # Title
        self.title_label = tk.Label(self.root, text="", font=("Times New Roman", 36, "bold"),
                                    fg="white", bg="#de2526")
        self.title_label.pack(pady=15)

        # Topic Label and Entry
        self.topic_label = tk.Label(self.root, text="Topic:", fg="white", font=("Times New Roman", 16), bg="#de2526")
        self.topic_label.place(relx=0.27, rely=0.21, anchor="center")

        self.topic_entry = tk.Entry(self.root, width=25, font=("Times New Roman", 12), bg="#de2526", fg="white",
                                    insertbackground="white", relief="solid", bd=2)
        self.topic_entry.place(relx=0.36, rely=0.212, anchor="center")

        # Count Label and Entry
        self.count_label = tk.Label(self.root, text="Count:", fg="white", font=("Times New Roman", 16), bg="#de2526")
        self.count_label.place(relx=0.535, rely=0.21, anchor="center")

        self.count_entry = tk.Entry(self.root, width=5, font=("Times New Roman", 12), bg="#de2526", fg="white",
                                    insertbackground="white", relief="solid", bd=2)
        self.count_entry.place(relx=0.575, rely=0.212, anchor="center")

        # Input instruction label
        input_label = tk.Label(self.root, text="✍️ Enter your own news text or fetch from Google News:",
                               fg="white", font=("Times New Roman", 16), bg="#de2526")
        input_label.place(relx=0.5, rely=0.35, anchor="center")

        # News content textbox
        # Frame to hold text box and scrollbar
        text_frame = tk.Frame(self.root, bg="#de2526")
        text_frame.place(relx=0.5, rely=0.50, anchor="center")

        # Text widget
        self.text_box = tk.Text(
            text_frame, wrap=tk.WORD, width=100, height=10,
            font=("Consolas", 14), bg="#de2526", fg="white",
            insertbackground="white", relief="solid", bd=1
        )
        self.text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Custom Scrollbar
        scrollbar = tk.Scrollbar(
            text_frame, command=self.text_box.yview,
            bg="#de2526", activebackground="#02295a", troughcolor="white",
            bd=0, relief="flat"
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_box.config(yscrollcommand=scrollbar.set)

        # ✅ Moved Status label BELOW text box and ABOVE buttons
        self.status_label = tk.Label(self.root, text="", fg="lime", font=("Arial", 14, "italic"), bg="#de2526")
        self.status_label.place(relx=0.5, rely=0.61, anchor="center")


        # Horizontal Buttons
        self.add_button("🧠 Use My Text", self.use_custom_text, 0.42,0.76)
        self.add_button("🌐 Fetch News", self.fetch_news, 0.42,0.81)
        self.add_button("🎬 Generate Video", self.generate_video, 0.57,0.76)
        self.add_button("  ❌ Exit  ", self.root.quit, 0.57,0.81)

        # Footer
        # self.creator_label = tk.Label(self.root, text="Made in India",
        #                               font=("Times New Roman", 16, "bold"),
        #                               fg="white", bg="#138808")
        # self.creator_label.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

    def add_button(self, text, command, relx_value, rely_value):
        def on_click_with_sound():
            # Play the sound asynchronously using pygame
            sound = pygame.mixer.Sound("assets/audio/click.wav")
            threading.Thread(target=sound.play, daemon=True).start()
            command()

        btn = tk.Button(self.root, text=text, command=on_click_with_sound,
                        bg="#de2526", fg="white", activebackground="#3949ab",
                        activeforeground="white", relief="solid", bd=1,
                        font=("Times New Roman", 12, "bold"), padx=15, pady=5,
                        cursor="hand2", width=16, height=1)

        def on_enter(e):
            btn.config(font=("Times New Roman", 13, "bold"), padx=18, pady=7)

        def on_leave(e):
            btn.config(font=("Times New Roman", 12, "bold"), padx=15, pady=5)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.place(relx=relx_value, rely=rely_value, anchor="center")

    def type_text(self, i):
        if i <= len(self.title_text):
            self.title_label.config(text=self.title_text[:i])
            self.title_label.after(100, self.type_text, i + 1)


    def use_custom_text(self):
        text = self.text_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Needed", "Please enter some text.")
        else:
            self.news_content = text
            self.status_label.config(text="✅ Custom news text loaded!")

    def show_welcome_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Welcome")
        popup.overrideredirect(True)
        popup.configure(bg="#de2526")

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        popup_width = 600
        popup_height = 120

        # Calculate x and y coordinates for centering the popup
        x = (screen_width // 2) - (popup_width // 2)
        y = (screen_height // 2) - (popup_height // 2)

        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        label = tk.Label(
            popup,
            text="🎙️ Welcome to the Virtual News Anchor Studio!",
            font=("Times New Roman", 20, "bold"),
            fg="white",
            bg="#de2526",
            pady=25,
            padx=35
        )
        label.pack(expand=True, fill="both")

        # Auto-close after 3 seconds
        popup.after(4000, popup.destroy)

    def fetch_news(self):
        topic = self.topic_entry.get().strip()
        count = self.count_entry.get().strip()

        if not topic or not count.isdigit():
            messagebox.showerror("Error", "Please enter a valid topic and numeric count.")
            return

        self.status_label.config(text="🔍 Fetching news...")
        self.root.update()

        news_text = fetch_latest_news_with_content(topic, int(count))
        if news_text:
            self.news_content = news_text
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, news_text)
            self.status_label.config(text="✅ News fetched and loaded!")
        else:
            self.status_label.config(text="⚠️ No news found.")

    def generate_video(self):
        if not self.news_content:
            messagebox.showerror("Error", "No news content to generate video.")
            return

        self.status_label.config(text="🔧 Generating video...")
        self.root.update()

        threading.Thread(target=self._generate_video_thread).start()

    def _generate_video_thread(self):
        try:
            audio_path = text_to_speech(self.news_content, method=self.voice_data['model'], voice_id=self.voice_data['voice_id'] if self.voice_data['voice_id'] else None)
            avatar_path = os.path.join(os.path.dirname(__file__), "assets/avatars/avatar-tech.png")
            
            if not validate_avatar(avatar_path):
                self.status_label.config(text="❌ Avatar validation failed.")
                return

            video_path = generate_lip_synced_video(audio_path, avatar_path)
            
            if video_path and os.path.exists(video_path):
                self.status_label.config(text=f"🎉 Video ready: {video_path}")
                play_video(video_path)
            else:
                self.status_label.config(text="❌ Video generation failed.")
        except Exception as e:
            print(f"❌ Exception: {e}")
            self.status_label.config(text=f"❌ Error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NewsAnchorApp(root)
    root.mainloop()