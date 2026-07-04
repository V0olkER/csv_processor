import os
import csv

class CSVProcessor:
    def __init__(self, path: str):
        if not validate_csv_path(path):
            raise FileNotFoundError(f"Некорректный CSV-файл: {path}")
        self.path = path
        self.cleaned_data: list[list[str]] =  None

    def read(self) -> list[list[str]]:
        raw_data = load_csv_to_list(self.path)
        self.cleaned_data = clean_csv_data(raw_data)
        return self.cleaned_data

    def save(self, output_path: str) -> None:
        """Сохраняет self.cleaned_data в CSV-файл по output_path."""
        if self.cleaned_data is None:
            raise ValueError("Нет данных для сохранения. Сначала вызовите .read().")
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(self.cleaned_data)

def validate_csv_path(path: str) -> bool:
    if not path.endswith('.csv'):
        return False
    if not os.path.isfile(path):
        return False
    
    return True


def load_csv_to_list(path: str) -> list[list[str]]:
     
    """
    Читает CSV-файл и возвращает его содержимое как список списков строк.
    
    Args:
        path: Путь к CSV-файлу
        
    Returns:
        Список строк, где каждая строка — список ячеек
    """
    if not validate_csv_path(path):
        raise FileNotFoundError(f"Файл {path} не найден или не является CSV")
     
    with open(path, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            return list(reader)
    
def clean_csv_data(raw_data: list[list[str]]) -> list[list[str]]:
    """
    Выполняет базовую предобработку данных:
    - обрезает пробелы
    - удаляет пустые строки
    - проверяет согласованность столбцов
    
    Args:
        raw_data: Сырые данные из CSV (результат csv.reader)
        
    Returns:
        Очищенные данные
    """
    if not raw_data:
        return []
    
    expected_cols = len(raw_data[0])
    
    cleaned = []
    
    for row in raw_data:
        
        stripped_row = [cell.strip() for cell in row]
        
        
        if all(cell=='' for cell in stripped_row):
            continue
        
        
        if len(stripped_row) != expected_cols:
            raise ValueError(f'Несогласованные столбцы: ожидалось {expected_cols}, получено {len(stripped_row)}')
        
        cleaned.append(stripped_row)
    
    return cleaned

if __name__ == "__main__":
    # validate_csv_path
    print("Проверка функции validate_csv_path:")
    print("report.csv →", validate_csv_path("report.csv"))      
    print("data.txt →", validate_csv_path("data.txt"))          
    print("valid.scv →", validate_csv_path("valid.scv"))  
    # load_csv_to_list
    print("\nПроверка load_csv_to_list:")
    try:
        data = load_csv_to_list("data/sample.csv")
        for row in data:
            print(row)
    except Exception as e:
        print("Ошибка:", e)

