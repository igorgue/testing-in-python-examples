import subprocess

def test_get_transaction():
    assert subprocess.check_output(['./example.py', '1']) == '$0.99\n'
    assert subprocess.check_output(['./example.py', '2']) == '$9.99\n'
    assert subprocess.check_output(['./example.py', '3']) == '$2.99\n'
