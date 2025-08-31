# dbt Natural Language Query

This project allows you to query your dbt project using natural language. It uses Azure OpenAI to convert natural language questions into SQL queries.

## Project Structure

The project is structured as a standard Poetry project. The main source code is located in the `dbt_nlq` directory.

## Setup

1. **Install Poetry**:
   If you don't have Poetry installed, follow the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

2. **Install Dependencies**:
   Install the project dependencies using Poetry:
   ```bash
   poetry install
   ```

3. **Configure Environment Variables**:
   Create a file named `config.env` in the root of the project and add your Azure OpenAI credentials and the path to your dbt `manifest.json` file.

   **Important**: Due to sandbox limitations, you might need to hardcode your credentials in `dbt_nlq/openai_service.py` for the application to run.

   Here is an example of the `config.env` file:
   ```
   # Azure OpenAI credentials
   AZURE_OPENAI_API_KEY="your_api_key"
   AZURE_OPENAI_ENDPOINT="your_endpoint"
   AZURE_OPENAI_DEPLOYMENT_NAME="your_deployment_name"

   # Path to dbt manifest.json file
   DBT_MANIFEST_PATH="manifest.json"
   ```

4. **dbt Manifest File**:
   Place your dbt `manifest.json` file in the root of the project. A sample `manifest.json` is provided.

## Usage

To run the application, use `poetry run` to execute the `main.py` script with your natural language question as an argument:

```bash
poetry run python -m dbt_nlq.main "Your natural language question here"
```

For example:
```bash
poetry run python -m dbt_nlq.main "How many customers are there?"
```

The script will then output the generated SQL query (or the prompt, as is the case in the current version).
