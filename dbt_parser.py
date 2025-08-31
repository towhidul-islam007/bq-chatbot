import json
from typing import List, Dict, Any

def parse_dbt_manifest(manifest_path: str) -> List[Dict[str, Any]]:
    """
    Parses the dbt manifest.json file to extract model information.

    Args:
        manifest_path: The path to the manifest.json file.

    Returns:
        A list of dictionaries, where each dictionary represents a dbt model.
    """
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    models = []
    for node_name, node_info in manifest.get("nodes", {}).items():
        if node_info.get("resource_type") == "model":
            models.append({
                "name": node_info.get("name"),
                "description": node_info.get("description"),
                "columns": [
                    {
                        "name": col_info.get("name"),
                        "description": col_info.get("description"),
                    }
                    for col_name, col_info in node_info.get("columns", {}).items()
                ],
            })
    return models

if __name__ == "__main__":
    # This is an example of how to use the parser.
    # It assumes that the script is run from the root of the project.
    manifest_path = "manifest.json"
    parsed_models = parse_dbt_manifest(manifest_path)
    print(json.dumps(parsed_models, indent=2))
