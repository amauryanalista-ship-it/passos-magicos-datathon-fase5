# 📊 Passos Mágicos - Datathon 2026

**Advanced Analytics & Prediction Platform for Educational Risk Assessment**

Análise completa de risco e previsão de defasagem educacional com Streamlit, XGBoost e análises multidimensionais.

---

## 🎯 Objetivo do Projeto

Desenvolver um sistema inteligente de análise e previsão para identificar alunos em risco de defasagem educacional, permitindo intervenções mais rápidas e efetivas através de:

- ✅ Análise exploratória profunda de 3.030 alunos (2022-2024)
- ✅ Modelagem preditiva com XGBoost (78.6% acurácia, 0.8592 ROC AUC)
- ✅ Comparação de 3 modelos (XGBoost vs Random Forest vs Gradient Boosting)
- ✅ Dashboard interativo com 15+ visualizações
- ✅ Respostas completas para 11 perguntas estratégicas
- ✅ Análises por faixas, temporal e multivariada
- ✅ Previsão interativa em tempo real

---

## 📊 Dados do Projeto

| Métrica | Valor |
|---------|-------|
| **Total de Alunos** | 3.030 únicos |
| **Período Analisado** | 2022-2024 (3 anos) |
| **Indicadores Principais** | 8 |
| **Indicadores Derivados** | 5+ |
| **Tipo de Análise** | Longitudinal (rastreamento ao longo do tempo) |
| **Registros Totais** | 9.090+ (3 anos × 3.030 alunos) |

### 📋 Indicadores Analisados

1. **IAN** - Adequação ao Nível (defasagem escolar)
2. **IDA** - Desempenho Acadêmico (notas e aproveitamento)
3. **IEG** - Engajamento (participação e interesse)
4. **IAA** - Autoavaliação (percepção do aluno sobre si mesmo)
5. **IPS** - Aspectos Psicossociais (bem-estar emocional)
6. **IPP** - Aspectos Psicopedagógicos (suporte pedagógico)
7. **IPV** - Ponto de Virada (transformação real do aluno)
8. **INDE** - Indicador Multidimensional (agregado de progresso)

---

## 🤖 Modelo Preditivo XGBoost

### Performance

| Métrica | Valor |
|---------|-------|
| **Acurácia** | 78.6% |
| **ROC AUC** | 0.8592 ⭐ (Excelente) |
| **Sensibilidade** | 71.0% (identifica 71% dos casos reais) |
| **Especificidade** | 83.7% (evita 83.7% de falsos alarmes) |
| **F1-Score** | 0.7273 |
| **CV ROC AUC** | 0.8441 ± 0.0398 |

### Top 3 Features (Importância)

1. **IAN (Adequação ao Nível)**: 19.6%
2. **IPP (Aspectos Pedagógicos)**: 18.1%
3. **INDICADORES_MEDIA**: 8.9%

### Comparação com Outros Modelos

| Modelo | Acurácia | ROC AUC | Sensibilidade | Especificidade |
|--------|----------|---------|----------------|----------------|
| **XGBoost** | 78.6% | **0.8592** ⭐ | 71.0% | 83.7% |
| Random Forest | 78.6% | 0.8436 | 66.1% | 87.0% |
| Gradient Boosting | 76.5% | 0.8250 | 64.5% | 85.1% |

**Conclusão**: XGBoost é o melhor modelo com melhor ROC AUC e equilíbrio entre sensibilidade e especificidade.

---

## 🚀 Novidades da v2.0

### 7 Páginas Completas

1. **🏠 Dashboard Principal**
   - Métricas principais (IAN, IDA, IEG, INDE)
   - Distribuições de indicadores
   - Evolução temporal (2022-2024)
   - Matriz de correlações

2. **📈 Análise Exploratória**
   - Análises detalhadas por indicador
   - Histogramas com distribuições
   - Box plots por ano
   - Estatísticas descritivas
   - Análise por quartis

3. **🤖 Comparação de Modelos**
   - Comparação lado a lado (XGBoost vs RF vs GB)
   - Tabela comparativa detalhada
   - Recomendação do melhor modelo
   - Análise de trade-offs

4. **❓ As 11 Perguntas**
   - Q1: IAN - Adequação ao Nível
   - Q2: IDA - Desempenho Acadêmico
   - Q3: IEG - Engajamento
   - Q4: IAA - Autoavaliação
   - Q5: IPS - Aspectos Psicossociais
   - Q6: IPP - Aspectos Pedagógicos
   - Q7: IPV - Ponto de Virada
   - Q8: INDE - Multidimensionalidade
   - Q9: Modelo Preditivo
   - Q10: Efetividade do Programa
   - Q11: Insights Adicionais

   Cada pergunta contém:
   - ✅ Resposta principal
   - ✅ Dados detalhados
   - ✅ Interpretação técnica
   - ✅ Implicações estratégicas
   - ✅ Recomendações acionáveis

5. **🎯 Previsão de Risco**
   - Sliders interativos para cada indicador
   - Previsão em tempo real (XGBoost + RF)
   - Probabilidade de risco
   - Recomendações personalizadas por nível de risco

6. **📊 Análises Detalhadas**
   - Análise por faixas de risco
   - Análise temporal (2022-2024)
   - Análise multivariada (PCA)
   - Visualizações avançadas

7. **ℹ️ Sobre**
   - Informações completas do projeto
   - Objetivos e dados
   - Indicadores e insights
   - Links úteis

### 15+ Gráficos Interativos

- ✅ Histogramas com distribuições
- ✅ Box plots por ano
- ✅ Gráficos de linha com evolução
- ✅ Matriz de correlações (heatmap)
- ✅ Gráficos de barras comparativos
- ✅ Scatter plots multivariados
- ✅ Análise de componentes principais (PCA)
- ✅ Gráficos de tendência
- ✅ Distribuições por categoria

---

## 💡 Insights Principais

### Achados Importantes

1. **Desempenho e Suporte Pedagógico são Motores Centrais**
   - IAN (19.6%) e IPP (18.1%) são os principais preditores
   - Combinação de desempenho + pedagógico é crítica

2. **Adequação ao Nível Melhorou 19.6% em 3 Anos**
   - 2022: 6.42 → 2024: 7.68
   - Redução consistente de defasagem severa

3. **Desempenho Acadêmico Caiu em 2024 (Preocupante)**
   - 2022: 6.09 → 2023: 6.66 → 2024: 6.35
   - Queda de 4.7% em 2024
   - Maior heterogeneidade entre alunos

4. **81% dos Alunos Superestimam Desempenho**
   - Desalinhamento médio: +1.54 pontos
   - Necessário feedback realista

5. **Engajamento Influencia Desempenho**
   - Correlação IEG ↔ IDA: r = 0.39
   - Correlação IEG ↔ INDE: r = 0.52

6. **Modelo Preditivo tem Excelente Performance**
   - ROC AUC: 0.8592 (excelente)
   - Pronto para implementação em produção

---

## 📁 Estrutura do Repositório

```
passos_magicos_v2/
├── app/
│   └── streamlit_app.py              # Aplicação principal (1.200+ linhas)
│
├── data/
│   ├── df_clean.csv                  # 3.030 alunos consolidados
│   ├── df_2022_clean.csv
│   ├── df_2023_clean.csv
│   ├── df_2024_clean.csv
│   └── BASE DE DADOS PEDE 2024 - DATATHON.csv             
│
├── models/
│   ├── risk_model_xgb.pkl            # XGBoost (Melhor!)
│   ├── risk_model_rf.pkl             # Random Forest
│   ├── risk_model_gb.pkl             # Gradient Boosting
│   ├── risk_model_scaler.pkl         # StandardScaler
│   └── risk_model_metadata.json      # Metadados dos modelos
│
├── notebooks/
│   ├── 01_Limpeza_Dados.ipynb        # Data cleaning
│   ├── 02_EDA.ipynb                  # Análise exploratória
│   ├── 03_Modelo_Predicao.ipynb      # Modelagem XGBoost
│   ├── 04_analises_respostas.ipynb   # 11 perguntas
│   ├── 05_graficos.ipynb             # Visualizações
|
│
├── docs/
│   ├── DOCUMENTACAO_TECNICA.md       # Documentação técnica completa
│   ├── GUIA_EXECUCAO.md              # Guia de execução
│   ├── DEPLOY_STREAMLIT_CLOUD.md     # Deploy na nuvem
|
│
├── presentations/
│   ├── Apresentacao_Comercial_Datathon_VF.pptx   # Apresentação Comercial
│   ├── Apresentacao_Comercial_Datathon_VF_PDF.pdf    # Versão PDF
│
├── .streamlit/
│   └── config.toml                   # Configuração Streamlit
│
├── requirements.txt                  # Dependências Python
├── .gitignore
├── README.md                         # Este arquivo
```

---

## 🚀 Como Usar

### Instalação Local

```bash
# Clone o repositório
git clone https://github.com/amauryanalista-ship-it/passos-magicos-datathon-fase5
cd passos-magicos-datathon-fase5

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app/streamlit_app.py
```

A aplicação será aberta em `http://localhost:8501`

### Deploy no Streamlit Cloud

1. **Faça um fork deste repositório** no GitHub
2. **Acesse** https://streamlit.io/cloud
3. **Conecte com sua conta GitHub**
4. **Selecione** `passos-magicos-datathon-fase5`
5. **Deploy automático** será iniciado

A aplicação estará disponível em: `https://paapps-magicos-datathon-fase5-drhwux83oefhemnech2i7w.streamlit.app/`

### Uso dos Notebooks

```bash
# Inicie Jupyter
jupyter notebook

# Abra os notebooks na ordem:
# 1. 01_Limpeza_Dados.ipynb
# 2. 02_EDA.ipynb
# 3. 03_Modelo_Predicao.ipynb
# 4. 04_analises_respostas.ipynb
# 5. 05_graficos.ipynb
```

---

## 📊 Dependências

| Pacote | Versão | Uso |
|--------|--------|-----|
| streamlit | ≥1.28 | Framework web |
| pandas | ≥2.0 | Manipulação de dados |
| numpy | ≥1.24 | Computação numérica |
| plotly | ≥5.14 | Gráficos interativos |
| scikit-learn | ≥1.3 | ML e preprocessing |
| xgboost | ≥2.0 | Modelo XGBoost |
| joblib | ≥1.3 | Serialização de modelos |
| matplotlib | ≥3.7 | Gráficos estáticos |
| seaborn | ≥0.12 | Visualizações estatísticas |

---

## 📚 Documentação

### Arquivos de Documentação

- **DOCUMENTACAO_TECNICA.md**: Documentação técnica completa com arquitetura, metodologia e detalhes de implementação
- **GUIA_EXECUCAO.md**: Guia passo a passo para executar o projeto
- **DEPLOY_STREAMLIT_CLOUD.md**: Instruções detalhadas para deploy na nuvem

### Apresentações

- **Apresentacao_Comercial_Datathon_VF.pptx**: Apresentação Comercial 
- **Apresentacao_Comercial_Datathon_VF_PDF.pdf**: Versão PDF da apresentação
  
---

## ❓ As 11 Perguntas

O projeto responde completamente às 11 perguntas do Datathon:

1. ✅ **IAN**: Melhora consistente 2022-2024 com redução de defasagem severa
2. ✅ **IDA**: Avanço até 2023, leve queda em 2024
3. ✅ **IEG**: Correlação moderada com IDA e IPV
4. ✅ **IAA**: Desalinhamento ~1.5 pontos; maioria superestima
5. ✅ **IPS**: Variação temporal relevante, baixa relação direta
6. ✅ **IPP**: Associação leve com defasagem, forte com progresso
7. ✅ **IPV**: Influenciado por IDA, IPP e IEG
8. ✅ **INDE**: Multidimensional, guiado por desempenho e pedagógico
9. ✅ **Modelo**: 78.6% acurácia, 0.8592 ROC AUC
10. ✅ **Programa**: Evidências de impacto positivo com desafios
11. ✅ **Insights**: Desempenho + pedagógico são motores centrais

---

## 🎯 Recomendações Estratégicas

### Curto Prazo (1-3 meses)
1. Implementar modelo XGBoost em sistema de gestão
2. Identificar alunos em risco proativamente
3. Intensificar suporte pedagógico para casos de alto risco
4. Implementar feedback realista com alunos

### Médio Prazo (3-6 meses)
1. Expandir análises por faixa etária/série
2. Integrar dados de frequência e comportamento
3. Criar dashboard para gestores
4. Treinar equipe no uso do modelo

### Longo Prazo (6+ meses)
1. Refinar modelo com dados novos
2. Implementar recomendações personalizadas
3. Medir impacto das intervenções
4. Escalar para outras organizações

---

## 📈 Métricas de Sucesso

- ✅ Identificar 71% dos alunos em risco (sensibilidade)
- ✅ Evitar 83.7% de falsos alarmes (especificidade)
- ✅ ROC AUC acima de 0.85 (excelente discriminação)
- ✅ Redução de defasagem em 20% (meta)
- ✅ Melhora de desempenho em 15% (meta)

---

## 🔗 Links Úteis

- **Streamlit Docs**: https://docs.streamlit.io
- **XGBoost Docs**: https://xgboost.readthedocs.io

---

## 👨‍💼 Sobre o Projeto

**Desenvolvido para**: Passos Mágicos NGO - Datathon 2024
**Objetivo**: Transformar dados educacionais em oportunidades de intervenção e transformação social.
**Impacto**: Identificar alunos em risco e permitir ações proativas para garantir sucesso educacional.

---

## 👨‍💼 Sobre o Projeto

**Desenvolvido Por**: 

- **Amaury Junior** Linkedin: https://www.linkedin.com/in/amaury-junior-78bb1836
- **William Mendes** Linkedin: https://www.linkedin.com/in/william-silva-mendes-378343211
 

---

## 📄 Licença

Este projeto é de código aberto e está disponível para uso educacional e não-comercial.

---

**Desenvolvido com dedicação para transformar dados em oportunidades educacionais.** 🎓✨
