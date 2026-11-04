from pathlib import Path

content = """# Retro Lens – Project Guide

Retro Lens is a real-time webcam project that uses **OpenCV and MediaPipe** to detect hand movements and apply visual effects using hand landmarks.

## 1. Setup

Open the project folder in the VS Code terminal and run:

### macOS or Linux

```bash
python3 -m venv venv
source venv/bin/activate

python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
```

## 2. How to Run

Run the files individually:

| Command | What it does |
|---|---|
| `python web.py` | Opens the webcam and displays the live video. |
| `python landmarks.py` | Detects hands and displays hand landmarks and connections. |
| `python grey.py` | Detects hand landmarks and applies a grayscale effect inside the selected fingertip region. |
| `python main.py` | Runs the complete Retro Lens application with multiple filters and gestures. |

## 3. Project Files

| File | Purpose |
|---|---|
| `web.py` | Webcam access and live video display. |
| `landmarks.py` | Hand detection and landmark visualization. |
| `grey.py` | Hand detection with a grayscale filter. |
| `main.py` | Complete application with interactive filters and effects. |
| `hand_landmarker.task` | Pre-trained MediaPipe model used for hand detection. |
| `requirements.txt` | Required Python libraries. |
| `venv/` | Virtual environment containing installed packages. |

## 4. Controls (`main.py`)

| Key / Gesture | Action |
|---|---|
| `C` | Switch between 2D and 3D modes. |
| `N` | Next filter. |
| `P` | Previous filter. |
| `S` | Save the current frame. |
| `Q` | Quit the application. |
| Pinch gesture | Change filter. |
| Both hands making fists | Toggle 3D mode. |

## 5. Important Notes

- Make sure your webcam is connected and accessible.
- Allow webcam permissions for VS Code or Terminal.
- Keep `hand_landmarker.task` in the project folder.
- If the webcam doesn't open, try changing the camera index from `0` to `1`.
- Run the files one at a time, not simultaneously.
"""
path = Path("/mnt/data/retro_lens_project_guide.md")
path.write_text(content, encoding="utf-8")
print(path)
