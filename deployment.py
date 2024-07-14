from github import Github, Auth

# Replace with your GitHub access token
ACCESS_TOKEN = ''  # Ensure to replace with your token

# Replace with the repository you want to check (e.g., "username/repo_name")
REPO_NAME = "Aditya-rgb/CI-CD-Pipeline"

def main():
    # Authenticate with GitHub using Auth
    auth = Auth.Token(ACCESS_TOKEN)
    g = Github(auth=auth)
    
    try:
        # Get the repository
        repo = g.get_repo(REPO_NAME)
        
        # Get total commits
        commits = repo.get_commits()
        total_commits = commits.totalCount
        print(f"Total commits in the repository '{REPO_NAME}': {total_commits}")
        
        # Print commit ID and message
        print("\nCommit ID and Message:")
        for commit in commits:
            print(f"Commit ID: {commit.sha}, Message: {commit.commit.message}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
