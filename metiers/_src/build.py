#!/usr/bin/env python3
"""Générateur des 13 landing pages « Formations AFGSU 2 - [Métier] ».

Chaque fiche site (sites/sNN.py) fournit sa configuration, son CSS et le corps
de sa page. Ce script assemble un fichier index.html autonome par site
(CSS dans <style>, JS dans <script>), puis vérifie chaque page contre la
checklist du cahier des charges et écrit metiers/README.md.

Usage : python3 metiers/_src/build.py
"""
import html
import importlib.util
import json
import re
import sys
import urllib.parse
from datetime import date
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from media import GALLERY, MAP_CITIES, PHOTOS, VIDEOS  # noqa: E402

SRC = Path(__file__).resolve().parent
OUT = SRC.parent
YEAR = date.today().year

ACCESS_KEY = "e4285b81-3704-4ac4-b5dc-411014b21fd4"
TEL_HREF = "tel:+33780912335"
TEL_TXT = "07 80 91 23 35"
PRICE_HTML = "<del>450 €</del> <strong>385 € TTC</strong>"

# Aucune ville n'est citée dans les pages : la carte de France montre les grandes villes sans les nommer.
CITY_WORDS = ["Paris", "Lyon", "Marseille", "Toulouse", "Bordeaux", "Lille", "Nantes",
              "Strasbourg", "Rennes", "Montpellier", "Nice", "Reims", "Grenoble",
              "Rouen", "Tours", "Dijon", "Clermont-Ferrand", "Metz", "Caen", "Angers"]
UPLOAD_DATE = "2026-11-16"

# Contour de la France (métropole + Corse) repris de la carte du site 11-france, et projection lon/lat
FR_PATH = (Path(__file__).resolve().parent / "france-path.txt").read_text().strip()
def MAP_X(lon): return 67.567 * lon + 351.341
def MAP_Y(lat): return -97.693 * lat + 4991.775

FORBIDDEN = ["financ", "OPCO", "CPF", "DPC", "FIF-PL", "FIFPL", "France Travail",
             "Pôle emploi", "prise en charge financière"]

esc = html.escape


# --------------------------------------------------------------------------
# Pièces communes (balisage préfixé par le préfixe CSS du site)
# --------------------------------------------------------------------------

def svg_logo(site, size=40, cls="logo-mark"):
    p = site["prefix"]
    return (f'<svg class="{p}{cls}" width="{size}" height="{size}" viewBox="0 0 32 32" '
            f'aria-hidden="true" focusable="false">{site["pict"]}</svg>')


def favicon(site):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
           f'{site.get("favicon_bg", "")}{site["pict"]}</svg>')
    return "data:image/svg+xml," + urllib.parse.quote(svg, safe=" =:/'\"#,.-")


def brand(site, href="#top"):
    """Logo complet : pictogramme + nom exact du site."""
    p = site["prefix"]
    head, tail = site["name"].split(" - ", 1)
    return (f'<a class="{p}brand" href="{href}" aria-label="{esc(site["name"])}, accueil">'
            f'{svg_logo(site)}<span class="{p}brand-txt"><span class="{p}brand-a">{esc(head)} - </span>'
            f'<span class="{p}brand-b">{esc(tail)}</span></span></a>')


def header(site, variant=""):
    p = site["prefix"]
    labels = site.get("nav", ["Programme", "Tarif", "Sessions", "FAQ"])
    ids = site.get("nav_ids", ["programme", "tarif", "sessions", "faq"])
    links = "".join(f'<a href="#{i}">{esc(l)}</a>' for l, i in zip(labels, ids))
    cta = site.get("header_cta", "Réserver ma place")
    return f'''<header class="{p}header {variant}">
  <div class="{p}wrap {p}header-in">
    {brand(site)}
    <nav class="{p}nav" aria-label="Navigation principale">{links}</nav>
    <div class="{p}header-act">
      <a class="{p}tel" href="{TEL_HREF}"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg><span class="{p}tel-num">{TEL_TXT}</span></a>
      <a class="{p}btn {p}btn-head" href="#inscription">{esc(cta)}</a>
    </div>
  </div>
</header>'''


def price(site, cls="price"):
    p = site["prefix"]
    return f'<p class="{p}{cls}"><span class="{p}sr">Prix : ancien tarif </span>{PRICE_HTML}</p>'


def photo_for(site, slot):
    for f, stem, alt, sl in PHOTOS[site["num"]]:
        if sl == slot:
            return stem, alt
    return None


def photo_size(site, stem, w):
    with Image.open(OUT / site["folder"] / "media" / f"{stem}-{w}.jpg") as im:
        return im.size


def img(site, slot, wide=False):
    """Photo réelle si l'emplacement en a une (media.py), sinon rien."""
    p = site["prefix"]
    ph = photo_for(site, slot)
    if not ph:
        return ""
    if slot == "hero" and hero_is_video(site):
        return hero_video(site)
    stem, alt = ph
    w1, h1 = photo_size(site, stem, 1200)
    w0, _ = photo_size(site, stem, 640)
    first = slot == "hero"
    load = 'loading="eager" fetchpriority="high"' if first else 'loading="lazy"'
    cls = f"{p}photo {p}photo-wide" if wide else f"{p}photo"
    badge = ""
    if slot == "hero":
        cls += f" {p}photo-hero"
        badge = (f'<figcaption class="{p}hero-badge"><span class="{p}hero-badge-ic" aria-hidden="true">'
                 f'<svg viewBox="0 0 24 24" width="18" height="18"><path d="M5 12.5l4.2 4.2L19 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
                 f'<span><b>Attestation délivrée par le CESU</b>valable 4 ans</span></figcaption>')
    return (f'<figure class="{cls}" data-slot="{slot}">'
            f'<img src="media/{stem}-1200.jpg" srcset="media/{stem}-640.jpg {w0}w, media/{stem}-1200.jpg {w1}w" '
            f'sizes="(max-width: 760px) 100vw, 600px" width="{w1}" height="{h1}" alt="{esc(alt)}" {load} decoding="async">'
            f'{badge}</figure>')


def gallery(site):
    """Galerie « en formation » : 3 photos en mosaïque, titre et légendes propres au site."""
    p = site["prefix"]
    title, intro, items = GALLERY[site["num"]]
    figs = []
    for i, (_f, stem, alt, cap) in enumerate(items):
        w1, h1 = photo_size(site, stem, 1200)
        w0, _ = photo_size(site, stem, 640)
        sizes = "(max-width: 640px) 100vw, 640px" if i == 0 else "(max-width: 640px) 100vw, 420px"
        figs.append(f'<figure class="{p}gal-fig">'
                    f'<img src="media/{stem}-1200.jpg" srcset="media/{stem}-640.jpg {w0}w, media/{stem}-1200.jpg {w1}w" '
                    f'sizes="{sizes}" width="{w1}" height="{h1}" alt="{esc(alt)}" loading="lazy" decoding="async">'
                    f'<figcaption><span class="{p}gal-n" aria-hidden="true">{i + 1:02d}</span>{esc(cap)}</figcaption></figure>')
    return (f'<section class="{p}gal" aria-labelledby="{p}gal-t">'
            f'<div class="{p}gal-head"><span class="{p}gal-k">En formation</span>'
            f'<h2 id="{p}gal-t">{esc(title)}</h2><p>{esc(intro)}</p></div>'
            f'<div class="{p}gal-grid">{"".join(figs)}</div></section>')


def video_meta(site):
    f, stem, title, desc = VIDEOS[site["num"]]
    return stem, title, desc


def video_ld(site):
    stem, title, desc = video_meta(site)
    import subprocess
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                str(OUT / site["folder"] / "media" / f"{stem}.mp4")],
                               capture_output=True, text=True).stdout.strip() or 0)
    return {"@type": "VideoObject", "@id": site["url"] + "#video", "name": title, "description": desc,
            "thumbnailUrl": site["url"] + f"media/{stem}-poster.jpg", "uploadDate": UPLOAD_DATE,
            "duration": f"PT{round(dur)}S", "contentUrl": site["url"] + f"media/{stem}.mp4", "inLanguage": "fr"}


SOUND_ICON = ('<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4z" fill="currentColor"/>'
              '<path class="snd-on" d="M16 9a4 4 0 0 1 0 6M18.5 6.5a7.5 7.5 0 0 1 0 11" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'
              '<path class="snd-off" d="M16.5 9.5l5 5M21.5 9.5l-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>')


def ad_video(site):
    p = site["prefix"]
    stem, title, desc = video_meta(site)
    return (f'<video data-ad autoplay muted loop playsinline preload="metadata" poster="media/{stem}-poster.jpg" width="720" height="1280" '
            f'aria-label="{esc(title)}"><source src="media/{stem}.mp4" type="video/mp4"></video>'
            f'<button type="button" class="{p}ad-sound" data-ad-sound aria-pressed="false" aria-label="Activer le son de la vidéo">{SOUND_ICON}</button>')


def hero_is_video(site):
    """La vidéo remplace la photo du haut de page, sauf sur les sites où elle est placée à côté du titre."""
    return site.get("ad", "overlay") != "none"


def hero_badge(p):
    return (f'<figcaption class="{p}hero-badge"><span class="{p}hero-badge-ic" aria-hidden="true">'
            f'<svg viewBox="0 0 24 24" width="18" height="18"><path d="M5 12.5l4.2 4.2L19 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
            f'<span><b>Attestation délivrée par le CESU</b>valable 4 ans</span></figcaption>')


def hero_video(site):
    """Grande vidéo verticale en haut de page, à la place de la photo principale."""
    p = site["prefix"]
    return (f'<figure class="{p}hv" data-slot="hero"><div class="{p}hv-frame">{ad_video(site)}</div>'
            f'{hero_badge(p)}</figure>')


def ad_phone(site):
    """Vidéo publicitaire courte, en format téléphone, posée sur la photo du haut de page."""
    p = site["prefix"]
    extra = f" {p}ad-top" if site.get("ad") == "top" else ""
    return f'<div class="{p}ad{extra}">{ad_video(site)}</div>'


def video(site, slot):
    """Vidéo en haut de page quand la photo principale n'y est pas : « band » (bandeau) ou « solo » (à côté du titre)."""
    p = site["prefix"]
    if slot == "solo":
        return hero_video(site)
    if slot != "band":
        return ""
    stem, title, desc = video_meta(site)
    return f'''<section class="{p}adband" aria-label="Vidéo de présentation">
<figure class="{p}reel">
  <div class="{p}reel-frame">{ad_video(site)}</div>
  <figcaption><span class="{p}reel-title">{esc(title)}</span><span class="{p}reel-desc">{esc(desc)}</span>
    <span class="{p}reel-pts"><span>21 h de pratique sur 3 jours</span><span>6 à 12 stagiaires par session</span><span>Attestation valable 4 ans</span></span>
    <a class="{p}btn {p}reel-cta" href="#inscription">Réserver ma session</a></figcaption>
</figure>
</section>'''


def france_map(site):
    """Carte de France avec les grandes villes (points), sans les nommer."""
    p = site["prefix"]
    pts = []
    for i, (lon, lat) in enumerate(MAP_CITIES):
        x, y = MAP_X(lon), MAP_Y(lat)
        r = 9 if i == 0 else 6.5
        pts.append(f'<circle class="{p}map-ring" cx="{x:.0f}" cy="{y:.0f}" r="{r}" style="animation-delay:{(i * 0.37) % 4:.2f}s"/>'
                   f'<circle class="{p}map-dot" cx="{x:.0f}" cy="{y:.0f}" r="{r}"/>')
    return (f'<figure class="{p}map"><svg viewBox="10 -10 1000 980" role="img" aria-label="Carte de France : sessions AFGSU 2 organisées dans les grandes villes, partout en France">'
            f'<path class="{p}map-land" d="{FR_PATH}"/>' + "".join(pts) + '</svg>'
            f'<figcaption><span class="{p}map-leg"><i aria-hidden="true"></i>Grandes villes de session</span>'
            f'<span>Sessions partout en France, ou directement dans votre structure.</span></figcaption></figure>')


def faq(site):
    p = site["prefix"]
    items = []
    for i, (q, a) in enumerate(site["faq"], 1):
        items.append(f'<details class="{p}faq-item" id="faq-{i}"><summary>{esc(q)}</summary>'
                     f'<div class="{p}faq-a"><p>{esc(a)}</p></div></details>')
    return f'<div class="{p}faq-list">' + "\n".join(items) + "</div>"


def form(site):
    p = site["prefix"]
    name = esc(site["name"])
    metier = esc(site["metier_form"])
    submit = esc(site.get("form_submit", "Envoyer ma demande"))
    return f'''<form class="{p}form" action="https://api.web3forms.com/submit" method="POST" data-w3f>
  <input type="hidden" name="access_key" value="{ACCESS_KEY}">
  <input type="hidden" name="subject" value="Nouvelle demande — {name}">
  <input type="hidden" name="from_name" value="{name}">
  <input type="checkbox" name="botcheck" class="hidden" style="display:none" tabindex="-1" autocomplete="off">
  <div class="{p}form-grid">
    <div class="{p}field"><label for="f-nom">Nom <span aria-hidden="true">*</span></label><input id="f-nom" name="nom" type="text" autocomplete="family-name" required></div>
    <div class="{p}field"><label for="f-prenom">Prénom</label><input id="f-prenom" name="prenom" type="text" autocomplete="given-name"></div>
    <div class="{p}field"><label for="f-email">E-mail <span aria-hidden="true">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" inputmode="email" required></div>
    <div class="{p}field"><label for="f-tel">Téléphone <span aria-hidden="true">*</span></label><input id="f-tel" name="telephone" type="tel" autocomplete="tel" inputmode="tel" required></div>
    <div class="{p}field"><label for="f-metier">Métier</label><input id="f-metier" name="metier" type="text" value="{metier}" autocomplete="organization-title"></div>
    <div class="{p}field"><label for="f-ville">Ville souhaitée</label><input id="f-ville" name="ville" type="text" autocomplete="address-level2" placeholder="Votre ville, ou dans votre structure"></div>
    <div class="{p}field {p}field-full"><label for="f-periode">Date ou période souhaitée</label><input id="f-periode" name="periode" type="text" autocomplete="off" placeholder="{esc(site.get("period_hint", "Ex. dès que possible, ou en mars"))}"></div>
    <div class="{p}field {p}field-full"><label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="4" placeholder="{esc(site.get("msg_hint", "Votre question, le nombre de participants…"))}"></textarea></div>
  </div>
  <div class="{p}rgpd"><input id="f-rgpd" name="rgpd" type="checkbox" value="accepte" required><label for="f-rgpd">J’accepte que mes données soient utilisées pour traiter ma demande, conformément à la <a href="#mentions-legales" data-dialog="mentions-legales">politique de confidentialité</a>. <span aria-hidden="true">*</span></label></div>
  <p class="{p}form-note">* Champs obligatoires. Réponse par téléphone ou par e-mail, sans engagement.</p>
  <button class="{p}btn {p}btn-submit" type="submit">{submit}</button>
  <p class="{p}form-status" role="status" aria-live="polite" hidden></p>
</form>'''


def legal_links(site):
    p = site["prefix"]
    return (f'<a href="#mentions-legales" data-dialog="mentions-legales">Mentions légales</a>'
            f'<a href="#cgv" data-dialog="cgv">CGV</a>')


def footer(site, extra=""):
    p = site["prefix"]
    return f'''<footer class="{p}footer">
  <div class="{p}wrap {p}footer-in">
    <div class="{p}footer-brand">{svg_logo(site, 36)}<p>{esc(site["name"])} by Digivoda</p></div>
    {extra}
    <p class="{p}footer-tel">Téléphone : <a href="{TEL_HREF}">{TEL_TXT}</a></p>
    <nav class="{p}footer-legal" aria-label="Informations légales">{legal_links(site)}</nav>
    <p class="{p}footer-copy">© <span data-year>{YEAR}</span> {esc(site["name"])} by Digivoda — Tous droits réservés</p>
  </div>
</footer>'''


DIGIVODA_BLOCK = '''<ul>
  <li>DIGIVODA — Société par actions simplifiée (SAS)</li>
  <li>Immatriculée au RCS de Nanterre sous le numéro SIREN 488 347 444</li>
  <li>SIRET (siège social) : 488 347 444 00033</li>
  <li>Capital social : 10 000 €</li>
  <li>TVA non applicable, article 293 B du Code Général des Impôts</li>
  <li>Siège social : 5 rue Jules Barbier, 92290 Châtenay-Malabry — France</li>
  <li>Locaux de formation : 4 allée des Garays, 91120 Palaiseau — France</li>
  <li>Contact : Email : <a href="mailto:contact@digivoda.com">contact@digivoda.com</a> — Téléphone : <a href="tel:+33189705570">01 89 70 55 70</a></li>
</ul>'''


def legal(site):
    p = site["prefix"]
    n = esc(site["name"])
    close = f'<form method="dialog" class="{p}dlg-close"><button type="submit" aria-label="Fermer">Fermer ✕</button></form>'
    mentions = f'''<dialog class="{p}dlg" id="mentions-legales" aria-labelledby="ml-t">
  {close}
  <h2 id="ml-t">Mentions légales</h2>
  <h3>Éditeur</h3>
  <p>Le présent site, « {n} », est édité par :</p>
  {DIGIVODA_BLOCK}
  <p>Directeur de la publication : le représentant légal de DIGIVODA.</p>
  <h3>Hébergeur</h3>
  <p>[À COMPLÉTER : raison sociale, adresse et téléphone de l’hébergeur]</p>
  <h3>Propriété intellectuelle</h3>
  <p>Les textes, logos, pictogrammes, mises en page et contenus de ce site sont protégés par le droit de la propriété intellectuelle. Toute reproduction, représentation ou adaptation, totale ou partielle, sans l’autorisation écrite préalable de DIGIVODA est interdite et peut constituer une contrefaçon (articles L335-2 et suivants du Code de la propriété intellectuelle).</p>
  <h3>Données personnelles</h3>
  <p>Responsable du traitement : DIGIVODA, 5 rue Jules Barbier, 92290 Châtenay-Malabry.</p>
  <p>Finalité : les informations saisies dans le formulaire (nom, prénom, e-mail, téléphone, métier, ville et période souhaitées, message) servent uniquement à traiter votre demande d’information ou d’inscription à la formation AFGSU 2 et à vous recontacter. Base légale : votre consentement et les mesures précontractuelles prises à votre demande.</p>
  <p>Destinataires : les seules équipes de DIGIVODA chargées des inscriptions. Le formulaire est transmis par le service Web3Forms, qui achemine le message par e-mail. Vos données ne sont ni vendues ni cédées à des tiers.</p>
  <p>Durée de conservation : 3 ans à compter du dernier contact pour une demande sans suite ; pour les stagiaires inscrits, durée de la relation contractuelle augmentée des délais légaux de conservation des documents de formation.</p>
  <p>Vos droits : vous disposez d’un droit d’accès, de rectification, d’effacement, de limitation, d’opposition et de portabilité de vos données. Pour les exercer, écrivez à <a href="mailto:contact@digivoda.com">contact@digivoda.com</a>. Vous pouvez également adresser une réclamation à la CNIL (www.cnil.fr).</p>
  <h3>Cookies</h3>
  <p>Ce site ne dépose aucun cookie publicitaire ni de mesure d’audience. Les polices de caractères sont chargées depuis Google Fonts, ce qui transmet votre adresse IP à Google lors de l’affichage de la page. Si un outil de mesure d’audience est ajouté, un bandeau de consentement sera mis en place au préalable.</p>
</dialog>'''
    cgv = f'''<dialog class="{p}dlg" id="cgv" aria-labelledby="cgv-t">
  {close}
  <h2 id="cgv-t">Conditions générales de vente</h2>
  <p>Les présentes conditions générales de vente (CGV) s’appliquent aux formations proposées sur le site « {n} », organisées par :</p>
  {DIGIVODA_BLOCK}
  <h3>Article 1 — Objet</h3>
  <p>Les CGV régissent la vente de la formation AFGSU 2 (Attestation de Formation aux Gestes et Soins d’Urgence de niveau 2) par DIGIVODA, organisme de formation, à toute personne physique ou morale (ci-après « le Client »). Toute inscription vaut acceptation sans réserve des CGV, qui prévalent sur tout autre document du Client.</p>
  <h3>Article 2 — Inscription et contrat de formation</h3>
  <p>La demande d’inscription se fait via le formulaire du site, par téléphone ou par e-mail. Elle devient définitive après l’envoi par DIGIVODA d’une confirmation écrite et la signature, par le Client, du contrat de formation professionnelle (personne physique) ou de la convention de formation (personne morale), conformément aux articles L6353-1 et suivants du Code du travail. Le programme, les dates, le lieu et les modalités d’évaluation y sont précisés. DIGIVODA peut refuser une inscription si la session est complète ou si le stagiaire ne relève pas du public visé par la réglementation de l’AFGSU 2.</p>
  <h3>Article 3 — Tarif</h3>
  <p>Le prix de la formation AFGSU 2 est de 385 € TTC par stagiaire pour 21 heures réparties sur 3 jours. TVA non applicable, article 293 B du CGI. Ce prix comprend l’enseignement, l’utilisation du matériel pédagogique (mannequins, défibrillateurs de formation, matériel d’urgence) et les démarches de délivrance de l’attestation. Les frais de déplacement, de repas et d’hébergement du stagiaire restent à sa charge. Pour une formation organisée dans les locaux du Client, un devis spécifique est établi.</p>
  <h3>Article 4 — Modalités de paiement</h3>
  <p>Le règlement s’effectue par carte bancaire ou par virement, selon l’échéancier prévu au contrat. Pour une personne physique, aucune somme ne peut être exigée avant l’expiration du délai de rétractation, et l’éventuel acompte ne peut dépasser 30 % du prix (article L6353-6 du Code du travail). Une facture est remise au Client. Tout retard de paiement d’un professionnel entraîne des pénalités au taux d’intérêt légal majoré de trois points et une indemnité forfaitaire de 40 € pour frais de recouvrement.</p>
  <h3>Article 5 — Droit de rétractation</h3>
  <p>Lorsque le contrat est conclu avec une personne physique qui s’inscrit à titre individuel et à ses frais, celle-ci dispose d’un délai de 10 jours à compter de la signature du contrat pour se rétracter, par lettre recommandée avec avis de réception (article L6353-5 du Code du travail). Aucune somme n’est due en cas de rétractation dans ce délai.</p>
  <h3>Article 6 — Annulation ou report par le stagiaire</h3>
  <p>Toute annulation ou demande de report doit être adressée par écrit à contact@digivoda.com. Plus de 30 jours avant le début de la session : report ou remboursement intégral. Entre 30 et 15 jours : report sans frais sur une session ultérieure, ou retenue de 30 % du prix en cas d’annulation. Moins de 15 jours : report possible une fois, sinon 50 % du prix reste dû. Sur justificatif (maladie, hospitalisation, décès d’un proche, cas de force majeure), le report est accordé sans frais. Le remplacement d’un stagiaire par une autre personne relevant du même public est accepté jusqu’à la veille de la session.</p>
  <h3>Article 7 — Annulation ou report par l’organisme</h3>
  <p>DIGIVODA peut reporter ou annuler une session si le nombre minimal de participants n’est pas atteint, en cas d’indisponibilité du formateur ou de force majeure. Le Client en est informé au plus tôt et se voit proposer une nouvelle date ; à défaut d’accord, les sommes versées sont intégralement remboursées, sans autre indemnité.</p>
  <h3>Article 8 — Absences et assiduité</h3>
  <p>L’attestation AFGSU 2 exige une présence à 100 % des 21 heures. Le stagiaire signe une feuille d’émargement par demi-journée. Toute absence, même partielle, empêche la délivrance de l’attestation : le stagiaire peut alors compléter sa formation sur une session ultérieure, dans la limite des places disponibles, sans que l’absence ouvre droit à remboursement des heures non suivies, sauf cas de force majeure dûment justifié.</p>
  <h3>Article 9 — Délivrance de l’attestation</h3>
  <p>L’attestation AFGSU de niveau 2 est délivrée par le CESU (Centre d’Enseignement des Soins d’Urgence) au stagiaire qui a suivi l’intégralité de la formation et validé l’évaluation continue des gestes. Elle est valable 4 ans ; son renouvellement suppose une formation de réactualisation avant l’échéance. Les délais d’édition dépendent du CESU.</p>
  <h3>Article 10 — Accessibilité et situation de handicap</h3>
  <p>Toute personne en situation de handicap est invitée à le signaler dès l’inscription. Le référent handicap de DIGIVODA étudie avec elle les adaptations possibles (accès aux locaux, rythme, supports, mises en situation) et, si nécessaire, l’oriente vers les partenaires compétents. Certains gestes techniques requièrent une aptitude physique ; leur adaptation est évaluée au cas par cas.</p>
  <h3>Article 11 — Responsabilité</h3>
  <p>Le stagiaire respecte le règlement intérieur et les consignes de sécurité du lieu de formation. DIGIVODA est tenue d’une obligation de moyens. Sa responsabilité ne saurait être engagée pour les dommages indirects ni pour les effets personnels du stagiaire. Le Client reste responsable des dommages qu’il cause aux locaux ou au matériel.</p>
  <h3>Article 12 — Propriété intellectuelle</h3>
  <p>Les supports remis pendant la formation sont la propriété de DIGIVODA. Ils sont destinés à l’usage personnel du stagiaire et ne peuvent être reproduits ou diffusés sans autorisation écrite.</p>
  <h3>Article 13 — Données personnelles</h3>
  <p>Les données du Client sont traitées par DIGIVODA pour gérer l’inscription, le suivi de la formation et la délivrance de l’attestation, conformément au RGPD et selon les modalités décrites dans les mentions légales. Le Client dispose d’un droit d’accès, de rectification et de suppression auprès de contact@digivoda.com.</p>
  <h3>Article 14 — Réclamations</h3>
  <p>Toute réclamation est adressée par écrit à contact@digivoda.com. DIGIVODA en accuse réception sous 7 jours ouvrés et apporte une réponse motivée dans un délai de 30 jours.</p>
  <h3>Article 15 — Droit applicable et litiges</h3>
  <p>Les CGV sont soumises au droit français. En cas de litige, les parties recherchent d’abord une solution amiable. Le consommateur peut recourir gratuitement à un médiateur de la consommation [coordonnées du médiateur À COMPLÉTER]. À défaut d’accord, le litige est porté devant les juridictions compétentes ; entre professionnels, le tribunal compétent est celui du ressort du siège social de DIGIVODA.</p>
</dialog>'''
    return mentions + "\n" + cgv


SCRIPT = r'''
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('video[data-ad]').forEach(function (v) {
    if (reduce) { v.removeAttribute('autoplay'); v.pause(); v.setAttribute('controls', ''); }
    var b = v.parentNode.querySelector('[data-ad-sound]');
    if (!b) return;
    b.addEventListener('click', function () {
      v.muted = !v.muted;
      if (!v.muted) { v.play(); }
      b.setAttribute('aria-pressed', v.muted ? 'false' : 'true');
      b.setAttribute('aria-label', v.muted ? 'Activer le son de la vidéo' : 'Couper le son de la vidéo');
    });
  });
})();
/* ---- Script commun : année, modales légales, envoi du formulaire ---- */
(function () {
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  function openDlg(id) {
    var d = document.getElementById(id);
    if (d && typeof d.showModal === 'function') { if (!d.open) d.showModal(); return true; }
    return false;
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-dialog]');
    if (a && openDlg(a.getAttribute('data-dialog'))) e.preventDefault();
    if (e.target.tagName === 'DIALOG') e.target.close();
  });
  document.querySelectorAll('[data-rappel]').forEach(function (a) {
    a.addEventListener('click', function () {
      var m = document.querySelector('form[data-w3f] textarea');
      if (m && !m.value) m.value = 'Merci de me rappeler pour fixer une session.';
    });
  });
  if (location.hash === '#mentions-legales' || location.hash === '#cgv') openDlg(location.hash.slice(1));
  document.querySelectorAll('form[data-w3f]').forEach(function (form) {
    var status = form.querySelector('[role="status"]');
    var btn = form.querySelector('button[type="submit"]');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var label = btn.textContent;
      btn.disabled = true; btn.textContent = 'Envoi en cours…';
      status.hidden = false; status.className = status.className.replace(/ is-(ok|err)/g, '');
      status.textContent = '';
      fetch(form.action, { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok && j.success, j: j }; }); })
        .then(function (res) {
          if (res.ok) {
            status.className += ' is-ok';
            status.textContent = 'Merci, votre demande est bien envoyée. Nous vous recontactons rapidement pour fixer votre session.';
            form.reset();
          } else { throw new Error('send'); }
        })
        .catch(function () {
          status.className += ' is-err';
          status.textContent = 'L’envoi n’a pas abouti. Réessayez dans un instant ou appelez-nous au 07 80 91 23 35.';
        })
        .then(function () { btn.disabled = false; btn.textContent = label; });
    });
  });
})();
'''

BASE_CSS = '''
/* ---- Base commune (reset léger, accessibilité, mouvement réduit) ---- */
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;line-height:1.6;font-weight:400}
img,svg{max-width:100%}
h1,h2,h3,h4,summary,strong,b,th,dt,legend,label{font-weight:600}
h1,h2,h3,h4{line-height:1.25;margin:0 0 .6em}
p{margin:0 0 1em}
[hidden]{display:none!important}
.hidden{display:none!important}
:focus-visible{outline:3px solid currentColor;outline-offset:3px}
details>summary{cursor:pointer}
dialog{max-width:min(760px,calc(100vw - 32px));max-height:85vh;overflow:auto;padding:28px;border:0;border-radius:10px}
dialog::backdrop{background:rgba(10,15,25,.55)}
dialog:target{display:block;position:static;margin:32px auto}
dialog h2{font-size:1.4rem}
dialog h3{font-size:1.05rem;margin-top:1.4em}
dialog ul{padding-left:1.2em}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{transition:none!important;animation:none!important}}
'''


def placeholder_css(site):
    p = site["prefix"]
    c = site["ph_colors"]  # (fond clair, ligne, texte foncé)
    t = site["theme"]
    return f'''
/* ---- Photos, vidéo, carte ---- */
.{p}photo{{margin:0;position:relative;overflow:hidden;border-radius:var(--{p}radius,12px);background:{c[0]};box-shadow:0 22px 44px -26px rgba(12,22,38,.55),0 2px 6px rgba(12,22,38,.08);width:100%}}
.{p}photo img{{display:block;width:100%;height:auto;aspect-ratio:3 / 2;object-fit:cover;transition:transform .6s ease}}
.{p}photo:hover img{{transform:scale(1.03)}}
.{p}photo-wide{{margin-top:28px}}
.{p}photo-wide img{{aspect-ratio:12 / 5}}
@media (max-width:640px){{.{p}photo-wide img{{aspect-ratio:3 / 2}}}}
.{p}photo-hero{{overflow:visible;background:none;box-shadow:none;isolation:isolate;align-self:center;height:auto}}
.{p}photo-hero::before{{content:"";position:absolute;inset:22px -16px -16px 22px;border-radius:calc(var(--{p}radius,12px) + 6px);background:{t};opacity:.16;z-index:-1}}
.{p}photo-hero img{{aspect-ratio:4 / 3;border-radius:var(--{p}radius,12px);box-shadow:0 28px 56px -28px rgba(12,22,38,.6)}}
.{p}photo-hero:hover img{{transform:none}}
.{p}hero-badge{{position:absolute;left:-14px;bottom:26px;display:flex;gap:10px;align-items:center;background:#fff;color:#1a1f26;border-radius:12px;padding:10px 16px 10px 10px;box-shadow:0 14px 34px -14px rgba(12,22,38,.5);font-size:.84rem;line-height:1.3;max-width:calc(100% - 24px)}}
.{p}hero-badge b{{display:block;font-weight:600}}
.{p}hero-badge-ic{{flex:0 0 34px;height:34px;border-radius:50%;background:{t};color:#fff;display:flex;align-items:center;justify-content:center}}
@media (max-width:640px){{.{p}hero-badge{{left:10px;bottom:12px}}.{p}photo-hero::before{{inset:14px -8px -8px 14px}}}}
.{p}ad{{position:absolute;right:-18px;bottom:-30px;width:clamp(118px,30%,190px);aspect-ratio:9 / 16;border-radius:22px;overflow:hidden;background:#0d1117;border:5px solid #0d1117;box-shadow:0 26px 50px -18px rgba(12,22,38,.7);z-index:2}}
.{p}ad video,.{p}reel-frame video{{display:block;width:100%;height:100%;object-fit:cover;background:#0d1117}}
.{p}ad-sound{{position:absolute;right:8px;bottom:8px;width:36px;height:36px;border:0;border-radius:50%;background:rgba(255,255,255,.92);color:#11161d;display:flex;align-items:center;justify-content:center;cursor:pointer;padding:0}}
.{p}ad-sound .snd-on{{display:none}}
.{p}ad-sound[aria-pressed="true"] .snd-on{{display:inline}}
.{p}ad-sound[aria-pressed="true"] .snd-off{{display:none}}
.{p}photo-hero{{margin-bottom:30px}}
.{p}ad-top{{top:-30px;bottom:auto}}
.{p}ad-solo{{position:relative;right:auto;bottom:auto;top:auto;width:170px;flex:0 0 auto}}
.{p}photo-hero .{p}hero-badge{{max-width:calc(70% - 10px)}}
@media (max-width:640px){{.{p}ad{{right:6px;bottom:-24px;width:112px;border-width:4px;border-radius:16px}}.{p}ad-top{{top:-24px;bottom:auto}}.{p}ad-solo{{width:150px}}.{p}ad-sound{{width:30px;height:30px;right:5px;bottom:5px}}}}
.{p}hv{{max-width:100%;margin:0 auto 34px;position:relative;isolation:isolate;width:clamp(250px,30vw,360px);align-self:center;justify-self:center;flex:0 0 auto}}
.{p}hv::before{{content:"";position:absolute;inset:28px 28px -22px -22px;border-radius:40px;background:{t};opacity:.18;z-index:-1}}
.{p}hv-frame{{position:relative;aspect-ratio:9 / 16;border-radius:32px;overflow:hidden;background:#0d1117;border:8px solid #0d1117;box-shadow:0 40px 70px -30px rgba(12,22,38,.7),0 0 0 1px rgba(255,255,255,.06)}}
.{p}hv-frame video{{display:block;width:100%;height:100%;object-fit:cover;background:#0d1117}}
.{p}hv .{p}ad-sound{{right:12px;bottom:12px;width:44px;height:44px}}
.{p}hv .{p}hero-badge{{left:-34px;bottom:64px;max-width:calc(100% + 10px)}}
.{p}reel-frame{{width:min(360px,80vw)!important}}
@media (max-width:640px){{.{p}hv{{width:min(310px,80vw)}}.{p}hv::before{{inset:18px 18px -10px -10px}}.{p}hv .{p}hero-badge{{left:-8px;bottom:58px}}}}
.{p}adband{{max-width:1180px;margin:0 auto;padding:clamp(28px,5vw,48px) 20px}}
.{p}adband .{p}reel{{justify-content:center}}
.{p}reel-frame{{position:relative}}
.{p}reel{{margin:0;display:flex;flex-wrap:wrap;gap:clamp(22px,5vw,56px);align-items:center;position:relative}}
.{p}reel-frame{{position:relative;flex:0 0 auto;width:min(280px,64vw);aspect-ratio:9 / 16;border-radius:28px;overflow:hidden;background:#0d1117;border:7px solid #0d1117;box-shadow:0 30px 60px -26px rgba(12,22,38,.65),0 0 0 1px rgba(255,255,255,.08) inset}}
.{p}reel-frame video{{display:block;width:100%;height:100%;object-fit:cover;background:#0d1117}}
.{p}reel figcaption{{display:flex;flex-direction:column;align-items:flex-start;gap:10px;max-width:40ch;flex:1 1 240px}}
.{p}reel-title{{font-weight:600;font-size:clamp(1.15rem,2.2vw,1.4rem);line-height:1.3}}
.{p}reel-desc{{font-size:1rem;opacity:.85}}
.{p}reel-pts{{display:flex;flex-direction:column;gap:8px;margin:6px 0 8px}}
.{p}reel-pts span{{display:flex;gap:10px;align-items:center;font-size:.97rem}}
.{p}reel-pts span::before{{content:"";flex:0 0 10px;height:10px;border-radius:50%;background:{t};box-shadow:0 0 0 4px {t}22}}
.{p}reel-cta{{margin-top:4px}}
@media (max-width:640px){{.{p}reel{{flex-direction:column;align-items:flex-start}}}}
.{p}gal{{max-width:1180px;margin:0 auto;padding:clamp(36px,6vw,64px) 20px;container-type:inline-size}}
.{p}gal-head{{max-width:62ch;margin-bottom:clamp(18px,3vw,28px)}}
.{p}gal-k{{display:inline-flex;align-items:center;gap:8px;font-size:.8rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:inherit;opacity:.8}}
.{p}gal-k::before{{content:"";width:22px;height:3px;border-radius:2px;background:{t}}}
.{p}gal-head h2{{margin:8px 0 8px}}
.{p}gal-head p{{margin:0;opacity:.88}}
.{p}gal-grid{{display:grid;gap:clamp(10px,1.6vw,16px);grid-template-columns:1fr}}
.{p}gal-fig{{margin:0;position:relative;overflow:hidden;border-radius:var(--{p}radius,12px);background:{c[0]};box-shadow:0 22px 44px -28px rgba(12,22,38,.55)}}
.{p}gal-fig img{{display:block;width:100%;height:100%;aspect-ratio:3 / 2;object-fit:cover;transition:transform .6s ease}}
.{p}gal-fig:hover img{{transform:scale(1.04)}}
.{p}gal-fig figcaption{{position:absolute;left:0;right:0;bottom:0;display:flex;gap:10px;align-items:center;padding:34px 16px 14px;color:#fff;font-weight:600;font-size:.95rem;line-height:1.3;background:linear-gradient(to top,rgba(8,12,20,.86),rgba(8,12,20,.55) 60%,rgba(8,12,20,0))}}
.{p}gal-n{{flex:0 0 auto;font-size:.75rem;letter-spacing:.06em;padding:3px 7px;border-radius:6px;background:{t};color:#fff}}
@container (min-width:620px){{.{p}gal-grid{{grid-template-columns:1.45fr 1fr;grid-template-rows:1fr 1fr}}.{p}gal-fig:first-child{{grid-row:span 2}}.{p}gal-fig:first-child img{{position:absolute;inset:0;aspect-ratio:auto}}.{p}gal-fig:not(:first-child) img{{aspect-ratio:16 / 10}}}}
@media (prefers-reduced-motion:reduce){{.{p}gal-fig img{{transition:none}}.{p}gal-fig:hover img{{transform:none}}}}
.{p}map{{margin:12px 0 20px;max-width:560px;padding:clamp(14px,3vw,26px);background:#fff;color:#1a1f26;border-radius:18px;box-shadow:0 24px 48px -30px rgba(12,22,38,.45),0 0 0 1px rgba(12,22,38,.06)}}
.{p}map svg{{display:block;width:100%;height:auto;overflow:visible}}
.{p}map-land{{fill:{c[0]};stroke:{t};stroke-width:2.2;stroke-linejoin:round;filter:drop-shadow(0 10px 14px rgba(12,22,38,.12))}}
.{p}map-dot{{fill:{t};stroke:#fff;stroke-width:3}}
.{p}map-ring{{fill:{t};opacity:0;transform-box:fill-box;transform-origin:center;animation:{p}pulse 4s ease-out infinite}}
@keyframes {p}pulse{{0%{{opacity:.35;transform:scale(1)}}70%{{opacity:0;transform:scale(3.4)}}100%{{opacity:0;transform:scale(3.4)}}}}
.{p}map figcaption{{display:flex;flex-direction:column;gap:4px;font-size:.92rem;margin-top:12px;color:#3a414b}}
.{p}map-leg{{display:flex;align-items:center;gap:8px;font-weight:600;color:#1a1f26}}
.{p}map-leg i{{width:12px;height:12px;border-radius:50%;background:{t};box-shadow:0 0 0 3px #fff,0 0 0 4px {t}}}
.{p}body .{p}btn{{transition:transform .2s ease,box-shadow .2s ease,filter .2s ease}}
.{p}body .{p}btn:hover{{transform:translateY(-1px);box-shadow:0 10px 22px -12px rgba(12,22,38,.55);filter:saturate(1.08)}}
.{p}sr{{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
@media (max-width:520px){{.{p}tel-num{{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}.{p}tel{{width:46px;height:46px;justify-content:center;border:1px solid currentColor;border-radius:50%;padding:0!important}}.{p}brand-txt{{font-size:.9rem}}.{p}brand{{flex:1 1 0;min-width:0}}}}
'''


# --------------------------------------------------------------------------
# JSON-LD
# --------------------------------------------------------------------------

def jsonld(site):
    url = site["url"]
    org_id = url + "#organisation"
    instances = [{
        "@type": "CourseInstance",
        "courseMode": "onsite",
        "location": {"@type": "Place", "name": "Sessions AFGSU 2 partout en France",
                     "address": {"@type": "PostalAddress", "addressCountry": "FR"}},
        "courseWorkload": "PT21H",
        "courseSchedule": {"@type": "Schedule", "duration": "PT7H", "repeatCount": 3, "repeatFrequency": "Daily"},
        "inLanguage": "fr",
    }]
    hero = PHOTOS[site["num"]][0][1]
    graph = [
        {"@type": "Organization", "@id": org_id, "name": site["name"], "url": url,
         "logo": url + "logo.svg", "telephone": "+33780912335",
         "contactPoint": {"@type": "ContactPoint", "telephone": "+33780912335", "contactType": "customer service",
                          "areaServed": "FR", "availableLanguage": "fr"},
         "parentOrganization": {"@type": "Organization", "name": "DIGIVODA", "legalName": "DIGIVODA SAS",
                                "taxID": "48834744400033", "email": "contact@digivoda.com", "telephone": "+33189705570",
                                "address": {"@type": "PostalAddress", "streetAddress": "5 rue Jules Barbier",
                                            "postalCode": "92290", "addressLocality": "Châtenay-Malabry", "addressCountry": "FR"}}},
        {"@type": "WebSite", "@id": url + "#website", "url": url, "name": site["name"], "inLanguage": "fr-FR",
         "publisher": {"@id": org_id}},
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": site["title"],
         "description": site["description"], "inLanguage": "fr-FR", "isPartOf": {"@id": url + "#website"},
         "about": {"@id": url + "#formation"}, "breadcrumb": {"@id": url + "#fil-ariane"},
         "primaryImageOfPage": url + f"media/{hero}-1200.jpg", "video": {"@id": url + "#video"}},
        {"@type": "BreadcrumbList", "@id": url + "#fil-ariane", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": url},
            {"@type": "ListItem", "position": 2, "name": site["breadcrumb"], "item": url + "#programme"}]},
        {"@type": "Course", "@id": url + "#formation", "name": site["course_name"],
         "description": site["course_desc"], "provider": {"@id": org_id}, "inLanguage": "fr",
         "image": url + f"media/{hero}-1200.jpg",
         "timeRequired": "PT21H", "educationalCredentialAwarded": "Attestation de Formation aux Gestes et Soins d’Urgence de niveau 2, délivrée par le CESU",
         "audience": {"@type": "EducationalAudience", "educationalRole": site["audience"]},
         "offers": {"@type": "Offer", "price": "385", "priceCurrency": "EUR", "category": "Paid",
                    "availability": "https://schema.org/InStock", "url": url + "#tarif"},
         "hasCourseInstance": instances},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in site["faq"]]},
        video_ld(site),
    ]
    txt = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    return txt.replace("</", "<\\/")


# --------------------------------------------------------------------------
# Assemblage
# --------------------------------------------------------------------------

def head(site):
    fonts = site["fonts_url"]
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(site["title"])}</title>
<meta name="description" content="{esc(site["description"])}">
<meta name="robots" content="index,follow">
<!-- [À COMPLÉTER] : remplacer l’URL provisoire ci-dessous (canonical, Open Graph, JSON-LD) par l’adresse définitive du site -->
<link rel="canonical" href="{site["url"]}">
<meta name="theme-color" content="{site["theme"]}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{esc(site["name"])}">
<meta property="og:title" content="{esc(site["og_title"])}">
<meta property="og:description" content="{esc(site["description"])}">
<meta property="og:url" content="{site["url"]}">
<meta property="og:image" content="{site["url"]}media/{PHOTOS[site["num"]][0][1]}-1200.jpg">
<meta property="og:image:alt" content="{esc(PHOTOS[site["num"]][0][2])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(site["og_title"])}">
<meta name="twitter:description" content="{esc(site["description"])}">
<link rel="icon" type="image/svg+xml" href="{favicon(site)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">'''


TOKEN = re.compile(r"\[\[([a-z\-]+)(?::([a-z0-9\-]+))?\]\]")


def render(site):
    def sub(m):
        k, arg = m.group(1), m.group(2)
        return {
            "header": lambda: header(site, arg or ""),
            "brand": lambda: brand(site),
            "logo": lambda: svg_logo(site),
            "price": lambda: price(site, arg or "price"),
            "img": lambda: img(site, arg),
            "wide": lambda: img(site, arg, wide=True),
            "video": lambda: video(site, arg),
            "map": lambda: france_map(site),
            "gallery": lambda: gallery(site),
            "faq": lambda: faq(site),
            "form": lambda: form(site),
            "footer": lambda: footer(site, site.get("footer_extra", "")),
            "legal": lambda: legal(site),
            "legal-links": lambda: legal_links(site),
            "tel": lambda: f'<a href="{TEL_HREF}">{TEL_TXT}</a>',
            "name": lambda: esc(site["name"]),
        }[k]()

    # Typographie française : espace insécable avant « : ? ! » dans le texte de la page
    raw = re.sub(r" ([:?!])(?=[\s<])", r"&nbsp;\1", site["body"])
    body = TOKEN.sub(sub, raw)
    css = BASE_CSS + placeholder_css(site) + site["css"]
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
{head(site)}
<style>{css}</style>
<script type="application/ld+json">
{jsonld(site)}
</script>
</head>
<body class="{site["prefix"]}body" id="top">
<a class="{site["prefix"]}skip" href="#contenu">Aller au contenu</a>
{body}
{legal(site) if "[[legal]]" not in site["body"] else ""}
<script>{SCRIPT}</script>
</body>
</html>
'''


# --------------------------------------------------------------------------
# Contrôles (section 7 du cahier des charges)
# --------------------------------------------------------------------------

def words(s):
    return len(re.findall(r"[\wÀ-ÿ’'-]+", s))


def check(site, page):
    errs, warns = [], []
    n = site["name"]
    if len(site["title"]) > 60: errs.append(f"title {len(site['title'])} > 60")
    if len(site["description"]) > 155: errs.append(f"description {len(site['description'])} > 155")
    if page.count("<h1") != 1: errs.append(f"{page.count('<h1')} h1")
    if not (12 <= len(site["faq"]) <= 15): errs.append(f"{len(site['faq'])} FAQ")
    if len(site["faq"]) - site.get("faq_generic", 0) < 8: errs.append("moins de 8 FAQ métier")
    for q, a in site["faq"]:
        w = words(a)
        if not 40 <= w <= 90: errs.append(f"FAQ {w} mots : {q[:50]}")
        if esc(a) not in page: errs.append(f"FAQ absente du HTML : {q[:40]}")
    nimg = len(re.findall(r'<img src="media/', page))
    nexp = len(PHOTOS[site["num"]]) + len(GALLERY[site["num"]][2])
    if hero_is_video(site) and any(sl == "hero" for *_x, sl in PHOTOS[site["num"]]): nexp -= 1
    if nimg != nexp: errs.append(f"{nimg} photos affichées sur {nexp}")
    if f'class="{site["prefix"]}gal"' not in page: errs.append("galerie manquante")
    if page.count("<video ") != 1: errs.append("vidéo manquante")
    if "placeholder" in page.split("<body", 1)[1].split("<form", 1)[0]: errs.append("emplacement média vide")
    if f'class="{site["prefix"]}map"' not in page: errs.append("carte de France manquante")
    text = re.sub(r"<[^>]+>", " ", page.split("<body", 1)[1])
    for c in CITY_WORDS:
        if re.search(r"\b" + c + r"\b", text): errs.append(f"ville citée : {c}")
    for m in re.findall(r'(?:src|poster|href)="(media/[^"]+)"', page) + re.findall(r'(media/[\w.-]+) \d+w', page):
        if not (OUT / site["folder"] / m).exists(): errs.append(f"fichier absent : {m}")
    if ACCESS_KEY not in page: errs.append("clé Web3Forms")
    if PRICE_HTML not in page: errs.append("prix")
    low = page.lower()
    # Le mot « financ » est interdit partout, CGV et mentions comprises
    for w in FORBIDDEN:
        if re.search(r"\b" + re.escape(w.lower()), low): errs.append(f"mot interdit : {w}")
    for w in re.findall(r"font-weight\s*:\s*(\d+)", page):
        if int(w) > 600: errs.append(f"font-weight {w}")
    for w in re.findall(r"wght@([\d;.]+)", site["fonts_url"]):
        for v in re.split(r"[;.]+", w):
            if v and int(v) > 600: errs.append(f"Google Fonts poids {v}")
    fams = re.findall(r"family=([^:&]+)", site["fonts_url"])
    if len(set(fams)) > 2: errs.append("plus de 2 polices")
    esc_n = esc(n)
    if f"<title>{esc(site['title'])}</title>" not in page: errs.append("title")
    if f"{esc_n} by Digivoda" not in page: errs.append("footer by Digivoda")
    if f'"name": "{n}"' not in page: errs.append("nom dans le schema")
    for kw in ("21 h", "3 jours", "4 ans", "CESU", "partout en France"):
        if kw not in page: errs.append(f"mention manquante : {kw}")
    if TEL_HREF not in page: errs.append("tel")
    for anchor in ("programme", "tarif", "sessions", "faq", "inscription"):
        if f'id="{anchor}"' not in page: errs.append(f"ancre #{anchor} manquante")
    # « Digivoda » uniquement dans le footer et les mentions/CGV
    main_part = page.split("<body", 1)[1].split(f'class="{site["prefix"]}footer"', 1)[0]
    if re.search("digivoda", main_part, re.I): errs.append("Digivoda hors footer")
    # FAQ JSON-LD = FAQ HTML
    ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S).group(1).replace("<\\/", "</"))
    fq = next(g for g in ld["@graph"] if g["@type"] == "FAQPage")["mainEntity"]
    html_q = [html.unescape(x) for x in re.findall(r"<summary>(.*?)</summary>", page)]
    ld_q = [x["name"] for x in fq]
    if html_q[-len(ld_q):] != ld_q: errs.append("FAQ HTML ≠ JSON-LD")
    # Ids uniques
    ids = re.findall(r'\sid="([^"]+)"', page)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: errs.append(f"ids dupliqués : {dup}")
    for m in re.finditer(r'href="#([^"]+)"', page):
        if m.group(1) not in ids and m.group(1) != "top": errs.append(f"ancre cassée #{m.group(1)}")
    return errs, warns


def load_sites():
    sites = []
    for f in sorted((SRC / "sites").glob("s*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        s = mod.SITE
        s["url"] = f"https://a-completer.example/{s['slug']}/"
        s.setdefault("breadcrumb", "Formation AFGSU 2")
        s["num"] = s["folder"][:2]
        sites.append(s)
    return sites


def readme(sites):
    out = ["# Formations AFGSU 2 par métier : 13 landing pages", "",
           "Chaque dossier contient un `index.html` autonome (CSS et JS inline, Google Fonts comme seule dépendance externe). "
           "Les mentions légales et les CGV s’ouvrent dans une modale `<dialog>` depuis le footer, et restent accessibles sans JavaScript via les ancres `#mentions-legales` et `#cgv`.",
           "", "Les pages sont générées par `metiers/_src/build.py` à partir des fiches `metiers/_src/sites/sNN.py`. "
           "Pour modifier un texte, éditez la fiche puis relancez `python3 metiers/_src/build.py` : le script régénère les 13 pages, "
           "vérifie la checklist du cahier des charges (titre ≤ 60, description ≤ 155, 12 à 15 FAQ de 40 à 90 mots identiques au JSON-LD, "
           "aucune mention de financement, graisses ≤ 600, clé Web3Forms, prix, médias…) et réécrit ce README.", "",
           "## À compléter avant la mise en ligne", "",
           "- **URL de chaque site** : remplacer `https://a-completer.example/<dossier>/` (canonical, Open Graph, JSON-LD). Le plus simple est de changer `s[\"url\"]` dans `build.py`, ou une URL par fiche.",
           "- **Hébergeur** dans les mentions légales : `[À COMPLÉTER]`.",
           "- **Médiateur de la consommation** dans l’article 15 des CGV : `[À COMPLÉTER]`.",
           "- **Médias** : les photos et la vidéo de chaque métier viennent de l’archive fournie (`afgsu.zip`). Elles sont renommées pour le SEO et encodées dans `metiers/NN-…/media/` par `python3 metiers/_src/prepare_media.py <archive dézippée>` (photos en 640 et 1200 px, vidéo MP4 720p). La correspondance photo → emplacement et les textes `alt` sont dans `metiers/_src/media.py`. L’image Open Graph est la photo principale de chaque site.",
           "- **Villes** : aucune ville n’est citée dans les pages. Une carte de France montre les grandes villes de session par des points, sans les nommer.",
           "- **Logo** : chaque dossier contient un `logo.svg` (le pictogramme du site), référencé dans le JSON-LD `Organization`. À déployer avec `index.html`.", "",
           "## Points à faire valider",
           "",
           "Les textes restent prudents sur les obligations, mais quelques affirmations méritent une relecture par un responsable pédagogique avant mise en ligne :",
           "",
           "- AFGSU 2 intégrée à la formation initiale : citée pour infirmiers, aides-soignants, auxiliaires de puériculture, ambulanciers, sages-femmes, médecins, chirurgiens-dentistes, pharmaciens, assistants dentaires et filières de rééducation. Pour les diplômés à l'étranger, la page dit explicitement qu'aucune obligation générale n'est établie.",
           "- Techniciens de laboratoire : l'AFGSU 2 est présentée comme « souvent associée » au certificat de capacité de prélèvements, sans affirmer d'obligation.",
           "- Pharmaciens : la page précise que la formation spécifique à la vaccination reste distincte de l'AFGSU 2.",
           "- Laboratoires : l'obligation de défibrillateur est renvoyée à la catégorie d'ERP, sans affirmation générale.",
           "- Médecins et chirurgiens-dentistes : la FAQ technique cite des doses et algorithmes (adrénaline IM 0,01 mg/kg, max 0,5 mg ; RCP 30:2) conformes aux recommandations usuelles, à faire relire par un formateur.",
           "- CGV : barème d'annulation (30 / 15 jours) et acompte plafonné à 30 % repris de l'article L6353-6 du Code du travail ; à aligner avec vos pratiques réelles.",
           "",
           "## Choix techniques",
           "",
           "- `<title>` du site 13 : le nom complet (76 caractères) ne tient pas dans 60 caractères. Le titre garde le début exact du nom (« Formations AFGSU 2 - Masseurs-kinésithérapeutes, ergo, ortho »). Le nom complet figure dans le logo, le footer, le schema et `og:site_name`.",
           "- JSON-LD `Course` : `timeRequired` PT21H, et pour chaque `CourseInstance` un `courseWorkload` PT21H et un `courseSchedule` (3 × PT7H), forme attendue par Google pour les cours.",
           "- Aucune date de session n'est inventée : les pages montrent la carte de France et invitent à demander les dates.",
           "- JSON-LD : un seul `CourseInstance` « partout en France », un `VideoObject` par site (durée réelle, poster) et l’image principale sur `Course` et `WebPage`.",
           "",
           "## Récapitulatif par site", ""]
    for s in sites:
        out += [f"### {s['folder']} · {s['name']}", "",
                f"- **Dossier** : `metiers/{s['folder']}/index.html`",
                f"- **`<title>`** ({len(s['title'])} car.) : {s['title']}",
                f"- **Meta description** ({len(s['description'])} car.) : {s['description']}",
                f"- **Mot-clé principal** : {s['kw_main']}",
                f"- **Mots-clés secondaires** : " + " · ".join(s["kw_secondary"]),
                f"- **Requêtes conversationnelles (GEO)** : " + " · ".join(s["kw_geo"]),
                f"- **Design** : préfixe CSS `{s['prefix']}`, polices {s['fonts_label']}, structure : {s['layout_label']}",
                "- **Médias** (`media/`) :"]
        for f, stem, alt, slot in PHOTOS[s["num"]]:
            out.append(f"  - `{stem}-640.jpg` / `-1200.jpg` ({slot}) : {alt}")
        for f, stem, alt, cap in GALLERY[s["num"]][2]:
            out.append(f"  - `{stem}-640.jpg` / `-1200.jpg` (galerie) : {alt}")
        vf, vstem, vt, vd = VIDEOS[s["num"]]
        out.append(f"  - `{vstem}.mp4` + `{vstem}-poster.jpg` (vidéo verticale) : **{vt}**")
        out.append("")
    return "\n".join(out)


def main():
    sites = load_sites()
    bad = 0
    for s in sites:
        page = render(s)
        d = OUT / s["folder"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page, encoding="utf-8")
        (d / "logo.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="256" height="256">' + s["pict"] + "</svg>\n", encoding="utf-8")
        errs, warns = check(s, page)
        status = "OK " if not errs else "ERR"
        print(f"{status} {s['folder']:<40} {len(page)//1024:>3} Ko  FAQ {len(s['faq'])}  title {len(s['title'])}  desc {len(s['description'])}")
        for e in errs:
            print("     -", e)
        bad += bool(errs)
    (OUT / "README.md").write_text(readme(sites), encoding="utf-8")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
