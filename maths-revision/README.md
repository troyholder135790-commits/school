# Maths Revision — Factorising & Pythagoras

Study pack for the 1 Sept 2026 test.
Covers **Hoofstuk 8 / Chapter 8** (Faktorisering, Eksamenfokus bl164) and
**Hoofstuk 13 / Chapter 13** (Pythagoras, Eksamenfokus bl239).

## Deliverables

| File | What it is |
|---|---|
| `Maths_Revision_Factorising_and_Pythagoras.pdf` | 16-page printable study guide: every rule, the trinomial sign table, a fully worked solution to every worksheet question, an Afrikaans/English glossary, top-10 mistakes, and a 12-question self-test with answers. |
| `Maths_Revision_Factorising_and_Pythagoras.mp4` | 14 min 54 s narrated explainer video, 1920×1080. 42 slides walking through every rule and every question. |

## Contents covered

**Chapter 8 — Factorising.** The Golden Order (common factor → 2 terms → 3 terms → 4 terms),
common factor, difference of two squares, trinomials with the sign table, common brackets,
the sign-flip trick `(1 − x) = −(x − 1)`, and grouping in pairs. All of (d)1, 7, 10, 21, 22,
23, 24, 25 and (e)1, 4, 7.

**Algebraic fractions.** Factorise top, factorise bottom, cancel brackets. All of (i)2–5.

**Chapter 13 — Pythagoras.** The theorem, choosing add vs subtract, surd form vs decimals,
two-triangle problems (Ex 13.1 d1), the converse (Ex 13.2 a1–2), the acute/obtuse test
(Ex 13.2 b1–2), and the Exam Focus p239 square and rectangle questions.

## Rebuilding

```sh
# study notes PDF
chromium --headless --no-pdf-header-footer \
  --print-to-pdf=Maths_Revision_Factorising_and_Pythagoras.pdf notes.html

# video (needs espeak-ng + mbrola/mb-us1, ffmpeg with libx264, Chromium)
cd video && python3 make_video.py
```

`video/slides.py` holds the 42 scene definitions (section, title, slide HTML, narration script);
`video/make_video.py` renders each slide with headless Chromium, synthesises the narration with
espeak-ng + mbrola, and muxes the result with ffmpeg.
