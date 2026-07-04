import pytest
from src.core import validate_csv_path, load_csv_to_list, clean_csv_data, CSVProcessor

def test_wrong_extension():
    assert validate_csv_path("report.txt") == False
    assert validate_csv_path("data.scv") == False

def test_nonexistent_csv():
    assert validate_csv_path("missing.csv") == False

def test_load_valid_csv():
    data = load_csv_to_list('data/sample.csv')
    
    expected = [
        ["name", "age"],
        ["Alice", "30"],
        ["Bob", "25"]
    ]
    
    # Проверяем точное совпадение
    assert data == expected

def test_clean_csv_data():
    raw = [
        [" name ", " age "],
        [" Alice ", " 30 "],
        ["", ""],
        ["Bob", "25"]
    ]
    cleaned = clean_csv_data(raw)
    expected = [
        ["name", "age"],
        ["Alice", "30"],
        ["Bob", "25"]
    ]
    assert cleaned == expected

def test_csvprocessor_valid_file():
    processor = CSVProcessor("data/sample.csv")
    data = processor.read()
    assert len(data) == 3
    assert data[1] == ["Alice", "30"]

def test_csvprocessor_invalid_file():
    with pytest.raises(FileNotFoundError):
        CSVProcessor("nonexistent.csv")

def test_csvprocessor_save(tmp_path):
    processor = CSVProcessor("data/sample.csv")
    processor.read()  
    output_file = tmp_path / "output.csv"
    processor.save(str(output_file))
    assert output_file.exists()