#!/usr/bin/python3

def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        max_score = max(a_dictionary.values()) if a_dictionary else None
        if max_score:
            for key, value in a_dictionary.items():
                if value == max_score:
                    return key
    return None
