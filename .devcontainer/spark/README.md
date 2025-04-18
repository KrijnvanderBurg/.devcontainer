# Spark Development Container

This development environment provides a complete Apache Spark cluster setup with automatic notebook integration.

## Quick Start

1. Open any Jupyter notebook (`.ipynb` file) in VS Code
2. A SparkSession named `spark` is automatically initialized and available in all notebooks
3. The SparkContext `sc` is also available
4. Run notebooks as usual - they will automatically connect to the Spark cluster

## Features

- Automatic Spark connection in all notebooks
- Web UIs:
  - Spark Application UI: http://localhost:4040 (when running jobs)
  - Spark Master UI: http://localhost:8080
  - History Server: http://localhost:18080

## Running PySpark Jobs

You can run PySpark scripts using the `spark-submit.sh` script: