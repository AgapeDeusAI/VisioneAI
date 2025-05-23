import json
import os

class VisioneAI:
    def __init__(self, file_log="log_visioni.json"):
        self.file_log = file_log
        self.log = self._carica_log()

    def _carica_log(self):
        if os.path.exists(self.file_log):
            with open(self.file_log, "r") as f:
                return json.load(f)
        return []

    def registra_visione(self, oggetto: str, descrizione: str):
        nuova_voce = {
            "oggetto": oggetto,
            "descrizione": descrizione
        }
        self.log.append(nuova_voce)
        self._salva_log()

    def _salva_log(self):
        with open(self.file_log, "w") as f:
            json.dump(self.log, f, indent=2)

    def get_log(self):
        return self.log