# PDF Audio Reader 🎧📖

An elegant, lightweight Python GUI application that converts PDF files into audiobooks. Built with Tkinter for the graphical interface, PyPDF2 for text extraction, and pyttsx3 for offline Text-to-Speech (TTS) synthesis.

---

## 🚀 Features

- **Simple GUI Interface**: Select any PDF from your file explorer using a clean Tkinter-based dialog.
- **Offline TTS Engine**: No internet connection required! Converts PDF text directly using your system's native TTS engines via `pyttsx3`.
- **Playback Controls**: Easy-to-use **Play** and **Stop** controls to manage audio narration.
- **Status Indicators**: Real-time status updates showing whether a PDF is loaded or playback has stopped.

---

## 🛠️ Prerequisites

- **Python**: 3.6 or higher.
- **OS Support**: Windows, macOS, and Linux.

---

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Suryacodeshere/PDF-TO-AUDIOBOOK.git
   cd PDF-TO-AUDIOBOOK
   ```

2. **Install dependencies**:
   Run the following command to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: If you run into issues installing `pyttsx3` or `PyPDF2` on Linux/macOS, ensure your system package manager has the necessary audio tools installed (e.g., `espeak` on Linux).*

---

## 🖥️ Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Click **Select PDF** to choose a PDF file from your computer.
3. Click **Play** to start listening to your PDF audiobook.
4. Click **Stop** to halt playback at any time.

---

## 👥 Contributors & Co-Authors

This project is co-authored and maintained by:
- **Suryacodeshere** (Owner)
- **samcodes** (saumyatiwari598@gmail.com)

Feel free to fork, open issues, or submit pull requests to contribute!