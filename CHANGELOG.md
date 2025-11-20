# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions CI/CD pipeline migration from Jenkins
- Separated build and deployment concerns into distinct workflows
- Multi-language support (Java, Node.js, Python)
- SonarCloud integration for code quality analysis
- Azure deployment automation
- Comprehensive health checks and monitoring
- Release management workflow
- Security scanning with CodeQL

### Changed
- Migrated from single Jenkins pipeline to multiple GitHub Actions workflows
- Improved deployment strategy with environment-specific configurations
- Enhanced artifact management and retention policies

### Deprecated
- Jenkins pipeline (will be removed after migration completion)

### Removed
- N/A

### Fixed
- N/A

### Security
- Added CodeQL security scanning
- Implemented secure secret management
- Enhanced dependency vulnerability scanning

---

## Migration Timeline

- **Week 1**: Setup and CI implementation
- **Week 2**: Deployment workflow integration  
- **Week 3**: Release workflow and production readiness
- **Week 4**: Full migration and Jenkins decommission