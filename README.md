# Flask Application Deployed on Amazon EKS

This project is a Flask web application that monitors the CPU and memory utilization of the machine where it's running. The application is containerized using Docker and deployed on Amazon EKS (Elastic Kubernetes Service) using Kubernetes Python client.

## Project Structure

- `app.py`: This is the main Flask application file.
- `Dockerfile`: This file is used to build a Docker image for the application.
- `requirements.txt`: This file lists the Python dependencies that need to be installed.
- `ecr.py`: This script uses `boto3` to push the Docker image to an Amazon ECR repository.
- `eks.py`: This script is used to create a Kubernetes Deployment and Service for the application on Amazon EKS.


## How to Run

1. Build the Docker image:
     docker build -t my-flask-app .
2. Push the Docker image to your Amazon ECR using boto3 python library:
     docker push /my-flask-app
3. Run the `eks.py` script to create the Kubernetes Deployment and Service:
     python3 eks.py


## Tools Used

- Flask: A lightweight Python web framework.
- Docker: A platform to develop, ship, and run applications.
- Amazon ECR: A fully-managed Docker container registry.
- Amazon EKS: A managed service that makes it easy to run Kubernetes on AWS.
- Kubernetes Python client: A Python client library for Kubernetes.


## Tools Used

- Flask: A lightweight Python web framework.
- Docker: A platform to develop, ship, and run applications.
- boto3: The Amazon Web Services (AWS) SDK for Python. It's used to interact with Amazon ECR.
- Amazon ECR: A fully-managed Docker container registry.
- Amazon EKS: A managed service that makes it easy to run Kubernetes on AWS.
- Kubernetes Python client: A Python client library for Kubernetes.

## Learnings

Through this project, I've gained a deeper understanding of cloud-native applications and how to leverage cloud services like Amazon EKS and ECR. I've also learned how to use the Kubernetes Python client and `boto3` to interact with a Kubernetes cluster and Amazon ECR programmatically, which opens up a lot of possibilities for automating and managing deployments.
