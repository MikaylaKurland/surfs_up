# Surfs_up Challenge


## Overview of the analysis

### Purpose
The purpose of this analysis is to use SQLAlchemy to find summary statistics for specified weather data for Oahu in order to investigate the efficacy of opening a new surf and shake shop for an investor.

### Method
The data for this analysis was obtained from sqlite:///hawaii.sqlite. We filtered the database for bi-annual results, running the query twice, once for June and once for December.


## Results

### Summary Statistics
For the June query there were 1700 temperature results returned. The minimum temperature was 64 degrees, and the maximum temperature was 85 degrees, with a mean of 75 degrees. 

![](june%20results.png)

For the December query there were 1517 temperature results returned. The average minimum temperature was 56 degrees, and the maximum temperature was 83 degrees, with a mean of 71 degrees.

![](december%20results.png)

### Main Differences
The three differences between the June and December data are:
1. The maximum recorded temperature in June is only two degrees different than the maximum temperature in December.
2. The minimum recorded temperature in June, however, is eight degrees different than the minumum temperature in December. 
3. The range of temperatures recorded was much larger in December than in June. 

## Summary
Neither the maximum or the minimum temperatures disqualify Oahu as a location for either surfing or selling icre cream. While December has a lower recorded temperature than June, the average temperature for both months is in the 70s. If you had to base a recommendation off of this data alone, there is no major concern that I can see for opening a surf and shake shop in Oahu. However, I would definitely not recommend opening a shop solely based on this analysis. Just in terms of weather, I would like to get a better picture of the weather by further filtering the data to only capture measurements taken during business hours. Additionally, other data points such as rainfall, high winds, or other conditions that would make surfing or the consumption of icecream less desirable should also be examined. I would also recommend looking for data on wave conditions in a few areas in Oahu to determine the best place to open. 


