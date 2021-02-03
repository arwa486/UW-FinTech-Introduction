# UW FinTech Bootcamp HW #07

## Data Engineering 
Created the corresponding SQL tables in 'tables.sql' file folder. Used direct imports in pgAdmin4 for the importation of the .csv files containing the data types. Future to code in import. 

The entity relationship diagram (ERD):  ![Entinty Relationship Diagram](QuickDBD-export.png "ERD")


## Data Analysis 

### Part 1 

- How can you isolate (or group) the transactions of each cardholder? 
There are a variety of ways to isolate the transactions of the card number. The transactions can be isolated  merchant_id and corresponding links (i.e. a specific bar or restaurant), timestamp, or amount. 
- Count the transactions that are less than $2.00 per cardholder. 

For Cardholder 2, the count of transactions less than or equal to $2.00 was 11 total. For Cardholder 18, the number of transactions less than or equal to $2.00 was 19 total. 

- Is there any evidence to suggest that a credit card has been hacked? Explain your rationale.
There is evidence that Cardholder 18's card #344119623920892 was hacked. Assuming Cardholder 2 and Cardholder 18 are "look-alike" customers, the spending habits across both cards should be similar, which is the case for Cardholder 2 ($529.80 to $419.80). for Cardholder 18, across both cards there is a difference of about $11,000 ($11,509.64 to $590.97). Looking at the plots, the unique spikes in Cardholder 18's purchases suggest that large one time purchases were made outside of the normal trend. 
- What are the top 100 highest transactions made between 7:00 am and 9:00 am?
Coffee shops 

- Do you see any anomalous transactions that could be fraudulent?
The large (> $1000) transactions for Cardholder 18 seem fraudlent. 

- Is there a higher number of fraudulent transactions made during this time frame versus the rest of the day?
It is likely that fradulent transactions would be made overnight as the cardholder would likely be asleep or unaware.

- If you answered yes to the previous question, explain why you think there might be fraudulent transactions during this time frame.
Again, the cardholder is likely asleep (unaware of the transaction) and the card is being used. 

### Part 2 

- What difference do you observe between the consumption patterns? Does the difference suggest a fraudulent transaction? Explain your rationale.
The consumption for Cardholder #25 is distributed between a narrow band (typically less than $20) but has a several 2nd order magnitude outliers each month.

- Are there any outliers for cardholder ID 25? How many outliers are there per month?
Yes there are outliers: one in January, March, and May; three in April and June. 

- Do you notice any anomalies? Describe your observations and conclusions.
Similar to Cardholder 18, Cardholder 25 has several outlier transactions that are orders of magnitude larger than the typical monthly transaction. If transactions were made overnight (22:00 to 06:00) and were at merchants outside of the typical spending for Cardholder 25, they would likely be fraudulent. It could be that both Cardholder 25 and Cardholder 18 are "look-alike" customers and have a few, significantly large transactions each month. Further analysis of the merchants and customer habits would be necessary to determine if a transaction is fraudulent. 