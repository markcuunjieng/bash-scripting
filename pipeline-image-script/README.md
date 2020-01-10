`Maintained and Developed by Mark Cu`

# Base Image for Gitlab CI
  - Build Amazon Linux 2
  - Amazon Linux Version 2
  - Linux/4.9.125-linuxkit botocore/1.12.50

## Dockerfile
  - `Common` - use for common pipeline (light image version)
  - `Advance` - multi purpose pipeline (with embedded credentials)

## Common Pre-installed Applications
`IMG: gitlab-registry.markcu.com/pipeline:common or latest`
  - Docker Version: 18.06.1-ce
  - Git Version: 2.17.2

## Site Pre-installed Applications
`IMG: gitlab-registry.markcu.com/pipeline:advance`
  - Docker Version: 18.06.1-ce
  - Python Verson: 3.7
  - Pip Version: 18.1
  - AWS CLI: 1.16.74 
  - ECS CLI: 1.12.1
  - ECS Deploy: 1.6.0
  - Tower CLI 3.3.0
  - Git Version: 2.17.2
  - Go lang Version: 1.9
  - Racher CLI 2.2.0
  - Rancher compose 0.12.5