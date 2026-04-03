import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = "https://jsearch.p.rapidapi.com/search"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

all_jobs = []

for page in range(1, 6):  # coleta 5 páginas
    params = {
        "query": "data analyst remote",
        "page": str(page),
        "num_pages": "1"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    for job in data.get("data", []):
        all_jobs.append({
            "titulo": job.get("job_title"),
            "empresa": job.get("employer_name"),
            "localizacao": job.get("job_city"),
            "descricao": job.get("job_description")
        })

df = pd.DataFrame(all_jobs)

df.to_csv("data/jobs.csv", index=False)

print(f"Total coletado: {len(df)} vagas")