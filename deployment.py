import os
from github import Github, Auth
import datetime

# Use an environment variable for your access token
#ACCESS_TOKEN = os.getenv('GITHUB_TOKEN')  # Set this in your environment
ACCESS_TOKEN = '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'
# If not using environment variables, you can directly assign it here for testing
# ACCESS_TOKEN = "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"

# Replace with the repository you want to find
TARGET_REPO_NAME = "CI-CD-Pipeline"

def get_new_commits(repo, since):
    print(f"Fetching commits since {since}")
    commits = repo.get_commits(since=since)
    print(f"Total commits found: {commits.totalCount}")
    return commits

def find_repo(g, target_repo_name):
    print(f"Searching for repository: {target_repo_name}")
    for repo in g.get_user().get_repos():
        if repo.name == target_repo_name:
            print(f"Found repository: {repo.name}")
            return repo
    print(f"Repository {target_repo_name} not found.")
    return None

def main():
    if not ACCESS_TOKEN:
        print("Access token not found. Please set the GITHUB_TOKEN environment variable.")
        return
    
    # Authenticate with GitHub using Auth
    auth = Auth.Token(ACCESS_TOKEN)
    g = Github(auth=auth)  # Public GitHub

    # Find the specific repository
    repo = find_repo(g, TARGET_REPO_NAME)
    if repo is None:
        return  # Exit if the repository is not found
    
    # Set the time to check for new commits (e.g., past 100 minutes)
    since = datetime.datetime.now() - datetime.timedelta(minutes=00)
    print(f"Checking for commits in repository: {repo.name} since: {since}")
    
    # Get new commits since the specified time
    try:
        commits = get_new_commits(repo, since)
    except Exception as e:
        print(f"Failed to get commits: {e}")
        return
    
    # Print new commits
    if commits.totalCount == 0:
        print("No new commits in the past 100 minutes.")
    else:
        print(f"New commits in the past 100 minutes: {commits.totalCount}")
        for commit in commits:
            commit_data = commit.commit
            print(f"Commit {commit.sha}: {commit_data.message} by {commit_data.author.name} at {commit_data.author.date}")

if __name__ == "__main__":
    main()
