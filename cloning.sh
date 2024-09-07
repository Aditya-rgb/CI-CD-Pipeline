#!/bin/bash

#---------------------------#
#      CONFIGURATION        #
#---------------------------#

# Github Repository URL.
REPO_URL="https://github.com/Aditya-rgb/CI-CD-Pipeline.git"

# Defining a local directory to clone/pull the repository
REPO_DIR="/home/$USER/CI-CD-Pipeline/"  # Change this to your desired local path

# Removing the cloned repository directory if it already exists with old code.
sudo rm -rf $REPO_DIR

# Checking if the above command was successfull or not.
if [ $? -ne 0 ]; then
    echo "Failed to delete the old cloned repository!"
    exit 1
fi

echo "Old Cloned repository deleted successfully!"



# Making the repo dir to fetch the latest changes from github.
sudo mkdir REPO_DIR

# Directory to copy the scripts to (e.g., where Nginx serves files resides i.e /var/www/html/)
TARGET_DIR="/var/www/html/"  # Change this to your target directory

# Branch to pull from
BRANCH="main"

#---------------------------#
#       SCRIPT START        #
#---------------------------#

echo "Starting the pulling and downloading of scripts... :)"

# Created the function to clone the repository if it doesn't exist
clone_repo() {
            echo "Cloning repository..."
            # Command to clone the repository into your linux directory...
            git clone -b $BRANCH $REPO_URL $REPO_DIR
            # Now putting a if statement to check the status of the last executed command using $?
            if [ $? -ne 0 ]; then
                    echo "Failed to clone your repository. Fix it!!"
                    exit 1
            fi
             }

# Created the function to pull the latest changes from the git
pull_repo() {
            echo "Pulling latest changes..."
            # Command to pull the latest code base if any new commits were made and were detected by the python script..
            git -C $REPO_DIR pull origin $BRANCH
            # Now putting a if statement tocheck the status of the last executed command using $?
            if [ $? -ne 0 ]; then
                    echo "Failed to pull all the latest changes!!"
                    exit 1
            fi
            }

# Checking if the repository directory which we made above exists or not... :)
if [ -d "$REPO_DIR/.git" ]; then
    pull_repo
else
    clone_repo
fi

#---------------------------#
#    COPY TO NGINX LOCATION  #
#---------------------------#

echo "Copying scripts to Nginx location..."

# Copying the contents of the repository to the target directory now i.e nginx location...
sudo cp -r $REPO_DIR* $TARGET_DIR

# Checking if the above copy operation was successful or not ...
if [ $? -ne 0 ]; then
    echo "Failed to copy files to the Nginx location!"
    exit 1
fi

echo "Files copied successfully!"


echo "Script execution completed successfully!"
