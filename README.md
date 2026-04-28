# Web Scraping Project

- A modular, multi-component web scraping architecture built in Python.
-  This project demonstrates advanced web scraping techniques, project structuring
-  - the creation of Command Line Interfaces (CLI) and API wrappers around core data extraction logic.

## Project Architecture

The project is thoughtfully divided into logical, decoupled components:

1. **`scraping/` (Core Package)**: The heart of the project. It contains the actual web scraping logic.
   - **`Wiki/` Module**: A specialized Wikipedia scraper designed to extract complex data about MMA Fighters (such as their opponents, biographical data, and fight attributes like height/weight using Regex). It uses `BeautifulSoup` and `Parsel` (XPATH/CSS Selectors).
   - **Dynamic Execution**: Contains `run.py`, `output.py`, and `importer.py` which allow executing specific scraper modules dynamically & handling data output.
2. **`scraping-cli/`**: A CLI wrapper that exposes the core scraping functionality to the terminal. It provides console scripts like `scrape-cli` to run scrapers and `scrape-import` to add new custom scrapers dynamically via text.
3. **`scraping-api/`**: An API layer that exposes the scraping capabilities over HTTP.

## Setup & Installation

The project uses modular `setup.py` configurations.

1. **Activate your Virtual Environment**:
   ```bash
   # Windows
   .\venv\Scripts\activate
   ```

2. **Install Core Package**:
   ```bash
   cd scraping
   pip install -e .
   ```

3. **Install CLI Wrapper** (Optional):
   ```bash
   cd ../scraping-cli
   pip install -e .
   ```

4. **Install API Wrapper** (Optional):
   ```bash
   cd ../scraping-api
   pip install -e .
   ```

## Usage (CLI)

Once installed, the CLI tool interacts with the core package modules:

```bash
# General Syntax
scrape-cli <module_name> <target> <url> <output_name>

# Example: Scrape opponent information from a Wikipedia Fighter page
scrape-cli Wiki oppon+info "https://en.wikipedia.org/wiki/Fighter_Name" output_data
```

You can also dynamically import new scrapers from a text file into the package:
```bash
scrape-import MyNewScraper path/to/file.txt
```

## Sample Output
The scrapers are capable of extracting clean, structured JSON data. Examples in the repository include `output.json`, which demonstrates extracting structured recipe blocks (title, description, difficulty). The core Wikipedia scrapers dump detailed player biographical statistics.

---

## Learning Outcomes & Technologies Mastered

Building this project provided deep, hands-on experience with advanced Python and Data Extraction concepts:

* **Web Scraping Libraries**: 
  * Mastered **`BeautifulSoup`** for robust HTML parsing and traversal.
  * Utilized **`Parsel`** (`Selector`) to leverage powerful XPath syntax for precise targeted data extraction, a technique widely used in production frameworks like Scrapy.
* **Advanced Text Processing**:
  * Implemented **Regular Expressions (`re`)** to parse complex, messy text nodes (e.g., converting mixed metric/imperial height and weight strings into clean JSON objects).
  * Used `dateparser` to interpret arbitrary human-readable birthdate strings into standardized date formats.
* **Software Architecture & Packaging**:
  * Learned how to structure a Python project into a core library with `setuptools` (`setup.py`).
  * Created CLI entry points (`console_scripts`) to make the package accessible from the terminal.
  * Decoupled the Core Logic from CLI and API boundaries, promoting reusability and clean maintainability.
* **Dynamic Loading & Reflection**: Implemented dynamic module routing based on command-line arguments using built-in `sys` properties and file I/O injection (like `importer.py`).
