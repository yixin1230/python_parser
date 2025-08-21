import pytest
from python_parser import PythonParser

@pytest.fixture
def parser():
    return PythonParser("https://docs.clustervision.com", max_depth=3)

class TestForForFor:
    def test_output_not_empty_and_unique(self, capsys, parser):
        parser.python_parser_for_for_for() 
        captured = capsys.readouterr()
        assert captured is not None
        lines = captured.out.splitlines()
        assert len(lines) == len(set(lines))

class TestRecrusion:
    def test_output_not_empty_and_unique(self, capsys, parser):
        parser.python_parser_recursion() 
        captured = capsys.readouterr()
        assert captured is not None
        lines = captured.out.splitlines()
        assert len(lines) == len(set(lines))

class TestBFS:
    def test_output_not_empty_and_unique(self, capsys, parser):
        parser.python_parser_bfs() 
        captured = capsys.readouterr()
        assert captured is not None
        lines = captured.out.splitlines()
        assert len(lines) == len(set(lines))

