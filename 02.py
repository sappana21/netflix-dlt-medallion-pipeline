# Databricks notebook source
import dlt
from pyspark.sql import functions as F


# COMMAND ----------

@dlt.table( name="silverN")
def silverN():
    df = dlt.read("bronzeN")
    cleaned_df = (
        df
        .dropDuplicates()
        .dropna()  
        .filter(F.col("show_id").isNotNull()) 
        .withColumn("processed_timestamp", F.current_timestamp())
    )
    
    return cleaned_df