# Deployment of Django Application in AWS ECS

## Project Overview

This project involves the creation of a simple **Django** application, which has been containerized using **Docker**, pushed to **Amazon Elastic Container Registry (ECR)**, and deployed on **Amazon ECS Fargate**. It demonstrates the full process of containerizing a Django app and deploying it in a serverless environment using AWS.

## Features

- Simple **Django** web application.
- **Dockerized** for easy deployment and scalability.
- Pushed Docker image to **Amazon ECR**.
- Deployed on **ECS Fargate**, enabling serverless container management.
- Fully scalable with **AWS** infrastructure.

## Technologies Used

- **Django** – Python web framework for building the web application.
- **Docker** – Containerization of the Django application for easy portability.
- **Amazon ECR** – Used for storing and managing the Docker image.
- **Amazon ECS Fargate** – Serverless compute engine for deploying containers.
- **AWS CLI & AWS Management Console** – Used for interacting with AWS services.
- **GitHub** – Repository hosting for version control.

## Deployment Architecture

- **Docker Image**: The Django application is containerized using Docker, making it easy to package and deploy across environments.
- **ECR**: The Docker image is pushed to **Amazon Elastic Container Registry**, which securely stores and manages Docker images.
- **ECS Fargate**: The containerized application is deployed on **ECS Fargate**, eliminating the need to manage underlying infrastructure. ECS Fargate automatically handles the scaling and load balancing of the application.

## Project Structure

- **Dockerfile**: Contains the instructions to build the Docker image for the Django application.
- **docker-compose.yml**: Defines how to run the containerized application locally (if needed).
- **AWS Resources**: The infrastructure for deploying the application on **ECS Fargate** and managing the Docker images in **ECR**.


![image](https://github.com/user-attachments/assets/d1b8323e-d3f0-400f-838f-095dd3a76500)
