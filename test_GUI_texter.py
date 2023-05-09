# TODO ALL test functions if wanted. Likely not necessary, though as we can't test GUI 
# commands and anything else to test is super basic anyways.s

import pytest
from GUI_texter import get_names_numbers, send_text

def test_get_names_numbers():
    test_data = get_names_numbers('path_to_your_test_csv_file.csv')
    expected_output = [
        # Expected output based on the test CSV file
        ['John', '1234567890'],
        ['Jane', '0987654321']
    ]
    assert test_data == expected_output, "Expected output does not match the returned data."
    

@pytest.mark.parametrize("csv_file_path", ["non_existing_path.csv", 123, None, ""])
def test_get_names_numbers_with_invalid_path(csv_file_path):
    with pytest.raises(Exception) as e:
        get_names_numbers(csv_file_path)
    assert str(e.value) == "[-] Unable to read and extract from CSV file. Exiting...", "Expected specific exception message"

