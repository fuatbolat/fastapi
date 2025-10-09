from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return [1,2,3,4]

@app.get("/{kisi}")
def getsoz(kisi : str):
    sozler = {
        "test1":"output is test1",
        "test2":"output is test2"
    }
    soz = sozler.get(kisi)
    return f"output : {soz}"



