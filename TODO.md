# To-Do List

## Project Initialization

- [x] Define project scope & plan
- [x] Set up project repository
- [ ] Set up folder structure

## Infrastructure Setup

- [ ] Create Packer Images for EC2
- [ ] Provision the images with Terraform inside a VPC structure
- [ ] Provision Kubernetes cluster on said servers
- [ ] Install networking plugin in the cluster
- [ ] Install & configure ArgoCD in the cluster
- [ ] Set up Helmfile & integrate with ArgoCD to manage applications more effectively
- [ ] Implement a modern approach to deployment environment management with Terraform / AWS to have deployment / staging / production

## Development

- [ ] Create dummy service Python
- [ ] Create dummy service Golang
- [ ] Make more complex application with simple authentication, API endpoints, unit test, database (S3) and simple frontend / dashboard
- [ ] Create docker-compose file for local development set-up / minikube script or something to test everything, a development environment

## Monitoring / Observability

- [ ] Configure Prometheus & Grafana for monitoring & visualization (kube-prometheus-stack)
- [ ] Set up Jaeger for distributed tracing
- [ ] Configure OpenTelemetry for telemetry data collection
- [ ] Integrate Datadog for more advanced monitoring, integrate it well with existing one.

## CI/CD Pipeline

- [ ] Set up GitHub repository
- [ ] Configure GitHub Actions for CI to build tagged images
- [ ] Integrate with AWS for deployment in 3 environments
- [ ] Test CI pipeline & CD pull

## Deployment

- [ ] Set up development, staging, production environment clusters / cloud resources
- [ ] Test roll-backs, image upgrade, CI pipeline build & CD automatic sync

## Post-Deployment

- [ ] Monitor system performance
- [ ] Plan for future updates
- [ ] Add security (DevSecOps): image scanning (in CI), runtime scanning (Trivy). Ensure best practices in the setup and microservice communication
- [ ] Add a platform (Platform Engineer blueprint)
- [ ] Add on-demand development environments
- [ ] Create set-up / clean-up bash script / Makefile & test everything works as intended on new spin-ups.
- [ ] Provide customization in the setup via a CLI depending on what is wanted (diff environments, docker-compose or not... helmfile or not etc)
- [ ] Write docs
  - [ ] Write API documentation
  - [ ] Document setup process
  - [ ] Different dashboards, workflow. Debugging process testing
