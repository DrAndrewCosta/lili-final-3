
import pandas as pd
from lili_voz_comandos import LiliComandosVoz

df = pd.read_csv("frases.csv")
lili = LiliComandosVoz(df)

comandos = [
    "lili, nódulo hepático",
    "lili, limpar laudo",
    "lili, salvar",
    "lili, desfazer",
    "lili, alteração que não existe"
]

texto_laudo = ""

for comando in comandos:
    texto_laudo, mensagem, acao = lili.processar_comando(comando, texto_laudo)
    print(f"Comando: {comando}")
    print(f"Mensagem: {mensagem}")
    print(f"Texto Atual:\n{texto_laudo}")
    print("-" * 40)
