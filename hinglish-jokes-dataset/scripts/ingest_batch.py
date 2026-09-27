import sys
import os
import json

sys.path.append(os.path.dirname(__file__))
from dataset_manager import DatasetManager

def ingest_batch(category_id, candidate_jokes, source_info):
    dm = DatasetManager()
    acc, dup = dm.ingest_category_jokes(category_id, candidate_jokes, source_info)
    dm.save_all()
    dm.update_progress_file()
    print(f"Ingested category {category_id}: {acc} accepted, {dup} duplicates.")
    return acc, dup

if __name__ == "__main__":
    if len(sys.argv) > 1:
        batch_file = sys.argv[1]
        with open(batch_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        ingest_batch(data["category_id"], data["candidate_jokes"], data["source_info"])
