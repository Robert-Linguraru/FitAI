from app.rag.chroma_service import ChromaService
from app.services.embedding_service import EmbeddingService
from app.services.workout_loader import load_workouts


def ingest_workouts() -> None:
    """Load workouts and store them in ChromaDB."""

    print("Loading workout knowledge base...")

    workouts = load_workouts()

    print(f"Loaded {len(workouts)} workout plans.")

    searchable_documents = [
        workout.to_searchable_text()
        for workout in workouts
    ]

    print("Generating embeddings...")

    embedding_service = EmbeddingService()

    embeddings = embedding_service.create_embeddings(
        searchable_documents
    )

    print("Opening ChromaDB collection...")

    chroma = ChromaService()

    print("Clearing previous documents...")

    chroma.reset()

    print("Saving workout vectors...")

    chroma.collection.add(
        ids=[
            workout.id
            for workout in workouts
        ],
        documents=searchable_documents,
        embeddings=embeddings,
        metadatas=[
            {
                "name": workout.name,
                "goal": workout.goal,
                "difficulty": workout.difficulty,
                "training_style": workout.training_style,
            }
            for workout in workouts
        ],
    )

    print()

    print(f"Successfully stored {chroma.count()} workouts.")


if __name__ == "__main__":
    ingest_workouts()