#coding=utf-8
#pylint: disable=invalid-name

"""
Тестирование по pytest
Обрати внимание, что test2.py файлом теста уже не считается

https://code.visualstudio.com/docs/python/unit-testing - настройка в vscode
https://habr.com/post/269759/ - статья про pytest
"""

import pytest
import mock

import main
from src.my_class import MyClass
from src.my_class import MAX_OPERATIONS

# = = = = = = = = = = = = = = = = = = = =
# Инициализация/финализация

def setup():
    """
        Инициализатор со значениями по умолчанию
        Вызывается перед выполнением каждой функции
        (не вызывается для методов класса)
    """
    print ("basic setup into module")

def teardown():
    """
        Финализатор со значениями по умолчанию
        Вызывается после выполнения каждой функции
        (не вызывается для методов класса)
    """
    print ("basic teardown into module")

def setup_module(module):
    " Выполняется при загрузке этого модуля"
    print("init " + module.__name__)

def teardown_module(module):
    " Выполняется при выгрузке модуля "
    print("teardown " + module.__name__)

def setup_function(function):
    """
        Аналогично setup() вызывается перед выполнением каждой функции
        (не вызывается для методов класса)
    """
    print ("function setup")

def teardown_function(function):
    """
        Аналогично setup() вызывается перед выполнением каждой функции
        (не вызывается для методов класса)
    """
    print ("function teardown")

# = = = = = = = = = = = = = = = = = = = =
# Тестирование

def test_mainSum():
    " test "
    print("test")
    assert main.mySum((1, 2)) == 3

def test_myClassLongUse():
    " test of MyClass.longUse() "
    obj = MyClass()
    assert (obj.longUse() == MAX_OPERATIONS)

def test_myClassMockLongUse():
    " test of MyClass.longUse() "
    obj = MyClass()
    obj.longUse = mock.MagicMock(return_value=MAX_OPERATIONS)
    assert (obj.longUse() == MAX_OPERATIONS)

class TestUM:
    def setup(self):
        """ Аналогично свободной setup(), выполняется перед каждым методом """
        print ("basic setup into class")

    def teardown(self):
        """ Аналогично свободному teardown(), выполняется после каждого метода """
        print ("basic teardown into class")

    def setup_class(cls):
        """ Аналогично setup_module(), выполняется один раз при инициализации класса """
        print ("class setup")

    def teardown_class(cls):
        """ Аналогично teardown_module(), выполняется один раз при финализации класса """
        print ("class teardown")

    def setup_method(self, method):
        """ Аналогично свободной setup_function(), выполняется перед каждым методом """
        print ("method setup")

    def teardown_method(self, method):
        """ Аналогично свободному teardown_function(), выполняется после каждого метода """
        print ("method teardown")

    def test_numbers_5_6(self):
        print "test 5*6"
        assert 5*6 == 30

    def test_strings_b_2(self):
        print "test b*2"
        assert 'b'*2 == 'bb'


# пример использования расширенных фикстур
@pytest.fixture()
def resource_setup(request):
    print("resource_setup")
    def resource_teardown():
        print("resource_teardown")
    request.addfinalizer(resource_teardown)

def test_1_that_needs_resource(resource_setup):
    print("test_1_that_needs_resource")

def test_2_that_does_not():
    print("test_2_that_does_not")

def test_3_that_does_again(resource_setup):
    print("test_3_that_does_again")
