## Adjust Workflow Permissions in Repository Settings:
Navigate to your repository's Settings.
In the left sidebar, select Actions, then General.
Scroll down to Workflow permissions.
Ensure that Read and write permissions is selected for the GITHUB_TOKEN.
If the action needs to create or approve pull requests, enable Allow GitHub Actions to create and approve pull requests.
Save the changes and re-run your workflow.
