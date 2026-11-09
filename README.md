# Asteria · Astral Field Notes

A reflective divination prototype for people who want to explore a real question without receiving a fixed prediction. Asteria combines tarot, a personal birth chart and a consent-based two-person synastry view inside one interactive star map.

**Live prototype:** [asteria-oracle.streamlit.app](https://asteria-oracle.streamlit.app)  
**Repository:** [github.com/wjy40118/asteria-oracle](https://github.com/wjy40118/asteria-oracle)  
**Stack:** Streamlit + HTML / CSS / JavaScript  
**Cost:** $0 in demo mode; no API key required

![Asteria home screen](docs/screenshots/home.png)

[![Deploy to Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=wjy40118/asteria-oracle&branch=main&mainModule=app.py)

## What it does

Most divination products compress a complicated situation into good, bad or certain. Asteria keeps the ritual of drawing and chart reading, but turns the result into something observable, reflective and open to disagreement. It is not a decision system and not a substitute for therapy.

## Main interactions

- **Fisheye exploration:** cards, planets and keywords enlarge as the pointer approaches.
- **Tarot:** one-card and three-card spreads with shuffle, draw, upright/reversed meanings and reflection.
- **Birth chart:** Sun, Moon, Rising, planetary aspects and a focused chart reading.
- **Two-person synastry:** both profiles, a relational resonance score, four score dimensions, four process cards and three practical relationship suggestions.
- **Edge states:** missing dates block generation; missing birth times are labeled as estimates; every reading includes a non-prediction disclaimer.

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Design deliverables

The complete nine-part Design Spec is in [DESIGN_SPEC.md](DESIGN_SPEC.md). The required two-slide PDF is at `presentation/Asteria_Design_Spec.pdf`.

## Data, models and licenses

- The 22 Major Arcana names and original English interpretations are stored in `data/tarot_major_arcana_en.json`.
- The star-watercolor background was supplied by the project owner and adapted for widescreen use in `assets/starfield-wide.webp`.
- The ambient particle field and constellation interaction are adapted from React Bits Particles. See `THIRD_PARTY_NOTICES.md`.
- No Rider-Waite-Smith or other copyrighted card artwork is included. Card backs are generated with CSS.
- Birth positions are deterministic browser-side demo calculations, not professional ephemeris data.
- AI readings use offline templates so the Streamlit demo works without an API key.
- The optional model target is `Qwen2.5-3B-Instruct`; its prompt is in `prompts/system_prompt.txt`.
- Tarot process language and the two-person spread structure are adapted from **Fractal Tarot Prompt** by Sun Yihao / Tai Yihao (yihao-sun), licensed CC BY-NC-SA 4.0. See `THIRD_PARTY_NOTICES.md`.
- User inputs are not written to a database and disappear when the page session ends.

## Streamlit Cloud

1. Connect this GitHub repository.
2. Set the main file path to `app.py`.
3. Let Streamlit install `requirements.txt`.
4. No Secrets are required because the default demo is offline.

## Boundaries

Asteria does not predict death, illness, pregnancy, investment returns or another person's private thoughts. It does not replace medical, psychological, legal or financial advice. Synastry scores compare the current input only and are not a verdict on relationship value.
