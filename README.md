# Job Analyzer Insights

Dashboard interativo desenvolvido em Python para análise de vagas de tecnologia em tempo real.

## Sobre o projeto

Este projeto coleta dados de vagas de emprego utilizando API, processa essas informações e gera insights sobre o mercado de tecnologia, como as habilidades mais demandadas e tendências atuais.

O objetivo é simular um cenário real de análise de dados, desde a coleta até a visualização.

---

## Funcionalidades

*  Coleta automática de vagas via API
*  Análise de tecnologias mais demandadas
*  Dashboard interativo com Streamlit
*  Filtros por cargo e tecnologia
*  Visualização de vagas coletadas

---

## Tecnologias utilizadas

* Python
* Pandas
* Streamlit
* Requests
* Python-dotenv

---

## Estrutura do projeto

```
job-analyzer/
 ├── app.py
 ├── coleta.py
 ├── analise.py
 ├── requirements.txt
 ├── .env (não versionado)
 └── data/
```

---

## Como executar o projeto

### 1. Clone o repositório

```
git clone https://github.com/aleesousa/job-analyzer.git
```

### 2. Acesse a pasta

```
cd job-analyzer
```

### 3. Crie o arquivo .env

```
API_KEY=your_api_key_here
```

### 4. Instale as dependências

```
pip install -r requirements.txt
```

### 5. Execute a coleta de dados

```
python coleta.py
```

### 6. Rode o dashboard

```
streamlit run app.py
```

---

## Segurança

As chaves de API são armazenadas utilizando variáveis de ambiente (.env), evitando exposição de dados sensíveis no repositório.

---

## Insights gerados

O projeto permite identificar:

* Tecnologias mais requisitadas no mercado
* Tendências em vagas de tecnologia
* Palavras-chave mais frequentes em descrições de vagas

---

## Próximas evoluções

*  Criação de API com FastAPI para gerenciamento de dados
*  Integração com banco de dados para persistência das vagas e parâmetros de busca
*  Sistema de agendamento para coleta automática de novas vagas
*  Funcionalidade de gerenciamento de candidaturas (aplicar/descartar vagas)
*  Possível deploy da aplicação para acesso online

---

## Autor

Desenvolvido por Alexandre Sousa