import json
import itertools


def generate_diff(file_path1, file_path2):
    result_diff = []
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    sorted_keys = sorted(set.union(set(file1), set(file2)))
    for key in sorted_keys:
        if key not in file1:
            result_diff.append(f" {key}: {file2[key]}")
        elif key not in file2:
            result_diff.append(f"- {key}: {file1[key]}")
        elif file1[key] == file2[key]:
            result_diff.append(f"  {key}: {file1[key]}")
        else:
            result_diff.append(f"- {key}: {file1[key]}")
            result_diff.append(f"+ {key}: {file2[key]}")
    result_string = '\n'.join(itertools.chain('{', result_diff, '}'))
    return result_string
