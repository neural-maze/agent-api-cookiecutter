from pydantic import BaseModel


class ChatRequest(BaseModel):
    pass


class EvalRequest(BaseModel):
    pass


class IngestDocumentsRequest(BaseModel):
    pass


class ResetMemoryRequest(BaseModel):
    pass
