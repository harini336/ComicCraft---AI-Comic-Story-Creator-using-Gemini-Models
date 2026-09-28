import os
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="ComicCraft", page_icon="🎨", layout="wide")

st.title("🎨 ComicCraft")
st.subheader("AI Comic Story Creator using Gemini Models")
st.write("Turn a simple idea into a structured comic story with scenes, dialogue, captions, and visual prompts.")

api_key = os.getenv("GEMINI_API_KEY") or st.sidebar.text_input("Gemini API Key", type="password")
if not api_key:
    st.info("Enter your Gemini API key in the sidebar or set GEMINI_API_KEY as an environment variable.")
    st.stop()

client = genai.Client(api_key=api_key)

with st.sidebar:
    st.header("Comic Settings")
    genre = st.selectbox("Genre", ["Superhero", "Fantasy", "Sci-Fi", "Comedy", "Mystery", "Adventure"])
    pages = st.slider("Number of pages", 2, 12, 6)
    audience = st.selectbox("Audience", ["Kids", "Teens", "General"])
    style = st.text_input("Art style", "Colorful modern comic book")
    generate = st.button("✨ Create Comic", use_container_width=True)

idea = st.text_area(
    "Comic idea",
    placeholder="Example: A student discovers a tiny robot that can pause time for 10 seconds.",
    height=130,
)

if generate:
    if not idea.strip():
        st.warning("Please enter a comic idea.")
        st.stop()

    prompt = f"""
You are ComicCraft, an expert comic writer and storyboard artist.
Create an original {pages}-page {genre} comic for a {audience} audience.

USER IDEA:
{idea}

ART STYLE:
{style}

Return the result in this exact structure:

TITLE:
A memorable title.

LOGLINE:
One sentence.

CHARACTERS:
- Name: description

STORY:
A concise beginning, middle, and ending.

PAGES:
PAGE 1
PANEL 1
Visual: ...
Dialogue: ...
Caption: ...

Continue for every page and use 2-4 panels per page.
Keep dialogue natural, visual descriptions specific, and the story self-contained.
Do not use copyrighted characters or existing franchise names.
"""

    with st.spinner("Creating your comic..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.9,
                    max_output_tokens=5000,
                ),
            )
            comic = response.text
            st.success("Comic created!")
            st.markdown(comic)

            st.download_button(
                "⬇️ Download Comic Story",
                data=comic,
                file_name="comiccraft_story.txt",
                mime="text/plain",
            )
        except Exception as e:
            st.error(f"Generation failed: {e}")

st.divider()
st.caption("ComicCraft • Built with Streamlit and Gemini")
