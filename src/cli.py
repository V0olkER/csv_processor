
import argparse
from src.core import load_csv_to_list

def main():
    
    parser = argparse.ArgumentParser(description="Утилита для чтения CSV-файлов")
    
    parser.add_argument(
        "--input",           
        type=str,
        required=True,   
        help="Путь к CSV-файлу"
    )
    
    
    args = parser.parse_args()
    
    data = load_csv_to_list(args.input)
        
    for row in data:
        print(row)

if __name__ == "__main__":
    main()