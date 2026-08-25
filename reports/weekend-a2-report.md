# Assignment 2 Report — World Happiness Report (2015–2022)

## Dataset
World Happiness Report, combined across 8 yearly files (2015–2022) from Kaggle
(kaggle.com/datasets/mathurinache/world-happiness-report), CC0 Public Domain.
1,230 rows after cleaning, covering roughly 150 countries per year.

## Question explored
How has happiness changed across regions over time, and does GDP per capita
actually explain why some countries are happier than others?

## What I found
Regional happiness rankings are far more stable than I expected, with one notable
exception. Western Europe and North America started 2015 roughly 0.7 points apart
(North America higher), but North America's score declined steadily every year
while Western Europe's rose, and the two lines crossed by 2022 (see `a2_chart1.png`).
Sub-Saharan Africa stayed the lowest-scoring region across all 8 years, but showed
the only sustained upward trend of the four regions plotted, rising from around
4.2 to 4.5.

GDP per capita does track happiness closely , countries with a higher GDP per
capita consistently reported higher happiness scores, in a fairly steady,
continuous relationship rather than a sharp cutoff (see `a2_chart2.png`).

## Limitation
The 2020 and 2021 source files reported GDP per capita as a logged value (roughly
6–11) instead of the pre-normalized index (roughly 0–2) every other year used.
Since a log-GDP figure and a normalized index aren't safely convertible into each
other without the original raw GDP numbers, I excluded 2020 and 2021 from the GDP
chart entirely rather than mix two incompatible scales or guess a conversion. This
means chart 2 reflects 6 of the 8 years, not all 8.