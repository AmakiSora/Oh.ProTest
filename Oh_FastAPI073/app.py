import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
def read_root():
    return "HelloWorld"


if __name__ == '__main__':
    uvicorn.run(app='app:app', host='0.0.0.0', port=8000)
