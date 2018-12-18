#coding=utf-8

""" Учимся тестировать с применением моков """

MAX_OPERATIONS = 100000

class MyClass(object):
    """ Класс, на котором будет проводиться тестирование """

    def __init__(self):
        self.member = 1
        # print("initialize %s" % self.member)

    def use(self):
        """ Типа мы используем класс """
        print(self.member)

    def longUse(self):
        """ Типа долгая операция """
        a = 0
        for i in range(MAX_OPERATIONS):
            # print(i)
            a = i

        return a + 1
