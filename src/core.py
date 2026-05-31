import os
import csv

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

