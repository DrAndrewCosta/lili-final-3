
# app_online_FINAL_PRONTO.py
# Versão com escuta contínua, timeout após "Lili", abas recolhíveis, botão ON/OFF, datas dd/mm/aaaa

import streamlit as st
import pandas as pd
import os
from datetime import datetime
from lili_voz_comandos import processar_comando_por_voz

st.set_page_config(layout="wide")

# Controle ON/OFF
if "voz_ativada" not in st.session_state:
    st.session_state.voz_ativada = True

st.sidebar.markdown("### 🎙️ Modo Voz")
st.sidebar.checkbox("Lili ON", value=st.session_state.voz_ativada, key="voz_ativada")

# Cabeçalho Clínico
with st.sidebar.expander("🩺 Cabeçalho Clínico", expanded=True):
    nome = st.text_input("Nome do Paciente")
    dn = st.date_input("Data de Nascimento", format="DD/MM/YYYY")
    medico = st.text_input("Médico Solicitante")
    data_exame = st.date_input("Data do Exame", format="DD/MM/YYYY")

# Upload de CSV
with st.sidebar.expander("📁 Upload de CSV"):
    csv_file = st.file_uploader("Envie um novo CSV", type="csv")
    if csv_file:
        df_base = pd.read_csv(csv_file, sep="|")
        st.success("Novo CSV carregado.")
    else:
        df_base = pd.read_csv("frases.csv", sep="|") if os.path.exists("frases.csv") else pd.DataFrame(columns=["nome_da_alteracao", "frase"])

# Busca Manual de Frases
with st.expander("🔍 Buscar e Inserir Frases"):
    termo = st.text_input("Buscar alteração...")
    resultados = df_base[df_base["nome_da_alteracao"].str.contains(termo, case=False, na=False)]
    for _, row in resultados.iterrows():
        if st.button(f"Inserir: {row['nome_da_alteracao']}"):
            st.session_state.texto_laudo += row['frase'] + "\n"

# Colunas fixas
col1, col2 = st.columns([1, 2])

with col1:
    if "texto_laudo" not in st.session_state:
        st.session_state.texto_laudo = ""

    st.text_area("📝 Laudo Interativo", value=st.session_state.texto_laudo, height=300, key="texto_laudo_area")

    if st.button("Salvar Laudo"):
        st.success("Laudo salvo!")

with col2:
    st.markdown("### 📄 Pré-visualização do Laudo")
    st.markdown(st.session_state.texto_laudo.replace("\n", "  
"))

# Script de escuta contínua (após "Lili", timeout de 10s, volta para escuta passiva)
st.markdown("""
<script>
let recognition;
let isListening = false;
let timeoutId;

function startRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.continuous = true;
    recognition.lang = 'pt-BR';

    recognition.onresult = function(event) {
        const transcript = event.results[event.results.length - 1][0].transcript.trim().toLowerCase();
        if (transcript.includes("lili")) {
            window.parent.postMessage({type: 'WAKE_WORD', command: transcript }, "*");

            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => {
                window.parent.postMessage({ type: 'VOICE_TIMEOUT' }, '*');
            }, 10000);
        }
    };

    recognition.onerror = function(event) {
        console.error("Erro no reconhecimento:", event);
    };

    recognition.onend = function() {
        if (isListening) recognition.start(); // reinicia
    };

    recognition.start();
    isListening = true;
}

window.addEventListener("load", function() {
    startRecognition();
});
</script>
""", unsafe_allow_html=True)
