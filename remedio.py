import pandas as pd
import os
from hashlib import sha256
from io import BytesIO
import zipfile

CSV_FILE = "estoque_remedios.csv"

def load_remedios():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame(columns=["id", "nome", "tarja", "preco", "validade"])

def save_remedios(df):
    df.to_csv(CSV_FILE, index=False)

def add_remedio(remedio):
    df = load_remedios()
    
    # Verificando se o remédio já existe com os mesmos parâmetros
    if not df[
        (df['nome'].str.contains(remedio['nome'], case=False, na=False)) &
        (df['tarja'].str.contains(remedio['tarja'], case=False, na=False)) &
        (df['preco'] == remedio['preco']) &
        (df['validade'] == remedio['validade'])
    ].empty:
        raise ValueError("Remédio com os mesmos parâmetros já existe.")

    if remedio['id'] in df['id'].values:
        raise ValueError("ID do remédio já existe.")

    df = pd.concat([df, pd.DataFrame([remedio])], ignore_index=True)
    save_remedios(df)

def update_remedio(id, remedio):
    df = load_remedios()
    df['id'] = df['id'].astype(str)

    if id not in df['id'].values:
        raise ValueError("Remédio não encontrado.")

    df.loc[df['id'] == id, ['nome', 'tarja', 'preco', 'validade']] = [
        remedio['nome'], remedio['tarja'], remedio['preco'], remedio['validade']
    ]
    save_remedios(df)

def delete_remedio(id):
    df = load_remedios()
    df['id'] = df['id'].astype(str)

    if id not in df['id'].values:
        raise ValueError("Remédio não encontrado.")

    df = df[df['id'] != id]
    if df.empty:
        os.remove(CSV_FILE)
    else:
        save_remedios(df)

def get_remedios():
    return load_remedios().to_dict(orient="records")

def get_quantidade_remedios():
    return len(load_remedios())

def compactar_remedios():
    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError("Arquivo CSV não encontrado.")
    
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(CSV_FILE, arcname="estoque_remedios.csv")
    zip_buffer.seek(0)
    return zip_buffer

def get_hash_remedios():
    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError("Arquivo CSV não encontrado.")
    
    with open(CSV_FILE, "rb") as file:
        return sha256(file.read()).hexdigest()
