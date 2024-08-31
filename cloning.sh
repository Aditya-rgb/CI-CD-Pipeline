#!/bin/bash

#---------------------------#
#      CONFIGURATION        #
#---------------------------#

# GitHub repository URL
REPO_URL="https://github.com/Aditya-rgb/CI-CD-Pipeline.git"

# Local directory to clone/pull the repository
REPO_DIR="/home/$USER/CI-CD-Pipeline/"  # Change this to your desired local path

# Remove the cloned repository directory if already exists with old code.
sudo rm -rf $REPO_DIR

# Check if the delete operation was successful
if [ $? -ne 0 ]; then
    echo "Failed to delete the old cloned repository!"
    exit 1
fi

echo "Old Cloned repository deleted successfully!"



# Making the repo dir to fetch the latest changes from github.
sudo mkdir REPO_DIR

# Directory to copy the scripts to (e.g., where Nginx serves files)
TARGET_DIR="/var/www/html/"  # Change this to your target directory

# Branch to pull from
BRANCH="main"

#---------------------------#
#       SCRIPT START        #
#---------------------------#

echo "Starting the pulling and downloading of scripts... :)"

# Function to clone the repository if it doesn't exist
clone_repo() {
            echo "Cloning repository..."
            # Command to clone the repository into your linux directory...
            git clone -b $BRANCH $REPO_URL $REPO_DIR
            # Now putting a if statement tocheck the status of the last executed command using $?
            if [ $? -ne 0 ]; then
                    echo "Failed to clone your repository. Fix it!!"
                    exit 1
            fi
             }

# Function to pull the latest changes
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

# Copy the contents of the repository to the target directory
sudo cp -r $REPO_DIR* $TARGET_DIR

# Check if the copy operation was successful
if [ $? -ne 0 ]; then
    echo "Failed to copy files to the Nginx location!"
    exit 1
fi

echo "Files copied successfully!"

#---------------------------#
#    DELETE CLONED REPO      #
#---------------------------#

#echo "Deleting the cloned repository..."

# Remove the cloned repository directory
#sudo rm -rf $REPO_DIR

# Check if the delete operation was successful
#if [ $? -ne 0 ]; then
#    echo "Failed to delete the cloned repository!"
#    exit 1
#fi

#echo "Cloned repository deleted successfully!"

echo "Script execution completed successfully!"
