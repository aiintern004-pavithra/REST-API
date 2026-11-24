from fastapi import APIRouter
from uuid import uuid4

from app.models.chat import ChatRequest, ChatResponse
from app.services.ai_service import generate_reply

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    session_id = request.session_id or str(uuid4())

    reply = generate_reply(request.message)

    return ChatResponse(
        reply=reply,
        session_id=session_id,
        success=True
    )