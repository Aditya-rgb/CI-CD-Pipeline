import os
from github import Github
import datetime

# Get GitHub access token from environment variable
#ACCESS_TOKEN = os.getenv('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')
ACCESS_TOKEN = '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'
# Replace with the repository you want to check (e.g., "username/repo_name")
REPO_NAME = "Aditya-rgb/CI-CD-Pipeline"

def get_new_commits(repo, since):
    commits = repo.get_commits(since=since)
    return commits

def main():
    if not ACCESS_TOKEN:
        print("Access token not found. Please set the GITHUB_TOKEN environment variable.")
        return
    
    # Authenticate with GitHub
    g = Github(ACCESS_TOKEN)
    
    # Get the repository
    repo = g.get_repo(REPO_NAME)
    
    # Set the time to check for new commits (e.g., past 10 minutes)
    since = datetime.datetime.now() - datetime.timedelta(minutes=10)
    
    # Get new commits since the specified time
    commits = get_new_commits(repo, since)
    
    # Print new commits
    if commits.totalCount == 0:
        print("No new commits in the past 10 minutes.")
    else:
        print(f"New commits in the past 10 minutes: {commits.totalCount}")
        for commit in commits:
            print(f"Commit {commit.sha}: {commit.commit.message} by {commit.commit.author.name} at {commit.commit.author.date}")

if __name__ == "__main__":
    main()
