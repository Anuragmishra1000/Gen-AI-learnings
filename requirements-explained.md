# Requirements Explained

Short reference for packages in `requirements.txt`.

## LangChain Core

| Package | Description |
|---------|-------------|
| **langchain** | High-level framework for building LLM apps (chains, agents, tools, memory). |
| **langchain-core** | Shared primitives: messages, runnables, prompts, output parsers. Other `langchain-*` packages depend on it. |

## OpenAI Integration

| Package | Description |
|---------|-------------|
| **langchain-openai** | LangChain adapters for OpenAI models (ChatGPT, embeddings, etc.). |
| **openai** | Official OpenAI Python SDK (API calls, streaming, etc.). Used under the hood by `langchain-openai`. |

## Anthropic Integration

| Package | Description |
|---------|-------------|
| **langchain-anthropic** | LangChain integration for Claude (Anthropic’s API). |

## Google Gemini Integration

| Package | Description |
|---------|-------------|
| **langchain-google-genai** | LangChain integration for Google’s Gemini models. |
| **google-generativeai** | Google’s SDK for the Generative AI API (Gemini). Used by the LangChain Google package. |

## Hugging Face Integration

| Package | Description |
|---------|-------------|
| **langchain-huggingface** | LangChain integration for Hugging Face models (local or hosted). |
| **transformers** | Hugging Face library to load and run transformer models (BERT, Llama, etc.). |
| **huggingface-hub** | Download/upload models and datasets from the Hugging Face Hub. |

## Environment Variable Management

| Package | Description |
|---------|-------------|
| **python-dotenv** | Loads variables from a `.env` file into the environment (e.g. `OPENAI_API_KEY`). |

## Machine Learning Utilities

| Package | Description |
|---------|-------------|
| **numpy** | Numerical arrays; common dependency for ML/data code. |
| **scikit-learn** | Classic ML (classification, clustering, metrics). Often used for embeddings similarity, preprocessing, or small ML tasks alongside LangChain. |

## Summary

LangChain plus provider plugins (OpenAI, Anthropic, Google, Hugging Face), env loading for API keys, and basic ML/numeric libraries for supporting code.
