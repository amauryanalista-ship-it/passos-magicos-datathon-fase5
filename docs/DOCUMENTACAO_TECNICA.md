# 📚 Documentação Técnica - Passos Mágicos Datathon 2024

## XGBoost - Modelo com Melhor Performance

---

## 1. VISÃO GERAL

Este documento descreve a arquitetura técnica, pipeline de processamento e resultados do projeto de análise e previsão de risco de defasagem educacional da ONG Passos Mágicos.

**Modelo Principal**: XGBoost
- **Acurácia**: 78.6%
- **ROC AUC**: 0.8592 ⭐ (Melhor!)
- **Sensibilidade**: 71.0%
- **Especificidade**: 83.7%
- **F1-Score**: 0.7273

---

## 2. PIPELINE DE PROCESSAMENTO

```
┌─────────────────────────────────────────────────────────────┐
│ ENTRADA: BASE DE DADOS PEDE 2024 - DATATHON.xlsx          │
│          (3 abas: PEDE2022, PEDE2023, PEDE2024)           │
└────────────────────┬────────────────────────────────────────┘
                     │
    ┌────────────────▼────────────────────────────┐
    │ 01_Limpeza_Dados.ipynb                      │
    │ • Consolidação das 3 abas                   │
    │ • Limpeza de dados                          │
    │ • Criação de 5 features derivadas           │
    │ • Saída: 3.030 registros consolidados       │
    └────────────────┬────────────────────────────┘
                     │
    ┌────────────────▼────────────────────────────┐
    │ 02_EDA.ipynb                                │
    │ • Análise exploratória completa             │
    │ • Responde 11 perguntas                     │
    │ • Correlações e tendências                  │
    │ • Saída: Relatório em console               │
    └────────────────┬────────────────────────────┘
                     │
    ┌────────────────▼────────────────────────────┐
    │ 03_Modelo_Predicao.ipynb                    │
    │ • Treina XGBoost (Melhor!)                  │
    │ • Treina Random Forest (comparação)         │
    │ • Valida com 5-fold CV                      │
    │ • Acurácia XGBoost: 78.6%                   │
    │ • ROC AUC XGBoost: 0.8592                   │
    │ • Saída: Modelos .pkl                       │
    └────────────────┬────────────────────────────┘
                     │
    ┌────────────────▼────────────────────────────┐
    │ 04_analises_respostas.ipynb                 │
    │ • Integra todas as análises                 │
    │ • Análise por fases                         │
    │ • Análise de risco                          │
    │ • Saída: Dados consolidados                 │
    └────────────────┬────────────────────────────┘
                     │
    ┌────────────────▼────────────────────────────┐
    │ 05_graficos.ipynb                           │
    │ • Gera 8 gráficos profissionais (300 DPI)   │
    │ • Visualizações de resultados               │
    │ • Saída: PNG para apresentações             │
    └────────────────┬────────────────────────────┘
                     │
    ┌────────────────▼────────────────────────────┐
    │ app/streamlit_app.py                        │
    │ • Dashboard interativo                      │
    │ • Previsão de risco em tempo real           │
    │ • 5 páginas completas                       │
    │ • Saída: Aplicação web                      │
    └─────────────────────────────────────────────┘
```

---

## 3. DADOS

### 3.1 Consolidação
```
PEDE2022: 860 alunos
PEDE2023: 1.014 alunos
PEDE2024: 1.156 alunos
─────────────────────
TOTAL:    3.030 alunos
```

### 3.2 Indicadores Principais (8)

| Indicador | Nome | Descrição | Range |
|-----------|------|-----------|-------|
| IAN | Adequação ao Nível | Defasagem entre fase ideal e efetiva | 0-15 |
| IDA | Desempenho Acadêmico | Média de notas (Mat, Port, Ing) | 0-10 |
| IEG | Engajamento | Participação em tarefas | 0-10 |
| IAA | Autoavaliação | Percepção do aluno | 0-10 |
| IPS | Aspectos Psicossociais | Avaliação de psicólogos | 0-10 |
| IPP | Aspectos Psicopedagógicos | Avaliação de pedagogos | 0-10 |
| IPV | Ponto de Virada | Indicador de transformação | 0-10 |
| INDE | Desenvolvimento Integral | Índice multidimensional | 0-10 |

### 3.3 Features Derivadas (5)

1. **INDICADORES_MEDIA** - Média de todos os 8 indicadores
2. **IEG_IDA_RATIO** - Razão engajamento/desempenho
3. **INDE_IDA_RATIO** - Razão desenvolvimento/desempenho
4. **DESALINHAMENTO_IAA_IDA** - Diferença autoavaliação-realidade
5. **ANO** - Ano do registro

---

## 4. MODELO PREDITIVO - XGBOOST ⭐

### 4.1 Performance

| Métrica | Valor |
|---------|-------|
| **Acurácia** | 78.6% |
| **Sensibilidade (Recall)** | 71.0% |
| **Especificidade** | 83.7% |
| **Precisão** | 75.0% |
| **F1-Score** | 0.7273 |
| **ROC AUC** | 0.8592 ⭐ |
| **CV ROC AUC** | 0.8441 ± 0.0398 |

### 4.2 Matriz de Confusão

```
              Predito
            Seguro  Risco
Real Seguro    77     15
     Risco     18     44
```

### 4.3 Arquitetura

- **Algoritmo**: XGBoost (Gradient Boosting)
- **Features**: 12 indicadores + derivados
- **Dados de Treino**: 615 alunos (80%)
- **Dados de Teste**: 154 alunos (20%)
- **Período de Treino**: 2022-2023
- **Período de Target**: 2024
- **Validação**: 5-fold Cross-Validation

### 4.4 Top 10 Features Mais Importantes

| Rank | Feature | Importância |
|------|---------|------------|
| 1 | IAN | 19.6% |
| 2 | IPP | 18.1% |
| 3 | INDICADORES_MEDIA | 8.9% |
| 4 | IPS | 8.6% |
| 5 | IPV | 7.7% |
| 6 | IEG_IDA_RATIO | 6.6% |
| 7 | INDE_IDA_RATIO | 6.3% |
| 8 | IAA | 6.3% |
| 9 | DESALINHAMENTO_IAA_IDA | 6.1% |
| 10 | IDA | 6.0% |

### 4.5 Interpretação

**Top 3 Drivers Principais**:
1. **IAN (19.6%)**: Adequação ao nível é o preditor mais importante
2. **IPP (18.1%)**: Suporte pedagógico é crítico
3. **INDICADORES_MEDIA (8.9%)**: Visão holística importa

---

## 5. AS 11 PERGUNTAS - RESPOSTAS TÉCNICAS

### Q1: Adequação do Nível (IAN)
**Resposta**: Melhora consistente 2022-2024 com forte redução da defasagem severa.

### Q2: Desempenho Acadêmico (IDA)
**Resposta**: Avanço até 2023, leve queda e maior heterogeneidade em 2024.

### Q3: Engajamento (IEG)
**Resposta**: Correlação moderada com IDA (~0.39) e IPV (~0.42).

### Q4: Autoavaliação (IAA)
**Resposta**: Desalinhamento médio ~1.5 pontos; maioria dos alunos superestima desempenho.

### Q5: Aspectos Psicossociais (IPS)
**Resposta**: Variação temporal relevante, mas baixa relação direta com resultados acadêmicos.

### Q6: Aspectos Psicopedagógicos (IPP)
**Resposta**: Associação leve com menor defasagem e forte relação com progresso educacional.

### Q7: Ponto de Virada (IPV)
**Resposta**: Principalmente influenciado por IDA, seguido por IPP e IEG.

### Q8: Multidimensionalidade (INDE)
**Resposta**: Indicador multidimensional guiado sobretudo por desempenho e fatores pedagógicos.

### Q9: Modelo Preditivo
**Resposta**: 78.6% acurácia, ROC AUC 0.8592, boa capacidade de identificar risco.

### Q10: Efetividade do Programa
**Resposta**: Evidências de impacto positivo na adequação, com desafios de sustentação no desempenho.

### Q11: Insights Adicionais
**Resposta**: Desempenho e suporte pedagógico são motores centrais; percepção dos alunos é pouco aderente à realidade.

---

## 6. ESTRUTURA DE ARQUIVOS

```
datathon_project/
├── notebooks/
│   ├── 01_Limpeza_Dados.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Modelo_Predicao.ipynb
│   ├── 04_analises_respostas.ipynb
│   └── 05_graficos.ipynb
├── app/
│   └── streamlit_app.py
├── data/
│   ├── df_clean.csv
│   ├── df_2022_clean.csv
│   ├── df_2023_clean.csv
│   └── df_2024_clean.csv
├── models/
│   ├── risk_model_xgb.pkl (XGBoost - Melhor!)
│   ├── risk_model_rf.pkl
│   ├── risk_model_scaler.pkl
│   └── risk_model_metadata.json
├── presentation/
│   ├── APRESENTACAO_COMERCIAL.pptx
│   ├── APRESENTACAO_COMERCIAL_COM_GRAFICOS.pptx
│   └── charts/
├── README.md
├── DOCUMENTACAO_TECNICA.md
├── GUIA_EXECUCAO.md
├── DEPLOY_STREAMLIT_CLOUD.md
└── requirements.txt
```

---

## 7. DEPENDÊNCIAS

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
scikit-learn>=1.3.0
xgboost>=2.0.0
joblib>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
```

---

## 8. COMO EXECUTAR

### 8.1 Ambiente Local

```bash
# 1. Clonar
git clone https://github.com/amauryanalista-ship-it/passos-magicos-datathon.git
cd datathon_project

# 2. Instalar
pip install -r requirements.txt

# 3. Executar Streamlit
streamlit run app/streamlit_app.py

# 4. Acessar
http://localhost:8501
```

### 8.2 Streamlit Cloud

1. Fork do repositório
2. Conectar em https://streamlit.io/cloud
3. Selecionar repositório
4. Deploy automático

---

## 9. RECOMENDAÇÕES

### 9.1 Curto Prazo (90 dias)
- Focar em redução de defasagem (IAN)
- Intensificar suporte pedagógico (IPP)
- Monitorar desalinhamento de percepção (IAA)

### 9.2 Médio Prazo (6-12 meses)
- Sustentar desempenho acadêmico (IDA)
- Aumentar engajamento (IEG)
- Fortalecer ponto de virada (IPV)

### 9.3 Longo Prazo (2025+)
- Consolidar ganhos em adequação
- Expandir programa com foco em IPP
- Implementar sistema de alerta baseado em modelo

---

**Versão**: 3.0 - XGBoost Final
**Data**: Março 2024
**Status**: ✅ Pronto para Produção
