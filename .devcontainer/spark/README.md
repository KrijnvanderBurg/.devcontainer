# Spark Development Container

This development environment provides a complete Apache Spark cluster setup with automatic notebook integration.

## Quick Start

1. Open any Jupyter notebook (`.ipynb` file) in VS Code
2. A SparkSession named `spark` is automatically initialized and available in all notebooks
3. The SparkContext `sc` is also available
4. Run notebooks as usual - they will automatically connect to the Spark cluster

## Features

- Automatic Spark connection in all notebooks
- Web UIs:host
  - Spark Application UI: http://localhost:4040 (when running jobs)
  - Spark Master UI: http://localhost:8080
  - History Server: http://localhost:18080

## Running PySpark Jobs

You can run PySpark scripts using the `spark-submit.sh` script:

## Examples

Here are some examples of how to use the Spark development container:

### Example 1: Running a PySpark Job

1. Create a PySpark script, for example `example.py`:
    ```python
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("example").getOrCreate()

    data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
    df = spark.createDataFrame(data, ["name", "value"])

    df.show()
    ```

2. Run the script using the `spark-submit.sh` script:
    ```sh
    ./spark-submit.sh example.py
    ```

### Example 2: Using Spark in a Jupyter Notebook

1. Open a Jupyter notebook in VS Code.
2. Use the following code to create a DataFrame and show its contents:
    ```python
    data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
    df = spark.createDataFrame(data, ["name", "value"])

    df.show()
    ```

## Troubleshooting

### Issue: Spark UI not accessible

- Ensure that the Spark cluster is running.
- Check if the ports (4040, 8080, 18080) are not being used by other applications.

### Issue: PySpark job fails to run

- Verify that the `spark-submit.sh` script has execute permissions:
    ```sh
    chmod +x spark-submit.sh
    ```
- Check the script for syntax errors or missing dependencies.
