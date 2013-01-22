#!/usr/bin/env python

from mock import patch
from mock import Mock

from example import get_transaction, save_transaction

def test_get_transaction():
    @patch('example.get_database')
    def test(get_database):
        database_mock = Mock()
        database_mock.__getitem__ = Mock(return_value='$20.33')
        database_mock.close = Mock(return_value=None)

        get_database.return_value = database_mock

        assert get_transaction('mocked_transaction_id') == '$20.33'

        get_database.assert_called_with()
        database_mock.__getitem__.assert_called_with('mocked_transaction_id')

    test()

def test_save_transaction():
    @patch('example.save_to_db')
    def test(save_to_db):
        save_to_db.return_value = None

        save_transaction('mock_transaction_id', '$23.22')

        save_to_db.assert_called_with(key='mock_transaction_id', value='$23.22', print_result=True)

        assert save_transaction(transaction_id=None, value='$44.99') is None

        save_to_db.assert_called_with(key=None, value='$44.99', print_result=True)

    test()
