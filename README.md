# Gen AI Learning Journey — LangChain

A hands-on repo for learning **Generative AI** with **LangChain** as the starting point. The goal is to go from basic LLM calls to building small, practical apps using multiple model providers.

## What I'm Learning

- **LangChain basics** — prompts, chains, chat models, output parsers
- **Multi-provider setup** — OpenAI, Anthropic (Claude), Google Gemini, Hugging Face
- **Practical patterns** — env-based API keys, embeddings, simple ML utilities
- **Next steps** — agents, RAG, memory, and small end-to-end projects

## Setup

```bash
# Create and activate virtual environment (macOS)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the project root for API keys:

```env
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

## Project Structure

```
langchain_models/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── requirements-explained.md # What each package does
└── venv/                     # Local virtual environment
```

## Dependencies

See [requirements-explained.md](./requirements-explained.md) for a short description of every package in `requirements.txt`.

## Learning Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| 1 | Environment setup & first LLM call | In progress |
| 2 | Prompts, chains, and chat models | Planned |
| 3 | Embeddings & vector search (RAG) | Planned |
| 4 | Agents & tools | Planned |
| 5 | Mini project (e.g. Q&A bot or summarizer) | Planned |

## Resources

- [LangChain Docs](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
