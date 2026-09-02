# Databricks notebook source
import dlt
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

# DBTITLE 1,Cell 2
@dlt.table(name="bronzeN")
def bronzeN():
    return(
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format","csv")
        .option("header","true")
        .option("inferSchema","true")
        .load("/Volumes/netflix_catalog/netflix_schema/netflix_volume/raw/")
        .withColumn("ingesttime",current_timestamp())
    )
