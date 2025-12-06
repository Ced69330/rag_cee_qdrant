import os
QDRANT_URL = "https://cddd7863-0d84-4373-b822-fc0e98335ea5.europe-west3-0.gcp.cloud.qdrant.io:6333"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.tTNN0BLJB12-xV9suHCb166ewGAPBX8gSIbQRXdTp7g"
COLLECTION_NAME = "documents_pdf"
GITHUB_PDF_FOLDER = "https://github.com/Ced69330/Cee-news-scrapper-/tree/main/pdf_lettres_info_c2e"
GITHUB_TOKEN = os.getenv("TOKEN_GITHUB") # définir ce secret dans ton environnement avant de lancer le script
if GITHUB_TOKEN is None: raise ValueError("Le token GitHub n'est pas défini. Veuillez définir la variable d'environnement GITHUB_TOKEN.")
