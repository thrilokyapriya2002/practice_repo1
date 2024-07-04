# Databricks notebook source
df1 = spark.read.format("delta").load("/mnt/silverlayer/delta1")

# COMMAND ----------

df1.display()

# COMMAND ----------


