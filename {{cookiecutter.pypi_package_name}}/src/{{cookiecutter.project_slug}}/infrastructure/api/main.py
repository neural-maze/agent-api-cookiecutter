from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup and shutdown events for the API."""
    # Startup code (if any) goes here
    yield
    

app = FastAPI(
    title=" {{ cookiecutter.project_name }} ",
    description=" {{ cookiecutter.project_short_description }} ",
    docs_url="/docs",
    lifespan=lifespan,
)

@app.get("/")
async def root():
    """
    Root endpoint that redirects to API documentation
    """
    return {"message": "Welcome to {{ cookiecutter.project_name }}. Visit /docs for documentation"}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
