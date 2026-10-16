from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseChatModel, ParrotFakeChatModel
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class ModelCard(BaseModel):
    name: str
    context_window: int
    input_cost_usd_per_MTok: float
    output_cost_usd_per_MTok: float
    chat_client: type[BaseChatModel] | None = Field(None, exclude=True)
    deprecated: bool = Field(False)


__all__ = ("AVAILABLE_MODELS", "ModelCard")

_AVAILABLE_MODELS = [
    {
        "name": "langchain-debug",
        "context_window": 200_000_000,
        "input_cost_usd_per_MTok": 0.0,
        "output_cost_usd_per_MTok": 0.0,
        "chat_client": ParrotFakeChatModel,
    },
    {
        "name": "gpt-6-astra",
        "context_window": 128000,
        "input_cost_usd_per_MTok": 10,
        "output_cost_usd_per_MTok": 50,
        "chat_client": ChatOpenAI,
    },
    {
        "name": "gpt-6.1-sol",
        "context_window": 128000,
        "input_cost_usd_per_MTok": 2,
        "output_cost_usd_per_MTok": 10,
        "chat_client": ChatOpenAI,
    },
    {
        "name": "claude-opus-5-5",
        "context_window": 1_000_000,
        "input_cost_usd_per_MTok": 4.00,
        "output_cost_usd_per_MTok": 20.00,
        "chat_client": ChatAnthropic,
    },
    {
        "name": "claude-sonnet-5-5",
        "context_window": 1_000_000,
        "input_cost_usd_per_MTok": 2.00,
        "output_cost_usd_per_MTok": 10.00,
        "chat_client": ChatAnthropic,
    },
    {
        "name": "claude-haiku-5-5",
        "context_window": 1_000_000,
        "input_cost_usd_per_MTok": 0.10,
        "output_cost_usd_per_MTok": 0.50,
        "chat_client": ChatAnthropic,
    },
    {
        "name": "gpt-6-luna",
        "context_window": 128000,
        "input_cost_usd_per_MTok": 0.10,
        "output_cost_usd_per_MTok": 0.50,
        "chat_client": ChatOpenAI,
    },
    {
        "name": "claude-3-5-sonnet-20241022",
        "context_window": 200_000,
        "input_cost_usd_per_MTok": 3.00,
        "output_cost_usd_per_MTok": 15.00,
        "chat_client": ChatAnthropic,
        "deprecated": True,
    },
    {
        "name": "claude-3-haiku-20241022",
        "context_window": 200_000,
        "input_cost_usd_per_MTok": 1.00,
        "output_cost_usd_per_MTok": 5.00,
        "chat_client": ChatAnthropic,
        "deprecated": True,
    },
    {
        "name": "claude-3-haiku-20240307",
        "context_window": 200_000,
        "input_cost_usd_per_MTok": 0.25,
        "output_cost_usd_per_MTok": 1.25,
        "chat_client": ChatAnthropic,
        "deprecated": True,
    },
    {
        "name": "claude-3-opus-20240229",
        "context_window": 200000,
        "input_cost_usd_per_MTok": 15.00,
        "output_cost_usd_per_MTok": 75.00,
        "chat_client": ChatAnthropic,
        "deprecated": True,
    },
    {
        "name": "gpt-4o",
        "context_window": 128000,
        "input_cost_usd_per_MTok": 5.00,
        "output_cost_usd_per_MTok": 15.00,
        "chat_client": ChatOpenAI,
        "deprecated": True,
    },
    {
        "name": "gpt-4o-mini",
        "context_window": 128_000,
        "input_cost_usd_per_MTok": 0.15,
        "output_cost_usd_per_MTok": 0.60,
        "chat_client": ChatOpenAI,
        "deprecated": True,
    },
    {
        "name": "gpt-4",
        "context_window": 8192,
        "input_cost_usd_per_MTok": 30.00,
        "output_cost_usd_per_MTok": 60.00,
        "chat_client": ChatOpenAI,
        "deprecated": True,
    },
    {
        "name": "gpt-4-turbo",
        "context_window": 128000,
        "input_cost_usd_per_MTok": 10.00,
        "output_cost_usd_per_MTok": 30.00,
        "chat_client": ChatOpenAI,
        "deprecated": True,
    },
]

AVAILABLE_MODELS: dict[str, ModelCard] = {
    model["name"]: ModelCard(**model) for model in _AVAILABLE_MODELS
}
