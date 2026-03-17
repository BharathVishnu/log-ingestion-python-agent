import faiss
import numpy as np
import pickle
from vector_store.embeddings import get_embedding

INDEX_FILE = "app/vector.index"
META_FILE = "app/vector_meta.pkl"

DIM = 384 


def load_store():

    try:
        index = faiss.read_index(INDEX_FILE)

        with open(META_FILE, "rb") as f:
            metadata = pickle.load(f)

    except:
        index = faiss.IndexFlatL2(DIM)
        metadata = []

    return index, metadata


def save_store(index, metadata):

    faiss.write_index(index, INDEX_FILE)

    with open(META_FILE, "wb") as f:
        pickle.dump(metadata, f)


def add_to_store(log, parsed, regex):

    index, metadata = load_store()

    emb = get_embedding(log)

    index.add(np.array([emb]).astype("float32"))

    metadata.append({
        "log": log,
        "parsed": parsed,
        "regex": regex
    })

    save_store(index, metadata)


def search_similar(log, threshold=0.7):

    index, metadata = load_store()

    if len(metadata) == 0:
        return None

    emb = get_embedding(log)

    D, I = index.search(np.array([emb]).astype("float32"), k=1)

    distance = D[0][0]
    idx = I[0][0]

    # lower distance = better match
    if distance < threshold:
        return metadata[idx]

    return None