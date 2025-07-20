# OpenTofu DevContainer (IN DEVELOPMENT)

A complete Infrastructure as Code development environment using OpenTofu (open-source Terraform alternative). This DevContainer provides a fully configured environment for managing cloud infrastructure with security scanning, validation, and deployment automation built-in.

## 🚀 Why Use This DevContainer?

### Zero-Configuration Infrastructure Development
This DevContainer provides a fully configured and isolated infrastructure development environment, ensuring consistent, reproducible, and platform-independent setup across your entire team. No more complex OpenTofu installation procedures or environment configuration issues.

### Comprehensive Infrastructure Tooling
This DevContainer includes essential infrastructure development tools:

- **🏗️ OpenTofu**: Open-source Terraform alternative for infrastructure provisioning
- **☁️ Azure CLI**: Cloud resource management and authentication
- **🔒 Security Scanning**: Built-in security analysis for infrastructure code
- **✅ Validation Tools**: Syntax checking and best practice validation
- **📋 VS Code Tasks**: Pre-configured workflows for common operations

> **⚠️ Development Status:** This DevContainer is currently under development. Basic functionality is available, but full feature integration is in progress.

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

2. **📦 Initialize Submodules** (Required):
   ```bash
   git submodule update --init --recursive
   ```

3. **🐳 Launch Container**: Open project in VS Code, press `F1` → "Dev Containers: Reopen in Container"
   - Select the `opentofu` configuration when prompted

4. **⚡ Verify Setup**: Run `opentofu version` in the terminal to confirm installation

## 🛠️ Common Operations

### Infrastructure Validation
- `Ctrl+Shift+P` → "Tasks: Run Task" → "opentofu-validate"
- Validates syntax and configuration consistency

### Infrastructure Planning  
- `Ctrl+Shift+P` → "Tasks: Run Task" → "opentofu-plan"
- Shows planned infrastructure changes

### Security Scanning
- `Ctrl+Shift+P` → "Tasks: Run Task" → "opentofu-security"
- Scans infrastructure code for security vulnerabilities

---

## 🚀 Complete Your Infrastructure Workflow

**Production Deployment:** Use the [Azure DevOps CI/CD templates](https://github.com/KrijnvanderBurg/.azuredevops) for automated infrastructure deployment with security scanning and compliance checks.

**Code Quality Integration:** Combine with the [Python DevContainer](https://github.com/KrijnvanderBurg/.devcontainer/tree/main/python-spark) for infrastructure automation scripts with comprehensive testing and quality controls.

**Full DevOps Integration:** Explore the [complete DevOps Toolkit](https://github.com/KrijnvanderBurg/DevOps-Toolkit) to see how infrastructure, development, and CI/CD workflows integrate seamlessly.