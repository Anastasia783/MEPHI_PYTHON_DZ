from fastapi import APIRouter, Depends, Response, status

from app.api.deps import get_chat_usecase, get_current_user_id
from app.schemas.chat import ChatMessageResponse, ChatRequest, ChatResponse
from app.usecases.chat import ChatUseCase


router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    user_id: int = Depends(get_current_user_id),
    chat_usecase: ChatUseCase = Depends(get_chat_usecase),
) -> ChatResponse:
    answer = await chat_usecase.ask(
        user_id=user_id,
        prompt=request.prompt,
    )
    return ChatResponse(answer=answer)


@router.get("/history", response_model=list[ChatMessageResponse])
async def get_history(
    user_id: int = Depends(get_current_user_id),
    chat_usecase: ChatUseCase = Depends(get_chat_usecase),
) -> list[ChatMessageResponse]:
    messages = await chat_usecase.get_history(user_id=user_id)
    return [ChatMessageResponse.model_validate(message) for message in messages]


@router.delete("/history", status_code=status.HTTP_204_NO_CONTENT)
async def clear_history(
    user_id: int = Depends(get_current_user_id),
    chat_usecase: ChatUseCase = Depends(get_chat_usecase),
) -> Response:
    await chat_usecase.clear_history(user_id=user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)