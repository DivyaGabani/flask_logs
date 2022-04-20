import pytest
import os


def test_debug_file():
    """test for debug log file existence check"""
    root = os.path.dirname(os.path.abspath(__file__))
    database = os.path.join(root, '../app/logs/mydebug.log')
    assert os.path.exists(database) is True


def test_info_file():
    """test for myinfo log file existence check"""
    root = os.path.dirname(os.path.abspath(__file__))
    database = os.path.join(root, '../app/logs/myinfo.log')
    assert os.path.exists(database) is True