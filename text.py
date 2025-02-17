import datetime

# Lista para armazenar as mensagens
text_db = []


class Text:
    def __init__(self, text):
        self.text = text
        self.date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Armazena a instância na lista
        text_db.append(self)

    def __repr__(self):
        return f"{self.text} - {self.date}"
