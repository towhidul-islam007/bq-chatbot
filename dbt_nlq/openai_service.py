import os
import openai
from dotenv import load_dotenv
from typing import List, Dict, Any

# Load environment variables from .env file in the root
load_dotenv()

def get_azure_openai_credentials():
    """
    Loads Azure OpenAI credentials from environment variables.
    """
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

    if not all([api_key, endpoint, deployment_name]):
        raise ValueError("Azure OpenAI credentials are not set in the config.env file.")

    return api_key, endpoint, deployment_name

def generate_sql_query(dbt_models: List[Dict[str, Any]], question: str) -> str:
    """
    Generates a SQL query from a natural language question using Azure OpenAI.

    Args:
        dbt_models: A list of dbt models parsed from the manifest.json file.
        question: The natural language question to convert to SQL.

    Returns:
        The generated SQL query.
    """
    api_key, endpoint, deployment_name = get_azure_openai_credentials()

    # In a real implementation, we would configure the openai client here.
    # openai.api_type = "azure"
    # openai.api_key = api_key
    # openai.api_base = endpoint
    # openai.api_version = "2023-07-01-preview"

    prompt = _build_prompt(dbt_models, question)

    # For now, we will just return the prompt to see what it looks like.
    # In the next step, we will make the actual API call.
    # response = openai.Completion.create(
    #     engine=deployment_name,
    #     prompt=prompt,
    #     max_tokens=150,
    #     temperature=0
    # )
    # return response.choices[0].text.strip()

    return prompt # Returning the prompt for now for verification.

def _build_prompt(dbt_models: List[Dict[str, Any]], question: str) -> str:
    """
    Builds the prompt to be sent to the language model.
    """
    prompt = "You are a SQL expert. Given the following database schema, please generate a SQL query to answer the user's question.\n\n"
    prompt += "Schema:\n"
    for model in dbt_models:
        prompt += f"- Table: {model['name']}\n"
        if model['description']:
            prompt += f"  Description: {model['description']}\n"
        prompt += "  Columns:\n"
        for column in model['columns']:
            prompt += f"  - {column['name']}: {column['description']}\n"
        prompt += "\n"

    prompt += f"Question: {question}\n"
    prompt += "SQL Query:"
    return prompt

if __name__ == "__main__":
    # Example usage (for testing purposes)
    from .dbt_parser import parse_dbt_manifest

    # Load the dbt models
    manifest_path = "manifest.json"
    dbt_models = parse_dbt_manifest(manifest_path)

    # Ask a question
    question = "How many customers are there?"

    try:
        generated_prompt = generate_sql_query(dbt_models, question)
        print("---- Generated Prompt ----")
        print(generated_prompt)
    except ValueError as e:
        print(f"Error: {e}")
        print("Please make sure to create a config.env file with your Azure OpenAI credentials.")
