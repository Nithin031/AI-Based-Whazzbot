AI-Based-WhazzBot
An AI-powered WhatsApp assistant that automates message replies using Meta's Llama 3-70B Instruct. It utilizes Selenium for web automation, PyAutoGUI for UI control, and gTTS for speech output. The bot supports multiple languages and features clipboard integration, Chrome profile persistence, and fast AI-generated responses.

🚀 Features
✅ Automated Message Retrieval (via Selenium) – Reads incoming messages from WhatsApp Web.
✅ AI-Powered Smart Replies (via Llama 3-70B Instruct) – Provides context-aware responses.
✅ Multi-Language Support – Supports English (EN), Hindi (HI), Kannada (KN), Telugu (TE), Tamil (TA), and Malayalam (ML).
✅ Voice Alerts & Speech Output (via gTTS) – Reads out messages for hands-free assistance.
✅ Clipboard Integration – AI responses are copied to the clipboard for quick pasting.
✅ Chrome Profile Persistence – Saves WhatsApp login sessions for a seamless experience.
✅ Optimized Speed & Stability – Faster message processing & AI response time.
✅ User-Friendly & Lightweight – Minimal resource usage with real-time automation.

🛠 Tech Stack
Python (Selenium, PyAutoGUI, Pyperclip, gTTS, Playsound, Keyboard)
Meta Llama 3-70B Instruct (for AI-generated responses)
Selenium WebDriver (for WhatsApp Web automation)
gTTS (for text-to-speech voice notifications)
PyAutoGUI & Pyperclip (for UI automation & clipboard control)
⚙️ How It Works
Opens WhatsApp Web in a Chrome session (persistent login).
Retrieves unread messages from selected chats.
Uses Meta's Llama 3-70B Instruct to generate context-aware responses.
Copies the AI-generated reply to the clipboard for quick pasting.
Optionally sends messages automatically (configurable).
