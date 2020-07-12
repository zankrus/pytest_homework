import logging

import pytest

#
# @pytest.fixture()
# def method_decorator(func):
#     with open('loger', 'w') as file:
#         file.write('Test')
#         yield func
#         file.write()


@pytest.fixture()
def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
        file.close()
