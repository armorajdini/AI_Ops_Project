from enum import Enum
from fastapi import FastAPI, Query
import random
from typing import Dict, List

# --- Stimmung als Enum (Dropdown in Swagger) ---
class Stimmung(str, Enum):
    muede = "müde"
    gestresst = "gestresst"
    fit = "fit"

# --- Sprüche-Datenbasis ---
SPRUECHE: Dict[str, List[str]] = {
    "müde": [
        "Auch kleine Schritte bringen dich ans Ziel.",
        "Ruhe ist Teil des Fortschritts – lade heute auf.",
        "Du musst nicht schnell sein, nur dranbleiben."
    ],
    "gestresst": [
        "Atme tief durch – du bist stärker als der Stress.",
        "Ordnung im Kopf bringt Ruhe im Herzen.",
        "Heute Fokus auf das Wesentliche – der Rest darf warten."
    ],
    "fit": [
        "Nutze deine Energie – heute setzt du ein Statement!",
        "Konstanz schlägt Intensität – weiter so!",
        "Dein Einsatz heute zahlt sich morgen aus."
    ],
}

app = FastAPI(title="Motivation API", version="0.2.0")

# GET mit Query-Parameter -> Swagger zeigt Dropdown & kein Body nötig
@app.get("/motivation", summary="Gib mir einen Spruch zur gewählten Stimmung")
def motivation(stimmung: Stimmung = Query(..., description="Wähle deine Stimmung")):
    gruppe = stimmung.value
    spruch = random.choice(SPRUECHE[gruppe])
    return {"stimmung": gruppe, "spruch": spruch}