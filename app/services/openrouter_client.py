from typing import Any, Literal

import httpx

from app.core.config import settings
from app.core.errors import ExternalServiceError


ChatRole = Literal["system", "user", "assistant"]


class OpenRouterClient:
    def __init__(self) -> None:
        self._base_url = settings.openrouter_base_url.rstrip("/")
        self._api_key = settings.openrouter_api_key
        self._model = settings.openrouter_model
        self._site_url = settings.openrouter_site_url
        self._app_name = settings.openrouter_app_name
        self._timeout = settings.openrouter_timeout 

    async def chat_completion(
        self,
        messages: list[tuple[ChatRole, str]],
    ) -> str:
        """
        messages: список кортежей (role, content)
        """
        url = f"{self._base_url}/chat/completions"

        headers = {
            "Authorization": f"Bearer {self._api_key}",  
            "Content-Type": "application/json",
            "HTTP-Referer": self._site_url,              
            "X-Title": self._app_name,                   
        }

        payload: dict[str, Any] = {
            "model": self._model,                       
            "messages": [
                {"role": role, "content": content}
                for role, content in messages           
            ],
        }

        async with httpx.AsyncClient(timeout=self._timeout) as client:
            response = await client.post(url, headers=headers, json=payload)

        
        if response.status_code >= 400:
            try:
                data = response.json()
                print(f"DEBUG OpenRouter error: {response.status_code} {data}")
                msg = (
                    data.get("error", {}).get("message")
                    or data.get("message")
                    or "OpenRouter request failed"
                )
            except Exception:
                msg = f"OpenRouter request failed with status {response.status_code}"
            raise ExternalServiceError(msg)

        data = response.json()
        
        try:
            return data["choices"][0]["message"]["content"]
        except Exception as exc:
            raise ExternalServiceError("Unexpected OpenRouter response format") from exc