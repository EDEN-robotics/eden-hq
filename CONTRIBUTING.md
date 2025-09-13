# 🤝 Contributing to Eden

> Guidelines for contributing to the Eden robotics project

Thank you for your interest in contributing to Eden! This document provides guidelines and information for contributors across all Eden repositories.

## 🚀 Quick Start

1. **Fork** the repository you want to contribute to
2. **Clone** your fork locally
3. **Create** a feature branch
4. **Make** your changes
5. **Test** your changes thoroughly
6. **Submit** a pull request

## 📋 Before You Start

### Prerequisites
- Basic knowledge of Git and GitHub
- Familiarity with the project's technology stack
- Understanding of the project's goals and architecture

### Technology Stack
- **Software**: ROS 2, Python, C++, Docker
- **Hardware**: SolidWorks, KiCad, 3D printing
- **Documentation**: Markdown, Mermaid diagrams

## 🔧 Development Workflow

### 1. Issue Creation
Before starting work, please:
- Check existing issues to avoid duplicates
- Use the appropriate issue template
- Provide clear description and context
- Label issues appropriately (bug, enhancement, documentation)

### 2. Branch Naming
Use descriptive branch names:
```bash
# Good examples
feature/navigation-slam
bugfix/motor-control-timing
docs/api-documentation
hotfix/critical-security-patch

# Avoid
fix
update
changes
```

### 3. Commit Messages
Follow the conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(navigation): add SLAM implementation
fix(hardware): correct motor driver pinout
docs(api): update ROS 2 service documentation
```

### 4. Pull Request Process
- Keep PRs focused and reasonably sized
- Include clear description of changes
- Reference related issues
- Ensure all tests pass
- Request review from maintainers

## 📁 Repository-Specific Guidelines

### eden-software
- **Test-Driven Development**: Write tests before implementing features
- **ROS 2 Standards**: Follow ROS 2 naming conventions and best practices
- **Code Coverage**: Maintain >80% test coverage
- **Documentation**: Include docstrings for all public functions
- **Dependencies**: Minimize external dependencies, document all additions

### eden-hardware
- **Git LFS**: Use Git LFS for CAD files and large binary assets
- **File Organization**: Follow consistent folder structure
- **Version Control**: Use meaningful commit messages for design iterations
- **Documentation**: Include assembly instructions and BOMs
- **Standards**: Follow mechanical and electrical design standards

### eden-docs
- **Markdown**: Use consistent Markdown formatting
- **Diagrams**: Use Mermaid for flowcharts and Gantt charts
- **Images**: Optimize images and use appropriate formats
- **Structure**: Follow the established documentation hierarchy
- **Links**: Ensure all internal links are valid

## 🧪 Testing Requirements

### Software Testing
- **Unit Tests**: Test individual functions and methods
- **Integration Tests**: Test component interactions
- **System Tests**: Test complete workflows
- **Performance Tests**: Ensure performance requirements are met

### Hardware Testing
- **Functional Tests**: Verify all components work as expected
- **Stress Tests**: Test under extreme conditions
- **Environmental Tests**: Test in various operating conditions
- **Safety Tests**: Ensure safety requirements are met

## 📝 Code Style

### Python (eden-software)
- Follow PEP 8 style guide
- Use type hints where appropriate
- Maximum line length: 88 characters
- Use `black` for code formatting
- Use `flake8` for linting

### C++ (eden-software)
- Follow Google C++ Style Guide
- Use `clang-format` for formatting
- Use `cpplint` for style checking
- Prefer modern C++ features (C++17+)

### Documentation
- Use clear, concise language
- Include code examples where helpful
- Use consistent terminology
- Include diagrams for complex concepts

## 🔍 Review Process

### What Reviewers Look For
- **Functionality**: Does the code work as intended?
- **Quality**: Is the code clean and maintainable?
- **Testing**: Are there adequate tests?
- **Documentation**: Is the code well-documented?
- **Performance**: Are there any performance concerns?
- **Security**: Are there any security vulnerabilities?

### Review Timeline
- Initial review: Within 48 hours
- Follow-up reviews: Within 24 hours
- Final approval: Within 1 week

## 🐛 Bug Reports

When reporting bugs, please include:
- **Environment**: OS, Python version, ROS 2 version
- **Steps to Reproduce**: Clear, numbered steps
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Screenshots/Logs**: Visual evidence when helpful
- **Additional Context**: Any other relevant information

## 💡 Feature Requests

When requesting features, please include:
- **Use Case**: Why is this feature needed?
- **Proposed Solution**: How should it work?
- **Alternatives**: Other approaches considered
- **Additional Context**: Any other relevant information

## 🏷️ Labels and Milestones

### Issue Labels
- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to documentation
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention is needed
- `priority: high`: High priority
- `priority: medium`: Medium priority
- `priority: low`: Low priority

### Pull Request Labels
- `ready for review`: Ready for reviewer attention
- `work in progress`: Still being worked on
- `needs testing`: Requires testing before merge
- `breaking change`: Changes existing functionality

## 📞 Getting Help

- **GitHub Discussions**: For questions and general discussion
- **GitHub Issues**: For bug reports and feature requests
- **Discord/Slack**: For real-time chat (if available)
- **Email**: For sensitive or private matters

## 📜 Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inspiring community for all. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

### Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated promptly and fairly.

## 📄 License

By contributing to Eden, you agree that your contributions will be licensed under the same license as the project. See the [LICENSE](LICENSE) file for details.

## 🙏 Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation
- Annual contributor appreciation

---

*Thank you for contributing to Eden! Together, we're building the future of robotics.* 🤖✨
