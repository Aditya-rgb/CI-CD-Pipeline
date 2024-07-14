# Project Title

## Introduction

> **Introduction**
> 
> Create a complete CI-CD pipeline using bash, Python, and crontabs. The tasks include setting up a simple HTML project in a GitHub repository, configuring an AWS EC2 or local Linux instance with Nginx, writing a Python script to check for new commits, creating a bash script for code deployment and Nginx restart, and setting up a cron job to run the Python script at regular intervals. Finally, test the setup by ensuring changes from new commits are automatically deployed.

## Features

> **Features**
> 
> - Automated Deployment: Ensures the latest code is automatically deployed to the server upon new commits.
> - Continuous Integration: Utilizes GitHub for version control and integration of changes.
> - Scheduled Checks: Uses cron jobs to regularly check for new commits and initiate deployment.
> - Bash Scripting: Bash scripts for deployment and server management and commit checking.
>-  Nginx Configuration: Configures Nginx to serve the deployed HTML project.
> - Flexible Setup: Can be configured to run on AWS EC2 or a local Linux instance.
> - Error Handling: Includes basic error handling to ensure smooth operation and troubleshooting.


## Prerequisites

> **Prerequisites**
> 
> List of software, libraries, or tools required before installing the project.

## Installation

> **Installation**
> 1. **Git:** For version control and managing the repository.  
>    [Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
> 
> 2. **Python 3.x:** Required for running the Python script to check for new commits.  
>    [Python Installation Guide](https://www.python.org/downloads/)
> 
> 3. **Pip:** Python package manager for installing required libraries.  
>    [Pip Installation Guide](https://pip.pypa.io/en/stable/installation/)
> 
> 4. **GitHub API Library for Python (PyGithub):** To interact with GitHub's API.  
>    Install using pip: `pip install PyGithub`
> 
> 5. **Nginx:** A web server to serve the deployed HTML project.  
>    [Nginx Installation Guide](https://nginx.org/en/docs/install.html)
> 
> 6. **Bash:** Required for running shell scripts.  
>    Bash is typically pre-installed on most Unix-like systems.
> 
> 7. **Cron:** To schedule the Python script to run at regular intervals.  
>    Cron is typically pre-installed on most Unix-like systems.
> 


## Configuration

**Configuration**
> 
> After installing the project, follow these steps to configure it:
>
> 1. **Clone the Repository:** If not already done, clone the repository to your local machine or server using:
>    ```bash
>    git clone https://github.com/Aditya-rgb/CI-CD-Pipeline.git /path/to/your/directory
>    ```
>
> 2. **Set Up Nginx:** 
>    - Open the Nginx configuration file (e.g., `/etc/nginx/sites-available/default`).
>    - Update the server block to point to the project directory:
>      ```nginx
>      server {
>          listen 80;
>          server_name your_domain_or_IP;
>
>          location / {
>              root /path/to/your/directory;
>              index index.html;
>          }
>      }
>      ```
>    - Test the Nginx configuration:
>      ```bash
>      sudo nginx -t
>      ```
>    - Reload Nginx to apply changes:
>      ```bash
>      sudo systemctl reload nginx
>      ```

> 3. **Configure the Python Script:** 
>    - Open the Python script (e.g., `ngi.py`) and update the `ACCESS_TOKEN` and `REPO_NAME` variables with your GitHub token and repository details.
>
> 4. **Set Up the Cron Job:**
>    - Open the crontab editor:
>      ```bash
>      crontab -e
>      ```
>    - Add a line to schedule the Python script to run at your desired interval. For example, to run every 5 minutes:
>      ```bash
>      */5 * * * * /usr/bin/python3 /path/to/your/directory/ngi.py
>      ```
> 
> 5. **Test the Configuration:**
>    - Make a test commit to your GitHub repository and ensure the changes are pulled and deployed automatically to the Nginx server.


## Usage

> **Usage**
> 
> Examples of how to use the project, including command-line examples, API usage, etc.

## Testing

> **Testing**
> 
> Instructions on how to run tests for the project.

## Troubleshooting

> **Troubleshooting**
> 
> Common issues and their solutions.

## Contributing

> **Contributing**
> 
> Guidelines for contributing to the project, including how to submit issues and pull requests.

## License

> **License**
> 
> Information about the project's license.

## Contact

> **Contact**
> 
> Contact information for the project maintainers.
