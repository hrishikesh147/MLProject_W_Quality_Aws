# MLProject_W_Quality_Aws

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py


### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/hrishikeshbhagawati01/MLProject_W_Quality_Aws.mlflow \
MLFLOW_TRACKING_USERNAME=hrishikeshbhagawati01 \
MLFLOW_TRACKING_PASSWORD=54ea801af58531a14ca0eff221a0736561c9f604 \
python script.py

## from cmd run the following
set MLFLOW_TRACKING_URI=https://dagshub.com/hrishikeshbhagawati01/MLProject_W_Quality_Aws.mlflow
set MLFLOW_TRACKING_USERNAME=hrishikeshbhagawati01 
set MLFLOW_TRACKING_PASSWORD=54ea801af58531a14ca0eff221a0736561c9f604 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
