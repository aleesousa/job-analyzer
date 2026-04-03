# Job Analyzer Insights

Dashboard interativo desenvolvido em Python para análise de vagas de tecnologia em tempo real.

## Funcionalidades
- Coleta automática de vagas via API
- Análise de tecnologias mais demandadas
- Dashboard interativo com Streamlit
- Filtros por cargo e tecnologia

## Tecnologias
- Python
- Pandas
- Streamlit
- Requests

## Segurança
As chaves de API são armazenadas via variáveis de ambiente (.env), garantindo segurança e boas práticas.

## Como rodar

```bash
pip install -r requirements.txt
streamlit run app.py