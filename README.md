# CI/CD Pipeline 
## Introduction

The problem statement involves automating the deployment of a website using a CI/CD pipeline. The pipeline integrates Python and Bash scripts to detect GitHub commits and deploy the website on an Nginx server hosted on an AWS EC2 instance or a local Linux server. When ever a change or commit is made to the git repo, the python script detects the concerned commit and automatically places the updated sample HTML project files to nginx location. 

## Prerequisites

- Python
- Bash
- AWS EC2 instance or Local Linux server
- Nginx

## Installation

1. **Set Up Nginx**:
   - Update Package Index:
     ```bash
     sudo apt-get update
     ```
   - Install Nginx:
     ```bash
     sudo apt-get install nginx
     ```
   - Start Nginx Service:
     ```bash
     sudo systemctl start nginx
     ```
   - Check Nginx Status:
     ```bash
     sudo systemctl status nginx
     ```

## Development Phase

1. **Create Sample HTML Website**:
   - A sample HTML website was created and pushed to GitHub using Git commands in Git Bash.

2. **Develop Python Script**:
   - A Python script was written to get the record of any commit that may have happened in the last 10 minutes from the time of pipeline run.
   - Key Components:
     - Utilizes GitHub API to get commit history.
     - Repository details are stored in Python variables.
     - Fetches commit history for the past 10 minutes (configurable).

3. **Create Bash Script**:
   - Developed a Bash script to clone the repository whenever a new commit is detected by the Python script.
   - Key Aspects:
     - Clone repository upon commit detection.
     - Perform `git pull` on the local server.
     - Copy files to Nginx location `/var/www/html/`.
     - Delete the cloned repository after copying.

4. **Integrate Scripts**:
   - Python script detects commits and triggers the Bash script.
   - Integration is achieved using Python’s `subprocess` library.
   - Configure the path to the Bash script in the Python script (`bash_script_path`).

5. **Automate with Crontab**:
   - Used crontab to run the Python script at a specified interval to detect changes and update the website.
   - Example crontab entry:
     ```bash
     */10 * * * * /usr/bin/python3 /path/to/your/deployment.py >> /path/to/your/logfile.log 2>&1
     ```

## Deployment Phase

#### AWS EC2 Setup and CI/CD Pipeline Deployment

#### Steps to Initialize the AWS EC2 Instance and Deploy the CI/CD Pipeline:

#### 1. Launch EC2 Instance

- **Step 1**: Sign in to the AWS Console.
  - Navigated to the [AWS Management Console](https://aws.amazon.com/console/), and logged in to my AWS account.
  
- **Step 2**: Navigate to EC2.
  - From the services menu, searcedh for **EC2** and selected **Launch Instance**.

- **Step 3**: Choose an Operating System.
  - Opted for **Ubuntu** as the OS.

- **Step 4**: Choose Architecture.
  - Selected **64-bit (arm)** architecture.

- **Step 5**: Choose Instance Type.
  - Chose **t4g.micro** for this case.

- **Step 6**: Configure Key Pair.
  - Set up key-pair login for the EC2 instance (download the `.pem` file for future access).

- **Step 7**: Configure Security Groups.
  - Allowed the following traffic:
    - SSH traffic
    - HTTPS traffic
    - HTTP traffic
  - Selected "Anywhere 0.0.0.0/0" for all.

- **Step 8**: Kept Storage as Default.

- **Step 9**: Review the Instance Summary.
  - Verified the summary on the right side of the screen before creating the instance.

- **Step 10**: Launch the Instance.
  - Launched the instance using **EC2 Instance Connect** instead of using the `.pem` file.

- **Note**: Downloaded the key pair (`.pem` file) for future access.

#### 2. Install Nginx on AWS EC2 Instance

Run the following commands on the EC2 instance:

```bash
sudo apt-get update
sudo apt-get install nginx
sudo service nginx start
sudo service nginx status
```

Now, Copy the PublicIPs of the EC2 instance and paste it in your browser. A default nginx web-page shall appear...


#### 3. Cloned the CI-CD git repository on EC2 instance
```bash
git clone https://github.com/Aditya-rgb/CI-CD-Pipeline.git

```
   
- Copied the deployment.py and cloning.sh to different directory in the EC2 instance.
- Made the config changes and the path location changes in the deployment.py
- Gave chmod +x (executable) permissions to the bash script responsible for cloning or pulling and copy pasting the sample HTML code file to nginx location.
- Made a small commit on github for the deployment.py to detect the commit made.
  
```bash
python3 deployment.py
```   
   
Did a refresh to the public IP of the EC2 instance on the web browser and the website got rendered successfully :)

## Testing Phase

1. **Push Changes**:
   - Introduce a small change in the HTML code and push it to GitHub.

2. **Run Python Script**:
   - Execute `deployment.py` to detect the commit:
     ```bash
     python3 deployment.py
     ```

3. **Verify Bash Script Execution**:
   - The Bash script should clone the repository, pull the latest changes, and update the Nginx location `/var/www/html/`by copying the smaple HTML project files to this location.

4. **Check Nginx Status**:
   - Verify Nginx status:
     ```bash
     sudo systemctl status nginx
     ```
   - Obtain the server IP address:
     ```bash
     ifconfig
     ```

5. **Verify Website**:
   - Open the IP address in a web browser to check if the website is rendered correctly.
   - Repeat steps 2-7 to ensure updates are applied after each commit.

## Automation

1. **Setup Cron Job**:
   - Automate the workflow using cron job on the local Linux system or AWS EC2 instance.
   - Edit crontab:
     ```bash
     crontab -e
     ```
   - Add cron job entry:
     ```bash
     */10 * * * * /usr/bin/python3 /path/to/your/deployment.py >> /path/to/your/logfile.log 2>&1
     ```

2. **Confirm Automation**:
   - Ensure the cron job is correctly set up and the process runs as expected.
   - The final outcome is automatic updates to the website with each commit made to the GitHub repository.



## Troubleshooting

If you encounter issues, here are some common troubleshooting steps:

1. **Nginx not starting:**
   - Ensure the service is installed and running.
     ```bash
     sudo service nginx start
     sudo service nginx status
     ```
   - Check if port 80 is already in use.
     ```bash
     sudo lsof -i:80
     ```

2. **Public IP not working:**
   - Confirm that your security group allows inbound traffic on HTTP (port 80) and HTTPS (port 443).
   - Double-check that Nginx is running and serving your application.

3. **GitHub repository not cloning:**
   - Make sure that the EC2 instance has internet access and that Git is installed.
     ```bash
     sudo apt-get install git
     ```

4. **Website not updating after a new commit:**
   - Ensure that the `deployment.py` script is running correctly.
   - Verify the `cloning.sh` script has executable permissions.
   - Check the cron job or automation settings if applicable.


## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request for review.

Make sure to follow the code style guidelines and include proper documentation for any new features.


## Contact

For any queries, feel free to contact me:

- **Email:** adityavakharia@gmail.com
- **GitHub:** [Aditya-rgb](https://github.com/Aditya-rgb)

You can also open an issue in the repository for questions or suggestions.


