from app.repositories.chat_messages import ChatMessagesRepository
from app.services.openrouter_client import OpenRouterClient


class ChatUseCase:
    def __init__(
        self,
        messages_repository: ChatMessagesRepository,
        openrouter_client: OpenRouterClient,
    ) -> None:
        self._messages_repository = messages_repository
        self._openrouter_client = openrouter_client

    async def ask(
        self,
        *,
        user_id: int,
        prompt: str,
        history_limit: int = 20,
        system_instruction: str | None = None,
    ) -> str:
        messages: list[tuple[str, str]] = []

        if system_instruction:
            messages.append(("system", system_instruction))

        history = await self._messages_repository.get_last_messages(
            user_id=user_id,
            limit=history_limit,
        )

        for message in reversed(history):
            messages.append((message.role, message.content))

        messages.append(("user", prompt))

        await self._messages_repository.add_message(
            user_id=user_id,
            role="user",
            content=prompt,
        )

        answer = await self._openrouter_client.chat_completion(messages)

        await self._messages_repository.add_message(
            user_id=user_id,
            role="assistant",
            content=answer,
        )

        return answer

    async def get_history(self, *, user_id: int, limit: int = 100):
        history = await self._messages_repository.get_last_messages(
            user_id=user_id,
            limit=limit,
        )
        return list(reversed(history))

    async def clear_history(self, *, user_id: int) -> None:
        await self._messages_repository.delete_all_for_user(user_id)