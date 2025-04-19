# Spark Development Environment

A complete Apache Spark development environment using VS Code DevContainers. This setup provides a fully configured Spark cluster with master, workers, and history server running in Docker containers.

## Features

- 🚀 Complete Spark cluster (easily configurable via `.env` file)
- 🐍 Python environment with PySpark
- 📊 Jupyter notebook integration with pre-configured Spark session
- 🧰 VS Code tasks for one-click Spark job submission
- 🔍 Web UIs for monitoring Spark clusters and jobs
- 🔄 Persistent event logs and history server

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed

## Getting Started

1. **Add the Spark DevContainer to your project**:
   - Copy the entire `spark` folder to your project's root directory.
   - Ensure the structure is `.devcontainer/*` or if you have multiple devcontainers `.devcontainer/spark/*` with all the files in this repo

2. **Open the project in VS Code**

3. **Build and start the DevContainer**:
   - Press `F1` to open the command palette
   - Type and select `Dev Containers: Rebuild and Reopen in Container`
   - VS Code will build the Docker images and start the containers defined in `docker-compose.yml`
   - This process may take several minutes the first time

4. **Once the container is running, you're ready to develop with Spark!**

> **Note**: This DevContainer focuses exclusively on providing a Spark environment. If you need a full Python development environment with additional tools like linters, formatters, etc., check out the [Python DevContainer](../python/README.md). You can combine elements from both DevContainers based on your needs.

## Working with Pyspark

```python
from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("Simple PySpark Demo").getOrCreate()

df = spark.createDataFrame([(1, "John"), (2, "Jane")], ["id", "name"])
df.show()
```

### Submitting Spark Jobs

**Using VS Code Task (Recommended)**
- Open your Spark job Python file
- Press `Ctrl+Shift+B` to run the default task
- This will submit the current file to the Spark cluster

**Using the Terminal**
```bash
./spark-submit.sh /path/to/your/spark_job.py
```

## Working with Jupyter Notebooks
The environment includes auto-initialization for Jupyter notebooks with the `spark_init.py` script, spark object already exists for immediate usage:

```python
# Just start using the pre-configured spark session
df = spark.createDataFrame([(1, "John"), (2, "Jane")], ["id", "name"])
df.show()
```

## Accessing Web UIs
- Spark Master: http://localhost:8080
- Worker 1: http://localhost:8081
- Worker 2: http://localhost:8082
- History Server: http://localhost:18080
- Application UI: http://localhost:4040 (while job is running)

## Configuration
Easily customize the environment by editing the .env file:

```ini
# Adjust Spark and Python versions
SPARK_VERSION=3.5.5
PYTHON_VERSION=3.11

## Configure worker resources
SPARK_WORKER1_CORES=2
SPARK_WORKER1_MEMORY=2G
SPARK_WORKER2_CORES=2
SPARK_WORKER2_MEMORY=2G
...
```
