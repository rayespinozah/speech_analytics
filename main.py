from fastapi.responses import RedirectResponse

from apps.core.router import router
from settings.config import create_app, load_spacy_model

app = create_app()
app.include_router(router, prefix="/api/v1", tags=["/api/v1"])


@app.get("/")
def home():
    return RedirectResponse(url="/hello")


@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    # uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    uvicorn.run('main:app', host='0.0.0.0', port=8000)