from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

spark = SparkSession.builder.appName("AirlineCostETL").getOrCreate()

# Load CSV data
input_path = "data/raw/airline_cost_data.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Data Cleaning
clean_df = df.dropna()

# Cost Reduction Logic
clean_df = clean_df.withColumn(
    "Reduced_Cost",
    round(col("Cost") * 0.9589, 2)
)

# Cost Savings
clean_df = clean_df.withColumn(
    "Savings",
    round(col("Cost") - col("Reduced_Cost"), 2)
)

# Show Results
clean_df.show()

# Save Processed Data
output_path = "data/processed/airline_cost_processed"
clean_df.write.mode("overwrite").csv(output_path, header=True)

print("ETL Pipeline Executed Successfully")
