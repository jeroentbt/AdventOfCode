from solution import *

def test_start_at_root():
    fs = Filesystem()
    assert "/" == fs.pwd()


def test_go_to_root():
    fs = Filesystem()
    fs.command("cd /")
    assert "/" == fs.pwd()


def test_create_dir_on_visit():
    fs = Filesystem()
    print(fs)
    fs.command("cd a")
    assert "a" == fs.pwd()
