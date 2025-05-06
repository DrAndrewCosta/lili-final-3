# Painel Lili – Assistente de Laudos com Voz

Este projeto permite gerar laudos médicos com auxílio de comandos de voz, preenchimento automático e exportação em .docx com base em templates formatados.

## ✅ Funcionalidades

- Comandos de voz com ativação por "Lili"
- Campos de cabeçalho clínico interativos
- Integração com CSVs de frases clínicas
- Pré-visualização do laudo em tempo real
- Exportação em `.docx` mantendo o layout original dos templates
- Suporte a upload de templates e frases

## ▶️ Como executar

### Local (via Streamlit)
```bash
pip install -r requirements.txt
streamlit run app_online.py
```

### Docker
```bash
docker build -t painel-lili .
docker run -p 8501:8501 painel-lili
```

## 📁 Estrutura de Pastas

- `templates/`: arquivos .docx formatados
- `aprendizado/`, `logs/`, `backups/`: dados internos
- `frases.csv`: base de frases clínicas acionadas por voz

---