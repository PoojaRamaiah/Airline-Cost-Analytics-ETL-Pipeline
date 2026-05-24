-- Total Cost by Airline
SELECT Airline,
SUM(Cost) AS Total_Cost
FROM airline_cost_data
GROUP BY Airline;

-- Average Shipment Cost
SELECT Airline,
AVG(Cost) AS Avg_Cost
FROM airline_cost_data
GROUP BY Airline;

-- Monthly Spend
SELECT Month,
SUM(Cost) AS Monthly_Spend
FROM airline_cost_data
GROUP BY Month;

-- Cost Savings Analysis
SELECT Airline,
SUM(Cost - Reduced_Cost) AS Total_Savings
FROM processed_airline_data
GROUP BY Airline;
