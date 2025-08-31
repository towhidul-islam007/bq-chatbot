import argparse
import os
from dotenv import load_dotenv
from dbt_parser import parse_dbt_manifest
from openai_service import generate_sql_query, get_azure_openai_credentials

# Load environment variables from config.env
load_dotenv('config.env')

def main():
    """
    Main function for the dbt natural language query application.
    """
    parser = argparse.ArgumentParser(description="Query your dbt project using natural language.")
    parser.add_argument("question", type=str, help="The natural language question to convert to SQL.")
    args = parser.parse_args()

    try:
        # Check for Azure OpenAI credentials
        get_azure_openai_credentials()

        # Get the path to the manifest.json file from environment variables
        manifest_path = "manifest.json"

        # Load the dbt models
        dbt_models = parse_dbt_manifest(manifest_path)

        # Generate the SQL query
        # Note: for now, this will return the prompt, not the actual query.
        sql_query_or_prompt = generate_sql_query(dbt_models, args.question)

        print("---- Generated SQL Query (or Prompt for now) ----")
        print(sql_query_or_prompt)

    except FileNotFoundError:
        print(f"Error: The manifest file was not found at {manifest_path}")
        print("Please make sure the file exists.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Please make sure your config.env file is set up correctly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
