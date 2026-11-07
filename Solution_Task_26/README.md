# Session 26 - Exploratory Data Analysis

Completed exploratory analyses of Facebook post performance, IMDb titles and ratings, and Telco customer churn. Notebooks include executed outputs, figures and data-driven conclusions.

## Open the results
| Analysis | Executed notebook | Report |
|---|---|---|
| Facebook | [Notebook](notebooks/01_Facebook_Metrics.ipynb) | [Summary](reports/facebook_report.md) / [PDF](reports/facebook_report.pdf) |
| IMDb | [Notebook](notebooks/02_IMDb_Analysis.ipynb) | [Summary](reports/imdb_report.md) / [PDF](reports/imdb_report.pdf) |
| Telco | [Notebook](notebooks/03_Telco_Churn.ipynb) | [Summary](reports/telco_report.md) / [PDF](reports/telco_report.pdf) |

## Two download packages
- **Solution_Task_26_With_Data.zip:** complete local working copy including the data used for this run. IMDb metadata alone are over 1 GB uncompressed; gzip parts preserve every row and column. Keep this copy locally for educational use.
- **Solution_Task_26_GitHub.zip:** notebooks with saved results, reports, figures and download script, without raw datasets. Extract this archive and upload its contents to GitHub. Do not upload the ZIP itself as your only submission.

## Reproduce on Windows / VS Code
Python 3.11+ is recommended. The full IMDb analysis can require several GB of RAM; a machine with 16 GB RAM is recommended. Saved results can be read without rerunning the analysis.
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
# Only needed for the GitHub package, which excludes raw data:
.\.venv\Scripts\python.exe download_data.py
.\.venv\Scripts\python.exe -m jupyterlab
```
Open each notebook and Run All, then save. Working directories supported: the project root or notebooks folder. On VS Code choose the .venv kernel. IMDb accepts the included split gzip files or one original title.basics.tsv / .tsv.gz and one ratings file. Internet is unnecessary for the With_Data version once dependencies are installed.

## Scope and methods
- Original datasets specified by the course, downloaded 2026-11-06. See provenance.json for file hashes.
- All IMDb title types and every source metadata row are loaded, not just movies or rated titles. Genre memberships overlap. Only a scatterplot is sampled for readable rendering.
- Exact duplicates and invalid numeric values are handled explicitly. Unknown interactions and outcomes are never assumed to be zero.
- Facebook type and timing comparisons include group counts, medians, means and reach-normalized engagement.
- IMDb includes vote-threshold sensitivity, genre and period comparisons and movie-only correlation checks.
- Telco includes known-outcome denominators, Wilson intervals and contract/service interaction comparisons.
- These are observational associations. Recommendations are hypotheses to test, not causal claims or predictive model results.

## Sources and attribution
- [Facebook Metrics](https://www.kaggle.com/datasets/masoodanzar/facebook-metrics).
- [IMDb dataset](https://www.kaggle.com/datasets/ashirwadsangwan/imdb-dataset/) - metadata in this downloaded snapshot were listed with creation date 2026-11-02. Source file dates do not establish complete release-year coverage.
- [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).

Information courtesy of IMDb (https://www.imdb.com). Used with permission. IMDb data are for personal, non-commercial use under their source terms; raw files should not be republished as a public movie database. [IMDb terms](https://help.imdb.com/article/imdb/general-information/can-i-use-imdb-data-in-my-software/G5JTRESSHJBBHTGX).

## GitHub submission
Extract **Solution_Task_26_GitHub.zip**. Create a new repository, then upload all its contents while preserving notebooks/, reports/, figures/ and data/README files. Raw data and .venv are intentionally excluded. Browser uploads do not enforce .gitignore. Verify that the notebooks and PDF reports open in the repository before submitting the link.

## شرح سريع بالعربي
النسخة With_Data فيها الداتا والنتائج لتشغيل المشروع عندك. النسخة GitHub أخف وجاهزة للرفع، وفيها النوت بوك بالنتائج والرسوم والتقارير؛ لا تحتاج تشغيلها من جديد لمشاهدة النتائج. فك الضغط وارفع المحتويات مع الحفاظ على المجلدات. اقرأ النتائج وافهمها قبل مناقشة المشروع.
