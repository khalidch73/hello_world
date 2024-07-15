from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World welcome to azure"}

@app.get("/main/")
def read_main_root():
    return {"Test": "Azure is working change again and again"}