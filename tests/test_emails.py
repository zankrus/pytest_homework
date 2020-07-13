import logging

import pytest

from common.common import email_validator, write_to_file
from conftest import log_file_name


@pytest.mark.parametrize('email', (')dfdfg@mail.ru', 'fdfdfdfdf', 'fdfefef', '144@45454.ru'))
def test_correct_email(email,  log_file_name):
    if email_validator(email):
        write_to_file(log_file_name, email + ' success \n')
    else:
        write_to_file(log_file_name, email + ' failed \n')


@pytest.mark.parametrize('email', (')dfdfg@mail.ru', 'fdfdfdfdf', 'fdfefef', '144@45454.ru'))
def test_incorrect_email(email,  log_file_name):
    if email_validator(email):
        write_to_file(log_file_name, email + ' success \n')
    else:
        write_to_file(log_file_name, email + ' failed \n')
