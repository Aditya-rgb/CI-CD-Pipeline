import requests
from datetime import datetime, timedelta, timezone
import subprocess

# Github reposiotry details being configured varibales below.
github_username = "Aditya-rgb"  # Replace with the owner of the repository
repository_name = "CI-CD-Pipeline"  # Replace with the repository name
branch = "main"  # Replace with the branch name you want to check

# GitHub API endpoint URL for fetching the commits:)
api_url = f"https://api.github.com/repos/{github_username}/{repository_name}/commits?sha={branch}"

# Time window to check for commits that may have been commited in the past 10 min.
time_window = timedelta(minutes=10)
current_time = datetime.now(timezone.utc)  # Use timezone-aware datetime object

# Fetching the commit details from the API.
response = requests.get(api_url)
commits = response.json()

# Now, Checking for new commits
new_commits = []
for commit in commits:
    commit_time = datetime.strptime(commit['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ")

    # Converting the commit_time to a timezone-aware datetime in UTC
    commit_time = commit_time.replace(tzinfo=timezone.utc)

    if commit_time > (current_time - time_window):
        new_commits.append(commit)

# Fetching any new commits that may have occured and if yes then running the Bash script... :)
if new_commits:
    print(f"New commits found in the last {time_window.total_seconds() / 60} minutes:")
    for commit in new_commits:
        print(f"- {commit['commit']['message']} by {commit['commit']['author']['name']} at {commit['commit']['author']['date']}")

    # Executing the bash script
    bash_script_path = "/home/deploy/deploy.sh"  # Replace with the actual path to your Bash script
    try:
        result = subprocess.run([bash_script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Bash script executed successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing the Bash script:\n{e.stderr}")
else:
    print("No new commits found.")
