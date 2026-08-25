# Weekend A2 Reflection

## 1. Which transform (groupby, merge, or the NumPy computation) took the longest to get right, and why?

The **merge step** took me the longest to get right. While combining the GDP per capita data across different years, everything initially appeared correct when I checked the dataset and its data types, so I did not immediately notice any problem. However, when I created the GDP versus happiness scatter plot, I saw two separate groups of dots with a large gap between them, which showed that something was wrong with the data. After investigating further, I realized that the GDP values were using different number scales or units, and this inconsistency had been introduced during the process of combining the datasets. It was difficult to identify because there were no obvious errors, and the problem only became clear after visualizing the data. This experience taught me that checking data types is not enough; I should also examine the actual values, ranges, and units before merging and analyzing datasets.

## 2. What would you do differently if you had another dataset to analyze this weekend?

If I had another dataset to analyze, I would spend more time exploring and validating the data before starting transformations and visualizations. I would check not only for missing values and incorrect data types but also for inconsistent units, unusual values, and differences in naming before performing operations such as `groupby` or `merge`. I would also create simple visualizations earlier in the process because charts can reveal problems that may not be obvious when looking only at tables. Finally, I would test and verify each transformation step by step before moving on to the next stage of the analysis.
