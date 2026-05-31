from src.core import validate_csv_path, load_csv_to_list

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