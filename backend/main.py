import uvicorn


from fastapi import FastAPI
from routes_user import router as user_router


app = FastAPI()

@app.get('/')
def link():
    return ("vá para localhost:8003/docs")


@app.get('/health-check')
def health_check():
    return True

app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn
                 
    uvicorn.run("main:app", host="127.0.0.1", port=8003, reload=True)