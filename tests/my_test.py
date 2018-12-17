#coding=utf-8
#pylint: disable=invalid-name

"""
Тестирование по pytest
Обрати внимание, что test2.py файлом теста уже не считается

https://code.visualstudio.com/docs/python/unit-testing - настройка в vscode
https://habr.com/post/269759/ - статья про pytest
"""

import pytest
import main


def setup_module():
    " init_something "
    pass

def teardown_module(module):
    " teardown_something "
    pass

def test_mainSum():
    " test "
    assert main.mySum((1, 2)) == 3
