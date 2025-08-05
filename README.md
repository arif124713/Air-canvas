cat << 'EOF' > README.md && git add README.md && git commit -m "Add README for Air Canvas project" && git push
# Air Canvas ✍️🖐️

This project lets you draw in the air using hand gestures, just like Doctor Strange summoning spells… but with Python and OpenCV instead of magic.

## 🚀 Features
- Real-time hand detection using MediaPipe
- Gesture-based drawing (uses index finger to draw)
- Two modes:
  - ✌️ Selection Mode (index + middle fingers up)
  - ☝️ Drawing Mode (only index finger up)
- Custom brush color and thickness

## 🛠️ Technologies
- Python
- OpenCV
- MediaPipe

## 📦 Installation
Install the required libraries:
\`\`\`
pip install opencv-python mediapipe
\`\`\`

## ▶️ Run the App
\`\`\`
python air_canvas.py
\`\`\`

## 💡 How it Works
1. Uses hand landmarks to detect finger positions.
2. Tracks fingertip (landmark 8) to draw on the screen.
3. Switches between drawing and selection based on fingers.

## 🎯 Use Cases
- Fun interactive drawing app
- Beginner CV/gesture control project
- Great for showing off nerd skills on social media 😎
EOF
