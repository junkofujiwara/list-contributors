# List GitHub Contributors in Organization

This script lists all contributors to all repositories in a GitHub organization.

## Prerquisites

`pip install -r requirements.txt`

## Usage

1. Create a GitHub token with the `repo` scope. (`metadata:read` is required for private repositories)
2. Update API_ENDPOINT in settings.py to your environment's API endpoint.
3. Run `python list_contributors.py -o <organization> -t <token>`
4. The script will output a CSV file with the contributors.

## Example
repo_a, contributor_x, 10
repo_b, contributor_y, 5
repo_a, contributor_z, 3

