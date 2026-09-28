# 🎨 ComicCraft - AI Comic Story Creator

ComicCraft is a Generative AI application that uses **Google Gemini models** to transform a simple idea into a structured comic story with characters, scenes, dialogue, captions, and visual prompts.

## Features

- ✨ AI-powered comic story generation
- 🎭 Multiple genres
- 📚 Adjustable number of pages
- 👥 Audience selection
- 🎨 Custom art-style prompt
- 🧩 Panel-by-panel storyboard format
- ⬇️ Download generated comic story as a text file
- 🔐 API key is kept outside the source code

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- google-genai SDK

## Project Structure

```text
ComicCraft/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 1. Install Python

Install Python 3.10 or newer.

Check:

```bash
python --version
```

## 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Get a Gemini API key

Create a Gemini API key using Google's Gemini developer tooling.

Do **not** commit your real API key to GitHub.

## 5. Run ComicCraft

You can enter the API key directly in the sidebar:

```bash
streamlit run app.py
```

Or set an environment variable.

PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
streamlit run app.py
```

Command Prompt:

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
streamlit run app.py
```

## GitHub Upload

Create a repository named:

```text
ComicCraft-AI
```

Then from the project folder:

```bash
git init
git add .
git commit -m "Initial ComicCraft AI project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

### Important

Never upload `.env` or your real Gemini API key.

## Example Prompt

```text
A college student discovers a tiny robot inside an old library book.
The robot can pause time for ten seconds, but every use creates a new
mystery around the student.
```

ComicCraft converts the idea into a multi-page comic storyboard with panels, visuals, dialogue, and captions.

## License

This project is intended for educational and portfolio use.
