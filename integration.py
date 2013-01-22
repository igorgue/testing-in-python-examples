#!/usr/bin/env python

from mock import patch
from mock import Mock

from example import get_transaction, save_transaction

def test_save_transaction_to_db():
    @patch('example.get_database')
    def test(get_database):
        database_mock = Mock()
        database_mock.__setitem__ = Mock(return_value=None)

        get_database.return_value = database_mock

        assert save_transaction('fds', '$12.00', False) == None
