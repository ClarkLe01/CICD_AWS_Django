#!/bin/bash

# Installing CodeDeploy Agent
sudo apt update
sudo apt install ruby-full
sudo apt install wget

cd /home/ubuntu

# Download the agent (replace the region)
wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent status

# CodeBuild locally
./codebuild_build.sh -i aws/codebuild/standard:5.0 -a OutputArtifact/ -s DemoCodeCommit/