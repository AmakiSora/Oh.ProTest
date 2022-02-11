import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
def read_root():
    return "HelloWorld"


if __name__ == '__main__':
    uvicorn.run(app='app:app', host='127.0.0.1', port=8001)
