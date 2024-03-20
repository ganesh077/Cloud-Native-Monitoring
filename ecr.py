import boto3

ecr_client = boto3.client('ecr',region_name='us-east-2')

repository_name = "cloud-native-repo"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']