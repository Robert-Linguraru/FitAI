# FitAI 🏋️‍♂️

FitAI is an AI-powered personal fitness coach that recommends workout plans based on a user's goals using **Retrieval Augmented Generation (RAG)** and **OpenAI Tool Calling**.

The application allows users to ask questions in natural language, such as:

- "I want to lose weight but only have 30 minutes."
- "Recommend a beginner dumbbell workout."
- "I want to build muscle at home."

FitAI uses semantic search to retrieve relevant workout plans from a local knowledge base before generating personalized recommendations with OpenAI.

## Tech Stack

### Frontend
- React
- TypeScript
- Vite

### Backend
- Python
- FastAPI
- OpenAI API
- ChromaDB

### Development
- Docker
- Docker Compose
- Rancher Desktop

## Project Structure

```text
fit-ai/
├── backend/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── compose.yaml
├── README.md
└── .gitignore
```

## Running the Project

```bash
docker compose up --build
```

Backend:

```
http://localhost:8000
```

Frontend:

```
http://localhost:5173
```

## Project Status

Finished 

This project is being developed as part of an AI engineering assignment to demonstrate:

- Retrieval Augmented Generation (RAG)
- Semantic Search
- OpenAI Embeddings
- ChromaDB
- OpenAI Tool Calling
- React + FastAPI application architecture