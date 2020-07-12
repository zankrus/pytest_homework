import logging

import pytest

from common.common import email_validator


@pytest.mark.parametrize('email', (')dfdfg@mail.ru', 'fdfdfdfdf', 'fdfefef', '144@45454.ru'))
def test_correct_email(email):
    assert email_validator(email)


@pytest.mark.parametrize('email', (')dfdfg@mail.ru', 'fdfdfdfdf', 'fdfefef', '144@45454.ru'))
def test_incorrect_email(caplog,email):
    caplog.set_level(logging.INFO)
    assert not email_validator(email)
