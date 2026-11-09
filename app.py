from __future__ import annotations

import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


ROOT = Path(__file__).resolve().parent
UI_PATH = ROOT / "ui" / "index.html"
TAROT_PATH = ROOT / "data" / "tarot_major_arcana.json"


st.set_page_config(
    page_title="Asteria · 星象手册",
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
    html = UI_PATH.read_text(encoding="utf-8")
    payload = json.dumps(cards, ensure_ascii=False)
    return html.replace("__TAROT_DATA__", payload)


components.html(build_ui(), height=1180, scrolling=True)
