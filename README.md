# Cloud-Native Starter Project

## Overview

This project showcases an architecture integrating various tools and cloud-native practices.

This can be useful for several cases:

- Someone who wants to learn an E2E cloud native project and how the different pieces are integrated into a solution that is state of the art, secure, performant & scalable, while also being reduced enough in complexity that doesn't make it overwhelming.
- An SRE / DevOps/ Cloud Engineer / any operation role who wants a cloud lab to test more complex dynamics than a home lab can provide and with minimal set up effort. Configuration, authentication, cloud provider, IaC... It has the different pieces that most companies use today and can be helpful to improve troubleshooting skills.
- It can also be a starting point for more complex projects

It involves:

- **Application code:** Python, Golang
- **Application orchestration:** Kubernetes (not EKS, but in EC2 for learning purposes and control plane access management), Helm, Helmfile
- **Server templating**: Docker, Packer
- **Infrastructure provisioning**: Terraform
- **CI**: GitHub Actions
- **CD**: ArgoCD
- **Monitoring:** Prometheus, Grafana, OpenTelemetry, Jaeger, Datadog
- **Local development environment**: Docker Compose

Building in public, it is still in its infancy (WIP). Some technologies might change, along with the documentation. The repository will be designed to automate the entire set up and provide a convenient script / CLI that manages the spin-up / delete of the set-up to ease onboarding & avoid cloud costs.

- **Note**: This project is intended for educational purposes. For production environments, ensure all components are configured and secured according to best practices. This will be progressively added.

## Repository Structure

```bash
├── README.md                   # Project overview and documentation
├── TODO.md                     # List of ongoing tasks and future improvements
├── application                 # Application-specific code and services
│   ├── orchestration           # Orchestration scripts and configurations (normally in a different repository than application code. But monorepo structure is desired for this project)
│   └── services                # Microservices and application logic
├── ci                          # Continuous Integration configurations and scripts
├── development                 # Development environment configurations
│   └── docker-compose.yml      # Docker Compose file for local development
├── infrastructure              # Infrastructure provisioning and management
│   ├── packer                  # Packer templates for creating machine images
│   └── terraform               # Terraform scripts for infrastructure as code
└── monitoring                  # Monitoring configurations and scripts
```

### 1. Infrastructure Provisioning with Terraform and Packer

- **Packer**: Creates golden AMIs with Docker, Kubernetes, and monitoring agents (Datadog) pre-installed.
- **Terraform**: Provisions AWS resources including EC2 machines with the golden AMIs created by Packer, inside VPC with its associated security groups, IAM roles, and S3 buckets. A kubernetes cluster will be running on top of them ;provisioned with kubeadm tool, as well as needed kubernetes add-ons.

### 2. Microservices Development (Python and Golang)

- **Python Service**: A Python-based microservice with dummy functionality.
- **Golang Service**: A Golang-based microservice with dummy functionality.

### 3. CI/CD Pipeline with GitHub Actions

- **Build Workflow**: Automatically builds and pushes Docker images for the microservices.
- **Deploy Workflow**: Deploys microservices to Kubernetes using ArgoCD, which pulls the Docker images.
- **Packer Workflow**: Automates the creation of AMIs.
- **Terraform Workflow**: Automates infrastructure provisioning.

### 4. Monitoring and Observability

- **Prometheus**: Monitors the Kubernetes cluster and microservices.
- **Grafana**: Provides visualization of metrics collected by Prometheus.
- **Datadog**: Monitors AWS infrastructure, Kubernetes, and application metrics.
- **Jaeger**: Provides distributed tracing to understand the flow and performance of requests through microservices.
- **OpenTelemetry**: Collects and exports telemetry data (metrics, traces) for both Jaeger and Datadog to provide insights into application performance.
<!--

## Setup Instructions

### Prerequisites #TODO

- AWS account. Set the ENV Variables
- GitHub account for CI/CD integration#

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cloud-native-project.git
cd cloud-native-project
```

### 2. Set Up Environment Variables

Ensure you have the necessary environment variables configured for AWS and GitHub. These are required for the CI/CD pipelines to work correctly.

### 3. Monitor and Observe

- **ArgoCD**: Access the ArgoCD UI to view and manage deployments.
- **Grafana**: Access Grafana to visualize metrics collected by Prometheus.
- **Prometheus**: For easier debugging, Prometheus can be checked directly
- **Datadog**: Use the Datadog dashboard to monitor AWS infrastructure and application metrics.
- **Jaeger**: Use Jaeger UI to view distributed traces and understand request flows.
- **OpenTelemetry**: Monitor telemetry data collected from your microservices.

## Future Enhancements

- Implement security best practices such as Docker image scanning.
- Expand microservices to include more complex functionalities.
- Integrate additional AWS services as needed.
- Add configuration management if needed

## FAQ:

- **Configuration management tools?:** None. Following golden image process to avoid configuration drift and need for configuration management tools. Could be added afterwards if a valid use case is found. -->

References:
https://roadmap.sh/devops
https://www.terraformupandrunning.com/
https://www.fundamentals-of-devops.com/
