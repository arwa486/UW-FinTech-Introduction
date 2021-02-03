# UW FinTech Project #01 Proposal 

## Project Title
Project Stock Rank

## Team Members
* Kedar Mohare
* Nicholas Nordby 
* Alex Rwamashongye

## Project Description 
What are we tring to do?

A program that allows an individul to select stocks they are are interested in, based on sector, and provides a stack rank of those stock based on different ratios and indicators (growth, liquidity, leverage, etc.)

How?

Our program would first propose a "Sector" prompt with 1-5 sectors in the dropdown. TBD.
From there there would be a list (static?) of companies to select from (this would ensure an apples to apples comparison for the stock analysis).
The user could select from up to 5 companies in that specific sector to be compared.
Our program would then take those five stocks, compute the ratios and indicators we have predetermined, set our proprietray weighting, and provide a stack rank of the stocks selected.

Update:

After review, we determined that our tool would be easier to both use and build if we allow an in individual to insert the stock tickers themselves.

## Research Questions to Answer
For an individual interested in stocks: what stock is the best place for me to park my money, based on my sector interest?

Update:

What is the best company to invest in, based on a company's financial health.

## Datasets/Technologies to be Used 
Datasets: We'll use free/public financial APIs to pull historical data on the various stocks within the sectors. 

Technologies: APIs, Pandas, Plotly/HvPlot

Update:
For an API we'll use Financial Modeling Prep ("FMP")
For a library we'll use Fundamental Analysis ("FA")

## Breakdown of Tasks 
1. Create  list of sectors to choose from
3. Select a set of 15-20 companies for each sector based on large cap, mid cap, small cap etc.
4. Finalize a set of metrics ( key ratios, revenue growth etc) to compare the companies against
5. For all companies query the public APIs to get finanical statistics for each company ( for last 5 years if possible, in order to show progress). If possible, also fetch the average statistics for the sector( might have to find this info)
5. Clean up the data obtained to get relevant metrics and also get the data for thr different years. Give weightage to the metrics and dervive a recommendation for the best company amongst the five picked.
6. Brainstrom on what would be good visualizations for the different metrics( line, vs bar vs something else)
7. Plot the data to see how it and verify the data is prepped and filtered as expected.
8. Build interactive functions to make the charts interactive and have filters applicable to all charts.
9. Render the charts in a dashboard locally.
10. Run this locally on a server and verify that it works.
11. Work on presentation 

## Stretch Goals (Time permitting)
1. Add average data statistics for each of the sector to compare individual company against avg sector performance.
2. Have a list of additional metrics and categorize them into operational metrics( based on income statement), fundamental metrics ( based on balance sheets)

## Where can this go beyond this project.
1. Instead of hardcoded list of sectors, have the sector dynamically fetched from the API.
2. Similar to sector, fetch companies dynamically.
3. THe data in #1 and #2 can be prefetched and preprocessed for a large number of companies and updated say, weekly! 
