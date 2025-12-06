sts
# ------------------------------
# 1) Initialisation de l'embedder
# ------------------------------
embedder = TextEmbedder("all-MiniLM-L6-v2")


def get_embedding(text: str):
return embedder.embed(text).tolist()


# ------------------------------
# 2) Récupération des PDFs depuis GitHub
# ------------------------------
def list_github_pdfs(folder_url: str):
# GitHub ne fournit pas d'API pour lister un dossier brut → nécessite liste manuelle OU API GitHub
# Pour un vrai cas : utiliser l'API GitHub
raise NotImplementedError("Fourni-moi la liste exacte des PDF ou le lien API GitHub.")


# ------------------------------
# 3) Ingestion d'un ensemble de PDFs
# ------------------------------
def ingest_pdfs(pdf_urls: list[str]):
texts = []


for i, url in enumerate(pdf_urls):
print(f"Téléchargement : {url}")
pdf_bytes = download_pdf(url)
text = extract_text_from_pdf(pdf_bytes)
text = clean_text(text)
texts.append((i, text))


# Création collection Qdrant
vector_size = len(get_embedding("test"))
create_collection_if_not_exists(vector_size)


# Insertion des documents
for doc_id, text in texts:
vector = get_embedding(text)
insert_document(doc_id, vector, text)
print(f"Document {doc_id} inséré.")


print("Ingestion terminée.")


# ------------------------------
# 4) Exemple de recherche
# ------------------------------
def run_search(query: str):
q_vec = get_embedding(query)
results = semantic_search(q_vec, limit=3)
for r in results:
print("→ Score:", r.score)
print("Texte extrait:", r.payload["text"][:300], "...\n")




if __name__ == "__main__":
# Exemple : liste de PDFs hébergés sur GitHub
pdf_urls = [
GITHUB_PDF_FOLDER + "fichier1.pdf",
GITHUB_PDF_FOLDER + "fichier2.pdf",
GITHUB_PDF_FOLDER + "fichier3.pdf",
]


ingest_pdfs(pdf_urls)


print("\nRecherche d'exemple :")
run_search("éducation canine")
