# MSFT Volatility Analyzer

A Python-based data utility designed to ingest historical Microsoft (MSFT) stock data, store it in a relational database, and calculate market volatility through price spread analysis.

## Project Goal
The primary objective of this script is to transform raw CSV stock data into actionable insights by identifying the most volatile trading days in Microsoft's history. By calculating the percentage difference between daily highs and lows, the tool provides a snapshot of historical intraday price swings, useful for risk assessment or algorithmic backtesting.

## Features

* **Persistent Storage**: Migrates flat CSV data into a structured SQLite database (`msft_high_lowdb.sqlite`) for faster querying and long-term storage.

* **Dynamic Data Ingestion**: Uses a flexible input prompt to handle different file names or paths at runtime.

* **Automated Schema Management**: Automatically resets the database table on each run to prevent data duplication while ensuring the schema is always up to date.

* **Statistical Sorting**: Leverages SQL `ORDER BY` and `LIMIT` clauses to instantly isolate the top 10 most volatile records from potentially thousands of rows.

## Built With

* **Python 3.x**: The core programming language used for logic and data orchestration.

* **SQLite3**: A lightweight, disk-based database engine used for data persistence and relational queries.

* **CSV Module**: Specifically `csv.DictReader`, utilized to map information directly to dictionary keys based on the file's header row.

## Key Achievements in Code

* **Robust Data Parsing**: By implementing `csv.DictReader`, the code avoids "magic numbers" or index-based errors (e.g., `row[1]`). This makes the script more resilient if the input CSV column order changes.

* **Calculated Fields via Real-Time Processing**: The spread calculation is performed during the transition from CSV to SQL:

$$spread = \frac{high − low}{low}$$

* **Professional CLI Formatting**: The output uses f-string alignment (`:<20`) and percentage formatting (`:.2%`) to create a clean, readable terminal dashboard that mirrors a professional financial report.

* **Efficient Memory Management**: The script processes data row-by-row and utilizes a database cursor, ensuring it can handle large historical datasets without exhausting system memory.
