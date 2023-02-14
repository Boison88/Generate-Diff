from diff import generate_diff


def test_gendiff():
    file1_path = '/home/boison/python-project-50/tests/fixtures/file1.json'
    file2_path = '/home/boison/python-project-50/tests/fixtures/file2.json'
    result = generate_diff(file1_path, file2_path)
    output = '\n'.join([
        '{',
        '- follow: false',
        '  host: hexlet.io',
        '- proxy: 123.234.53.22',
        '- timeout: 50',
        '+ timeout: 20',
        '+ verbose: true',
        '}'
    ])
    assert result == output
