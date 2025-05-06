
import pandas as pd

class LiliComandosVoz:
    def __init__(self, df_frases, responder_em_voz=False):
        self.df = df_frases
        self.responder_em_voz = responder_em_voz

    def processar_comando(self, comando, texto_laudo_atual):
        comando = comando.lower().replace("lili", "").strip()
        mensagem = ""
        acao = None

        if "limpar laudo" in comando:
            return "", "🧹 Laudo limpo com sucesso.", "limpar"

        elif "desfazer" in comando:
            return "", "↩️ Ação desfeita (reset do texto).", "desfazer"

        elif "salvar" in comando:
            return texto_laudo_atual, "💾 Laudo salvo (simulado).", "salvar"

        else:
            matches = self.df[self.df["nome_da_alteracao"].str.lower().str.contains(comando)]
            if not matches.empty:
                frase = matches.iloc[0]["frase"]
                novo_texto = texto_laudo_atual + "\n" + frase
                return novo_texto.strip(), f"✅ Frase adicionada ao laudo: {frase}", "adicionar"
            else:
                return texto_laudo_atual, "❓ Comando não reconhecido ou frase não encontrada.", "nenhum"
