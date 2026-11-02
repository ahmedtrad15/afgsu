# AFGSU 2: 11 landing sites (10 regional + 1 national)

Each folder is one standalone site: a single `index.html` with inline CSS, vanilla JS and inline SVG. Google Fonts is the only external dependency. Content is in French (fr-FR).

| Folder | Brand | Concept | Signature interactive |
|---|---|---|---|
| `01-ile-de-france` | Ligne Vitale | Transit-network plan, ECG blips on the lines | Clickable station map (address, sessions, « Réserver à cette station ») |
| `02-pays-de-la-loire` | Estuaire Réa | Editorial river guide; the Loire turns into an ECG as you scroll | « Quel niveau pour moi ? » 3-question quiz |
| `03-bretagne` | Phare Secours | Night nautical chart, lighthouse beam, signal flags | CPR metronome (100–120/min, 30:2) |
| `04-grand-est` | Planche 21 | Engraved anatomical plates, Pl. I–III | Body explorer (front/back, 5 zones → modules) |
| `05-hauts-de-france` | Nord Réflexe | Industrial brutalism, brick, hazard tape, block map | Intra team planner (sessions/days, no price) |
| `06-normandie` | Fiche Bilan | Medical transmission form, VALIDÉ stamps | Validity simulator (expiry, countdown, urgent < 6 months) |
| `07-provence-alpes-cote-d-azur` | Azur Gestes | Risograph poster, grain, overprint | 3-day timeline scrubber |
| `08-occitanie` | Garde de Nuit | Night-shift patient monitor, live ECG | « Il est 3 h, chambre 12… » branching scenario |
| `09-auvergne-rhone-alpes` | Relief Urgences | Mountain rescue, contour lines | Scroll-driven altimeter, camps unlock modules |
| `10-centre-val-de-loire` | Carnet de Gestes | Trainer's notebook, pencil sketches, highlighter | Financing finder + document checklist |
| `11-france` | Réseau AFGSU France | Regulation-room dashboard | National map (pulses, network, region filter) + city/postcode search, 33 city anchors `#afgsu-2-[ville]` |

## Editing sessions

Each site's script starts with a single `SESSIONS` array (ISO dates `[start, end]`), followed by the `SUR_DEMANDE` text. Add or remove dates there and nothing else. Past sessions are hidden automatically. Cities with no future dates show « Prochaine date sur demande — on vous rappelle sous 48 h ».

Regional sites outside Île-de-France also carry the Palaiseau entry, so they can mention the confirmed sessions as an out-of-region option.

On `11-france`, the city cards (`data-sess="Ville"`) and the sessions table are rebuilt from the array. The static HTML inside them is only the no-JS fallback. **If dates change, also update the `hasCourseInstance` entries in the JSON-LD `Course`** (they are static on 01 and 11).

## Still to do before going live

- **Forms:** every form is `action="#"` with a `TODO` comment where the submit handler should POST the data. The hidden field `formation` is pre-filled by the CTAs (AFGSU 2 / AFGSU 1 / Recyclage / Intra). `centre` is pre-selected where relevant, and some tools pre-fill `message`.
- **Media:** photos are `div.img-ph[data-img="…"]` (the label says what to shoot). Logos are `.logo-ph`. The favicon is `<link rel="icon" href="data:,">` under a `PLACEHOLDER favicon` comment. `og:image` is a `TODO` comment in each `<head>`.
- **National → regional links:** `11-france` links to `https://afgsu2-<region>.example/`. Replace these URLs (search for `.example`).
- **Canonical URLs:** none are set (no domains yet).
- **Legal pages:** footer links « Mentions légales », « CGV » and « Accessibilité » point to `#`.

## Content rules applied

- Facts come only from the brief. There are no reviews (only « [Avis stagiaire à insérer] »), no stats or ratings, and no partnerships. CPF is always described as « en principe non éligible ». The recyclage price is « sur demande » because it isn't in the brief.
- « DIGIVODA » and the e-mail appear only in each footer.
- Copy is unique per site: a checker compared every sentence, CTA label and FAQ entry across the 11 sites (exact and near-duplicate). The only shared wording is the fixed facts: course module names, legal references, the profession list in the form selects, and the required « sur demande » sentence.

## Checks performed

- Size: 55–70 KB per regional site, 116 KB for the national site (excluding fonts).
- At 375×667, the price (450 € struck → 385 € TTC), « 21 h · 3 jours · valable 4 ans », the primary CTA and the phone number are all visible without scrolling, above the sticky bar. There is no horizontal scroll.
- Forms: an empty submit is blocked by native validation, and a valid submit shows the inline success state. Errors use `:user-invalid` with `aria-invalid` kept in sync.
- `prefers-reduced-motion: reduce`: no animation runs. Long-running animations (01, 03, 08, 11) also have a pause button.
- axe-core (WCAG 2.1 A/AA) reports 0 violations on all 11 sites at desktop and mobile widths. Brand colours are kept for graphics; slightly darker variants are used where small text needed AA contrast.
- JSON-LD on every site: `EducationalOrganization` (with the centres), `Course` (385 EUR, PT21H) and `FAQPage` (the same questions as the visible FAQ).
