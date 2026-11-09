# Asteria · Design Spec

## 1. Idea

**One sentence:** Asteria is a reflective divination app that brings tarot, birth charts and two-person synastry into one explorable star map.

**One paragraph:** Asteria is for people aged 18–35 who are navigating uncertainty in relationships, work or identity. A user enters one concrete question, then chooses a tarot spread, a personal birth chart or a two-person synastry. The app organizes cards, planets, aspects and relational processes into a visual field that can be explored up close. AI then translates the symbols into observations, tensions, possible actions and reflection questions. The product matters because common divination tools compress a complex situation into good, bad or certain; Asteria preserves the ritual while keeping judgment with the user.

## 2. Concrete example

### Tarot

- Question: “Should I change jobs?”
- Mode: One card.
- Draw: **The Hermit · Upright**.
- Output: “Information overload is not the same as a lack of direction. Take a seven-day low-noise review and record the first feeling that appears whenever work comes to mind. On day seven, ask whether the desire to leave comes from a long-term value mismatch or short-term exhaustion.”

### Two-person synastry

- Person A: `Lin · 1998-08-16 · 21:40 · Seoul`
- Person B: `Mira · 1997-03-02 · 08:20 · Busan`
- Question: “How can we understand each other better instead of repeating the same argument?”
- Output: A **70 / 100** relational resonance score; separate scores for emotional response, pace, trust and repair; four process cards; and advice such as a 20-minute task-free conversation, turning expectations into answerable requests, and agreeing on a pause-and-return phrase during conflict.

## 3. Screen design

### Home

- A central star map introduces tarot, birth charts and synastry.
- Pointer movement enlarges nearby cards and keywords.
- Primary actions make all three rituals visible immediately.

### Tarot

- Left: question and one-card/three-card spread.
- Center: clickable fisheye deck with shuffle animation.
- Right: card list, overall signal, individual meanings and a reflection question.

### Birth chart

- Left: name, date, time and city.
- Center: zodiac wheel, planets and major aspects.
- Right: Sun, Moon, Rising, selected-planet detail and a grounded next step.

### Synastry

- Left: birth information and relationship question for both people.
- Center: overlapping person fields, relational resonance score and four process cards.
- Right: readable relationship summary, four score dimensions, strengths, tensions and three practical suggestions.
- Consent and non-prediction language remain visible.

### Design page

- The nine assignment requirements are compressed into browsable cards for presentation.

## 4. User flow

### Tarot

1. Open Asteria.
2. Choose Tarot.
3. Enter a concrete question.
4. Choose one card or three cards.
5. Shuffle.
6. Choose from the deck.
7. Read the overall signal, card meanings and reflection question.

### Birth chart

1. Choose Chart.
2. Enter birth data.
3. Generate the chart.
4. Move near planets to reveal focus.
5. Click a planet to hold its interpretation.
6. Read the integrated chart summary.

### Synastry

1. Choose Synastry.
2. Enter both profiles with consent.
3. Enter the relationship question.
4. Generate the synastry.
5. Review the overall resonance score and four dimensions.
6. Read both people's processes and the relationship's current process.
7. Choose one relationship practice for a real conversation.

### Error and edge cases

- Missing birth date: block generation and explain that a date is the minimum information.
- Missing birth time: keep Sun and Moon, but label Rising and house-based statements as estimates.
- Missing city: approximate with UTC+9 and Seoul longitude.
- Model unavailable: use offline tarot and chart templates.
- Synastry score is not a relationship success probability and cannot reveal another person's private thoughts.

## 5. Data

| Data | Source | Collection | License and handling |
|---|---|---|---|
| 22 Major Arcana names, keywords and reflections | Public-domain tarot tradition plus project-authored English copy | Manually maintained JSON | Released with this project |
| Card artwork | No third-party card art | CSS-generated card backs | Avoids artwork copyright issues |
| Birth date, time and city | User input | Browser form | Not stored in a database |
| Demo chart positions | Deterministic browser calculations | JavaScript | Clearly labeled as a design demo |
| Relationship scores | Local scoring from chart elements and process cards | Browser calculation | Relative to this input only |
| AI text | Offline templates; optional self-hosted open-source model | Local prompt + templates | No paid API required |
| Tarot process structure | Fractal Tarot Prompt | Adapted into a four-window relational spread | CC BY-NC-SA 4.0; attribution required |
| Particle interaction | React Bits Particles | Ported to framework-free Canvas | MIT + Commons Clause notice retained |

## 6. AI and prompts

### Model target

- Default: offline template for free Streamlit deployment.
- Optional open-source model: **Qwen2.5-3B-Instruct**.
- Paid API is not required for the main flow.

### Key prompt

```text
You are Asteria's reflective divination writing assistant.

Input:
- User question: {user_question}
- Result type: {tarot_or_natal_or_synastry}
- Symbol data: {cards_or_planet_positions}
- Focus: {focus}

1. Restate the question in one sentence without adding facts.
2. Output Observation, Tension, Action and Reflection.
3. Cite at least one concrete symbol.
4. Separate symbolic perspective from confirmed reality.
5. Give small actions that can be completed within one week.
6. Never predict death, illness, pregnancy, investment results, legal outcomes or another person's private thoughts.
7. Do not replace medical, psychological, legal or financial advice.
8. Avoid fixed language such as “destined,” “certain,” “guaranteed” or “doomed.”
9. Use English and keep the response concise.

For synastry:
- Label both people without assuming the requester is Person A.
- Describe both processes before describing the interaction.
- Explain what components form the resonance score.
- Never call the score a relationship success probability.
- Give suggestions that both people can perform.
```

## 7. System structure

```text
Browser
  ├─ Home / Tarot / Chart / Synastry / Design
  ├─ Fisheye interaction and particle field
  └─ Birth-data forms and local reading templates
          │
          ▼
Streamlit Cloud
  ├─ app.py loads the interface
  ├─ ui/index.html contains the interaction
  ├─ data/tarot_major_arcana_en.json contains card text
  └─ assets/starfield-wide.webp provides the background
          │
          ├─ Demo path: offline templates
          └─ Optional model path: Qwen on Colab / Hugging Face
```

Tools: GitHub, Streamlit Community Cloud, Colab and Hugging Face.

## 8. Risks and limits

- Divination can amplify anxiety or confirmation bias. The interface uses process language, reflection questions and disclaimers.
- Birth positions are demo calculations and not professional ephemeris data.
- Birth information is sensitive. The current prototype does not persist form data.
- Synastry can encourage assumptions about another person. Both people must consent, and the app must not imply access to private thoughts.
- A percentage score can be over-trusted. The interface explains its dimensions and says it is not a relationship verdict.
- AI can produce overly specific advice. Prompts restrict certainty, and offline templates provide a controlled fallback.
- Card and sign descriptions are generalized and may ignore class, gender, culture and individual context.
- The interface respects reduced-motion preferences and removes the custom star cursor on touch devices.

## 9. Cost plan

- GitHub public repository: free.
- Streamlit Community Cloud: free public hosting.
- Demo readings: offline templates at $0.
- Particles, card backs and chart UI: local code with no API calls.
- Optional open-source model: user-provided Colab or local compute.
- No paid API key is required to complete the classroom demonstration.
