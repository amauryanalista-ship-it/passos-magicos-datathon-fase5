# 🚀 Deploy no Streamlit Cloud

## Guia Completo para Deploy Automático

### **Pré-requisitos**

1. ✅ Conta GitHub
2. ✅ Conta Streamlit Cloud (gratuita)
3. ✅ Repositório GitHub com este código

---

## **Passo 1: Preparar Repositório GitHub**

### 1.1 Fazer Push do Código
```bash
cd datathon_project
git add -A
git commit -m "Ready for Streamlit Cloud deployment"
git push origin main
```

### 1.2 Verificar Estrutura
```
datathon_project/
├── app/
│   └── streamlit_app.py          ← Arquivo principal
├── models/
│   ├── risk_model_rf.pkl
│   ├── risk_model_gb.pkl
│   ├── risk_model_scaler.pkl
│   └── risk_model_metadata.json
├── data/
│   ├── df_2020_clean.csv
│   ├── df_2021_clean.csv
│   ├── df_2022_clean.csv
│   └── df_long_clean.csv
├── requirements.txt               ← Dependências
├── .streamlit/
│   └── config.toml               ← Configuração
└── .github/
    └── workflows/
        └── streamlit-deploy.yml  ← CI/CD
```

---

## **Passo 2: Conectar com Streamlit Cloud**

### 2.1 Acessar Streamlit Cloud
1. Ir para https://streamlit.io/cloud
2. Clicar "Sign in with GitHub"
3. Autorizar Streamlit a acessar seus repositórios

### 2.2 Criar Nova Aplicação
1. Clicar "New app"
2. Selecionar:
   - **Repository**: `amauryanalista-ship-it/passos-magicos-datathon`
   - **Branch**: `main` (ou `master`)
   - **Main file path**: `app/streamlit_app.py`

### 2.3 Configurar Secrets (Opcional)
Se a aplicação precisar de variáveis de ambiente:
1. Ir para "Advanced settings"
2. Adicionar secrets em formato TOML:
```toml
[secrets]
api_key = "seu-valor"
database_url = "sua-url"
```

### 2.4 Deploy
1. Clicar "Deploy"
2. Aguardar 2-3 minutos
3. Acessar URL fornecida (ex: `https://seu-app.streamlit.app`)

---

## **Passo 3: Monitorar Deployment**

### 3.1 Logs de Deploy
- Acessar dashboard do Streamlit Cloud
- Clicar na aplicação
- Ver logs em tempo real

### 3.2 Verificar Status
- 🟢 Verde: Aplicação rodando
- 🟡 Amarelo: Deployando
- 🔴 Vermelho: Erro

### 3.3 Troubleshooting
Se houver erro:
1. Verificar logs
2. Consultar seção "Troubleshooting" deste documento
3. Fazer ajustes e fazer push novamente

---

## **Passo 4: Atualizações Automáticas**

### 4.1 Como Funciona
- Qualquer push para `main` dispara novo deploy
- Streamlit Cloud reconstrói a aplicação automaticamente
- Novo deploy disponível em 2-3 minutos

### 4.2 Fazer Atualização
```bash
# Fazer mudanças no código
git add -A
git commit -m "Descrição das mudanças"
git push origin main

# Streamlit Cloud detecta e faz deploy automaticamente
```

---

## **Passo 5: Compartilhar Aplicação**

### 5.1 URL Pública
- Aplicação está disponível em: `https://seu-app.streamlit.app`
- Compartilhar com qualquer pessoa

### 5.2 Adicionar ao README
```markdown
## 🚀 Aplicação Online

Acesse a aplicação em produção: [Passos Mágicos App](https://seu-app.streamlit.app)
```

---

## 🔧 Troubleshooting

### **Problema: "ModuleNotFoundError"**
**Solução**: Verificar `requirements.txt`
```bash
# Adicionar pacote faltante
pip install nome-do-pacote
pip freeze > requirements.txt
git push
```

### **Problema: "FileNotFoundError: data/df_long_clean.csv"**
**Solução**: Dados não foram processados
1. Executar localmente:
```bash
python3 notebooks/01_data_cleaning.py
```
2. Fazer commit dos arquivos CSV
3. Fazer push

### **Problema: "Modelo não carrega"**
**Solução**: Arquivos .pkl não estão no repositório
```bash
git add models/
git commit -m "Add trained models"
git push
```

### **Problema: Aplicação muito lenta**
**Solução**: Usar cache do Streamlit
```python
import streamlit as st

@st.cache_resource
def load_model():
    return joblib.load('models/risk_model_rf.pkl')

model = load_model()
```

### **Problema: Port 8501 em uso**
**Solução**: Não é problema no Streamlit Cloud (usa porta padrão)

---

## 📊 Monitoramento em Produção

### **Acessar Métricas**
1. Ir para dashboard do Streamlit Cloud
2. Clicar na aplicação
3. Ver:
   - Número de usuários
   - Tempo de resposta
   - Uso de memória

### **Configurar Alertas**
1. Ir para "Settings"
2. Ativar notificações de erro
3. Receber email se aplicação falhar

---

## 🔐 Segurança

### **Boas Práticas**
1. ✅ Não commitar secrets em código
2. ✅ Usar Streamlit Cloud secrets
3. ✅ Manter dependências atualizadas
4. ✅ Revisar código antes de push

### **Exemplo de Uso de Secrets**
```python
import streamlit as st

# Acessar secret
api_key = st.secrets["api_key"]

# Usar em requisição
response = requests.get(
    "https://api.example.com",
    headers={"Authorization": f"Bearer {api_key}"}
)
```

---

## 📈 Otimizações

### **1. Usar Cache**
```python
@st.cache_data
def load_data():
    return pd.read_csv('data/df_long_clean.csv')

df = load_data()
```

### **2. Lazy Loading**
```python
if st.checkbox("Mostrar análise detalhada"):
    # Código pesado só executa se checkbox ativo
    expensive_computation()
```

### **3. Reduzir Tamanho de Dados**
```python
# Carregar apenas colunas necessárias
df = pd.read_csv('data.csv', usecols=['col1', 'col2'])
```

---

## 📞 Suporte

- **Documentação Streamlit**: https://docs.streamlit.io
- **Comunidade**: https://discuss.streamlit.io
- **Issues**: Abrir issue no repositório GitHub

---

## ✅ Checklist de Deploy

- [ ] Código está no GitHub
- [ ] `requirements.txt` atualizado
- [ ] Dados estão no repositório
- [ ] Modelos estão no repositório
- [ ] `.streamlit/config.toml` configurado
- [ ] Conectado com Streamlit Cloud
- [ ] Aplicação deployada com sucesso
- [ ] URL funciona em navegador
- [ ] Todas as páginas carregam
- [ ] Previsões funcionam corretamente

---

**Pronto para deploy? Siga os passos acima!** 🚀

---

**Última atualização**: Março 2024
**Status**: ✅ Pronto para Produção
