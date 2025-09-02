from pydantic import BaseModel


# Example Pydantic models for the API (one for each service in the application layer)

class ChatRequest(BaseModel):
    pass

class EvalRequest(BaseModel):
    pass

class IngestDocumentsRequest(BaseModel):
    pass

class ResetMemoryRequest(BaseModel):
    pass