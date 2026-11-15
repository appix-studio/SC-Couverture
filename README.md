# SC Couverture – maquette de refonte

Maquette de proposition réalisée par APPIX STUDIO.

## Lancer

Ouvrir `index.html` dans un navigateur. Aucune dépendance à installer.
`python3 build.py` génère `dist/sc-couverture-maquette.html` (fichier unique, images incluses) et `dist/sc-couverture-projet.zip`.

## Structure

- `index.html` : sections de la page (hero, entreprise, prestations, avantages, réalisations, étapes, avis, zone, FAQ, contact, pied de page)
- `css/styles.css` : variables de couleurs et de typographie en tête de fichier
- `js/main.js` : animations au scroll, menu mobile, galerie, validation du formulaire
- `assets/img` : photos issues du site actuel et logo

## Contenus provisoires (repères orange « Provisoire »)

- Textes de présentation de l'entreprise et de la section « Pourquoi SC Couverture » : reformulés à partir du site actuel, à valider avec le dirigeant
- Les trois avis clients : emplacements à remplacer par de vrais avis Google
- Liste des communes desservies, mentions légales, politique de confidentialité
- Formulaire : renseigner `data-endpoint` sur la balise `<form id="quote">` pour l'envoyer à un service de messagerie

## Référencement de base

- Titre de page, meta description, balises Open Graph et données structurées (RoofingContractor) dans `<head>`
- Un seul `<h1>` avec le métier et la ville, puis un `<h2>` par section et des `<h3>` pour les cartes
- Textes alternatifs descriptifs sur toutes les photos
- À définir à la mise en ligne : URL canonique, image de partage (og:image), plan du site et fiche Google
- Adresse postale reprise de la fiche Google : à confirmer avec l'entreprise

## À vérifier

- 77 avis Google et note de 5/5 : à contrôler sur la fiche Google
- Photos : issues de captures d'écran, à remplacer par les originaux en haute définition
- Polices Fraunces et Inter chargées depuis Google Fonts
