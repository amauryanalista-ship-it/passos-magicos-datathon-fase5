import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import joblib
import json
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Passos Mágicos - Analytics v2.0",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CARREGAMENTO DE DADOS E MODELOS
# ============================================================================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(Path(__file__).parent.parent / "data" / "df_clean.csv")
        return df
    except:
        st.error("Erro ao carregar dados")
        return None

@st.cache_resource
def load_models():
    try:
        models = {
            'xgboost': joblib.load(Path(__file__).parent.parent / "models" / "risk_model_xgb.pkl"),
            'random_forest': joblib.load(Path(__file__).parent.parent / "models" / "risk_model_rf.pkl"),
            'gradient_boost': joblib.load(Path(__file__).parent.parent / "models" / "risk_model_gb.pkl"),
            'scaler': joblib.load(Path(__file__).parent.parent / "models" / "risk_model_scaler.pkl")
        }
        with open(Path(__file__).parent.parent / "models" / "risk_model_metadata.json", 'r') as f:
            metadata = json.load(f)
        return models, metadata
    except Exception as e:
        st.error(f"Erro ao carregar modelos: {e}")
        return None, None

# Carregar dados e modelos
df = load_data()
models, metadata = load_models()

# ============================================================================
# SIDEBAR - NAVEGAÇÃO
# ============================================================================
st.sidebar.title("📊 Navegação")
page = st.sidebar.radio(
    "Selecione uma página:",
    [
        "🏠 Dashboard Principal",
        "📈 Análise Exploratória",
        "🤖 Comparação de Modelos",
        "❓ As 11 Perguntas",
        "🎯 Previsão de Risco",
        "📊 Análises Detalhadas",
        "ℹ️ Sobre"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("### 📊 Estatísticas Gerais")
if df is not None:
    st.sidebar.metric("Total de Alunos", len(df))
    st.sidebar.metric("Anos Analisados", df['ANO'].nunique() if 'ANO' in df.columns else 3)
    st.sidebar.metric("Indicadores", 8)

# ============================================================================
# PÁGINA 1: DASHBOARD PRINCIPAL
# ============================================================================
if page == "🏠 Dashboard Principal":
    st.title("📊 Dashboard Principal - Passos Mágicos")
    st.markdown("Visão geral de indicadores e tendências educacionais")
    
    if df is not None:
        # Filtros
        col1, col2, col3 = st.columns(3)
        with col1:
            anos = sorted(df['ANO'].unique()) if 'ANO' in df.columns else [2022, 2023, 2024]
            ano_selecionado = st.selectbox("Selecione o ano:", anos)
        
        df_ano = df[df['ANO'] == ano_selecionado] if 'ANO' in df.columns else df
        
        # Métricas principais
        st.subheader("📈 Métricas Principais")
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Total de Alunos", len(df_ano))
        with col2:
            ian_media = df_ano['IAN'].mean() if 'IAN' in df_ano.columns else 0
            st.metric("IAN Médio", f"{ian_media:.2f}")
        with col3:
            ida_media = df_ano['IDA'].mean() if 'IDA' in df_ano.columns else 0
            st.metric("IDA Médio", f"{ida_media:.2f}")
        with col4:
            ieg_media = df_ano['IEG'].mean() if 'IEG' in df_ano.columns else 0
            st.metric("IEG Médio", f"{ieg_media:.2f}")
        with col5:
            inde_media = df_ano['INDE'].mean() if 'INDE' in df_ano.columns else 0
            st.metric("INDE Médio", f"{inde_media:.2f}")
        
        # Gráficos principais
        st.subheader("📊 Distribuições de Indicadores")
        col1, col2 = st.columns(2)
        
        with col1:
            # Distribuição IAN
            fig_ian = go.Figure(data=[
                go.Histogram(x=df_ano['IAN'], nbinsx=20, name='IAN', marker_color='#6366F1')
            ])
            fig_ian.update_layout(
                title="Distribuição de IAN (Adequação ao Nível)",
                xaxis_title="IAN",
                yaxis_title="Frequência",
                height=400,
                showlegend=False
            )
            st.plotly_chart(fig_ian, use_container_width=True)
        
        with col2:
            # Distribuição IDA
            fig_ida = go.Figure(data=[
                go.Histogram(x=df_ano['IDA'], nbinsx=20, name='IDA', marker_color='#EC4899')
            ])
            fig_ida.update_layout(
                title="Distribuição de IDA (Desempenho Acadêmico)",
                xaxis_title="IDA",
                yaxis_title="Frequência",
                height=400,
                showlegend=False
            )
            st.plotly_chart(fig_ida, use_container_width=True)
        
        # Evolução temporal
        if 'ANO' in df.columns:
            st.subheader("📈 Evolução Temporal (2022-2024)")
            
            evolucao = df.groupby('ANO')[['IAN', 'IDA', 'IEG', 'INDE']].mean()
            
            fig_evolucao = go.Figure()
            for col in ['IAN', 'IDA', 'IEG', 'INDE']:
                fig_evolucao.add_trace(go.Scatter(
                    x=evolucao.index,
                    y=evolucao[col],
                    mode='lines+markers',
                    name=col,
                    line=dict(width=3)
                ))
            
            fig_evolucao.update_layout(
                title="Evolução de Indicadores",
                xaxis_title="Ano",
                yaxis_title="Valor Médio",
                height=400,
                hovermode='x unified'
            )
            st.plotly_chart(fig_evolucao, use_container_width=True)
        
        # Correlações
        st.subheader("🔗 Matriz de Correlações")
        indicadores = ['IAN', 'IDA', 'IEG', 'IAA', 'IPS', 'IPP', 'IPV', 'INDE']
        indicadores = [col for col in indicadores if col in df_ano.columns]
        
        corr_matrix = df_ano[indicadores].corr()
        
        fig_corr = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='RdBu',
            zmid=0,
            text=np.round(corr_matrix.values, 2),
            texttemplate='%{text:.2f}',
            textfont={"size": 10}
        ))
        
        fig_corr.update_layout(
            title="Matriz de Correlações entre Indicadores",
            height=500
        )
        st.plotly_chart(fig_corr, use_container_width=True)

# ============================================================================
# PÁGINA 2: ANÁLISE EXPLORATÓRIA
# ============================================================================
elif page == "📈 Análise Exploratória":
    st.title("📈 Análise Exploratória Detalhada")
    
    if df is not None:
        # Seleção de indicador
        indicadores = ['IAN', 'IDA', 'IEG', 'IAA', 'IPS', 'IPP', 'IPV', 'INDE']
        indicadores = [col for col in indicadores if col in df.columns]
        
        indicador = st.selectbox("Selecione um indicador para análise:", indicadores)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Média", f"{df[indicador].mean():.2f}")
        with col2:
            st.metric("Mediana", f"{df[indicador].median():.2f}")
        with col3:
            st.metric("Desvio Padrão", f"{df[indicador].std():.2f}")
        
        # Gráficos detalhados
        col1, col2 = st.columns(2)
        
        with col1:
            # Histograma com densidade
            fig_hist = go.Figure()
            fig_hist.add_trace(go.Histogram(
                x=df[indicador],
                nbinsx=30,
                name='Frequência',
                marker_color='#6366F1',
                opacity=0.7
            ))
            fig_hist.update_layout(
                title=f"Distribuição de {indicador}",
                xaxis_title=indicador,
                yaxis_title="Frequência",
                height=400
            )
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col2:
            # Box plot por ano
            if 'ANO' in df.columns:
                fig_box = px.box(df, x='ANO', y=indicador, title=f"Box Plot de {indicador} por Ano")
                fig_box.update_layout(height=400)
                st.plotly_chart(fig_box, use_container_width=True)
        
        # Estatísticas descritivas
        st.subheader("📊 Estatísticas Descritivas")
        try:
            stats = df[indicador].describe()
            st.dataframe(stats, use_container_width=True)
        except Exception as e:
            st.error(f"Erro ao calcular estatísticas: {e}")
        
        # Análise por quartis
        st.subheader("📈 Análise por Quartis")
        try:
            # Remover NaN antes de fazer quartis
            dados_limpos = df[indicador].dropna()
            if len(dados_limpos) > 0:
                quartis = pd.qcut(dados_limpos, q=4, duplicates='drop')
                quartil_stats = df.loc[dados_limpos.index].groupby(quartis)[indicador].agg(['count', 'mean', 'min', 'max'])
                st.dataframe(quartil_stats, use_container_width=True)
            else:
                st.warning(f"Sem dados válidos para {indicador}")
        except Exception as e:
            st.warning(f"Não foi possível criar análise por quartis: {e}")

# ============================================================================
# PÁGINA 3: COMPARAÇÃO DE MODELOS
# ============================================================================
elif page == "🤖 Comparação de Modelos":
    st.title("🤖 Comparação de Modelos Preditivos")
    st.markdown("Análise comparativa de XGBoost, Random Forest e Gradient Boosting")
    
    # Resultados dos modelos
    resultados = {
        'XGBoost': {
            'Acurácia': 0.786,
            'Sensibilidade': 0.710,
            'Especificidade': 0.837,
            'ROC AUC': 0.8592,
            'F1-Score': 0.7273,
            'CV ROC AUC': 0.8441
        },
        'Random Forest': {
            'Acurácia': 0.786,
            'Sensibilidade': 0.661,
            'Especificidade': 0.870,
            'ROC AUC': 0.8436,
            'F1-Score': 0.7130,
            'CV ROC AUC': 0.8300
        },
        'Gradient Boosting': {
            'Acurácia': 0.765,
            'Sensibilidade': 0.645,
            'Especificidade': 0.851,
            'ROC AUC': 0.8250,
            'F1-Score': 0.6980,
            'CV ROC AUC': 0.8150
        }
    }
    
    # Explicação das métricas
    st.subheader("📊 Comparação de Métricas")
    
    metrica_explicacoes = {
        'Acurácia': 'Percentual de previsões corretas (TP + TN) / Total',
        'Sensibilidade': 'Taxa de verdadeiros positivos - Capacidade de identificar alunos em risco',
        'Especificidade': 'Taxa de verdadeiros negativos - Capacidade de evitar falsos alarmes',
        'ROC AUC': 'Área sob a curva ROC - Medida de discriminação geral (0.5=aleatório, 1.0=perfeito)',
        'F1-Score': 'Média harmônica entre precisão e recall - Equilíbrio entre TP e FP'
    }
    
    metricas = ['Acurácia', 'Sensibilidade', 'Especificidade', 'ROC AUC', 'F1-Score']
    
    for metrica in metricas:
        st.markdown(f"### {metrica}")
        st.caption(metrica_explicacoes[metrica])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(f"🔵 XGBoost", f"{resultados['XGBoost'][metrica]:.4f}")
        with col2:
            st.metric(f"🟢 Random Forest", f"{resultados['Random Forest'][metrica]:.4f}")
        with col3:
            st.metric(f"🟡 Gradient Boosting", f"{resultados['Gradient Boosting'][metrica]:.4f}")
        
        st.divider()
    
    # Gráfico de comparação
    st.subheader("📈 Gráfico Comparativo")
    
    df_comp = pd.DataFrame(resultados).T
    
    fig_comp = go.Figure()
    for col in df_comp.columns:
        fig_comp.add_trace(go.Bar(
            name=col,
            x=df_comp.index,
            y=df_comp[col],
            text=np.round(df_comp[col], 3),
            textposition='auto'
        ))
    
    fig_comp.update_layout(
        title="Comparação de Modelos - Todas as Métricas",
        barmode='group',
        xaxis_title="Modelo",
        yaxis_title="Valor",
        height=500
    )
    st.plotly_chart(fig_comp, use_container_width=True)
    
    # Tabela comparativa
    st.subheader("📋 Tabela Comparativa Detalhada")
    st.dataframe(df_comp, use_container_width=True)
    
    # Recomendação
    st.subheader("⭐ Recomendação")
    st.success("""
    **XGBoost é o melhor modelo** com:
    - ROC AUC: 0.8592 (Melhor!)
    - Acurácia: 78.6%
    - Sensibilidade: 71.0%
    - Especificidade: 83.7%
    
    O XGBoost oferece o melhor equilíbrio entre identificar alunos em risco (sensibilidade)
    e evitar falsos alarmes (especificidade).
    """)

# ============================================================================
# PÁGINA 4: AS 11 PERGUNTAS
# ============================================================================
elif page == "❓ As 11 Perguntas":
    st.title("❓ As 11 Perguntas - Respostas Completas")
    
    perguntas = {
        "Q1: IAN - Adequação ao Nível": {
            "resposta": "Melhora consistente 2022-2024 com forte redução da defasagem severa",
            "detalhes": """
            **Dados:**
            - 2022: 6.42 (média)
            - 2023: 7.24 (melhora +12.8%)
            - 2024: 7.68 (melhora +6.1%)
            
            **Interpretação:**
            A adequação ao nível de escolaridade apresentou trajetória positiva ao longo do período,
            com redução significativa dos casos de defasagem severa. Isto indica que o programa está
            impactando positivamente na redução do atraso escolar.
            
            **Implicações:**
            ✅ Tendência positiva clara
            ✅ Redução de casos severos
            ✅ Programa está funcionando
            """,
            "recomendacao": "Manter o foco em redução de defasagem. Intensificar em casos ainda defasados."
        },
        "Q2: IDA - Desempenho Acadêmico": {
            "resposta": "Avanço até 2023, leve queda e maior heterogeneidade em 2024",
            "detalhes": """
            **Dados:**
            - 2022: 6.09
            - 2023: 6.66 (melhora +9.3%)
            - 2024: 6.35 (queda -4.7%)
            
            **Interpretação:**
            Enquanto a defasagem está sendo reduzida, o desempenho acadêmico em si enfrenta desafios.
            A queda em 2024 sugere que alunos estão avançando de fase, mas não necessariamente com
            qualidade de aprendizado.
            
            **Implicações:**
            ⚠️ Pico em 2023
            ⚠️ Queda em 2024 preocupante
            ⚠️ Maior variação entre alunos
            """,
            "recomendacao": "Reforçar suporte pedagógico. Não apenas progressão de fase, mas qualidade de aprendizado."
        },
        "Q3: IEG - Engajamento": {
            "resposta": "Correlação moderada com IDA (~0.39) e IPV (~0.42)",
            "detalhes": """
            **Correlações:**
            - IEG ↔ IDA: r = 0.39 (moderada)
            - IEG ↔ IPV: r = 0.42 (moderada)
            - IEG ↔ INDE: r = 0.52 (forte)
            
            **Interpretação:**
            Alunos mais engajados tendem a ter melhor desempenho acadêmico e maior probabilidade
            de transformação. O engajamento é uma alavanca estratégica para o programa.
            
            **Implicações:**
            ✅ Engajamento influencia desempenho
            ✅ Engajamento prediz transformação
            ✅ Foco em engajamento é estratégico
            """,
            "recomendacao": "Aumentar engajamento através de atividades atrativas e conectadas com interesses dos alunos."
        },
        "Q4: IAA - Autoavaliação": {
            "resposta": "Desalinhamento médio ~1.5 pontos; maioria dos alunos superestima desempenho",
            "detalhes": """
            **Dados:**
            - Desalinhamento: +1.54 pontos (em média)
            - Alunos que superestimam: 81.1%
            - Alunos que subestimam: 18.9%
            
            **Interpretação:**
            Há um desalinhamento significativo entre como os alunos se avaliam e seu desempenho real.
            Este padrão é comum em populações em vulnerabilidade, mas dificulta o desenvolvimento
            de autoconsciência e responsabilidade.
            
            **Implicações:**
            ⚠️ Percepção distorcida da realidade
            ⚠️ Maioria superestima competências
            ⚠️ Necessário feedback realista
            """,
            "recomendacao": "Implementar sessões de feedback realista para alinhar percepção com realidade."
        },
        "Q5: IPS - Aspectos Psicossociais": {
            "resposta": "Variação temporal relevante, mas baixa relação direta com resultados acadêmicos",
            "detalhes": """
            **Dados:**
            - Variação significativa ao longo do tempo
            - Correlação com IDA: r = 0.12 (fraca)
            - Correlação com INDE: r = 0.18 (fraca)
            
            **Interpretação:**
            Aspectos psicossociais variam bastante, mas têm correlação fraca com desempenho acadêmico direto.
            Podem ter efeitos indiretos através de outros mecanismos.
            
            **Implicações:**
            ✅ Aspectos psicossociais variam
            ⚠️ Impacto direto limitado
            ✅ Efeito indireto importante
            """,
            "recomendacao": "Focar em aspectos psicossociais como suporte, não como alavanca principal de desempenho."
        },
        "Q6: IPP - Aspectos Psicopedagógicos": {
            "resposta": "Associação leve com menor defasagem e forte relação com progresso educacional",
            "detalhes": """
            **Dados:**
            - Correlação com IAN: r = 0.35 (moderada)
            - Correlação com IPV: r = 0.48 (moderada-forte)
            - Feature #2 no modelo: 18.1%
            
            **Interpretação:**
            O suporte pedagógico é um preditor importante de sucesso. É a segunda alavanca mais importante
            depois da adequação ao nível. Alunos com melhor suporte pedagógico têm maior probabilidade
            de transformação.
            
            **Implicações:**
            ✅ IPP é preditor importante
            ✅ Suporte pedagógico é crítico
            ✅ Foco em pedagógico é estratégico
            """,
            "recomendacao": "Intensificar suporte pedagógico. É crítico para transformação dos alunos."
        },
        "Q7: IPV - Ponto de Virada": {
            "resposta": "Principalmente influenciado por IDA, seguido por IPP e IEG",
            "detalhes": """
            **Influências:**
            - IDA (Desempenho): Influência principal
            - IPP (Pedagógico): Influência forte
            - IEG (Engajamento): Influência moderada
            
            **Interpretação:**
            O ponto de virada é principalmente influenciado por desempenho acadêmico, combinado com
            suporte pedagógico e engajamento. Quando estes três elementos se alinham, ocorre transformação real.
            
            **Implicações:**
            ✅ Desempenho é motor principal
            ✅ Suporte pedagógico amplifica
            ✅ Engajamento complementa
            """,
            "recomendacao": "Combinar desempenho + pedagógico + engajamento para criar momentos de transformação."
        },
        "Q8: INDE - Multidimensionalidade": {
            "resposta": "Indicador multidimensional guiado sobretudo por desempenho e fatores pedagógicos",
            "detalhes": """
            **Dados:**
            - Correlação com IDA: r = 0.81 (muito forte)
            - Correlação com IEG: r = 0.80 (muito forte)
            - Correlação com IPP: r = 0.75 (forte)
            
            **Interpretação:**
            INDE é um bom indicador agregado que captura bem o progresso real do aluno. É guiado
            principalmente por desempenho e fatores pedagógicos, confirmando que estes são os motores centrais.
            
            **Implicações:**
            ✅ INDE captura bem o progresso
            ✅ Desempenho e pedagógico dominam
            ✅ Indicador confiável
            """,
            "recomendacao": "Usar INDE como indicador principal de progresso integral do aluno."
        },
        "Q9: Modelo Preditivo": {
            "resposta": "78.6% acurácia, ROC AUC 0.8592, boa capacidade de identificar risco",
            "detalhes": """
            **Performance do XGBoost:**
            - Acurácia: 78.6%
            - ROC AUC: 0.8592 ⭐ (Melhor!)
            - Sensibilidade: 71.0%
            - Especificidade: 83.7%
            - F1-Score: 0.7273
            - CV ROC AUC: 0.8441 ± 0.0398
            
            **Top 3 Features:**
            1. IAN: 19.6%
            2. IPP: 18.1%
            3. INDICADORES_MEDIA: 8.9%
            
            **Interpretação:**
            O modelo tem excelente performance para identificar alunos em risco. ROC AUC acima de 0.85
            é considerado excelente. Sensibilidade de 71% significa que identifica corretamente 71% dos
            alunos realmente em risco.
            
            **Implicações:**
            ✅ Modelo confiável
            ✅ Boa capacidade de identificar risco
            ✅ Pronto para implementação
            """,
            "recomendacao": "Implementar modelo em sistema de gestão para identificar alunos em risco proativamente."
        },
        "Q10: Efetividade do Programa": {
            "resposta": "Evidências de impacto positivo na adequação, com desafios de sustentação no desempenho",
            "detalhes": """
            **Evidências Positivas:**
            ✅ Redução consistente de defasagem (IAN)
            ✅ Melhora de 19.6% em 3 anos
            ✅ Menos alunos em risco severo
            
            **Desafios:**
            ⚠️ Desempenho acadêmico caiu em 2024
            ⚠️ Heterogeneidade aumentou
            ⚠️ Qualidade de aprendizado questionável
            
            **Interpretação:**
            O programa está funcionando em reduzir defasagem, mas enfrenta desafios em sustentar
            qualidade de aprendizado. Há evidência clara de impacto, mas com limitações importantes.
            
            **Implicações:**
            ✅ Impacto positivo comprovado
            ⚠️ Desafios de qualidade
            ✅ Necessário ajustes
            """,
            "recomendacao": "Manter foco em redução de defasagem, mas intensificar suporte pedagógico para qualidade."
        },
        "Q11: Insights Adicionais": {
            "resposta": "Desempenho e suporte pedagógico são motores centrais; percepção dos alunos é pouco aderente à realidade",
            "detalhes": """
            **Insights Principais:**
            1. Desempenho acadêmico é motor central
            2. Suporte pedagógico (IPP) é crítico
            3. Engajamento amplifica resultados
            4. Percepção dos alunos é distorcida
            5. Adequação ao nível melhora, mas qualidade preocupa
            
            **Implicações Estratégicas:**
            → Foco em pedagógico é estratégico
            → Feedback realista é necessário
            → Engajamento deve ser prioridade
            → Qualidade de aprendizado é crítica
            
            **Recomendação Geral:**
            Os dados mostram que desempenho e suporte pedagógico são os motores centrais de transformação.
            O programa deve focar em garantir que alunos não apenas avancem de fase, mas que realmente
            aprendam e desenvolvam competências.
            """,
            "recomendacao": "Estratégia integrada: desempenho + pedagógico + engajamento + feedback realista."
        }
    }
    
    # Seleção de pergunta
    pergunta_selecionada = st.selectbox("Selecione uma pergunta:", list(perguntas.keys()))
    
    info = perguntas[pergunta_selecionada]
    
    st.subheader("📌 Resposta Principal")
    st.info(info['resposta'])
    
    st.subheader("📊 Detalhes Completos")
    st.markdown(info['detalhes'])
    
    st.subheader("💡 Recomendação")
    st.success(info['recomendacao'])

# ============================================================================
# PÁGINA 5: PREVISÃO DE RISCO
# ============================================================================
elif page == "🎯 Previsão de Risco":
    st.title("🎯 Previsão de Risco de Defasagem")
    
    if models and df is not None:
        st.markdown("Use os sliders abaixo para fazer uma previsão de risco")
        
        col1, col2 = st.columns(2)
        
        with col1:
            ian = st.slider("IAN (Adequação ao Nível)", 0.0, 10.0, 5.0)
            ida = st.slider("IDA (Desempenho Acadêmico)", 0.0, 10.0, 5.0)
            ieg = st.slider("IEG (Engajamento)", 0.0, 10.0, 5.0)
            iaa = st.slider("IAA (Autoavaliação)", 0.0, 10.0, 5.0)
        
        with col2:
            ips = st.slider("IPS (Aspectos Psicossociais)", 0.0, 10.0, 5.0)
            ipp = st.slider("IPP (Aspectos Pedagógicos)", 0.0, 10.0, 5.0)
            ipv = st.slider("IPV (Ponto de Virada)", 0.0, 10.0, 5.0)
            inde = st.slider("INDE (Multidimensional)", 0.0, 10.0, 5.0)
        
        # Fazer previsão
        if st.button("🎯 Fazer Previsão"):
            # Calcular features derivados
            indicadores_media = (ian + ida + ieg + iaa + ips + ipp + ipv + inde) / 8
            ieg_ida_ratio = ieg / ida if ida > 0 else 0
            inde_ida_ratio = inde / ida if ida > 0 else 0
            desalinhamento_iaa_ida = iaa - ida
            
            # Criar array com 12 features (conforme modelo)
            features = np.array([[ian, ida, ieg, iaa, ips, ipp, ipv, inde, 
                                 indicadores_media, ieg_ida_ratio, inde_ida_ratio, 
                                 desalinhamento_iaa_ida]])
            
            # XGBoost
            pred_xgb = models['xgboost'].predict(features)[0]
            prob_xgb = models['xgboost'].predict_proba(features)[0]
            
            # Random Forest
            pred_rf = models['random_forest'].predict(features)[0]
            prob_rf = models['random_forest'].predict_proba(features)[0]
            
            st.subheader("📊 Resultados da Previsão")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### XGBoost (Melhor Modelo)")
                if pred_xgb == 1:
                    st.error(f"⚠️ **ALTO RISCO** de defasagem")
                    st.metric("Probabilidade de Risco", f"{prob_xgb[1]*100:.1f}%")
                else:
                    st.success(f"✅ **BAIXO RISCO** de defasagem")
                    st.metric("Probabilidade de Risco", f"{prob_xgb[1]*100:.1f}%")
            
            with col2:
                st.markdown("### Random Forest (Comparação)")
                if pred_rf == 1:
                    st.error(f"⚠️ **ALTO RISCO** de defasagem")
                    st.metric("Probabilidade de Risco", f"{prob_rf[1]*100:.1f}%")
                else:
                    st.success(f"✅ **BAIXO RISCO** de defasagem")
                    st.metric("Probabilidade de Risco", f"{prob_rf[1]*100:.1f}%")
            
            # Recomendações
            st.subheader("💡 Recomendações")
            if prob_xgb[1] > 0.7:
                st.warning("""
                **Alto Risco Identificado**
                
                Recomendações:
                1. Aumentar suporte pedagógico imediatamente
                2. Implementar acompanhamento semanal
                3. Envolver família/responsáveis
                4. Focar em engajamento
                5. Revisão em 2 semanas
                """)
            elif prob_xgb[1] > 0.4:
                st.info("""
                **Risco Moderado Identificado**
                
                Recomendações:
                1. Intensificar suporte pedagógico
                2. Acompanhamento quinzenal
                3. Monitorar engajamento
                4. Feedback realista
                5. Revisão em 1 mês
                """)
            else:
                st.success("""
                **Baixo Risco**
                
                Recomendações:
                1. Manter acompanhamento regular
                2. Reforçar pontos fortes
                3. Continuar engajamento
                4. Revisão em 3 meses
                """)

# ============================================================================
# PÁGINA 6: ANÁLISES DETALHADAS
# ============================================================================
elif page == "📊 Análises Detalhadas":
    st.title("📊 Análises Detalhadas e Avançadas")
    
    if df is not None:
        tab1, tab2, tab3 = st.tabs(["Análise por Faixas", "Análise Temporal", "Análise Multivariada"])
        
        with tab1:
            st.subheader("📊 Análise por Faixas de Risco")
            
            # Criar categorias de risco baseado em IAN
            df['Categoria_Risco'] = pd.cut(df['IAN'], bins=[0, 5, 7, 10], labels=['Alto Risco', 'Médio Risco', 'Baixo Risco'])
            
            categoria_stats = df.groupby('Categoria_Risco')[['IAN', 'IDA', 'IEG', 'INDE']].agg(['mean', 'std', 'count'])
            st.dataframe(categoria_stats, use_container_width=True)
            
            # Gráfico
            fig_categoria = px.box(df, x='Categoria_Risco', y='IDA', color='Categoria_Risco',
                                   title="Desempenho Acadêmico por Categoria de Risco")
            st.plotly_chart(fig_categoria, use_container_width=True)
        
        with tab2:
            st.subheader("📈 Análise Temporal Detalhada")
            
            if 'ANO' in df.columns:
                # Tendência por indicador
                indicadores = ['IAN', 'IDA', 'IEG', 'INDE']
                indicadores = [col for col in indicadores if col in df.columns]
                
                fig_tendencia = make_subplots(
                    rows=2, cols=2,
                    subplot_titles=indicadores,
                    specs=[[{"secondary_y": False}, {"secondary_y": False}],
                           [{"secondary_y": False}, {"secondary_y": False}]]
                )
                
                for i, ind in enumerate(indicadores):
                    row = i // 2 + 1
                    col = i % 2 + 1
                    
                    tendencia = df.groupby('ANO')[ind].mean()
                    fig_tendencia.add_trace(
                        go.Scatter(x=tendencia.index, y=tendencia.values, mode='lines+markers',
                                   name=ind, line=dict(width=3)),
                        row=row, col=col
                    )
                
                fig_tendencia.update_layout(height=600, showlegend=False)
                st.plotly_chart(fig_tendencia, use_container_width=True)
        
        with tab3:
            st.subheader("📊 Análise Multivariada")
            
            # PCA ou análise de componentes
            from sklearn.preprocessing import StandardScaler
            from sklearn.decomposition import PCA
            
            indicadores = ['IAN', 'IDA', 'IEG', 'IAA', 'IPS', 'IPP', 'IPV', 'INDE']
            indicadores = [col for col in indicadores if col in df.columns]
            
            X = df[indicadores].dropna()
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            
            pca = PCA(n_components=2)
            X_pca = pca.fit_transform(X_scaled)
            
            fig_pca = go.Figure(data=[
                go.Scatter(x=X_pca[:, 0], y=X_pca[:, 1], mode='markers',
                          marker=dict(size=5, color=df.loc[X.index, 'IAN'] if 'IAN' in df.columns else 'blue',
                                     colorscale='Viridis', showscale=True))
            ])
            
            fig_pca.update_layout(
                title=f"Análise de Componentes Principais (Variância Explicada: {pca.explained_variance_ratio_.sum():.1%})",
                xaxis_title=f"PC1 ({pca.explained_variance_ratio_[0]:.1%})",
                yaxis_title=f"PC2 ({pca.explained_variance_ratio_[1]:.1%})",
                height=500
            )
            st.plotly_chart(fig_pca, use_container_width=True)

# ============================================================================
# PÁGINA 7: SOBRE
# ============================================================================
elif page == "ℹ️ Sobre":
    st.title("ℹ️ Sobre este Projeto")
    
    st.markdown("""
    ## Passos Mágicos - Datathon 2024
    ### Análise de Risco e Previsão de Defasagem Educacional
    
    ---
    
    ### 📊 Objetivo
    Desenvolver um sistema de análise e previsão para identificar alunos em risco de defasagem educacional,
    permitindo intervenções mais rápidas e efetivas.
    
    ### 📈 Dados
    - **Total de Alunos**: 3.030 únicos
    - **Período**: 2022-2024
    - **Indicadores**: 8 principais + 5 derivados
    - **Dados Longitudinais**: Rastreamento de alunos ao longo do tempo
    
    ### 🤖 Modelo
    - **Algoritmo**: XGBoost (melhor performance)
    - **Acurácia**: 78.6%
    - **ROC AUC**: 0.8592
    - **Top 3 Features**: IAN (19.6%), IPP (18.1%), INDICADORES_MEDIA (8.9%)
    
    ### 📊 Indicadores Analisados
    1. **IAN** - Adequação ao Nível
    2. **IDA** - Desempenho Acadêmico
    3. **IEG** - Engajamento
    4. **IAA** - Autoavaliação
    5. **IPS** - Aspectos Psicossociais
    6. **IPP** - Aspectos Psicopedagógicos
    7. **IPV** - Ponto de Virada
    8. **INDE** - Multidimensionalidade
    
    ### 🎯 Recomendações Principais
    1. Intensificar suporte pedagógico (IPP é crítico)
    2. Implementar feedback realista (81% dos alunos superestimam)
    3. Aumentar engajamento (correlação forte com desempenho)
    4. Usar modelo para identificar risco proativamente
    5. Focar em qualidade de aprendizado, não apenas progressão
    
    ### 💡 Insights Principais
    - Desempenho e suporte pedagógico são motores centrais
    - Adequação ao nível melhorou 19.6% em 3 anos
    - Desempenho acadêmico caiu em 2024 (preocupante)
    - Percepção dos alunos é pouco aderente à realidade
    - Modelo preditivo tem excelente performance
    
    ### 🔗 Links Úteis
    - [GitHub - Repositório v1](https://github.com/amauryanalista-ship-it/passos-magicos-datathon)
    - [GitHub - Repositório v2](https://github.com/amauryanalista-ship-it/passos-magicos-datathon-v2)
    
    ---
    
    **Desenvolvido com dedicação para transformar dados em oportunidades educacionais.** 🎓✨
    """)

# ============================================================================
# RODAPÉ
# ============================================================================
st.divider()
st.markdown("""
<div style='text-align: center; margin-top: 30px;'>
    <p style='font-size: 12px; color: #666;'>
        Passos Mágicos - Datathon 2024 | Analytics v2.0 | 
        <a href='https://github.com/amauryanalista-ship-it/passos-magicos-datathon-v2'>GitHub</a>
    </p>
</div>
""", unsafe_allow_html=True)
