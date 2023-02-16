from gendiff.diff import generate_diff


def test_gendiff_json():
    file1_path = '.tests/fixtures/file1.json'
    file2_path = '.tests/fixtures/file2.json'
    result = generate_diff(file1_path, file2_path)
    output = open('.tests/fixtures/output.txt')

    assert result == output.read()


def test_gendiff_yml():
    file1_path = '.tests/fixtures/file1.yml'
    file2_path = '.tests/fixtures/file2.yml'
    result = generate_diff(file1_path, file2_path)
    output = open('.tests/fixtures/output.txt')

    assert result == output.read()
