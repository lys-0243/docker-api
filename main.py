from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API Formation Docker")


class Texte(BaseModel):
    texte: str


@app.get("/")
def accueil():
    return {
        "message": "Bienvenue sur notre API !",
        "statut": "en ligne"
    }


@app.post("/analyse")
def analyser(donnees: Texte):
    texte = donnees.texte.lower()

    mots_positifs = ["super", "excellent", "adore"]

    if any(mot in texte for mot in mots_positifs):
        sentiment = "positif"
    else:
        sentiment = "indetermine"

    return {
        "texte": donnees.texte,
        "sentiment": sentiment
    }