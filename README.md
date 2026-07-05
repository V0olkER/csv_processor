# CSV Processor

[🇷🇺 Русский](https://github.com/V0olkER/csv_processor/blob/main/README.md#-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9) | [🇬🇧 English](https://github.com/V0olkER/csv_processor/blob/main/README.md#-english)

---

## 🇷🇺 Русский

CLI-утилита для предобработки CSV-файлов:

- Обрезка пробелов в ячейках  
- Удаление полностью пустых строк  
- Проверка согласованности числа столбцов  

### Установка

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

### Использование

Чтение и вывод в консоль:

```bash
python -m src.cli --input data/sample.csv
```

Сохранение результата:

```bash
python -m src.cli --input data/raw.csv --output data/clean.csv
```

### Тесты

```bash
pytest
```

---

## 🇬🇧 English

CLI utility for CSV preprocessing:

- Strips whitespace from cells  
- Removes completely empty rows  
- Validates column count consistency  

### Installation

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

### Usage

Read and print to console:

```bash
python -m src.cli --input data/sample.csv
```

Save cleaned output:

```bash
python -m src.cli --input data/raw.csv --output data/clean.csv
```

### Tests

```bash
pytest
```
