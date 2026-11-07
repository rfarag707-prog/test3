# Solution Task 24 — Pandas projects

## التشغيل
1. فك ضغط الحل، وافتح النوت بوك المطلوب من مجلد `notebooks` في VS Code أو Jupyter.
2. ثبّت المكتبات: `python -m pip install -r requirements.txt`.
3. غيّر `DATA_ROOT` في أول خلية لمسار مجلد الداتا عندك، مثلاً `Path(r"C:\Users\HP\Downloads\pandas_exercises")`.
4. اختار Python kernel وشغّل الخلايا بالترتيب. الملفات لا تحتوي نتائج محفوظة؛ النتائج تظهر من بياناتك.

## Structure
- `notebooks/`: 28 named notebooks, original questions followed by answer code.
- `requirements.txt`: runtime dependencies.
- Data files are not duplicated in this ZIP. `data_file()` searches the selected data folder recursively.

## Status
Solutions are supplied for the stated questions in projects 01–27.
Project 28 (Indexing) in the supplied archive has **no question text for steps 4–16**, and does not specify the variable name in step 3. Its import and bonus are completed; the missing questions are explicitly marked. Those 13 answers cannot be completed until the question text is provided. This package is therefore not a claim that all 28 source projects are fully complete.

## Required local data
Included in the original archive: Euro_2012_stats_TEAM.csv, student-mat.csv, US_Crime_Rates_1960_2014.csv, cars1.csv, cars2.csv, US_Baby_Names_right.csv, wind.data, Online_Retail.csv, tips.csv, train.csv and appl_1980_2014.csv.

Additional local files used by the original exercises:
- `chipotle.tsv`, `u.user`, `drinks.csv`
- `en.openfoodfacts.org.products.tsv` (rename the downloaded TSV or edit the filename in project 03)
- `iris.data`, `wine.data`, `weekly.csv`
- Project 24: `AAPL.csv`, `TSLA.csv`, `IBM.csv`, `MSFT.csv`, with a `date` or `timestamp` column and a numeric `volume` column, covering the requested dates from January 2015. Alternatively set `USE_LOCAL_CSV = False` and provide your own `ALPHAVANTAGE_API_KEY` environment variable. API availability/history access depends on the provider; the API route was not run here.

The linked upstream `weekly.csv` currently returned column headers without observations. Project 25 needs the original nonempty dataset on your device; an empty file triggers a clear error.

## Validation
- All Python code cells passed syntax checks.
- 24 complete projects ran against supplied/downloaded real datasets or the exact constructed data requested by the exercises.
- Projects 03, 24 (local CSV mode), and 25 ran against synthetic structural fixtures to verify code paths. These fixtures are not included as real data and no fixture outputs are presented as assignment results.
- Project 28's available import/bonus code ran; steps 4–16 remain unspecified in the source.
- Random-number exercises use a fixed seed. Notebook outputs are cleared for local execution.

## GitHub submission
The assignment requires a repository link. This ZIP has not been published to GitHub. Create your repository and upload this folder's contents after running the notebooks on your data and obtaining project 28's missing questions. Do not upload API keys or large datasets.

## Projects

| File | Status |
|---|---|
| 01_Chipotle.ipynb | Solution supplied |
| 02_Occupation.ipynb | Solution supplied |
| 03_World_Food_Facts.ipynb | Solution supplied |
| 04_Chipotle.ipynb | Solution supplied |
| 05_Euro12.ipynb | Solution supplied |
| 06_Fictional_Army.ipynb | Solution supplied |
| 07_Alcohol_Consumption.ipynb | Solution supplied |
| 08_Occupation.ipynb | Solution supplied |
| 09_Regiment.ipynb | Solution supplied |
| 10_Students_Alcohol_Consumption.ipynb | Solution supplied |
| 11_US_Crime_Rates.ipynb | Solution supplied |
| 12_Auto_MPG.ipynb | Solution supplied |
| 13_Fictitous_Names.ipynb | Solution supplied |
| 14_Housing_Market.ipynb | Solution supplied |
| 15_US_Baby_Names.ipynb | Solution supplied |
| 16_Wind_Stats.ipynb | Solution supplied |
| 17_Chipotle.ipynb | Solution supplied |
| 18_Online_Retail.ipynb | Solution supplied |
| 19_Scores.ipynb | Solution supplied |
| 20_Tips.ipynb | Solution supplied |
| 21_Titanic_Desaster.ipynb | Solution supplied |
| 22_Pokemon.ipynb | Solution supplied |
| 23_Apple_Stock.ipynb | Solution supplied |
| 24_Getting_Financial_Data.ipynb | Solution supplied |
| 25_Investor_Flow_of_Funds_US.ipynb | Solution supplied |
| 26_Iris.ipynb | Solution supplied |
| 27_Wine.ipynb | Solution supplied |
| 28_Indexing.ipynb | Source questions missing (steps 4-16) |

## Source
Exercise questions and supplied datasets: the user-provided `28_Project.zip` (`pandas_exercises`). Original exercise credits and links remain in the question text where present. API reference: https://pydata.github.io/pandas-datareader/readers/alphavantage.html
