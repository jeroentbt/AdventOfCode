from solution import *


def test_go_to_root():
    fs = Filesystem()
    fs.cd("/")
    assert "/" == fs.cwd


def test_create_dir():
    fs = Filesystem()
    fs.mkdir("a")
    assert {"/": 0, "/a/": 0} == fs.tree


def test_move_down_one_dir():
    fs = Filesystem()
    fs.mkdir("a")
    fs.cd("a")
    assert "/a/" == fs.cwd


def test_add_file():
    fs = Filesystem()
    fs.touch("testfile", 10)
    assert {"/": 0, "/testfile": 10} == fs.tree


def test_move_up_one_dir():
    fs = Filesystem()
    fs.cwd = "/a/b/"
    fs.cd("..")
    assert "/a/" == fs.cwd


test_input = ["$ cd /",
              "$ ls",
              "dir a",
              "14848514 b.txt",
              "8504156 c.dat",
              "dir d",
              "$ cd a",
              "$ ls",
              "dir e",
              "29116 f",
              "2557 g",
              "62596 h.lst",
              "$ cd e",
              "$ ls",
              "584 i",
              "$ cd ..",
              "$ cd ..",
              "$ cd d",
              "$ ls",
              "4060174 j",
              "8033020 d.log",
              "5626152 d.ext",
              "7214296 k"]


def test_verify_example_tree():
    fs = read_output(test_input)
    print(fs)
    assert 14 == len(fs.tree)


def test_part1():
    fs = read_output(test_input)
    assert 95437 == part_one_count(fs)
