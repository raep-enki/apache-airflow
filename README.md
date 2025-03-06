## Apache Airflow with Devcontainer

This repository provides Apache Airflow configured with a development container (devcontainer) for a consistent development environment.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/)
- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

### Getting Started with Devcontainer

1. Clone this repository:
    ```bash
    git clone https://github.com/raep-enki/apache-airflow.git
    cd apache-airflow
    ```

2. Open the project in VSCode:
    ```bash
    code .
    ```

3. When prompted, click "Reopen in Container" or use the command palette (F1) and select "Remote-Containers: Reopen in Container".

4. VSCode will build the devcontainer and open the project inside it. This may take a few minutes the first time.

### Using Apache Airflow

Once the devcontainer is running:

- Access the Airflow webserver at http://localhost:8080
- Default credentials are:
  - Username: `airflow`
  - Password: `airflow`

### Project Structure

- `/dags`: Place your DAGs in this directory
- `/plugins`: Custom plugins go here
- `/logs`: Airflow logs directory
- `/config`: Configuration files

### Useful Commands

From the terminal within VSCode:

```bash
# Create a new user
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

# Test a specific DAG
airflow dags test [dag_id] [execution_date]
```

### Customization

You can modify the devcontainer configuration in `.devcontainer/devcontainer.json` to add additional tools or settings.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.