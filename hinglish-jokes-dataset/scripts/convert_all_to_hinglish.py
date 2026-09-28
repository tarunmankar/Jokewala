# -*- coding: utf-8 -*-
"""
Converts all Hindi (Devanagari) jokes in jokes-master.json to natural, colloquial Hinglish.
Retains original Hindi text in 'hindi_content' field so no source fidelity is lost.
"""

import os
import json
from hindi_to_hinglish import hindi_to_hinglish
from dataset_manager import DatasetManager

def convert_dataset_to_hinglish():
    dm = DatasetManager()
    total = len(dm.master_jokes)
    converted_count = 0
    already_hinglish = 0

    for joke in dm.master_jokes:
        raw_source = joke.get("hindi_content") or joke["content"]
        has_devanagari = any('\u0900' <= c <= '\u097f' for c in raw_source)
        if has_devanagari:
            if "hindi_content" not in joke:
                joke["hindi_content"] = raw_source
            hinglish_text = hindi_to_hinglish(raw_source)
            joke["content"] = hinglish_text
            joke["language"] = "hinglish"
            converted_count += 1
        else:
            joke["language"] = "hinglish"
            already_hinglish += 1

    print(f"Total jokes: {total}")
    print(f"Converted from Hindi to Hinglish: {converted_count}")
    print(f"Already pure Hinglish: {already_hinglish}")

    # Save to master and exports
    dm.save_all()
    dm.update_progress_file()
    print("Dataset saved and exported successfully.")

if __name__ == "__main__":
    convert_dataset_to_hinglish()
