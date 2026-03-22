# 📖 Guia de Execução - Datathon Passos Mágicos 2024

## ⏱️ Tempo Total: 5 Minutos

Este guia permite executar todo o projeto em 5 minutos com os dados corretos (2022-2024).

---

## 🚀 Passo 1: Preparação (1 minuto)

### 1.1 Clonar Repositório
```bash
git clone https://github.com/amauryanalista-ship-it/passos-magicos-datathon.git
cd datathon_project
```

### 1.2 Criar Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows
```

### 1.3 Instalar Dependências
```bash
pip install -r requirements.txt
```

---

## 📊 Passo 2: Pipeline de Processamento (3 minutos)

Execute os 5 notebooks na sequência:

### 2.1 Limpeza de Dados (15-20 segundos)
```bash
python3 notebooks/01_data_cleaning.py
```

**O que faz:**
- Consolida 3 abas do Excel (PEDE2022, PEDE2023, PEDE2024)
- Processa 3.030 registros
- Converte tipos de dados
- Trata valores faltantes
- Cria 5 features derivadas

**Saída esperada:**
```
✓ Dataset consolidado: 3030 linhas × 64 colunas
✓ Dataset completo salvo: data/df_clean.csv
✓ Dataset 2022 salvo: data/df_2022_clean.csv (860 registros)
✓ Dataset 2023 salvo: data/df_2023_clean.csv (1014 registros)
✓ Dataset 2024 salvo: data/df_2024_clean.csv (1156 registros)
```

---

### 2.2 Análise Exploratória (20-30 segundos)
```bash
python3 notebooks/02_eda_full.py
```

**O que faz:**
- Responde todas as 11 perguntas do Datathon
- Análise estatística completa
- Correlações entre indicadores
- Tendências por ano
- Distribuição de risco

**Saída esperada:**
```
✓ PERGUNTA 1: Adequação ao nível (IAN) - Analisado
✓ PERGUNTA 2: Desempenho acadêmico (IDA) - Analisado
✓ PERGUNTA 3: Engajamento (IEG) - Analisado
✓ PERGUNTA 4: Autoavaliação (IAA) - Analisado
✓ PERGUNTA 5: Aspectos psicossociais (IPS) - Analisado
✓ PERGUNTA 6: Aspectos psicopedagógicos (IPP) - Analisado
✓ PERGUNTA 7: Ponto de virada (IPV) - Analisado
✓ PERGUNTA 8: Multidimensionalidade (INDE) - Analisado
✓ PERGUNTA 9: Modelo preditivo - Próximo notebook
✓ PERGUNTA 10: Efetividade do programa - Analisado
✓ PERGUNTA 11: Insights adicionais - Analisado
```

---

### 2.3 Modelagem Preditiva (30-45 segundos) ⭐ XGBOOST
```bash
python3 notebooks/03_Modelo_Predicao.ipynb
```

**O que faz:**
- Treina XGBoost (Melhor Performance!)
- Treina Random Forest (comparação)
- Valida com 5-fold cross-validation
- Calcula métricas (acurácia, sensibilidade, ROC AUC)
- Identifica features mais importantes
- Salva 4 modelos em formato .pkl

**Saída esperada:**
```
✓ XGBoost Accuracy: 78.6% ⭐
✓ XGBoost Sensitivity: 71.0%
✓ XGBoost Specificity: 83.7%
✓ XGBoost ROC AUC: 0.8592 ⭐ MELHOR!
✓ XGBoost F1-Score: 0.7273
✓ Cross-Validation (5-fold): 0.8441 ± 0.0398
✓ Modelos salvos com sucesso!
  - risk_model_xgb.pkl (XGBoost - MELHOR)
  - risk_model_rf.pkl (Random Forest)
  - risk_model_scaler.pkl
  - risk_model_metadata.json
```

---

### 2.4 Análise Integrada (20-30 segundos)
```bash
python3 notebooks/04_comprehensive_analysis.py
```

**O que faz:**
- Integra resultados de todas as análises
- Análise por fases educacionais
- Análise de risco
- Comparações entre grupos
- Preparação de dados para visualização

**Saída esperada:**
```
✓ Análise integrada concluída com sucesso!
✓ Dados consolidados prontos para visualização
```

---

### 2.5 Geração de Gráficos (15-20 segundos) - ✨ NOVO
```bash
python3 notebooks/05_generate_charts.py
```

**O que faz:**
- Gera 8 gráficos profissionais (300 DPI)
- Gráficos prontos para apresentação PPT
- Cores corporativas aplicadas
- Salva em PNG

**Saída esperada:**
```
✓ Salvo: 01_evolucao_defasagem.png
✓ Salvo: 02_desempenho_academico.png
✓ Salvo: 03_correlacoes.png
✓ Salvo: 04_performance_modelo.png
✓ Salvo: 05_feature_importance.png
✓ Salvo: 06_distribuicao_risco.png
✓ Salvo: 07_ida_ieg_inde.png
✓ Salvo: 08_evolucao_indicadores.png
```

---

## 🎨 Passo 3: Iniciar Aplicação Web (1 minuto)

### 3.1 Iniciar Streamlit
```bash
streamlit run app/streamlit_app.py
```

**Saída esperada:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

### 3.2 Acessar Dashboard
Abra seu navegador em: **http://localhost:8501**

---

## 📊 Arquivos Gerados

Após executar todo o pipeline, você terá:

### Dados (7 arquivos CSV)
```
data/
├── df_clean.csv              # 3.030 registros consolidados
├── df_2022_clean.csv         # 860 registros
├── df_2023_clean.csv         # 1.014 registros
├── df_2024_clean.csv         # 1.156 registros
└── ... (3 arquivos adicionais)
```

### Modelos (4 arquivos)
```
models/
├── risk_model_rf.pkl         # Random Forest
├── risk_model_gb.pkl         # Gradient Boosting
├── risk_model_scaler.pkl     # StandardScaler
└── risk_model_metadata.json  # Metadados
```

### Gráficos (8 arquivos PNG - 300 DPI) - ✨ NOVO
```
presentation/charts/
├── 01_evolucao_defasagem.png
├── 02_desempenho_academico.png
├── 03_correlacoes.png
├── 04_performance_modelo.png
├── 05_feature_importance.png
├── 06_distribuicao_risco.png
├── 07_ida_ieg_inde.png
└── 08_evolucao_indicadores.png
```

### Apresentações (2 formatos - ATUALIZADO)
```
presentation/
├── APRESENTACAO_COMERCIAL.pptx  # 19 slides com gráficos
└── APRESENTACAO_COMERCIAL.pdf   # 23 slides
```

---

## 🎯 Resultados Esperados - XGBOOST ⭐

### Modelo Preditivo (XGBoost - Melhor!)
| Métrica | Valor |
|---------|-------|
| Acurácia | 78.6% |
| Sensibilidade | 71.0% |
| Especificidade | 83.7% |
| ROC AUC | 0.8592 ⭐ |
| F1-Score | 0.7273 |
| CV ROC AUC | 0.8441 ± 0.0398 |

### Distribuição de Risco
- Baixo Risco: 44.3%
- Risco Moderado: 54.2%
- Alto Risco: 1.5%

### Top 3 Features (XGBoost)
1. IAN (19.6%) - Adequação ao Nível
2. IPP (18.1%) - Suporte Pedagógico
3. INDICADORES_MEDIA (8.9%) - Média Geral

---

## 📊 O Que Você Verá no Streamlit

### **Página 1: Dashboard**
- Visualizações de indicadores por ano
- Gráficos de tendências
- Estatísticas resumidas

### **Página 2: Análise Exploratória**
- Correlações entre indicadores
- Distribuições de dados
- Análises por fase

### **Página 3: Previsão de Risco**
- Interface para inserir dados do aluno
- Previsão de probabilidade de risco
- Recomendações personalizadas

### **Página 4: Indicadores**
- Dicionário de todos os indicadores
- Explicações detalhadas
- Fórmulas de cálculo

---

## ✅ Verificação Rápida

### Verificar se dados foram processados
```bash
ls -la data/
# Deve mostrar: df_clean.csv, df_2022_clean.csv, df_2023_clean.csv, df_2024_clean.csv
```

### Verificar se modelos foram treinados
```bash
ls -la models/
# Deve mostrar: risk_model_rf.pkl, risk_model_gb.pkl, risk_model_scaler.pkl
```

### Verificar se gráficos foram gerados
```bash
ls -la presentation/charts/
# Deve mostrar: 8 arquivos PNG
```

### Verificar se aplicação está rodando
```bash
# Se ver mensagem "You can now view your Streamlit app in your browser"
# Significa que está funcionando!
```

---

## 🔧 Troubleshooting Rápido

| Problema | Solução |
|----------|---------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `FileNotFoundError: data/` | `python3 notebooks/01_data_cleaning.py` |
| `Port 8501 already in use` | `streamlit run app/streamlit_app.py --server.port=8502` |
| Aplicação muito lenta | Aumentar RAM ou reduzir dataset |
| Modelo não carrega | `python3 notebooks/03_predictive_model.py` |
| Gráficos não aparecem | `python3 notebooks/05_generate_charts.py` |

---

## 🔄 Executar Novamente

Se precisar executar novamente:

```bash
# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows

# Executar pipeline completo
python3 notebooks/01_data_cleaning.py
python3 notebooks/02_eda_full.py
python3 notebooks/03_predictive_model.py
python3 notebooks/04_comprehensive_analysis.py
python3 notebooks/05_generate_charts.py

# Iniciar Streamlit
streamlit run app/streamlit_app.py
```

---

## 📱 Acessar de Outro Computador

### Na mesma rede:
```bash
# Descobrir seu IP
ipconfig  # Windows
ifconfig  # Linux/Mac

# Acessar em outro computador:
http://<seu-ip>:8501
```

### Na internet:
Use Streamlit Cloud (veja DEPLOY_STREAMLIT_CLOUD.md)

---

## ⏱️ Resumo de Tempo

| Etapa | Tempo |
|-------|-------|
| Preparação | 1 min |
| 01_data_cleaning.py | 15-20s |
| 02_eda_full.py | 20-30s |
| 03_predictive_model.py | 30-45s |
| 04_comprehensive_analysis.py | 20-30s |
| 05_generate_charts.py | 15-20s |
| Streamlit startup | 30s |
| **TOTAL** | **~5 min** |

---

## 📚 Documentação Completa

Para detalhes técnicos, ver:
- **README.md** - Visão geral completa do projeto (ATUALIZADO)
- **DOCUMENTACAO_TECNICA.md** - Guia técnico completo (ATUALIZADO)
- **APRESENTACAO_COMERCIAL.pptx** - Apresentação com insights (ATUALIZADO)
- **APRESENTACAO_COMERCIAL.pdf** - Apresentação em PDF (ATUALIZADO)
- **DEPLOY_STREAMLIT_CLOUD.md** - Deploy em produção

---

## 🎯 Próximos Passos

1. ✅ Explorar o Dashboard
2. ✅ Testar a Previsão de Risco
3. ✅ Revisar Análise Exploratória
4. ✅ Abrir a Apresentação PPT/PDF
5. ✅ Consultar Recomendações Estratégicas

---

**Pronto para começar? Execute o Passo 1!** 🚀

**Desenvolvido com dedicação para transformar dados em oportunidades educacionais.** 🎓✨
