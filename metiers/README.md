# Formations AFGSU 2 par métier : 13 landing pages

Chaque dossier contient un `index.html` autonome (CSS et JS inline, Google Fonts comme seule dépendance externe). Les mentions légales et les CGV s’ouvrent dans une modale `<dialog>` depuis le footer, et restent accessibles sans JavaScript via les ancres `#mentions-legales` et `#cgv`.

Les pages sont générées par `metiers/_src/build.py` à partir des fiches `metiers/_src/sites/sNN.py`. Pour modifier un texte, éditez la fiche puis relancez `python3 metiers/_src/build.py` : le script régénère les 13 pages, vérifie la checklist du cahier des charges (titre ≤ 60, description ≤ 155, 12 à 15 FAQ de 40 à 90 mots identiques au JSON-LD, aucune mention de financement, graisses ≤ 600, clé Web3Forms, prix, médias…) et réécrit ce README.

## À compléter avant la mise en ligne

- **URL de chaque site** : remplacer `https://a-completer.example/<dossier>/` (canonical, Open Graph, JSON-LD). Le plus simple est de changer `s["url"]` dans `build.py`, ou une URL par fiche.
- **Hébergeur** dans les mentions légales : `[À COMPLÉTER]`.
- **Médiateur de la consommation** dans l’article 15 des CGV : `[À COMPLÉTER]`.
- **Images, vidéos, image Open Graph** : remplacer les emplacements listés ci-dessous. Chaque `<figure class="media-placeholder">` contient en commentaire la balise `<img>` à poser avec son `alt` déjà rédigé ; chaque vidéo contient en commentaire son balisage `VideoObject` à compléter.
- **Avis stagiaires** : un encart « Avis stagiaires (à intégrer) » est prévu sur chaque page. Ne publier que de vrais avis vérifiables.
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
- Aucune date de session n'est inventée : les pages listent les villes et invitent à demander les dates.

## Récapitulatif par site

### 01-diplomes-sante-etranger · Formations AFGSU 2 - Diplômés en santé à l'étranger

- **Dossier** : `metiers/01-diplomes-sante-etranger/index.html`
- **`<title>`** (59 car.) : Formations AFGSU 2 - Diplômés en santé à l'étranger | 385 €
- **Meta description** (148 car.) : AFGSU 2 pour diplômés en santé à l'étranger : 3 jours pour maîtriser l'urgence à la française (15, 112, chariot). 385 € TTC. Demandez votre session.
- **Mot-clé principal** : AFGSU 2 diplômé à l'étranger
- **Mots-clés secondaires** : formation AFGSU 2 PADHUE · AFGSU 2 médecin diplômé hors UE · AFGSU 2 infirmier diplômé à l'étranger · AFGSU 2 diplôme étranger prix · AFGSU 2 exercer en France · AFGSU 2 diplômé étranger Paris · AFGSU 2 diplômé étranger Lyon / Marseille · attestation gestes et soins d'urgence diplômé étranger
- **Requêtes conversationnelles (GEO)** : Un professionnel de santé diplômé à l'étranger doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un diplômé à l'étranger ? · Mon BLS ou ACLS étranger remplace-t-il l'AFGSU 2 ?
- **Design** : préfixe CSS `dse-`, polices Source Sans 3 / Merriweather, structure : hero sobre puis parcours en étapes (timeline « De votre diplôme étranger à l'exercice en France »)
- **Placeholders médias** :
  - `hero` (image, 4 / 3) : une médecin et un infirmier d'origines différentes, en tenue de service française, pendant un exercice de réanimation sur mannequin adulte avec défibrillateur.
  - `pratique-mannequin` (image, 3 / 2) : gros plan sur les mains d'un stagiaire qui réalise des compressions thoraciques, le formateur corrige la position.
  - `groupe-formation` (image, 3 / 2) : petit groupe de 8 stagiaires autour d'un formateur, carte des numéros d'urgence français (15, 112, 114) affichée au tableau.
  - `materiel` (image, 1 / 1) : chariot d'urgence ouvert, tiroirs étiquetés en français, DAE de formation posé à côté.
  - `situation-metier` (image, 3 / 2) : une soignante au téléphone dans un couloir de service, en train de passer un bilan au SAMU (15), fiche de bilan en main.
  - `video-1` (vidéo 16/9) : **Appeler le 15 en France : le bilan en 60 secondes**. Un formateur joue le médecin régulateur et une stagiaire passe l'alerte : qui appeler, dans quel ordre donner les informations, quels mots employer.
  - `video-2` (vidéo 16/9) : **Trois jours de formation AFGSU 2, du premier massage à l'exercice de crise**. Montage court des temps forts : RCP sur mannequins, ouverture du chariot d'urgence, exercice d'afflux de victimes, remise de l'attestation.

### 02-etudiants-sante · Formations AFGSU 2 - Étudiants en santé

- **Dossier** : `metiers/02-etudiants-sante/index.html`
- **`<title>`** (56 car.) : Formations AFGSU 2 - Étudiants en santé | 3 jours, 385 €
- **Meta description** (145 car.) : AFGSU 2 pour étudiants en santé : validez l'attestation avant vos stages ou en rattrapage. 21 h sur 3 jours, 385 € TTC. Choisissez votre session.
- **Mot-clé principal** : AFGSU 2 étudiant
- **Mots-clés secondaires** : formation AFGSU 2 étudiant infirmier · AFGSU 2 étudiant en médecine · AFGSU 2 rattrapage étudiant · AFGSU 2 avant stage · AFGSU 2 étudiant prix · AFGSU 2 étudiant Toulouse / Bordeaux / Lille · AFGSU 2 obligatoire diplôme · attestation gestes et soins d'urgence étudiant
- **Requêtes conversationnelles (GEO)** : Un étudiant en santé doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un étudiant ? · Peut-on rattraper l'AFGSU 2 hors de son école ?
- **Design** : préfixe CSS `etu-`, polices Inter / Lora, structure : page compacte en cartes, accent sur les fenêtres de session
- **Placeholders médias** :
  - `hero` (image, 16 / 10) : trois étudiants en tenue de stage (blouse ou tunique) autour d'un mannequin, l'un masse, l'autre prépare le défibrillateur, le troisième compte à voix haute.
  - `pratique-mannequin` (image, 1 / 1) : étudiante qui pratique la désobstruction sur un mannequin nourrisson, le formateur accroupi à côté.
  - `groupe-formation` (image, 1 / 1) : groupe de 10 étudiants en salle de formation, débriefing en cercle après une mise en situation.
  - `materiel` (image, 1 / 1) : sur une table : gants, lunettes de protection, collecteur d'aiguilles, kit AES et affiche de conduite à tenir.
  - `situation-metier` (image, 16 / 10) : étudiant en stage dans un couloir de service, qui accompagne une patiente prise de malaise jusqu'à un fauteuil.
  - `video-1` (vidéo 16/9) : **Premier stage : votre patient fait un malaise, que faites-vous ?**. Mise en situation filmée à hauteur d'étudiant : repérer les signes, installer, appeler l'infirmier référent, surveiller. Commentée par le formateur.
  - `video-2` (vidéo 16/9) : **Accident d'exposition au sang : les 4 réflexes**. Une étudiante se pique avec une aiguille souillée. La vidéo montre, minute par minute, le lavage, l'antisepsie, la déclaration et la consultation.

### 03-techniciens-laboratoire · Formations AFGSU 2 - Techniciens de laboratoire

- **Dossier** : `metiers/03-techniciens-laboratoire/index.html`
- **`<title>`** (55 car.) : Formations AFGSU 2 - Techniciens de laboratoire | 385 €
- **Meta description** (145 car.) : AFGSU 2 technicien de laboratoire : malaise vagal, anaphylaxie, AES au poste de prélèvement. 21 h sur 3 jours, 385 € TTC. Réservez votre session.
- **Mot-clé principal** : formation AFGSU 2 technicien de laboratoire
- **Mots-clés secondaires** : AFGSU 2 technicien laboratoire prix · AFGSU 2 préleveur · AFGSU 2 prélèvement sanguin · AFGSU 2 laboratoire de biologie médicale · renouvellement AFGSU 2 technicien de laboratoire · AFGSU 2 technicien de laboratoire Lyon / Strasbourg · attestation gestes et soins d'urgence technicien de laboratoire
- **Requêtes conversationnelles (GEO)** : Un technicien de laboratoire doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un technicien de laboratoire ? · Que faire si un patient fait un malaise pendant une prise de sang ?
- **Design** : préfixe CSS `lab-`, polices IBM Plex Sans / IBM Plex Serif, structure : fiche technique en 2 colonnes (spécifications fixes à gauche, contenu à droite)
- **Placeholders médias** :
  - `hero` (image, 16 / 9) : box de prélèvement d'un laboratoire : une technicienne soutient un patient qui s'affaisse sur le fauteuil de prélèvement, garrot encore en place.
  - `pratique-mannequin` (image, 4 / 3) : technicien en blouse réalisant un massage cardiaque sur mannequin adulte, électrodes de DAE posées.
  - `groupe-formation` (image, 4 / 3) : groupe de techniciens et biologistes en salle de formation, formateur expliquant la conduite à tenir face à une anaphylaxie.
  - `materiel` (image, 4 / 3) : plan de travail : stylo d'adrénaline de démonstration, collecteur d'aiguilles, kit AES, tensiomètre, bouteille d'oxygène.
  - `situation-metier` (image, 4 / 3) : salle d'attente de laboratoire, patiente âgée au sol, technicien accroupi qui lui parle et évalue sa conscience.
  - `video-1` (vidéo 16/9) : **Malaise vagal au fauteuil de prélèvement : la séquence complète**. Du retrait de l'aiguille à la surélévation des jambes, puis la surveillance et le moment où l'on appelle le 15. Reconstitution commentée en box de prélèvement.
  - `video-2` (vidéo 16/9) : **Piqûre accidentelle au laboratoire : que faire dans l'heure**. Un technicien se pique en recapuchonnant. Lavage, antisepsie, déclaration, consultation référente : chaque étape chronométrée.

### 04-ambulanciers · Formations AFGSU 2 - Ambulanciers

- **Dossier** : `metiers/04-ambulanciers/index.html`
- **`<title>`** (51 car.) : Formations AFGSU 2 - Ambulanciers | 21 h, 385 € TTC
- **Meta description** (137 car.) : AFGSU 2 ambulancier : arrêt cardiaque en transport, DAE embarqué, relevage, accouchement inopiné. 3 jours, 385 € TTC. Renouvelez à temps.
- **Mot-clé principal** : formation AFGSU 2 ambulancier
- **Mots-clés secondaires** : AFGSU 2 ambulancier prix · renouvellement AFGSU 2 ambulancier · AFGSU 2 ambulancier obligatoire · recyclage AFGSU 2 ambulancier · AFGSU 2 ambulancier Marseille / Lyon / Paris · AFGSU 2 transport sanitaire · attestation gestes et soins d'urgence ambulancier
- **Requêtes conversationnelles (GEO)** : Un ambulancier doit-il avoir son AFGSU 2 à jour ? · Combien coûte l'AFGSU 2 pour un ambulancier ? · Que faire si l'AFGSU 2 d'un ambulancier a expiré ?
- **Design** : préfixe CSS `amb-`, polices Barlow (400 à 600), structure : hero avec barre de faits clés horizontale, sections courtes
- **Placeholders médias** :
  - `hero` (image, 3 / 2) : cellule sanitaire d'une ambulance, porte arrière ouverte : un ambulancier masse un mannequin sur le brancard pendant que son équipier pose les électrodes du DAE.
  - `pratique-mannequin` (image, 4 / 3) : deux ambulanciers en tenue réalisant une RCP à deux sauveteurs, relais toutes les deux minutes.
  - `groupe-formation` (image, 4 / 3) : groupe d'ambulanciers autour d'un brancard pendant un exercice de relevage avec matelas immobilisateur.
  - `materiel` (image, 4 / 3) : sac d'urgence ouvert : BAVU, canules, aspirateur de mucosités, garrot tourniquet, kit accouchement.
  - `situation-metier` (image, 3 / 2) : accident de la route simulé sur parking : ambulanciers sécurisant la zone, l'un maintient la tête d'une victime assise dans un véhicule.
  - `video-1` (vidéo 16/9) : **Arrêt cardiaque en plein transport : l'ambulance s'arrête, l'équipage enchaîne**. Le patient décroche sur l'autoroute. Arrêt du véhicule, alerte du 15, RCP et DAE embarqué : la séquence à deux, filmée en cellule.
  - `video-2` (vidéo 16/9) : **Relevage et brancardage : les techniques revues en formation**. Pont simplifié, cuillère, matelas immobilisateur, escaliers étroits : démonstration commentée des techniques travaillées pendant les trois jours.

### 05-assistantes-dentaires · Formations AFGSU 2 - Assistantes dentaires

- **Dossier** : `metiers/05-assistantes-dentaires/index.html`
- **`<title>`** (54 car.) : Formations AFGSU 2 - Assistantes dentaires | 385 € TTC
- **Meta description** (143 car.) : AFGSU 2 assistante dentaire : malaise au fauteuil, allergie après anesthésie, inhalation, saignement. 21 h, 385 € TTC. Inscrivez-vous en ligne.
- **Mot-clé principal** : AFGSU 2 assistante dentaire
- **Mots-clés secondaires** : formation AFGSU 2 assistant dentaire · AFGSU 2 assistante dentaire prix · AFGSU 2 assistante dentaire obligatoire · renouvellement AFGSU 2 assistante dentaire · AFGSU 2 cabinet dentaire · AFGSU 2 assistante dentaire Nantes / Rennes / Paris · attestation gestes et soins d'urgence assistante dentaire
- **Requêtes conversationnelles (GEO)** : Une assistante dentaire doit-elle faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour une assistante dentaire ? · Que faire si un patient fait un malaise au fauteuil dentaire ?
- **Design** : préfixe CSS `ad-`, polices Nunito Sans, structure : hero centré très aéré, sections alternées image / texte
- **Placeholders médias** :
  - `hero` (image, 21 / 9) : cabinet dentaire lumineux : une assistante dentaire bascule le fauteuil en position allongée pendant que la praticienne parle au patient pâle.
  - `pratique-mannequin` (image, 4 / 3) : assistante dentaire en tunique réalisant des compressions thoraciques sur mannequin posé au sol, à côté d'un fauteuil dentaire.
  - `groupe-formation` (image, 4 / 3) : petit groupe d'assistantes dentaires autour d'une formatrice qui montre la manœuvre de désobstruction sur mannequin.
  - `materiel` (image, 4 / 3) : trousse d'urgence du cabinet dentaire ouverte : bouteille d'oxygène, masque, stylo d'adrénaline de démonstration, sucre, compresses.
  - `situation-metier` (image, 4 / 3) : assistante dentaire comprimant une compresse sur une alvéole après extraction, le patient mord, la praticienne observe.
  - `video-1` (vidéo 16/9) : **Malaise au fauteuil : qui fait quoi entre la praticienne et l'assistante**. Reconstitution dans un cabinet : bascule du fauteuil, oxygène, surveillance, appel au 15 si besoin. Les rôles de chacune sont détaillés.
  - `video-2` (vidéo 16/9) : **Un instrument tombe dans la gorge du patient**. Toux efficace, toux inefficace, claques dans le dos, compressions abdominales : la conduite à tenir face à une inhalation de corps étranger au cabinet.

### 06-auxiliaires-puericulture · Formations AFGSU 2 - Auxiliaires de puériculture

- **Dossier** : `metiers/06-auxiliaires-puericulture/index.html`
- **`<title>`** (48 car.) : Formations AFGSU 2 - Auxiliaires de puériculture
- **Meta description** (137 car.) : AFGSU 2 auxiliaire de puériculture : étouffement du nourrisson, convulsions, RCP pédiatrique. 3 jours, 385 € TTC. Demandez votre session.
- **Mot-clé principal** : AFGSU 2 auxiliaire de puériculture
- **Mots-clés secondaires** : formation AFGSU 2 auxiliaire de puériculture · AFGSU 2 crèche · AFGSU 2 auxiliaire de puériculture prix · renouvellement AFGSU 2 auxiliaire de puériculture · gestes d'urgence nourrisson formation · AFGSU 2 auxiliaire de puériculture Bordeaux / Lyon / Lille · attestation gestes et soins d'urgence auxiliaire de puériculture
- **Requêtes conversationnelles (GEO)** : Une auxiliaire de puériculture doit-elle faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour une auxiliaire de puériculture ? · Que faire si un bébé s'étouffe à la crèche ?
- **Design** : préfixe CSS `ap-`, polices Quicksand (titres 600) / Open Sans, structure : blocs arrondis, ton rassurant, encadré « gestes pédiatriques »
- **Placeholders médias** :
  - `hero` (image, 5 / 4) : auxiliaire de puériculture en blouse colorée, assise au sol dans une section de crèche, un mannequin nourrisson en position de désobstruction sur son avant-bras.
  - `pratique-mannequin` (image, 4 / 3) : gros plan sur deux doigts réalisant des compressions thoraciques sur un mannequin nourrisson posé sur une table à langer.
  - `groupe-formation` (image, 4 / 3) : groupe d'auxiliaires de puériculture et d'éducatrices autour d'une formatrice, mannequins nourrisson et enfant alignés sur des tapis.
  - `materiel` (image, 4 / 3) : mannequins nourrisson et enfant, défibrillateur avec électrodes pédiatriques, thermomètre, trousse PAI avec stylo d'adrénaline de démonstration.
  - `situation-metier` (image, 4 / 3) : en maternité, auxiliaire de puériculture qui observe un nouveau-né dans son berceau, main posée sur son ventre pour suivre la respiration.
  - `video-1` (vidéo 16/9) : **Un bébé s'étouffe pendant le repas : les gestes en temps réel**. Une formatrice montre, sur mannequin nourrisson, les claques dans le dos et les compressions thoraciques, puis ce qu'il faut faire si l'enfant perd connaissance.
  - `video-2` (vidéo 16/9) : **Convulsions fébriles à la crèche : rester calme, protéger, alerter**. Reconstitution en section des grands : protéger l'enfant, chronométrer la crise, mettre en PLS, appeler le 15, prévenir les parents ensuite.

### 07-aides-soignants · Formations AFGSU 2 - Aides-soignants

- **Dossier** : `metiers/07-aides-soignants/index.html`
- **`<title>`** (54 car.) : Formations AFGSU 2 - Aides-soignants | 21 h, 385 € TTC
- **Meta description** (137 car.) : AFGSU 2 aide-soignant : fausse route, chute, malaise, arrêt cardiaque en chambre. 3 jours en présentiel, 385 € TTC. Réservez votre place.
- **Mot-clé principal** : formation AFGSU 2 aide-soignant
- **Mots-clés secondaires** : AFGSU 2 aide-soignant prix · AFGSU 2 aide-soignant obligatoire · renouvellement AFGSU 2 aide-soignant · AFGSU 2 EHPAD · AFGSU 2 aide-soignant Lille / Toulouse / Paris · recyclage AFGSU 2 aide-soignante · attestation gestes et soins d'urgence aide-soignant
- **Requêtes conversationnelles (GEO)** : Un aide-soignant doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un aide-soignant ? · Que faire en cas de fausse route en EHPAD ?
- **Design** : préfixe CSS `as-`, polices Work Sans, structure : hero image à gauche / texte à droite, section « une journée type »
- **Placeholders médias** :
  - `hero` (image, 4 / 5) : aide-soignante en tunique, accroupie près d'une résidente assise au sol dans une chambre d'EHPAD, main posée sur son épaule, en train d'évaluer la situation.
  - `pratique-mannequin` (image, 4 / 3) : aide-soignant réalisant un massage cardiaque sur mannequin posé sur un lit médicalisé abaissé, planche de massage glissée dessous.
  - `groupe-formation` (image, 4 / 3) : groupe de 10 aides-soignants en formation, la formatrice montre la manœuvre de Heimlich sur un stagiaire volontaire.
  - `materiel` (image, 4 / 3) : chariot d'urgence d'EHPAD, aspirateur de mucosités, lecteur de glycémie, défibrillateur de formation.
  - `situation-metier` (image, 4 / 3) : aide-soignant à domicile, aidant un patient âgé à s'asseoir au bord du lit, mallette de soins posée à côté.
  - `video-1` (vidéo 16/9) : **Fausse route au repas : les gestes qui débloquent**. En salle à manger d'EHPAD, une résidente s'étouffe. La vidéo montre la toux encouragée, les claques dans le dos, les compressions abdominales et l'alerte.
  - `video-2` (vidéo 16/9) : **Résident retrouvé au sol : bilan avant relevage**. Que regarder, que demander, quand appeler et comment relever sans se blesser : la séquence complète, commentée par une formatrice.

### 08-infirmiers · Formations AFGSU 2 - Infirmiers

- **Dossier** : `metiers/08-infirmiers/index.html`
- **`<title>`** (59 car.) : Formations AFGSU 2 - Infirmiers | Hôpital et libéral, 385 €
- **Meta description** (142 car.) : AFGSU 2 infirmier : chariot d'urgence, arrêt cardiaque, anaphylaxie, urgences à domicile. 21 h sur 3 jours, 385 € TTC. Réservez votre session.
- **Mot-clé principal** : formation AFGSU 2 infirmier
- **Mots-clés secondaires** : AFGSU 2 infirmier prix · AFGSU 2 infirmier libéral · renouvellement AFGSU 2 infirmier · recyclage AFGSU 2 IDE · AFGSU 2 infirmier obligatoire · AFGSU 2 infirmier Paris / Lyon / Marseille · attestation gestes et soins d'urgence infirmier
- **Requêtes conversationnelles (GEO)** : Un infirmier doit-il renouveler son AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un infirmier ? · L'AFGSU 2 est-elle utile pour un infirmier libéral ?
- **Design** : préfixe CSS `ide-`, polices Roboto / Roboto Slab, structure : hero avec comparatif hôpital / libéral en onglets CSS
- **Placeholders médias** :
  - `hero` (image, 16 / 10) : infirmière en tenue hospitalière ouvrant le tiroir d'un chariot d'urgence, collègue en arrière-plan qui prépare le défibrillateur près d'un lit.
  - `pratique-mannequin` (image, 4 / 3) : infirmier ventilant un mannequin au ballon autoremplisseur à valve unidirectionnelle (BAVU) pendant qu'une collègue masse.
  - `groupe-formation` (image, 4 / 3) : groupe d'infirmiers hospitaliers et libéraux en débriefing autour d'un tableau, scénario d'anaphylaxie détaillé.
  - `materiel` (image, 4 / 3) : sacoche d'infirmier libéral ouverte sur une table de salon : masque de poche, gants, stylo d'adrénaline de démonstration, saturomètre.
  - `situation-metier` (image, 4 / 3) : infirmière libérale au domicile d'un patient âgé, téléphone à l'oreille, main sur le pouls du patient allongé sur le canapé.
  - `video-1` (vidéo 16/9) : **Arrêt cardiaque en chambre : les trois premières minutes en service**. Appel, massage, chariot, défibrillateur, répartition des rôles avant l'arrivée de l'équipe de réanimation. Simulation en chambre filmée en continu.
  - `video-2` (vidéo 16/9) : **Infirmier libéral : réaction anaphylactique au domicile après une injection**. Reconnaître l'anaphylaxie, appeler le 15, positionner le patient, appliquer le protocole d'urgence. Reconstitution commentée.

### 09-pharmaciens · Formations AFGSU 2 - Pharmaciens

- **Dossier** : `metiers/09-pharmaciens/index.html`
- **`<title>`** (54 car.) : Formations AFGSU 2 - Pharmaciens | Officine, 385 € TTC
- **Meta description** (140 car.) : AFGSU 2 pharmacien : malaise au comptoir, anaphylaxie après vaccination, arrêt cardiaque devant l'officine. 3 jours, 385 € TTC. Inscription.
- **Mot-clé principal** : AFGSU 2 pharmacien
- **Mots-clés secondaires** : formation AFGSU 2 pharmacien d'officine · AFGSU 2 pharmacie vaccination · AFGSU 2 préparateur en pharmacie · AFGSU 2 pharmacien prix · renouvellement AFGSU 2 pharmacien · AFGSU 2 pharmacien Lyon / Paris / Nice · attestation gestes et soins d'urgence pharmacien
- **Requêtes conversationnelles (GEO)** : Un pharmacien doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un pharmacien ? · Que faire en cas de réaction allergique après une vaccination en pharmacie ?
- **Design** : préfixe CSS `phar-`, polices Manrope (600 max), structure : page en sections numérotées (1, 2, 3…)
- **Placeholders médias** :
  - `hero` (image, 16 / 9) : comptoir d'officine : un pharmacien en blouse fait le tour du comptoir pour soutenir un client qui vacille, une préparatrice décroche le téléphone.
  - `pratique-mannequin` (image, 4 / 3) : pharmacienne réalisant un massage cardiaque sur mannequin au sol, défibrillateur ouvert à côté.
  - `groupe-formation` (image, 4 / 3) : équipe officinale (pharmaciens et préparateurs) en formation, la formatrice montre l'injection d'adrénaline avec un stylo d'entraînement.
  - `materiel` (image, 4 / 3) : espace de confidentialité de vaccination : siège, stylos d'adrénaline de démonstration, tensiomètre, fiche de conduite à tenir affichée.
  - `situation-metier` (image, 4 / 3) : trottoir devant une pharmacie, pharmacien agenouillé auprès d'un passant au sol, défibrillateur mural de la pharmacie ouvert.
  - `video-1` (vidéo 16/9) : **Vaccination à l'officine : reconnaître l'anaphylaxie dans les 15 minutes**. Pendant la surveillance post-vaccinale, une patiente se plaint de démangeaisons puis de gêne respiratoire. Les signes, la position, l'adrénaline, l'appel au 15.
  - `video-2` (vidéo 16/9) : **Arrêt cardiaque sur le trottoir : l'équipe officinale en action**. Un passant s'effondre devant la vitrine. Qui sort, qui appelle, qui apporte le défibrillateur, qui gère la file d'attente : démonstration chronométrée.

### 10-sages-femmes · Formations AFGSU 2 - Sages-femmes

- **Dossier** : `metiers/10-sages-femmes/index.html`
- **`<title>`** (51 car.) : Formations AFGSU 2 - Sages-femmes | 21 h, 385 € TTC
- **Meta description** (140 car.) : AFGSU 2 sage-femme : accouchement inopiné, hémorragie du post-partum, réanimation du nouveau-né. 3 jours, 385 € TTC. Réservez votre session.
- **Mot-clé principal** : AFGSU 2 sage-femme
- **Mots-clés secondaires** : formation AFGSU 2 sage-femme · AFGSU 2 sage-femme libérale · renouvellement AFGSU 2 sage-femme · AFGSU 2 sage-femme prix · urgences obstétricales formation · AFGSU 2 sage-femme Lyon / Paris / Montpellier · attestation gestes et soins d'urgence sage-femme
- **Requêtes conversationnelles (GEO)** : Une sage-femme doit-elle faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour une sage-femme ? · L'AFGSU 2 couvre-t-elle l'hémorragie du post-partum ?
- **Design** : préfixe CSS `sf-`, polices Libre Franklin / Libre Baskerville, structure : hero éditorial (citation + texte), mise en page type magazine sobre
- **Placeholders médias** :
  - `hero` (image, 3 / 4) : portrait sobre d'une sage-femme en tenue de salle de naissance, mannequin d'accouchement en arrière-plan flou, lumière naturelle.
  - `pratique-mannequin` (image, 4 / 3) : réanimation d'un mannequin nouveau-né sur table de réanimation chauffante : ventilation au masque, pouce sur le sternum.
  - `groupe-formation` (image, 4 / 3) : groupe de sages-femmes autour d'un simulateur d'accouchement, formatrice qui commente la délivrance.
  - `materiel` (image, 4 / 3) : kit d'accouchement inopiné déplié : champs stériles, clamps, ciseaux, bonnet, couverture de survie, sac de recueil gradué.
  - `situation-metier` (image, 4 / 3) : sage-femme libérale à domicile, accroupie près d'une femme enceinte allongée sur le côté gauche, téléphone à la main.
  - `video-1` (vidéo 16/9) : **Accouchement inopiné hors maternité : les gestes, dans l'ordre**. Reconstitution sur simulateur d'un accouchement à domicile : appel au 15, installation, accueil de l'enfant, clampage, surveillance de la mère.
  - `video-2` (vidéo 16/9) : **Hémorragie du post-partum : les premières minutes**. Quantifier les pertes, masser l'utérus, alerter, préparer l'équipe : le scénario de simulation filmé avec débriefing.

### 11-chirurgiens-dentistes · Formations AFGSU 2 - Chirurgiens-dentistes

- **Dossier** : `metiers/11-chirurgiens-dentistes/index.html`
- **`<title>`** (54 car.) : Formations AFGSU 2 - Chirurgiens-dentistes | 385 € TTC
- **Meta description** (143 car.) : AFGSU 2 chirurgien-dentiste : syncope, angor, anaphylaxie, inhalation au cabinet. Formez-vous et votre équipe. 21 h, 385 € TTC. Contactez-nous.
- **Mot-clé principal** : AFGSU 2 chirurgien-dentiste
- **Mots-clés secondaires** : formation AFGSU 2 dentiste · AFGSU 2 chirurgien-dentiste prix · urgences au cabinet dentaire formation · trousse d'urgence cabinet dentaire · renouvellement AFGSU 2 dentiste · AFGSU 2 dentiste Paris / Lyon / Bordeaux · attestation gestes et soins d'urgence chirurgien-dentiste
- **Requêtes conversationnelles (GEO)** : Un chirurgien-dentiste doit-il faire l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un chirurgien-dentiste ? · Que doit contenir la trousse d'urgence d'un cabinet dentaire ?
- **Design** : préfixe CSS `cd-`, polices DM Sans / DM Serif Display (titres de taille modérée), structure : hero premium discret, encart « formez tout votre cabinet »
- **Placeholders médias** :
  - `hero` (image, 16 / 10) : cabinet dentaire haut de gamme, lumière douce : le praticien et son assistante en tenue, chariot d'urgence ouvert près du fauteuil, cadrage sobre.
  - `pratique-mannequin` (image, 4 / 3) : chirurgien-dentiste ventilant un mannequin au masque avec oxygène, assistante aux compressions.
  - `groupe-formation` (image, 4 / 3) : équipe complète d'un cabinet (praticiens, assistantes, secrétaire) en formation dans la salle d'attente transformée en salle de cours.
  - `materiel` (image, 4 / 3) : trousse d'urgence dentaire rangée par compartiments étiquetés : oxygène, masque, adrénaline de démonstration, bronchodilatateur, sucre, trinitrine factice.
  - `situation-metier` (image, 4 / 3) : patient au fauteuil, main sur la poitrine, le praticien interrompt le soin et l'assistante apporte l'oxygène.
  - `video-1` (vidéo 16/9) : **Syncope ou angor au fauteuil : faire la différence en une minute**. Deux scénarios filmés au cabinet, côte à côte : les signes qui orientent, la position, l'oxygène, la trinitrine si prescrite, le moment d'appeler le 15.
  - `video-2` (vidéo 16/9) : **Former tout le cabinet : une demi-journée de simulation en équipe**. Le praticien dirige, l'assistante apporte la trousse, la secrétaire appelle le 15 et guide les secours. Images d'une session réalisée sur site.

### 12-medecins · Formations AFGSU 2 - Médecins

- **Dossier** : `metiers/12-medecins/index.html`
- **`<title>`** (57 car.) : Formations AFGSU 2 - Médecins | Cabinet, SSE, NRBC, 385 €
- **Meta description** (142 car.) : AFGSU 2 médecin : arrêt cardiaque au cabinet, douleur thoracique, détresse respiratoire, SSE et NRBC. 21 h, 385 € TTC. Programme détaillé ici.
- **Mot-clé principal** : AFGSU 2 médecin
- **Mots-clés secondaires** : formation AFGSU 2 médecin généraliste · AFGSU 2 médecin prix · renouvellement AFGSU 2 médecin · urgences au cabinet médical formation · AFGSU 2 maison de santé · AFGSU 2 médecin Paris / Lyon / Toulouse · formation situations sanitaires exceptionnelles médecin · attestation gestes et soins d'urgence médecin
- **Requêtes conversationnelles (GEO)** : Un médecin doit-il renouveler son AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un médecin ? · Quel matériel d'urgence au cabinet médical ?
- **Design** : préfixe CSS `med-`, polices Public Sans, structure : page dense et factuelle, tableau récapitulatif en haut, FAQ technique
- **Placeholders médias** :
  - `hero` (image, 16 / 9) : cabinet de médecine générale, médecin agenouillé auprès d'un mannequin au sol, défibrillateur ouvert, bureau et table d'examen en arrière-plan.
  - `pratique-mannequin` (image, 4 / 3) : deux médecins en simulation : l'un ventile au BAVU, l'autre lit le tracé du défibrillateur.
  - `groupe-formation` (image, 4 / 3) : salle de formation, médecins autour d'une table avec un plan de crise ORSAN projeté, exercice de tabletop.
  - `materiel` (image, 4 / 3) : matériel d'urgence d'un cabinet : DAE, bouteille d'oxygène, BAVU adulte et enfant, adrénaline de démonstration, ECG portable.
  - `situation-metier` (image, 4 / 3) : stagiaires en tenue de protection NRBC pendant un exercice de décontamination simulée.
  - `video-1` (vidéo 16/9) : **Arrêt cardiaque au cabinet : de la reconnaissance au relais SMUR**. Simulation en temps réel dans un cabinet : appel, RCP, analyse du DAE, voie d'abord, transmission structurée à l'équipe SMUR. Débriefing commenté.
  - `video-2` (vidéo 16/9) : **Situations sanitaires exceptionnelles : la place du médecin de ville**. Exercice de crise sur table : déclenchement ORSAN, afflux de patients en MSP, suspicion de contamination chimique. Ce que l'on attend des soignants libéraux.

### 13-kine-ergo-orthophonistes · Formations AFGSU 2 - Masseurs-kinésithérapeutes (kiné, ergo, orthophoniste)

- **Dossier** : `metiers/13-kine-ergo-orthophonistes/index.html`
- **`<title>`** (60 car.) : Formations AFGSU 2 - Masseurs-kinésithérapeutes, ergo, ortho
- **Meta description** (139 car.) : AFGSU 2 kiné, ergothérapeute, orthophoniste : malaise à l'effort, chute, fausse route, arrêt cardiaque en salle. 21 h, 385 € TTC. Réservez.
- **Mot-clé principal** : formation AFGSU 2 kinésithérapeute
- **Mots-clés secondaires** : AFGSU 2 kiné prix · AFGSU 2 ergothérapeute · AFGSU 2 orthophoniste · renouvellement AFGSU 2 kinésithérapeute · AFGSU 2 masseur-kinésithérapeute obligatoire · AFGSU 2 kiné Nantes / Lyon / Marseille · attestation gestes et soins d'urgence ergothérapeute · attestation gestes et soins d'urgence orthophoniste
- **Requêtes conversationnelles (GEO)** : Un kinésithérapeute doit-il faire l'AFGSU 2 ? · Un ergothérapeute peut-il suivre l'AFGSU 2 ? · Un orthophoniste est-il concerné par l'AFGSU 2 ? · Combien coûte l'AFGSU 2 pour un kiné ?
- **Design** : préfixe CSS `reed-`, polices Mulish, structure : onglets par profession (kiné / ergo / orthophoniste) + accordéons par module
- **Placeholders médias** :
  - `hero` (image, 16 / 10) : salle de rééducation lumineuse : un kinésithérapeute soutient un patient qui se sent mal sur un vélo d'appartement, une ergothérapeute arrive avec le défibrillateur.
  - `pratique-mannequin` (image, 4 / 3) : kinésithérapeute en polo réalisant un massage cardiaque sur mannequin posé sur un tapis de rééducation.
  - `groupe-formation` (image, 4 / 3) : groupe mêlant kinés, ergothérapeutes et orthophonistes autour d'une formatrice qui montre la désobstruction des voies aériennes.
  - `materiel` (image, 4 / 3) : matériel d'un cabinet de rééducation : défibrillateur mural, saturomètre, tensiomètre, sucre, couverture de survie.
  - `situation-metier` (image, 4 / 3) : séance d'orthophonie avec un patient âgé : l'orthophoniste observe la déglutition pendant un essai alimentaire, verre d'eau gélifiée sur la table.
  - `video-1` (vidéo 16/9) : **Malaise à l'effort en salle : arrêter, évaluer, alerter**. Un patient en réadaptation cardiaque pâlit sur le tapis de marche. La vidéo montre l'arrêt de l'exercice, les signes d'alerte et l'enchaînement vers le défibrillateur.
  - `video-2` (vidéo 16/9) : **Fausse route en séance d'orthophonie**. Toux efficace ou inefficace, claques dans le dos, compressions abdominales, adaptation chez la personne en fauteuil : démonstration commentée.
