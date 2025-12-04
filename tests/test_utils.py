from unittest.mock import patch, mock_open
from src.utils import get_file_operation
import json


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}, {"id": 2}]')
def test_valid_json(mock_file):
    result = get_file_operation('valid_file.json')
    assert result == [{"id": 1}, {"id": 2}]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_open):
    result = get_file_operation('wrong_path.json')
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data='')
def test_empty_file(mock_file):
    result = get_file_operation('empty_file.json')
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data='invalid json')
def test_invalid_json(mock_file):
    result = get_file_operation('invalid_file.json')
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data='{}')
@patch("json.load", return_value={})  # для случая, когда файл не содержит список
def test_file_not_list(mock_json_load, mock_file):
    result = get_file_operation('empty_file.json')
    assert result == []
