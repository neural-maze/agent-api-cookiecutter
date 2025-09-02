from contextlib import asynccontextmanager

from fastapi import FastAPI

from .models import ChatRequest, EvalRequest, IngestDocumentsRequest, ResetMemoryRequest


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup and shutdown events for the API."""
    # Startup code (if any) goes here
    yield


app = FastAPI(
    title=" Agent API ",
    description=" This is a template for creating powerful Agent APIs. ",
    docs_url="/docs",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    """
    Root endpoint that redirects to API documentation
    """
    return {"message": "Welcome to Agent API. Visit /docs for documentation"}


@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Uses the Chat Service from application layer
    """
    return {"message": "Chat request received"}


@app.post("/eval")
async def eval(request: EvalRequest):
    """
    Uses the Chat Service from application layer
    """
    return {"message": "Eval request received"}


@app.post("/eval")
async def ingest_documents(request: IngestDocumentsRequest):
    """
    Uses the Chat Service from application layer
    """
    return {"message": "Ingest documents request received"}


@app.post("/reset-memory")
async def reset_memory(request: ResetMemoryRequest):
    """
    Uses the Chat Service from application layer
    """
    return {"message": "Reset memory request received"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
