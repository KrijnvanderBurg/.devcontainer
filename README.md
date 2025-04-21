# .devcontainer
This repository contains several specialized DevContainers for different development environments. It's designed to be included as a Git submodule in your projects.

> **Note**: The `.devcontainer` folder might be invisible in some file explorers due to the leading dot (`.`) in its name. Ensure your file explorer is configured to show hidden files and folders.

## Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed

## Usage
1. Add this repository as a Git submodule to your project:
```bash
git submodule add https://github.com/YOUR-USERNAME/.devcontainer.git .devcontainer
git submodule update --init --recursive
```

2. **Build and start the DevContainer**:
   - Press `F1` to open the command palette
   - Type and select `Dev Containers: Rebuild and Reopen in Container`
   - VS Code will build the Docker images and start the containers defined in `docker-compose.yml`
   - This process may take several minutes the first time

## Available Containers
### [Python DevContainer](./python)
A complete Python development environment with:

- Python 3.11 runtime and Poetry package manager
- Comprehensive linting and static analysis tools (Ruff, PyLint, Flake8, MyPy)
- Code quality tools (Bandit, DevSkim, Semgrep)
- Testing configuration with pytest and coverage reporting
- Pre-configured VS Code tasks for all development workflows

### [Spark DevContainer](./spark/)
A complete Apache Spark development environment:

- Fully configured Spark cluster (master, workers, history server)
- PySpark integration with Python
- Jupyter notebook support with pre-configured Spark session
- One-click Spark job submission via VS Code tasks
- Web UIs for monitoring Spark clusters and jobs

### [OpenTofu DevContainer (in development)](./opentofu)
An environment for infrastructure as code development:

- OpenTofu (open-source Terraform alternative) pre-installed
- Azure CLI integration
- Security scanning tools
- VS Code tasks for common OpenTofu operations (init, plan, validate)
