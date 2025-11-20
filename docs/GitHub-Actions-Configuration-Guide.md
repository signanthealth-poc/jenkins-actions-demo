# GitHub Actions Configuration Guide
*Signant Health Demo - Jenkins to GitHub Actions Migration*

## Repository Setup Checklist

### 1. GitHub Repository Settings

#### Environments
Create the following environments in your repository settings:
- **dev** - Development environment
- **staging** - Staging environment  
- **prod** - Production environment (with protection rules)

#### Environment Protection Rules (for Production)
- ✅ Required reviewers (recommend 2+ reviewers)
- ✅ Restrict deployments to main branch
- ✅ Deployment timeout: 10 minutes

### 2. Repository Secrets

Add these secrets in GitHub Repository Settings → Secrets and variables → Actions:

#### Required Secrets
```
AZURE_CREDENTIALS          # Azure service principal credentials (JSON)
SONAR_TOKEN                # SonarCloud authentication token
GITHUB_TOKEN               # Automatically provided by GitHub
```

#### Optional Secrets
```
SLACK_WEBHOOK_URL          # For notifications (if using Slack)
DOCKER_REGISTRY_PASSWORD   # If using private container registry
```

### 3. Repository Variables

Add these variables in GitHub Repository Settings → Secrets and variables → Actions:

#### Global Variables
```
RESOURCE_GROUP_NAME        # Azure resource group name
APP_NAME_PREFIX           # Prefix for Azure app service names
TERRAFORM_RESOURCE_GROUP  # Resource group for Terraform state
```

#### Environment-Specific Variables

**Development Environment:**
```
RESOURCE_GROUP_NAME=rg-signant-demo-dev
APP_NAME_PREFIX=signant-demo-dev
DATABASE_NAME=signant-demo-dev-db
```

**Staging Environment:**
```
RESOURCE_GROUP_NAME=rg-signant-demo-staging
APP_NAME_PREFIX=signant-demo-staging
DATABASE_NAME=signant-demo-staging-db
```

**Production Environment:**
```
RESOURCE_GROUP_NAME=rg-signant-demo-prod
APP_NAME_PREFIX=signant-demo-prod
DATABASE_NAME=signant-demo-prod-db
```

## Azure Configuration

### 1. Service Principal Setup

Create an Azure service principal for GitHub Actions:

```bash
# Login to Azure
az login

# Create service principal
az ad sp create-for-rbac \
  --name "GitHub-Actions-Signant-Demo" \
  --role contributor \
  --scopes /subscriptions/{subscription-id} \
  --sdk-auth
```

Copy the JSON output to the `AZURE_CREDENTIALS` secret.

### 2. Azure Resources Required

#### Resource Groups
```bash
# Development
az group create --name rg-signant-demo-dev --location eastus

# Staging
az group create --name rg-signant-demo-staging --location eastus

# Production
az group create --name rg-signant-demo-prod --location eastus
```

#### App Services (Example for Java component)
```bash
# Development
az appservice plan create \
  --name asp-signant-demo-dev \
  --resource-group rg-signant-demo-dev \
  --sku B1

az webapp create \
  --name signant-demo-java-dev \
  --resource-group rg-signant-demo-dev \
  --plan asp-signant-demo-dev \
  --runtime "JAVA:17-java17"
```

## SonarCloud Configuration

### 1. SonarCloud Project Setup
1. Go to [SonarCloud.io](https://sonarcloud.io)
2. Import your GitHub repository
3. Generate a token in Account → Security
4. Add token to `SONAR_TOKEN` secret

### 2. Quality Gate Configuration
Update your sonar-project.properties:
```properties
sonar.projectKey=signant-health_demo-repo
sonar.organization=signant-health
sonar.sources=.
sonar.exclusions=**/node_modules/**,**/target/**,**/*.spec.ts,**/*.test.js
sonar.coverage.exclusions=**/test/**,**/*.test.*,**/*.spec.*
sonar.java.binaries=**/target/classes
sonar.javascript.lcov.reportPaths=coverage/lcov.info
sonar.python.coverage.reportPaths=coverage.xml
```

## Branch Protection Rules

Configure branch protection for main branch:
- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass before merging
  - CI Pipeline / quality-gate
  - CI Pipeline / test
  - CI Pipeline / analyze
- ✅ Require branches to be up to date before merging
- ✅ Restrict pushes that create files larger than 100MB

## Notification Setup

### Slack Integration (Optional)
1. Create a Slack webhook URL
2. Add URL to `SLACK_WEBHOOK_URL` secret
3. Configure channel for notifications

### Email Notifications
GitHub automatically sends email notifications for:
- Failed workflow runs
- Deployment status updates
- Security alerts

## Migration Steps

### Phase 1: Basic Setup (Week 1)
1. ✅ Create GitHub repository structure
2. ✅ Configure environments and secrets
3. ✅ Set up Azure resources
4. ✅ Configure SonarCloud integration
5. ✅ Test CI workflow with development branch

### Phase 2: Deployment Integration (Week 2)
1. Deploy workflow testing with dev environment
2. Configure infrastructure provisioning
3. Set up health checks and monitoring
4. Test end-to-end pipeline

### Phase 3: Production Readiness (Week 3)
1. Configure production environment protection
2. Set up release workflow
3. Configure monitoring and alerting
4. Run parallel Jenkins/GitHub Actions for validation

### Phase 4: Full Migration (Week 4)
1. Switch default branch protection to require GitHub Actions
2. Disable Jenkins pipeline
3. Monitor and optimize performance
4. Team training on new workflows

## Troubleshooting Guide

### Common Issues

#### 1. Azure Authentication Failures
```bash
# Verify service principal credentials
az login --service-principal \
  --username {app-id} \
  --password {password} \
  --tenant {tenant-id}
```

#### 2. SonarCloud Quality Gate Failures
- Check coverage thresholds
- Verify exclusion patterns
- Review security hotspots

#### 3. Deployment Failures
- Check Azure resource availability
- Verify environment variables
- Review application logs

#### 4. Artifact Download Failures
- Ensure build workflow completed successfully
- Check artifact retention policy
- Verify workflow permissions

### Monitoring and Maintenance

#### Weekly Tasks
- Review failed workflow runs
- Monitor deployment success rates
- Check security alerts

#### Monthly Tasks
- Review and update dependencies
- Analyze pipeline performance metrics
- Update documentation

## Cost Optimization

### GitHub Actions Minutes
- Use self-hosted runners for long-running tasks
- Optimize matrix strategies
- Cache dependencies effectively

### Azure Resources
- Use appropriate service tiers for each environment
- Implement auto-scaling policies
- Review and clean up unused resources

## Security Best Practices

### Secrets Management
- Rotate secrets regularly
- Use least-privilege access
- Monitor secret usage

### Code Security
- Enable Dependabot alerts
- Configure CodeQL analysis
- Review security advisories

### Infrastructure Security
- Use Azure Key Vault for sensitive data
- Implement network security groups
- Enable Azure Security Center

## Support and Documentation

### Internal Resources
- Migration documentation: [Link to internal wiki]
- Team contacts: [Development team contacts]
- Escalation procedures: [Support procedures]

### External Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Azure DevOps Integration](https://docs.microsoft.com/en-us/azure/devops/)
- [SonarCloud Documentation](https://docs.sonarcloud.io/)

---

## Next Steps

1. **Review this configuration guide** with your team
2. **Set up the Azure resources** in your subscription
3. **Configure the GitHub repository** with secrets and variables
4. **Test the CI workflow** with a feature branch
5. **Gradually roll out** the deployment and release workflows

Would you like me to create any specific configuration files or help with any particular aspect of the setup?