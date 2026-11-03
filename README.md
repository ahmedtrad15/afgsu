# Formation AFGSU: 11 sites (10 regional + 1 national)

Each folder is a standalone site:

- `index.html`: HTML, CSS and vanilla JS inline. Google Fonts is the only external dependency.
- `mentions-legales.html` and `cgv.html`: the legal pages linked from the footer.
- `media/`: logos, favicons and the site's photos.

The `photos-sources/` folder at the root holds the original uploaded photos. It is not part of any site: don't deploy it.

| Folder | Site name | Concept | Signature interactive |
|---|---|---|---|
| `01-ile-de-france` | Formation AFGSU Île-de-France | Transit plan (5 stations) | Clickable station map + full departures board |
| `02-pays-de-la-loire` | Formation AFGSU Pays de la Loire | The Loire as one thread, from the coast to Le Mans | « Quel niveau pour moi ? » quiz |
| `03-bretagne` | Formation AFGSU Bretagne | Night nautical chart, lighthouse | CPR metronome |
| `04-grand-est` | Formation AFGSU Grand Est | Engraved anatomical plates | Body explorer |
| `05-hauts-de-france` | Formation AFGSU Hauts-de-France | Brick / block industrial | Intra team planner |
| `06-normandie` | Formation AFGSU Normandie | Medical transmission form | Validity simulator |
| `07-provence-alpes-cote-d-azur` | Formation AFGSU Provence-Alpes-Côte d’Azur | Risograph poster | 3-day timeline scrubber |
| `08-occitanie` | Formation AFGSU Occitanie | Night-shift monitor | « Il est 3 h, chambre 12… » scenario |
| `09-auvergne-rhone-alpes` | Formation AFGSU Auvergne-Rhône-Alpes | Mountain rescue | Scroll-driven altimeter |
| `10-centre-val-de-loire` | Formation AFGSU Centre-Val de Loire | Trainer's notebook | Financing finder + document checklist |
| `11-france` | Formation AFGSU France | Regulation-room dashboard | National map + city/postcode search, 32 anchors `#afgsu-2-[ville]` |

## Maps

The regional maps (`01`–`10`) are static: no line drawing, pulses or moving beam. Only the national map in `11-france` is animated (pulses, network lines, region filter), with a pause button and a reduced-motion fallback.

## Sessions

Each site's script starts with a single `SESSIONS` array (ISO dates `[start, end]`). Past sessions disappear on their own. A centre with no future date shows « Nous contacter ».

- **Île-de-France** (`01` and `11`): Palaiseau (4 allée des Garays, 91120), Choisy-le-Roi (16 avenue Jean Jaurès, 94600), Noisy-le-Sec (9 rue Saint-Just, 93130), Pontault-Combault (77) and Houilles (78, « Nous contacter »). There are 21 sessions from November 2026 to March 2027. Paris and Meaux have been removed.
- **All other regions:** « Nous contacter ».
- When dates change, also update the JSON-LD `hasCourseInstance` list in `01` and `11`. It is static in the HTML: one `CourseInstance` per session.

## Forms (Web3Forms)

Every form posts to `https://api.web3forms.com/submit` with the access key `e4285b81-3704-4ac4-b5dc-411014b21fd4`.

- JS sends the data with `fetch` and shows the inline confirmation, or an error message with the phone number if the send fails.
- Without JS, the native form still submits to Web3Forms.
- Hidden fields: `subject`, `from_name` (the site name), `formation` (pre-filled by the buttons: AFGSU 2 / AFGSU 1 / Recyclage / Intra), and a `botcheck` anti-spam honeypot.

## Media

Each `media/` folder contains:

- `logo.svg`, `logo.png` (full logo), `logo-mark.svg` (symbol only), `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`.
- `logo-fond-clair.png`: a dark-text version, for `03`, `05` and `08`.
- `afgsu-….jpg`: the site's photos, web-compressed, each in two widths (`-640`/`-1280`, or `-600`/`-1000` for portrait shots). The page picks the right width with `srcset`.
- `LISEZ-MOI.txt`: the list of photos used by that site. To change a photo, replace both files and keep exactly the same names, then adapt the `alt` text in `index.html` if the subject changes.

Each site shows 4 to 6 photos: its existing photo slots, plus a strip of 3 captioned photos (4 on `11`) in its programme section (`09`: in « La cordée »). No two sites open with the same photo, and no photo appears on more than two sites. Two uploads are not used: `recyclage-afgsu1.png` (351 px wide, too small) and `formation-afgsu.jpg` (first-aid-kit product shot).

## Still to do

- **Mentions légales & CGV:** the pages exist and are linked from every footer, but **they don't contain DIGIVODA's text yet** (this environment couldn't reach digivoda.com). Once the texts are available they get inserted into all 22 pages at once.
- `og:image`: add `media/og-image.jpg` (1200 × 630) and un-comment the line in each `<head>`.
- National → regional links: replace the `.example` URLs in `11-france`.
