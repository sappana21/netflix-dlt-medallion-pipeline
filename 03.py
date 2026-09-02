# Databricks notebook source
# DBTITLE 1,Cell 1
import dlt
from pyspark.sql import functions as F


# COMMAND ----------

@dlt.table(name="gold_SUMMARY_BY_COUNTRY")
def gold_SUMMARY_BY_COUNTRY():
    return(
        dlt.read("silverN")
        .groupBy("country")
        .agg(
            F.count("show_id").alias("Total_shows"),
            F.sum("rating").alias("Total_rating")

        )
    )
@dlt.table(name="gold_summary_by_type")
def gold_summary_by_type():
    return(
        dlt.read("silverN")
        .groupBy("type")
        .agg(
            F.count("show_id").alias("total_shows"),
            F.sum("duration").alias("total_time")
        )
    )
@dlt.table(name="gold_summary_by_year")
def gold_summary_by_year():
    return(
        dlt.read("silverN")
        .groupBy("release_year")
        .agg(
            F.count("show_id").alias("total_shows"),
            F.count("country").alias("total_countries"),
            F.collect_set("cast").alias("cast") 
                                    
        )
    )