# dbt Natural Language Query

This project allows you to query your dbt project using natural language. It uses Azure OpenAI to convert natural language questions into SQL queries.

## Project Structure

Due to limitations in the development environment, the project structure has been flattened. All Python scripts (`main.py`, `dbt_parser.py`, `openai_service.py`) are located in the root directory.

## Setup

1. **Install Dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   Create a file named `config.env` in the root of the project and add your Azure OpenAI credentials and the path to your dbt `manifest.json` file.

   **Important**: Due to sandbox limitations, you might need to hardcode your credentials in `openai_service.py` for the application to run.

   Here is an example of the `config.env` file:
   ```
   # Azure OpenAI credentials
   AZURE_OPENAI_API_KEY="your_api_key"
   AZURE_OPENAI_ENDPOINT="your_endpoint"
   AZURE_OPENAI_DEPLOYMENT_NAME="your_deployment_name"

   # Path to dbt manifest.json file
   DBT_MANIFEST_PATH="manifest.json"
   ```

3. **dbt Manifest File**:
   Place your dbt `manifest.json` file in the root of the project. A sample `manifest.json` is provided.

## Usage

To run the application, execute the `main.py` script from the root of the project with your natural language question as an argument:

```bash
python main.py "Your natural language question here"
```

For example:
```bash
python main.py "How many customers are there?"
```

The script will then output the generated SQL query (or the prompt, as is the case in the current version).
