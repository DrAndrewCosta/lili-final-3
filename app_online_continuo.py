
import streamlit as st
import pandas as pd
from lili_voz_comandos import LiliComandosVoz
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Painel Lili (Modo Manual)", layout="centered")
st.title("🎙️ Painel Lili - Modo de Escuta Manual")

df_base = pd.read_csv("frases.csv", sep="|") if os.path.exists("frases.csv") else pd.DataFrame(columns=["nome_da_alteracao", "frase"])
lili = LiliComandosVoz(df, responder_em_voz=True)

if "texto_laudo" not in st.session_state:
    st.session_state.texto_laudo = ""

st.subheader("📝 Texto do laudo (editável)")
st.session_state.texto_laudo = st.text_area("Laudo:", value=st.session_state.texto_laudo, height=400)

st.subheader("🎧 Comando por voz (manual)")
fala = st.text_input("Diga algo como: 'Lili, nódulo hepático'")

if fala and fala.lower().startswith("lili"):
    novo_laudo, mensagem, acao = lili.processar_comando(fala, st.session_state.texto_laudo)
    if mensagem:
        st.success(mensagem)
    st.session_state.texto_laudo = novo_laudo

if st.button("🎙️ Iniciar escuta por 10 segundos"):
    streamlit_js_eval(js_expressions="""
    (() => {
      const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.lang = 'pt-BR';
      let timeoutId = null;
      recognition.onstart = () => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => recognition.stop(), 10000);
      };
      recognition.onresult = (event) => {
        const result = event.results[0][0].transcript;
        if (result.toLowerCase().startsWith("lili")) {
          window.parent.postMessage({ type: 'VOICE_RESULT', result }, '*');
        }
      };
      recognition.onerror = (event) => {
        window.parent.postMessage({ type: 'VOICE_ERROR', error: event.error }, '*');
      };
      recognition.start();
    })();
    """, key="voz_manual_button", trigger=False)

st.caption("Assistente Lili - Escuta manual por voz com palavra-chave 'Lili'")
