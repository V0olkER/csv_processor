
import argparse
from src.core import load_csv_to_list
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def main():
    
    parser = argparse.ArgumentParser(description="Утилита для чтения CSV-файлов")
    parser.add_argument(
        "--input",           
        type=str,
        required=True,   
        help="Путь к CSV-файлу"
    )
    args = parser.parse_args()

    try:
        data = load_csv_to_list(args.input)
        logger.info(f"Успешно прочитан файл {args.input}. Строк: {len(data)}")
        for row in data:
            print(row)

    except Exception as e:
        logger.error(f"Ошибка в строке {e}")
        exit(1)

if __name__ == "__main__":
    main()