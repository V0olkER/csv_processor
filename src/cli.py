import argparse
import logging
from src.core import CSVProcessor  

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="CLI-утилита предобработки CSV")
    parser.add_argument("--input", required=True, help="Путь к входному CSV")
    parser.add_argument("--output", help="Путь для сохранения очищенного CSV")  # ← новый флаг
    args = parser.parse_args()

    logger.info(f"Начало обработки: {args.input}")
    
    try:
        # Создаём объект-процессор
        processor = CSVProcessor(args.input)  
        
        # Читаем и очищаем данные
        cleaned_data = processor.read() 
        
        # Выводим результат в консоль
        for row in cleaned_data:
            print(row)
        
        
        if args.output:  
            processor.save(args.output)  
            logger.info(f"Результат сохранён: {args.output}")
            
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        exit(1)

if __name__ == "__main__":  
    main()