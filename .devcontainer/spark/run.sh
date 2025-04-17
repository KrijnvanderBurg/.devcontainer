#!/bin/bash

# Submit a PySpark job to the cluster with more specific settings
/opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --deploy-mode client \
  --conf spark.executor.memory=1g \
  --conf spark.executor.cores=1 \
  --conf spark.driver.host=devcontainer \
  --conf spark.driver.bindAddress=0.0.0.0 \
  jobbie.py

echo "Spark job completed. Check the output above."