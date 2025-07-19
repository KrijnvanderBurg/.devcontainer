# Apache Spark Cluster DevContainer - Complete Distributed Computing Environment

A complete Apache Spark cluster development environment using VS Code DevContainers. This setup provides a fully configured multi-node Spark cluster with master, workers, history server, and comprehensive monitoring capabilities running in Docker containers with zero-configuration setup.

## 🚀 Why Use This DevContainer?

### Zero-Configuration Distributed Spark Environment
This DevContainer provides a fully configured and isolated Spark cluster environment inside containers, ensuring consistent, reproducible, and platform-independent setup across your entire team. No more complex Spark installation procedures or "_works on my machine_" cluster configuration issues.

### Complete Multi-Node Spark Cluster
This DevContainer includes a full Spark ecosystem with enterprise-grade capabilities:

- **🏗️ Spark Master**: Cluster coordination and resource management
- **⚡ Multiple Workers**: Configurable worker nodes with custom CPU/memory allocation
- **📊 History Server**: Persistent job history and metrics across cluster restarts
- **🔍 Web UIs**: Comprehensive monitoring dashboards for cluster, jobs, and applications
- **📝 Event Logging**: Persistent storage for Spark events and application logs
- *�🐍 PySpark Integration**: Pre-configured Python environment with Spark integration

> **Note**: This DevContainer focuses exclusively on providing a Spark cluster environment. If you need additional Python development tools like linters, formatters, and code quality checkers, check out the [Python DevContainer](../python-spark/README.md). You can combine elements from both DevContainers based on your project needs.

### Two Modes of Deploying a Job to Spark

#### Primary: VS Code Actions
Interactive development with integrated VS Code tasks and real-time monitoring.

- **VS Code Tasks**: One-click job submission with `Ctrl+Shift+B` or `Terminal` → `Run Task` → `spark-submit`
- **Real-time Monitoring**: Web UIs accessible for live cluster and job inspection
- **Integrated Development**: Seamless file editing and job submission workflow

![Spark Cluster Demo](./docs/spark-cluster_final.gif)

#### Secondary: Shell Script  
Traditional `spark-submit` command-line interface for production workflows and CI/CD integration.

```bash
./spark-submit.sh .devcontainer/examples/test_job.py
```

### Jupyter Notebooks Integration
**Jupyter notebooks automatically deploy to the Spark cluster** with zero configuration required:

- Pre-configured Spark session (`spark`) ready for immediate use via `spark_init.py`
- Automatic cluster connectivity - no session setup needed
- Interactive data exploration with distributed computing power
- **Note**: Only one notebook can run at a time on the cluster

## 🏁 Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

### Quick Installation

1. **📥 Clone This Repository**: 
   ```bash
   git clone https://github.com/KrijnvanderBurg/DevOps-Toolkit
   cd DevOps-Toolkit
   ```
2. **🐳 Launch Container**: Open project in VS Code, press `F1` → "Dev Containers: Rebuild and Reopen in Container"
   - Select the `spark-cluster` configuration when prompted
   - The build process may take several minutes the first time as it downloads Spark images
3. **⚡ Verify Cluster**: Access http://localhost:8080 **on your host machine** to view the Spark Master UI
   - **Important**: You may not be prompted to open this URL automatically - you need to manually navigate to localhost:8080 in your browser
   - The port is forwarded from the DevContainer to your host machine
4. **🧪 Test Setup**: Submit the included test job via `Terminal` → `Run Task` → `spark-submit` or run the test notebook

### Centralized Access Point
**Primary Entry**: http://localhost:8080 (Spark Master UI)  
From the Master UI, you can navigate to all other components:
- Click on worker links to access individual worker UIs
- Click on application IDs to view detailed job execution
- Access History Server through navigation links

## Architecture Overview
![Architecture Diagram](./design.drawio.png)

The cluster consists of:
- **DevContainer**: Your development environment with VS Code, Python, and PySpark
- **Spark Master** (port 8080): Cluster coordinator and resource manager
- **Spark Workers** (ports 8081, 8082): Distributed processing nodes
- **History Server** (port 18080): Persistent job history and metrics
- **Shared Storage**: Event logs and workspace files across all containers

## 🛠️ Working with PySpark

### Jupyter Notebooks vs Spark Jobs

#### Jupyter Notebooks: Interactive Development
Notebooks include auto-initialization via `spark_init.py` with a pre-configured Spark session ready for immediate use:

```python
# Spark session is already available - no initialization needed
df = spark.createDataFrame([(1, "John"), (2, "Jane")], ["id", "name"])
df.show()

# SparkContext is also available for RDD operations
rdd = sc.parallelize([1, 2, 3, 4, 5])
print(rdd.collect())
```

**Benefits**: 
- Instant development with pre-configured session
- Interactive data exploration and visualization
- Shared cluster resources across notebook cells

#### Spark Jobs: Production Workloads  
Standalone Python scripts require explicit SparkSession creation for production deployments:

```python
from pyspark.sql import SparkSession

# Explicit session creation for job submission
spark = SparkSession.builder \
    .appName("Production Job") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

df = spark.createDataFrame([(1, "John"), (2, "Jane")], ["id", "name"])
df.show()

spark.stop()  # Clean shutdown
```

## ⚙️ Configuration & Customization

### Environment Variables (.env)
Easily customize cluster resources and versions:

```ini
# Spark and Python versions
SPARK_VERSION=3.5.5
PYTHON_VERSION=3.11

# Master configuration
SPARK_MASTER_WEBUI_PORT=8080
SPARK_MASTER_PORT=7077

# Worker 1 resources
SPARK_WORKER1_CORES=2
SPARK_WORKER1_MEMORY=2G
SPARK_WORKER1_WEBUI_PORT=8081

# Worker 2 resources  
SPARK_WORKER2_CORES=2
SPARK_WORKER2_MEMORY=2G
SPARK_WORKER2_WEBUI_PORT=8082

# History Server
SPARK_HISTORY_WEBUI_PORT=18080
```

### Docker Compose Architecture
The `docker-compose.yml` defines a scalable multi-container architecture:

```yaml
services:
  devcontainer:     # VS Code development environment
  spark-master:     # Cluster coordinator (port 8080)
  spark-worker-1:   # Processing node 1 (port 8081)
  spark-worker-2:   # Processing node 2 (port 8082)  
  spark-history-server: # Job history (port 18080)

volumes:
  spark-logs:       # Shared log storage
  spark-events:     # Event log persistence

networks:
  spark-network:    # Isolated cluster communication
```

### Port Forwarding Configuration
All web UIs are forwarded to your host machine:

- **8080**: Spark Master UI (cluster management)
- **8081**: Worker 1 UI (individual worker monitoring)
- **8082**: Worker 2 UI (individual worker monitoring)  
- **18080**: History Server (completed jobs)
- **4040**: Application UI (active jobs only)

### VS Code Extensions & Settings
Pre-configured extensions for optimal Spark development:

- **Jupyter**: Interactive notebook development with PySpark
- **Python**: Language support with IntelliSense
- **Pylance**: Advanced type checking and code completion
- **Data Wrangler**: Visual data exploration and manipulation

### Extending the Cluster
To add more workers or modify resources:

1. **Update .env**: Add new worker environment variables
2. **Modify docker-compose.yml**: Add additional services using the template
3. **Restart DevContainer**: Rebuild to apply changes

This comprehensive Spark cluster environment provides everything needed for professional distributed computing development, from interactive exploration to production job deployment.
