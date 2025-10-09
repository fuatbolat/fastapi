from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return [1,2,3,4]

@app.get("/{kisi}")
def getsoz(kisi : str):
    sozler = {
        "ataturk":"umutusz kurumlar",
        "fuat":"fuat bolat taradından"
    }
    soz = sozler.get(kisi)
    return f"output : {soz}"



