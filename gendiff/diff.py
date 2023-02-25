from gendiff.json_parser import convert_json
from gendiff.yaml_parser import convert_yaml
from gendiff.parser import parse
from gendiff.formater import stylish


def generate_diff(file_path1, file_path2, format=stylish):
    if file_path1.endswith('json') and file_path2.endswith('json'):
        file1, file2 = convert_json(file_path1, file_path2)
    else:
        file1, file2 = convert_yaml(file_path1, file_path2)

    difference_dictionary = parse(file1, file2)
    return format(difference_dictionary)
