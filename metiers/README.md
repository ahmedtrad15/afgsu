# Formations AFGSU 2 par métier : 13 landing pages

Chaque dossier contient un `index.html` autonome (CSS et JS inline, Google Fonts comme seule dépendance externe). Les mentions légales et les CGV s’ouvrent dans une modale `<dialog>` depuis le footer, et restent accessibles sans JavaScript via les ancres `#mentions-legales` et `#cgv`.

Les pages sont générées par `metiers/_src/build.py` à partir des fiches `metiers/_src/sites/sNN.py`. Pour modifier un texte, éditez la fiche puis relancez `python3 metiers/_src/build.py` : le script régénère les 13 pages, vérifie la checklist du cahier des charges (titre ≤ 60, description ≤ 155, 12 à 15 FAQ de 40 à 90 mots identiques au JSON-LD, aucune mention de financement, graisses ≤ 600, clé Web3Forms, prix, médias…) et réécrit ce README.

## À compléter avant la mise en ligne

- **URL de chaque site** : remplacer `https://a-completer.example/<dossier>/` (canonical, Open Graph, JSON-LD). Le plus simple est de changer `s["url"]` dans `build.py`, ou une URL par fiche.
- **Hébergeur** dans les mentions légales : `[À COMPLÉTER]`.
- **Médiateur de la consommation** dans l’article 15 des CGV : `[À COMPLÉTER]`.
- **Médias** : les photos et la vidéo de chaque métier viennent de l’archive fournie (`afgsu.zip`). Elles sont renommées pour le SEO et encodées dans `metiers/NN-…/media/` par `python3 metiers/_src/prepare_media.py <archive dézippée>` (photos en 640 et 1200 px, vidéo MP4 720p). La correspondance photo → emplacement et les textes `alt` sont dans `metiers/_src/media.py`. L’image Open Graph est la photo principale de chaque site.
- **Villes** : aucune ville n’est citée dans les pages. Une carte de France montre les grandes villes de session par des points, sans les nommer.
- **Logo** : chaque dossier contient un `logo.svg` (le pictogramme du site), référencé dans le JSON-LD `Organization`. À déployer avec `index.html`.

## Points à faire valider

Les textes restent prudents sur les obligations, mais quelques affirmations méritent une relecture par un responsable pédagogique avant mise en ligne :

- AFGSU 2 intégrée à la formation initiale : citée pour infirmiers, aides-soignants, auxiliaires de puériculture, ambulanciers, sages-femmes, médecins, chirurgiens-dentistes, pharmaciens, assistants dentaires et filières de rééducation. Pour les diplômés à l'étranger, la page dit explicitement qu'aucune obligation générale n'est établie.
- Techniciens de laboratoire : l'AFGSU 2 est présentée comme « souvent associée » au certificat de capacité de prélèvements, sans affirmer d'obligation.
- Pharmaciens : la page précise que la formation spécifique à la vaccination reste distincte de l'AFGSU 2.
- Laboratoires : l'obligation de défibrillateur est renvoyée à la catégorie d'ERP, sans affirmation générale.
- Médecins et chirurgiens-dentistes : la FAQ technique cite des doses et algorithmes (adrénaline IM 0,01 mg/kg, max 0,5 mg ; RCP 30:2) conformes aux recommandations usuelles, à faire relire par un formateur.
- CGV : barème d'annulation (30 / 15 jours) et acompte plafonné à 30 % repris de l'article L6353-6 du Code du travail ; à aligner avec vos pratiques réelles.

## Choix techniques

- `<title>` du site 13 : le nom complet (76 caractères) ne tient pas dans 60 caractères. Le titre garde le début exact du nom (« Formations AFGSU 2 - Masseurs-kinésithérapeutes, ergo, ortho »). Le nom complet figure dans le logo, le footer, le schema et `og:site_name`.
- JSON-LD `Course` : `timeRequired` PT21H, et pour chaque `CourseInstance` un `courseWorkload` PT21H et un `courseSchedule` (3 × PT7H), forme attendue par Google pour les cours.
- Aucune date de session n'est inventée : les pages montrent la carte de France et invitent à demander les dates.
- JSON-LD : un seul `CourseInstance` « partout en France », un `VideoObject` par site (durée réelle, poster) et l’image principale sur `Course` et `WebPage`.

## Récapitulatif par site

### 01-diplomes-sante-etranger · Formations AFGSU 2 - Diplômés en santé à l'étranger

- **Dossier** : `metiers/01-diplomes-sante-etranger/index.html`
- **`<title>`** (59 car.) : Formations AFGSU 2 - Diplômés en santé à l'étranger | 385 €
- **Meta description** (148 car.) : AFGSU 2 pour diplômés en santé à l'étranger : 3 jours pour maîtriser l'urgence à la française (15, 112, chariot). 385 € TTC. Demandez votre session.
- **Mot-clé principal** : AFGSU 2 diplômé à l'étranger
- **Mots-clés secondaires** : formation AFGSU 2 PADHUE · AFGSU 2 médecin diplômé hors UE · AFGSU 2 infirmier diplômé à l'étranger · AFGSU 2 diplôme étranger prix · AFGSU 2 exercer en France · AFGSU 2 diplômé étranger partout en France · AFGSU 2 diplômé étranger près de chez moi · attestation gestes et soins d'urgence diplômé étranger
- **Requêtes conversationnelles (GEO)** : Un professionnel de santé diplômé à l'étranger doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un diplômé à l'étranger ? · Mon BLS ou ACLS étranger remplace-t-il l'AFGSU 2 ?
- **Design** : préfixe CSS `dse-`, polices Source Sans 3 / Merriweather, structure : hero sobre puis parcours en étapes (timeline « De votre diplôme étranger à l'exercice en France »)
- **Médias** (`media/`) :
  - `formation-afgsu-2-diplome-sante-etranger-medecin-640.jpg` / `-1200.jpg` (hero) : Médecin en blouse blanche, bras croisés, stéthoscope à la main, prêt à exercer en France
  - `afgsu-2-equipe-soignante-couloir-hopital-640.jpg` / `-1200.jpg` (groupe-formation) : Équipe soignante en tenue qui avance dans un couloir d'hôpital
  - `afgsu-2-diplome-etranger-dossier-patient-tablette-640.jpg` / `-1200.jpg` (situation-metier) : Soignant qui consulte un dossier patient sur tablette, stéthoscope posé sur le bureau
  - `video-afgsu-2-diplome-sante-etranger.mp4` + `video-afgsu-2-diplome-sante-etranger-poster.jpg` (vidéo verticale) : **L'AFGSU 2, obligatoire pour exercer en France**

### 02-etudiants-sante · Formations AFGSU 2 - Étudiants en santé

- **Dossier** : `metiers/02-etudiants-sante/index.html`
- **`<title>`** (56 car.) : Formations AFGSU 2 - Étudiants en santé | 3 jours, 385 €
- **Meta description** (145 car.) : AFGSU 2 pour étudiants en santé : validez l'attestation avant vos stages ou en rattrapage. 21 h sur 3 jours, 385 € TTC. Choisissez votre session.
- **Mot-clé principal** : AFGSU 2 étudiant
- **Mots-clés secondaires** : formation AFGSU 2 étudiant infirmier · AFGSU 2 étudiant en médecine · AFGSU 2 rattrapage étudiant · AFGSU 2 avant stage · AFGSU 2 étudiant prix · AFGSU 2 étudiant près de chez moi · AFGSU 2 obligatoire diplôme · attestation gestes et soins d'urgence étudiant
- **Requêtes conversationnelles (GEO)** : Un étudiant en santé doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un étudiant ? · Peut-on rattraper l'AFGSU 2 hors de son école ?
- **Design** : préfixe CSS `etu-`, polices Inter / Lora, structure : page compacte en cartes, accent sur les fenêtres de session
- **Médias** (`media/`) :
  - `formation-afgsu-2-etudiants-sante-stage-640.jpg` / `-1200.jpg` (situation-metier) : Deux étudiants en santé en blouse qui consultent une tablette pendant leur stage
  - `afgsu-2-etudiante-infirmiere-tenue-stage-640.jpg` / `-1200.jpg` (pratique-mannequin) : Étudiante en tunique de stage, stéthoscope autour du cou, dans une chambre d'hôpital
  - `afgsu-2-etudiant-sante-consultation-patient-640.jpg` / `-1200.jpg` (groupe-formation) : Étudiante en médecine en consultation avec un patient âgé et un enfant
  - `afgsu-2-etudiant-sante-revision-stethoscope-640.jpg` / `-1200.jpg` (materiel) : Étudiant qui prend des notes, un stéthoscope posé sur son cahier
  - `video-afgsu-2-etudiant-sante.mp4` + `video-afgsu-2-etudiant-sante-poster.jpg` (vidéo verticale) : **Étudiant en santé : l'AFGSU 2 est obligatoire**

### 03-techniciens-laboratoire · Formations AFGSU 2 - Techniciens de laboratoire

- **Dossier** : `metiers/03-techniciens-laboratoire/index.html`
- **`<title>`** (55 car.) : Formations AFGSU 2 - Techniciens de laboratoire | 385 €
- **Meta description** (145 car.) : AFGSU 2 technicien de laboratoire : malaise vagal, anaphylaxie, AES au poste de prélèvement. 21 h sur 3 jours, 385 € TTC. Réservez votre session.
- **Mot-clé principal** : formation AFGSU 2 technicien de laboratoire
- **Mots-clés secondaires** : AFGSU 2 technicien laboratoire prix · AFGSU 2 préleveur · AFGSU 2 prélèvement sanguin · AFGSU 2 laboratoire de biologie médicale · renouvellement AFGSU 2 technicien de laboratoire · AFGSU 2 technicien de laboratoire près de chez moi · attestation gestes et soins d'urgence technicien de laboratoire
- **Requêtes conversationnelles (GEO)** : Un technicien de laboratoire doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un technicien de laboratoire ? · Que faire si un patient fait un malaise pendant une prise de sang ?
- **Design** : préfixe CSS `lab-`, polices IBM Plex Sans / IBM Plex Serif, structure : fiche technique en 2 colonnes (spécifications fixes à gauche, contenu à droite)
- **Médias** (`media/`) :
  - `formation-afgsu-2-technicienne-laboratoire-640.jpg` / `-1200.jpg` (hero) : Technicienne de laboratoire en blouse blanche dans un laboratoire d'analyses
  - `afgsu-2-technicien-laboratoire-microscope-640.jpg` / `-1200.jpg` (pratique-mannequin) : Technicien de laboratoire en charlotte qui observe un échantillon au microscope
  - `afgsu-2-laboratoire-pipette-echantillons-640.jpg` / `-1200.jpg` (materiel) : Mains gantées qui pipettent des échantillons dans un portoir de tubes
  - `afgsu-2-laboratoire-tubes-prelevement-640.jpg` / `-1200.jpg` (situation-metier) : Mains en gants violets qui manipulent des tubes de prélèvement sur un plan de travail
  - `video-afgsu-2-technicien-laboratoire.mp4` + `video-afgsu-2-technicien-laboratoire-poster.jpg` (vidéo verticale) : **Prises de sang : l'AFGSU 2 pour les techniciens de laboratoire**

### 04-ambulanciers · Formations AFGSU 2 - Ambulanciers

- **Dossier** : `metiers/04-ambulanciers/index.html`
- **`<title>`** (51 car.) : Formations AFGSU 2 - Ambulanciers | 21 h, 385 € TTC
- **Meta description** (137 car.) : AFGSU 2 ambulancier : arrêt cardiaque en transport, DAE embarqué, relevage, accouchement inopiné. 3 jours, 385 € TTC. Renouvelez à temps.
- **Mot-clé principal** : formation AFGSU 2 ambulancier
- **Mots-clés secondaires** : AFGSU 2 ambulancier prix · renouvellement AFGSU 2 ambulancier · AFGSU 2 ambulancier obligatoire · recyclage AFGSU 2 ambulancier · AFGSU 2 ambulancier près de chez moi · AFGSU 2 transport sanitaire · attestation gestes et soins d'urgence ambulancier
- **Requêtes conversationnelles (GEO)** : Un ambulancier doit-il avoir son AFGSU 2 à jour ? · Combien coûte l'AFGSU 2 pour un ambulancier ? · Que faire si l'AFGSU 2 d'un ambulancier a expiré ?
- **Design** : préfixe CSS `amb-`, polices Barlow (400 à 600), structure : hero avec barre de faits clés horizontale, sections courtes
- **Médias** (`media/`) :
  - `formation-afgsu-2-ambulanciers-intervention-nuit-640.jpg` / `-1200.jpg` (hero) : Deux ambulanciers en gilet réfléchissant qui prennent en charge un patient sur un brancard, de nuit, devant l'ambulance
  - `afgsu-2-ambulanciers-cellule-sanitaire-640.jpg` / `-1200.jpg` (pratique-mannequin) : Deux ambulanciers en tenue rouge dans la cellule sanitaire de l'ambulance
  - `afgsu-2-ambulancier-sac-urgence-brancard-640.jpg` / `-1200.jpg` (materiel) : Ambulancière gantée qui prépare le sac d'urgence posé sur le brancard
  - `afgsu-2-ambulancier-radio-alerte-640.jpg` / `-1200.jpg` (situation-metier) : Ambulancier au volant qui transmet un bilan par radio
  - `video-afgsu-2-ambulancier.mp4` + `video-afgsu-2-ambulancier-poster.jpg` (vidéo verticale) : **Ambulancier : votre AFGSU 2 doit être à jour**

### 05-assistantes-dentaires · Formations AFGSU 2 - Assistantes dentaires

- **Dossier** : `metiers/05-assistantes-dentaires/index.html`
- **`<title>`** (54 car.) : Formations AFGSU 2 - Assistantes dentaires | 385 € TTC
- **Meta description** (143 car.) : AFGSU 2 assistante dentaire : malaise au fauteuil, allergie après anesthésie, inhalation, saignement. 21 h, 385 € TTC. Inscrivez-vous en ligne.
- **Mot-clé principal** : AFGSU 2 assistante dentaire
- **Mots-clés secondaires** : formation AFGSU 2 assistant dentaire · AFGSU 2 assistante dentaire prix · AFGSU 2 assistante dentaire obligatoire · renouvellement AFGSU 2 assistante dentaire · AFGSU 2 cabinet dentaire · AFGSU 2 assistante dentaire près de chez moi · attestation gestes et soins d'urgence assistante dentaire
- **Requêtes conversationnelles (GEO)** : Une assistante dentaire doit-elle faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour une assistante dentaire ? · Que faire si un patient fait un malaise au fauteuil dentaire ?
- **Design** : préfixe CSS `ad-`, polices Nunito Sans, structure : hero centré très aéré, sections alternées image / texte
- **Médias** (`media/`) :
  - `formation-afgsu-2-assistante-dentaire-cabinet-640.jpg` / `-1200.jpg` (hero) : Assistante dentaire et praticienne au travail dans un cabinet dentaire lumineux
  - `afgsu-2-assistante-dentaire-aspiration-640.jpg` / `-1200.jpg` (situation-metier) : Assistante dentaire qui tient l'aspiration pendant que le praticien soigne une patiente
  - `afgsu-2-assistante-dentaire-soin-fauteuil-640.jpg` / `-1200.jpg` (pratique-mannequin) : Praticienne et assistante masquées autour d'un patient au fauteuil
  - `afgsu-2-cabinet-dentaire-microscope-640.jpg` / `-1200.jpg` (materiel) : Deux professionnelles en tunique qui travaillent au microscope opératoire du cabinet
  - `video-afgsu-2-assistante-dentaire.mp4` + `video-afgsu-2-assistante-dentaire-poster.jpg` (vidéo verticale) : **Assistante dentaire : l'AFGSU 2 est obligatoire**

### 06-auxiliaires-puericulture · Formations AFGSU 2 - Auxiliaires de puériculture

- **Dossier** : `metiers/06-auxiliaires-puericulture/index.html`
- **`<title>`** (48 car.) : Formations AFGSU 2 - Auxiliaires de puériculture
- **Meta description** (137 car.) : AFGSU 2 auxiliaire de puériculture : étouffement du nourrisson, convulsions, RCP pédiatrique. 3 jours, 385 € TTC. Demandez votre session.
- **Mot-clé principal** : AFGSU 2 auxiliaire de puériculture
- **Mots-clés secondaires** : formation AFGSU 2 auxiliaire de puériculture · AFGSU 2 crèche · AFGSU 2 auxiliaire de puériculture prix · renouvellement AFGSU 2 auxiliaire de puériculture · gestes d'urgence nourrisson formation · AFGSU 2 auxiliaire de puériculture près de chez moi · attestation gestes et soins d'urgence auxiliaire de puériculture
- **Requêtes conversationnelles (GEO)** : Une auxiliaire de puériculture doit-elle faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour une auxiliaire de puériculture ? · Que faire si un bébé s'étouffe à la crèche ?
- **Design** : préfixe CSS `ap-`, polices Quicksand (titres 600) / Open Sans, structure : blocs arrondis, ton rassurant, encadré « gestes pédiatriques »
- **Médias** (`media/`) :
  - `formation-afgsu-2-auxiliaire-puericulture-enfant-640.jpg` / `-1200.jpg` (hero) : Auxiliaire de puériculture qui accompagne une petite fille pendant une activité en crèche
  - `afgsu-2-auxiliaire-puericulture-activite-dessin-640.jpg` / `-1200.jpg` (situation-metier) : Adulte qui dessine avec un jeune enfant assis à une petite table
  - `video-afgsu-2-auxiliaire-puericulture.mp4` + `video-afgsu-2-auxiliaire-puericulture-poster.jpg` (vidéo verticale) : **Auxiliaire de puériculture : l'AFGSU 2 est obligatoire**

### 07-aides-soignants · Formations AFGSU 2 - Aides-soignants

- **Dossier** : `metiers/07-aides-soignants/index.html`
- **`<title>`** (54 car.) : Formations AFGSU 2 - Aides-soignants | 21 h, 385 € TTC
- **Meta description** (137 car.) : AFGSU 2 aide-soignant : fausse route, chute, malaise, arrêt cardiaque en chambre. 3 jours en présentiel, 385 € TTC. Réservez votre place.
- **Mot-clé principal** : formation AFGSU 2 aide-soignant
- **Mots-clés secondaires** : AFGSU 2 aide-soignant prix · AFGSU 2 aide-soignant obligatoire · renouvellement AFGSU 2 aide-soignant · AFGSU 2 EHPAD · AFGSU 2 aide-soignant près de chez moi · recyclage AFGSU 2 aide-soignante · attestation gestes et soins d'urgence aide-soignant
- **Requêtes conversationnelles (GEO)** : Un aide-soignant doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un aide-soignant ? · Que faire en cas de fausse route en EHPAD ?
- **Design** : préfixe CSS `as-`, polices Work Sans, structure : hero image à gauche / texte à droite, section « une journée type »
- **Médias** (`media/`) :
  - `formation-afgsu-2-aide-soignante-residente-ehpad-640.jpg` / `-1200.jpg` (hero) : Aide-soignante souriante penchée vers une résidente âgée en EHPAD
  - `afgsu-2-aide-soignante-chambre-patient-640.jpg` / `-1200.jpg` (situation-metier) : Aide-soignante en tunique bleu marine qui se penche vers un patient alité
  - `afgsu-2-aide-soignant-tenue-service-640.jpg` / `-1200.jpg` (groupe-formation) : Soignante en tunique blanche, stéthoscope autour du cou, dans un service hospitalier
  - `video-afgsu-2-aide-soignant.mp4` + `video-afgsu-2-aide-soignant-poster.jpg` (vidéo verticale) : **Aide-soignant : l'AFGSU 2 est obligatoire**

### 08-infirmiers · Formations AFGSU 2 - Infirmiers

- **Dossier** : `metiers/08-infirmiers/index.html`
- **`<title>`** (59 car.) : Formations AFGSU 2 - Infirmiers | Hôpital et libéral, 385 €
- **Meta description** (142 car.) : AFGSU 2 infirmier : chariot d'urgence, arrêt cardiaque, anaphylaxie, urgences à domicile. 21 h sur 3 jours, 385 € TTC. Réservez votre session.
- **Mot-clé principal** : formation AFGSU 2 infirmier
- **Mots-clés secondaires** : AFGSU 2 infirmier prix · AFGSU 2 infirmier libéral · renouvellement AFGSU 2 infirmier · recyclage AFGSU 2 IDE · AFGSU 2 infirmier obligatoire · AFGSU 2 infirmier près de chez moi · attestation gestes et soins d'urgence infirmier
- **Requêtes conversationnelles (GEO)** : Un infirmier doit-il renouveler son AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un infirmier ? · L'AFGSU 2 est-elle utile pour un infirmier libéral ?
- **Design** : préfixe CSS `ide-`, polices Roboto / Roboto Slab, structure : hero avec comparatif hôpital / libéral en onglets CSS
- **Médias** (`media/`) :
  - `formation-afgsu-2-infirmiere-couloir-hopital-640.jpg` / `-1200.jpg` (situation-metier) : Infirmière en tenue bleue qui pousse une couveuse dans un couloir d'hôpital
  - `afgsu-2-infirmier-prise-tension-640.jpg` / `-1200.jpg` (pratique-mannequin) : Infirmière qui prend la tension artérielle d'un patient
  - `afgsu-2-infirmier-tenue-stethoscope-640.jpg` / `-1200.jpg` (materiel) : Infirmier en tenue de soins bleue, stéthoscope autour du cou
  - `video-afgsu-2-infirmier.mp4` + `video-afgsu-2-infirmier-poster.jpg` (vidéo verticale) : **Infirmier : l'AFGSU 2 est obligatoire**

### 09-pharmaciens · Formations AFGSU 2 - Pharmaciens

- **Dossier** : `metiers/09-pharmaciens/index.html`
- **`<title>`** (54 car.) : Formations AFGSU 2 - Pharmaciens | Officine, 385 € TTC
- **Meta description** (140 car.) : AFGSU 2 pharmacien : malaise au comptoir, anaphylaxie après vaccination, arrêt cardiaque devant l'officine. 3 jours, 385 € TTC. Inscription.
- **Mot-clé principal** : AFGSU 2 pharmacien
- **Mots-clés secondaires** : formation AFGSU 2 pharmacien d'officine · AFGSU 2 pharmacie vaccination · AFGSU 2 préparateur en pharmacie · AFGSU 2 pharmacien prix · renouvellement AFGSU 2 pharmacien · AFGSU 2 pharmacien près de chez moi · attestation gestes et soins d'urgence pharmacien
- **Requêtes conversationnelles (GEO)** : Un pharmacien doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un pharmacien ? · Que faire en cas de réaction allergique après une vaccination en pharmacie ?
- **Design** : préfixe CSS `phar-`, polices Manrope (600 max), structure : page en sections numérotées (1, 2, 3…)
- **Médias** (`media/`) :
  - `formation-afgsu-2-pharmacien-officine-patiente-640.jpg` / `-1200.jpg` (hero) : Pharmacien en blouse qui conseille une patiente au comptoir de l'officine
  - `afgsu-2-pharmacienne-rayonnage-officine-640.jpg` / `-1200.jpg` (pratique-mannequin) : Pharmacienne souriante qui attrape une boîte dans les rayonnages
  - `afgsu-2-pharmacien-reserve-medicaments-640.jpg` / `-1200.jpg` (situation-metier) : Pharmacien en blouse dans l'allée de la réserve de médicaments
  - `video-afgsu-2-pharmacien.mp4` + `video-afgsu-2-pharmacien-poster.jpg` (vidéo verticale) : **Pharmacien : l'AFGSU 2, c'est obligatoire**

### 10-sages-femmes · Formations AFGSU 2 - Sages-femmes

- **Dossier** : `metiers/10-sages-femmes/index.html`
- **`<title>`** (51 car.) : Formations AFGSU 2 - Sages-femmes | 21 h, 385 € TTC
- **Meta description** (140 car.) : AFGSU 2 sage-femme : accouchement inopiné, hémorragie du post-partum, réanimation du nouveau-né. 3 jours, 385 € TTC. Réservez votre session.
- **Mot-clé principal** : AFGSU 2 sage-femme
- **Mots-clés secondaires** : formation AFGSU 2 sage-femme · AFGSU 2 sage-femme libérale · renouvellement AFGSU 2 sage-femme · AFGSU 2 sage-femme prix · urgences obstétricales formation · AFGSU 2 sage-femme près de chez moi · attestation gestes et soins d'urgence sage-femme
- **Requêtes conversationnelles (GEO)** : Une sage-femme doit-elle faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour une sage-femme ? · L'AFGSU 2 couvre-t-elle l'hémorragie du post-partum ?
- **Design** : préfixe CSS `sf-`, polices Libre Franklin / Libre Baskerville, structure : hero éditorial (citation + texte), mise en page type magazine sobre
- **Médias** (`media/`) :
  - `formation-afgsu-2-sage-femme-nouveau-ne-640.jpg` / `-1200.jpg` (hero) : Sage-femme qui tient un nouveau-né près du lit de la mère, en maternité
  - `afgsu-2-sage-femme-tenue-stethoscope-640.jpg` / `-1200.jpg` (situation-metier) : Sage-femme en tenue verte, stéthoscope autour du cou
  - `video-afgsu-2-sage-femme.mp4` + `video-afgsu-2-sage-femme-poster.jpg` (vidéo verticale) : **Sage-femme : l'AFGSU 2 est obligatoire**

### 11-chirurgiens-dentistes · Formations AFGSU 2 - Chirurgiens-dentistes

- **Dossier** : `metiers/11-chirurgiens-dentistes/index.html`
- **`<title>`** (54 car.) : Formations AFGSU 2 - Chirurgiens-dentistes | 385 € TTC
- **Meta description** (143 car.) : AFGSU 2 chirurgien-dentiste : syncope, angor, anaphylaxie, inhalation au cabinet. Formez-vous et votre équipe. 21 h, 385 € TTC. Contactez-nous.
- **Mot-clé principal** : AFGSU 2 chirurgien-dentiste
- **Mots-clés secondaires** : formation AFGSU 2 dentiste · AFGSU 2 chirurgien-dentiste prix · urgences au cabinet dentaire formation · trousse d'urgence cabinet dentaire · renouvellement AFGSU 2 dentiste · AFGSU 2 dentiste près de chez moi · attestation gestes et soins d'urgence chirurgien-dentiste
- **Requêtes conversationnelles (GEO)** : Un chirurgien-dentiste doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un chirurgien-dentiste ? · Que doit contenir la trousse d'urgence d'un cabinet dentaire ?
- **Design** : préfixe CSS `cd-`, polices DM Sans / DM Serif Display (titres de taille modérée), structure : hero premium discret, encart « formez tout votre cabinet »
- **Médias** (`media/`) :
  - `formation-afgsu-2-chirurgien-dentiste-cabinet-640.jpg` / `-1200.jpg` (hero) : Chirurgienne-dentiste en tenue bleue qui règle l'éclairage au-dessus d'une patiente
  - `afgsu-2-chirurgien-dentiste-assistante-soin-640.jpg` / `-1200.jpg` (situation-metier) : Chirurgien-dentiste et assistante en tenue qui soignent ensemble un patient
  - `afgsu-2-chirurgien-dentiste-instruments-640.jpg` / `-1200.jpg` (materiel) : Gros plan sur des instruments dentaires pendant un soin au fauteuil
  - `video-afgsu-2-chirurgien-dentiste.mp4` + `video-afgsu-2-chirurgien-dentiste-poster.jpg` (vidéo verticale) : **Chirurgien-dentiste : l'AFGSU 2 est obligatoire pour vous**

### 12-medecins · Formations AFGSU 2 - Médecins

- **Dossier** : `metiers/12-medecins/index.html`
- **`<title>`** (57 car.) : Formations AFGSU 2 - Médecins | Cabinet, SSE, NRBC, 385 €
- **Meta description** (142 car.) : AFGSU 2 médecin : arrêt cardiaque au cabinet, douleur thoracique, détresse respiratoire, SSE et NRBC. 21 h, 385 € TTC. Programme détaillé ici.
- **Mot-clé principal** : AFGSU 2 médecin
- **Mots-clés secondaires** : formation AFGSU 2 médecin généraliste · AFGSU 2 médecin prix · renouvellement AFGSU 2 médecin · urgences au cabinet médical formation · AFGSU 2 maison de santé · AFGSU 2 médecin près de chez moi · formation situations sanitaires exceptionnelles médecin · attestation gestes et soins d'urgence médecin
- **Requêtes conversationnelles (GEO)** : Un médecin doit-il renouveler son AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un médecin ? · Quel matériel d'urgence au cabinet médical ?
- **Design** : préfixe CSS `med-`, polices Public Sans, structure : page dense et factuelle, tableau récapitulatif en haut, FAQ technique
- **Médias** (`media/`) :
  - `formation-afgsu-2-medecin-cabinet-640.jpg` / `-1200.jpg` (hero) : Médecin généraliste en blouse, bras croisés, dans son cabinet
  - `afgsu-2-medecin-consultation-patient-640.jpg` / `-1200.jpg` (pratique-mannequin) : Médecin en consultation avec un patient, à son bureau
  - `afgsu-2-medecin-ordonnance-640.jpg` / `-1200.jpg` (groupe-formation) : Médecin qui remplit un document sur un porte-bloc face à un patient
  - `afgsu-2-medecin-stethoscope-coeur-640.jpg` / `-1200.jpg` (materiel) : Soignante qui tient un stéthoscope formant un cœur
  - `video-afgsu-2-medecin.mp4` + `video-afgsu-2-medecin-poster.jpg` (vidéo verticale) : **Médecin : l'AFGSU 2 est obligatoire**

### 13-kine-ergo-orthophonistes · Formations AFGSU 2 - Masseurs-kinésithérapeutes (kiné, ergo, orthophoniste)

- **Dossier** : `metiers/13-kine-ergo-orthophonistes/index.html`
- **`<title>`** (60 car.) : Formations AFGSU 2 - Masseurs-kinésithérapeutes, ergo, ortho
- **Meta description** (139 car.) : AFGSU 2 kiné, ergothérapeute, orthophoniste : malaise à l'effort, chute, fausse route, arrêt cardiaque en salle. 21 h, 385 € TTC. Réservez.
- **Mot-clé principal** : formation AFGSU 2 kinésithérapeute
- **Mots-clés secondaires** : AFGSU 2 kiné prix · AFGSU 2 ergothérapeute · AFGSU 2 orthophoniste · renouvellement AFGSU 2 kinésithérapeute · AFGSU 2 masseur-kinésithérapeute obligatoire · AFGSU 2 kiné près de chez moi · attestation gestes et soins d'urgence ergothérapeute · attestation gestes et soins d'urgence orthophoniste
- **Requêtes conversationnelles (GEO)** : Un kinésithérapeute doit-il faire l'AFGSU 2 ? · Un ergothérapeute peut-il suivre l'AFGSU 2 ? · Un orthophoniste est-il concerné par l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un kiné ?
- **Design** : préfixe CSS `reed-`, polices Mulish, structure : onglets par profession (kiné / ergo / orthophoniste) + accordéons par module
- **Médias** (`media/`) :
  - `formation-afgsu-2-kinesitherapeute-seance-640.jpg` / `-1200.jpg` (hero) : Kinésithérapeute qui traite une patiente allongée sur la table de soin
  - `afgsu-2-kinesitherapeute-patient-640.jpg` / `-1200.jpg` (situation-metier) : Rééducatrice en tunique qui se penche vers un patient pendant une séance
  - `video-afgsu-2-kine-ergo-orthophoniste.mp4` + `video-afgsu-2-kine-ergo-orthophoniste-poster.jpg` (vidéo verticale) : **Kinés, ergos, orthophonistes : l'AFGSU 2 est obligatoire**
