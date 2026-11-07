# IMDb — findings
- Source files: 26 complete metadata part(s), title.ratings.tsv.gz.
- Clean metadata titles: 12,917,629; rated titles: 1,727,596.
- Rating coverage: 13.4%.
- Median rating among rated titles: 7.20.
- Titles with at least 1,000 votes: 108,974.
- Leading genre by eligible median rating (at least 30 titles): Animation (median 7.70; n=15563).

## Interpretation and actions
Use genre comparisons to shortlist content for further audience research. Inspect title-type and decade tables before interpreting aggregate differences. Compare high-rated titles alongside vote counts and test whether rankings change with the vote threshold. Do not treat high ratings as evidence of commercial success.

## Limitations
Multiple genres per title, missing ratings, selection bias among voters, unequal vote counts, historical snapshot coverage and mixed title types limit generalization. Correlations are not causal. The latest year may be incomplete. No revenue data are analyzed.

## Evidence
See imdb_*.csv tables in this folder and ../figures/imdb_*.png. Scatterplots are sampled for rendering; tables use the full loaded data.
