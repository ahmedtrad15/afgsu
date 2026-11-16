"""Photos et vidéos de chaque site, fournies par Ahmed (archive afgsu.zip).

Chaque entrée de PHOTOS associe une photo source à :
  - un nom de fichier SEO (sans extension) ;
  - un texte alternatif rédigé ;
  - l'emplacement (slot) du site où elle s'affiche.

Les emplacements non listés ici ne sont plus affichés.
`prepare_media.py` encode les fichiers dans metiers/NN-…/media/.
"""

# dossier de l'archive pour chaque site
FOLDERS = {
    "01": "afgsu-diplom#U00e9-en-sant#U00e9-#U00e0-l'etranger-media",
    "02": "afgsu-etudiant-en-sante-media",
    "03": "afgsu-technicien-de-labo-media",
    "04": "afgsu-ambulancier-media",
    "05": "afgsu-assistant-dentaire-media",
    "06": "afgsu-auxiliaire-de-periculture-media",
    "07": "afgsu-aide-soignant",
    "08": "afgsu-infirmier-media",
    "09": "afgsu-pharmacien-media",
    "10": "afgsu-sage-femme-media",
    "11": "afgsu-chirurgien-dentiste",
    "12": "afgsu-medecin-media",
    "13": "afgsu-kin#U00e9-media",
}

# (fichier source, nom SEO, alt, slot)
PHOTOS = {
    "01": [
        ("online-marketing-hIgeoQjS_iE-unsplash.jpg", "formation-afgsu-2-diplome-sante-etranger-medecin",
         "Médecin en blouse blanche, bras croisés, stéthoscope à la main, prêt à exercer en France", "hero"),
        ("luis-melendez-Pd4lRfKo16U-unsplash.jpg", "afgsu-2-equipe-soignante-couloir-hopital",
         "Équipe soignante en tenue qui avance dans un couloir d'hôpital", "groupe-formation"),
        ("nappy-heGTlwA705U-unsplash.jpg", "afgsu-2-diplome-etranger-dossier-patient-tablette",
         "Soignant qui consulte un dossier patient sur tablette, stéthoscope posé sur le bureau", "situation-metier"),
    ],
    "02": [
        ("vitaly-gariev-2kopEHjST-g-unsplash (1).jpg", "formation-afgsu-2-etudiants-sante-stage",
         "Deux étudiants en santé en blouse qui consultent une tablette pendant leur stage", "situation-metier"),
        ("jeshoots-com-l0j0DHVWcIE-unsplash (1).jpg", "afgsu-2-etudiante-infirmiere-tenue-stage",
         "Étudiante en tunique de stage, stéthoscope autour du cou, dans une chambre d'hôpital", "pratique-mannequin"),
        ("vitaly-gariev-eVrm8G3UhYQ-unsplash (1).jpg", "afgsu-2-etudiant-sante-consultation-patient",
         "Étudiante en médecine en consultation avec un patient âgé et un enfant", "groupe-formation"),
        ("frederick-medina-ai5uaJfRFxc-unsplash (1).jpg", "afgsu-2-etudiant-sante-revision-stethoscope",
         "Étudiant qui prend des notes, un stéthoscope posé sur son cahier", "materiel"),
    ],
    "03": [
        ("diana-hauan-YNZW7KW0uqs-unsplash (1).jpg", "formation-afgsu-2-technicienne-laboratoire",
         "Technicienne de laboratoire en blouse blanche dans un laboratoire d'analyses", "hero"),
        ("lucas-vasques-9vnACvX2748-unsplash (1).jpg", "afgsu-2-technicien-laboratoire-microscope",
         "Technicien de laboratoire en charlotte qui observe un échantillon au microscope", "pratique-mannequin"),
        ("national-institute-of-allergy-and-infectious-diseases-Cdt3s_jp1OY-unsplash (1).jpg",
         "afgsu-2-laboratoire-pipette-echantillons",
         "Mains gantées qui pipettent des échantillons dans un portoir de tubes", "materiel"),
        ("cdc-XLhDvfz0sUM-unsplash (1).jpg", "afgsu-2-laboratoire-tubes-prelevement",
         "Mains en gants violets qui manipulent des tubes de prélèvement sur un plan de travail", "situation-metier"),
    ],
    "04": [
        ("pexels-mikhail-nilov-8942627.jpg", "formation-afgsu-2-ambulanciers-intervention-nuit",
         "Deux ambulanciers en gilet réfléchissant qui prennent en charge un patient sur un brancard, de nuit, devant l'ambulance", "hero"),
        ("pexels-pavel-danilyuk-6754146 (1).jpg", "afgsu-2-ambulanciers-cellule-sanitaire",
         "Deux ambulanciers en tenue rouge dans la cellule sanitaire de l'ambulance", "pratique-mannequin"),
        ("pexels-mikhail-nilov-28123712.jpg", "afgsu-2-ambulancier-sac-urgence-brancard",
         "Ambulancière gantée qui prépare le sac d'urgence posé sur le brancard", "materiel"),
        ("pexels-mikhail-nilov-8942225.jpg", "afgsu-2-ambulancier-radio-alerte",
         "Ambulancier au volant qui transmet un bilan par radio", "situation-metier"),
    ],
    "05": [
        ("pexels-olly-3881292.jpg", "formation-afgsu-2-assistante-dentaire-cabinet",
         "Assistante dentaire et praticienne au travail dans un cabinet dentaire lumineux", "hero"),
        ("pexels-tima-miroshnichenko-5355928.jpg", "afgsu-2-assistante-dentaire-aspiration",
         "Assistante dentaire qui tient l'aspiration pendant que le praticien soigne une patiente", "situation-metier"),
        ("pexels-shvetsa-3845951.jpg", "afgsu-2-assistante-dentaire-soin-fauteuil",
         "Praticienne et assistante masquées autour d'un patient au fauteuil", "pratique-mannequin"),
        ("pexels-gustavo-fring-5622035.jpg", "afgsu-2-cabinet-dentaire-microscope",
         "Deux professionnelles en tunique qui travaillent au microscope opératoire du cabinet", "materiel"),
    ],
    "06": [
        ("pexels-kseniachernaya-8537196.jpg", "formation-afgsu-2-auxiliaire-puericulture-enfant",
         "Auxiliaire de puériculture qui accompagne une petite fille pendant une activité en crèche", "hero"),
        ("gabe-pierce-mLqWFEtlIEs-unsplash.jpg", "afgsu-2-auxiliaire-puericulture-activite-dessin",
         "Adulte qui dessine avec un jeune enfant assis à une petite table", "situation-metier"),
    ],
    "07": [
        ("age-cymru-dMhB7w99ju8-unsplash (1).jpg", "formation-afgsu-2-aide-soignante-residente-ehpad",
         "Aide-soignante souriante penchée vers une résidente âgée en EHPAD", "hero"),
        ("maria-luisa-queiroz-KlBltbAwxWk-unsplash (1).jpg", "afgsu-2-aide-soignante-chambre-patient",
         "Aide-soignante en tunique bleu marine qui se penche vers un patient alité", "situation-metier"),
        ("jeshoots-com-l0j0DHVWcIE-unsplash (1).jpg", "afgsu-2-aide-soignant-tenue-service",
         "Soignante en tunique blanche, stéthoscope autour du cou, dans un service hospitalier", "groupe-formation"),
    ],
    "08": [
        ("hush-naidoo-jade-photography-ZCO_5Y29s8k-unsplash (1).jpg", "formation-afgsu-2-infirmiere-couloir-hopital",
         "Infirmière en tenue bleue qui pousse une couveuse dans un couloir d'hôpital", "situation-metier"),
        ("julia-taubitz-vN5s_G5SPkY-unsplash (1).jpg", "afgsu-2-infirmier-prise-tension",
         "Infirmière qui prend la tension artérielle d'un patient", "pratique-mannequin"),
        ("nappy-6LV3V1gLrP8-unsplash (1).jpg", "afgsu-2-infirmier-tenue-stethoscope",
         "Infirmier en tenue de soins bleue, stéthoscope autour du cou", "materiel"),
    ],
    "09": [
        ("national-cancer-institute-NNpo-liY5aU-unsplash.jpg", "formation-afgsu-2-pharmacien-officine-patiente",
         "Pharmacien en blouse qui conseille une patiente au comptoir de l'officine", "hero"),
        ("national-cancer-institute-byGTytEGjBo-unsplash.jpg", "afgsu-2-pharmacienne-rayonnage-officine",
         "Pharmacienne souriante qui attrape une boîte dans les rayonnages", "pratique-mannequin"),
        ("national-cancer-institute-fTQHPb6r4wQ-unsplash.jpg", "afgsu-2-pharmacien-reserve-medicaments",
         "Pharmacien en blouse dans l'allée de la réserve de médicaments", "situation-metier"),
    ],
    "10": [
        ("pexels-jonathanborba-19357671.jpg", "formation-afgsu-2-sage-femme-nouveau-ne",
         "Sage-femme qui tient un nouveau-né près du lit de la mère, en maternité", "hero"),
        ("pexels-karola-g-5206934.jpg", "afgsu-2-sage-femme-tenue-stethoscope",
         "Sage-femme en tenue verte, stéthoscope autour du cou", "situation-metier"),
    ],
    "11": [
        ("soybreno-z8BIWPwV3zo-unsplash.jpg", "formation-afgsu-2-chirurgien-dentiste-cabinet",
         "Chirurgienne-dentiste en tenue bleue qui règle l'éclairage au-dessus d'une patiente", "hero"),
        ("shedrack-salami-sS6qV__PFR4-unsplash.jpg", "afgsu-2-chirurgien-dentiste-assistante-soin",
         "Chirurgien-dentiste et assistante en tenue qui soignent ensemble un patient", "situation-metier"),
        ("lafayett-zapata-montero-loBRFqXm1QA-unsplash.jpg", "afgsu-2-chirurgien-dentiste-instruments",
         "Gros plan sur des instruments dentaires pendant un soin au fauteuil", "materiel"),
    ],
    "12": [
        ("vitaly-gariev-XqMo4OlBnh0-unsplash.jpg", "formation-afgsu-2-medecin-cabinet",
         "Médecin généraliste en blouse, bras croisés, dans son cabinet", "hero"),
        ("vitaly-gariev-iyeUwItlIPk-unsplash.jpg", "afgsu-2-medecin-consultation-patient",
         "Médecin en consultation avec un patient, à son bureau", "pratique-mannequin"),
        ("vitaly-gariev-8WYkI3cEZm8-unsplash.jpg", "afgsu-2-medecin-ordonnance",
         "Médecin qui remplit un document sur un porte-bloc face à un patient", "groupe-formation"),
        ("patty-brito-Y-3Dt0us7e0-unsplash.jpg", "afgsu-2-medecin-stethoscope-coeur",
         "Soignante qui tient un stéthoscope formant un cœur", "materiel"),
    ],
    "13": [
        ("pexels-yankrukov-5794033.jpg", "formation-afgsu-2-kinesitherapeute-seance",
         "Kinésithérapeute qui traite une patiente allongée sur la table de soin", "hero"),
        ("pexels-funkcines-terapijos-centras-927573878-20860618.jpg", "afgsu-2-kinesitherapeute-patient",
         "Rééducatrice en tunique qui se penche vers un patient pendant une séance", "situation-metier"),
    ],
}

# vidéo verticale (courte) de chaque site : (fichier source, nom SEO, titre, description)
VIDEOS = {
    "01": ("DIGIVODA_AFGSU2_SNAP_13_DIPLOME_ETRANGER.mp4", "video-afgsu-2-diplome-sante-etranger",
           "L'AFGSU 2, obligatoire pour exercer en France",
           "En quelques secondes : pourquoi un diplômé en santé à l'étranger doit valider l'AFGSU 2."),
    "02": ("DIGIVODA_AFGSU2_SNAP_12_ETUDIANT_SANTE.mp4", "video-afgsu-2-etudiant-sante",
           "Étudiant en santé : l'AFGSU 2 est obligatoire",
           "Le rappel en vidéo courte : l'AFGSU 2 fait partie de votre cursus."),
    "03": ("DIGIVODA_AFGSU2_SNAP_11_TECHNICIEN_LABO.mp4", "video-afgsu-2-technicien-laboratoire",
           "Prises de sang : l'AFGSU 2 pour les techniciens de laboratoire",
           "Pourquoi l'AFGSU 2 est exigée des techniciens qui réalisent des prélèvements."),
    "04": ("DIGIVODA_AFGSU2_SNAP_10_AMBULANCIER.mp4", "video-afgsu-2-ambulancier",
           "Ambulancier : votre AFGSU 2 doit être à jour",
           "Le rappel en vidéo courte : l'AFGSU 2 se renouvelle tous les 4 ans."),
    "05": ("DIGIVODA_AFGSU2_SNAP_09_ASSISTANT_DENTAIRE.mp4", "video-afgsu-2-assistante-dentaire",
           "Assistante dentaire : l'AFGSU 2 est obligatoire",
           "En quelques secondes : l'AFGSU 2 au cabinet dentaire."),
    "06": ("DIGIVODA_AFGSU2_SNAP_07_AUXILIAIRE_PUERICULTURE.mp4", "video-afgsu-2-auxiliaire-puericulture",
           "Auxiliaire de puériculture : l'AFGSU 2 est obligatoire",
           "Le rappel en vidéo courte, gestes sur mannequin à l'appui."),
    "07": ("DIGIVODA_AFGSU2_SNAP_06_AIDE_SOIGNANT.mp4", "video-afgsu-2-aide-soignant",
           "Aide-soignant : l'AFGSU 2 est obligatoire",
           "En quelques secondes : l'AFGSU 2 pour les aides-soignants."),
    "08": ("DIGIVODA_AFGSU2_SNAP_05_INFIRMIER.mp4", "video-afgsu-2-infirmier",
           "Infirmier : l'AFGSU 2 est obligatoire",
           "Le rappel en vidéo courte : ventilation et massage cardiaque en formation."),
    "09": ("DIGIVODA_AFGSU2_SNAP_04_PHARMACIEN.mp4", "video-afgsu-2-pharmacien",
           "Pharmacien : l'AFGSU 2, c'est obligatoire",
           "En quelques secondes : l'AFGSU 2 pour les pharmaciens d'officine."),
    "10": ("DIGIVODA_AFGSU2_SNAP_03_SAGE_FEMME.mp4", "video-afgsu-2-sage-femme",
           "Sage-femme : l'AFGSU 2 est obligatoire",
           "Le rappel en vidéo courte, sur mannequin en formation."),
    "11": ("DIGIVODA_AFGSU2_SNAP_02_CHIRURGIEN_DENTISTE.mp4", "video-afgsu-2-chirurgien-dentiste",
           "Chirurgien-dentiste : l'AFGSU 2 est obligatoire pour vous",
           "En quelques secondes : l'AFGSU 2 pour les chirurgiens-dentistes."),
    "12": ("DIGIVODA_AFGSU2_SNAP_01_MEDECIN.mp4", "video-afgsu-2-medecin",
           "Médecin : l'AFGSU 2 est obligatoire",
           "Le rappel en vidéo courte : l'AFGSU 2 pour les médecins."),
    "13": ("DIGIVODA_AFGSU2_SNAP_08_PARAMEDICAUX.mp4", "video-afgsu-2-kine-ergo-orthophoniste",
           "Kinés, ergos, orthophonistes : l'AFGSU 2 est obligatoire",
           "En quelques secondes : l'AFGSU 2 pour les professions de rééducation."),
}

# grandes villes affichées sur la carte de France (longitude, latitude), sans les nommer dans le texte
MAP_CITIES = [
    (2.35, 48.86), (4.84, 45.76), (5.37, 43.30), (1.44, 43.60), (7.26, 43.71), (-1.55, 47.22),
    (3.88, 43.61), (7.75, 48.58), (-0.58, 44.84), (3.06, 50.63), (-1.68, 48.11), (4.03, 49.26),
    (5.72, 45.19), (5.04, 47.32), (3.08, 45.78), (1.10, 49.44), (0.69, 47.39), (-4.49, 48.39),
    (1.26, 45.83), (6.18, 49.12), (0.34, 46.58), (5.93, 43.12), (2.30, 49.89), (-0.37, 49.18),
]
