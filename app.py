from __future__ import annotations

import base64
import json
from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent
UI_PATH = ROOT / "ui" / "index.html"
TAROT_PATH = ROOT / "data" / "tarot_major_arcana_en.json"
STARFIELD_PATH = ROOT / "assets" / "starfield-wide.webp"


st.set_page_config(
    page_title="Asteria · Astral Field Notes",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"], .stApp {
        background: #070812;
        margin: 0;
      }
      header[data-testid="stHeader"],
      [data-testid="stToolbar"],
      [data-testid="stDecoration"],
      [data-testid="stStatusWidget"],
      #MainMenu,
      footer {
        display: none !important;
      }
      [data-testid="stAppViewContainer"] > .main {
        padding: 0;
      }
      .block-container {
        max-width: none;
        padding: 0 !important;
      }
      iframe {
        display: block;
        width: 100%;
        border: 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_tarot_cards(path: str) -> list[dict]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def build_ui() -> str:
    cards = load_tarot_cards(str(TAROT_PATH))
    background = base64.b64encode(STARFIELD_PATH.read_bytes()).decode("ascii")
    html = UI_PATH.read_text(encoding="utf-8")
    payload = json.dumps(cards, ensure_ascii=False)
    return (
        html.replace("__TAROT_DATA__", payload)
        .replace("__STARFIELD_BACKGROUND__", background)
    )


st.iframe(
    build_ui(),
    height=1180,
    alt="Asteria tarot and natal chart interactive prototype",
)
