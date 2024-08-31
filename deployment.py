import requests
from datetime import datetime, timedelta, timezone

# GitHub repository details
repo_owner = "Aditya-rgb"  # Replace with the owner of the repository
repo_name = "CI-CD-Pipeline"  # Replace with the repository name
branch = "main"  # Replace with the branch name you want to check

# GitHub API endpoint for commits
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits?sha={branch}"

# Time window to check for new commits (e.g., last 10 minutes)
time_window = timedelta(minutes=10)
time_now = datetime.now(timezone.utc)  # Use timezone-aware datetime object

# Fetch commits from the GitHub API
response = requests.get(api_url)
commits = response.json()

# Check for new commits
new_commits = []
for commit in commits:
    commit_time = datetime.strptime(commit['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ")
    
    # Convert the commit_time to a timezone-aware datetime in UTC
    commit_time = commit_time.replace(tzinfo=timezone.utc)
    
    if commit_time > (time_now - time_window):
        new_commits.append(commit)

# Display new commits
if new_commits:
    print(f"New commits found in the last {time_window.total_seconds() / 60} minutes:")
    for commit in new_commits:
        print(f"- {commit['commit']['message']} by {commit['commit']['author']['name']} at {commit['commit']['author']['date']}")
else:
    print("No new commits found.")
