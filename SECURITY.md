# Security Policy

## Supported Versions

We currently support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| v1.x    | :white_check_mark: |
| older   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in the AI Employee course template, please report it to us privately:

### How to Report

1. **DO NOT** open a public GitHub issue for security vulnerabilities
2. **Email**: security@skalers.io
3. **Subject Line**: `[SECURITY] AI Employee Template - Brief description`
4. **Include**:
   - Description of the vulnerability
   - Affected template/file
   - Potential impact on students using the template
   - Suggested fix (if any)

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 5 business days
- **Fix Timeline**: Critical: 7 days, High: 14 days, Medium: 30 days

## Security Practices

### Template Security

- **No Real Secrets**: Templates use placeholder values only
- **Example Data**: All API keys, tokens are fake examples
- **Clear Warnings**: Templates include security warnings
- **Best Practices**: Templates demonstrate secure patterns

### Student Security Education

Templates teach students to:

1. **Never commit secrets**: Use `.env` files (gitignored)
2. **Rotate API keys**: Change placeholder keys immediately
3. **Validate inputs**: Sanitize all user-provided data
4. **Use parameterized queries**: Prevent SQL injection
5. **Keep dependencies updated**: Run security audits regularly

### Documentation Security

- **Security Sections**: All SOPs include security considerations
- **Common Pitfalls**: Documented with solutions
- **Secure Coding**: Examples follow security best practices
- **Compliance Notes**: GDPR, CAN-SPAM, etc. mentioned where relevant

## Security Vulnerabilities We've Fixed

_None reported yet. This section will be updated as issues are discovered and resolved._

## Security Best Practices for Students

If you're using the AI Employee template:

1. **Replace all placeholder values**: Never use example API keys
2. **Gitignore secrets**: Always add `.env` to `.gitignore`
3. **Review dependencies**: Check for vulnerabilities before deployment
4. **Test security**: Use staging environment before production
5. **Follow SOPs**: Security instructions in each template
6. **Ask questions**: Join Skool community for security advice

## Security Best Practices for Contributors

If you're contributing to the AI Employee template:

1. **No real secrets**: Use fake/placeholder values only
2. **Security comments**: Add warnings where security matters
3. **Test templates**: Verify they work and are secure
4. **Update documentation**: Keep security guidance current
5. **Review dependencies**: No vulnerable packages in templates

## Responsible Disclosure

We follow responsible disclosure practices:

1. Private notification to security@skalers.io
2. Fix developed and tested
3. Template updated for all students
4. Security advisory published
5. Credit given to reporter (if desired)

## Scope

This security policy covers:

- ✅ Context file templates (business.md, strategy.md, personal.md)
- ✅ Instruction files (SOPs and task guides)
- ✅ Automation templates (n8n workflows, scripts)
- ✅ Integration examples (API clients)
- ❌ Student implementations (students responsible for their own security)
- ❌ Third-party services used by students (report to vendors)

## Student Support

For security questions about using the template:

- **Skool Community**: Ask in the private community
- **Email**: support@skalers.io
- **GitHub Issues**: For template bugs (not security vulnerabilities)

## Template Version Updates

When security issues are fixed:

1. **New Release**: Created on GitHub with version bump
2. **Changelog**: Security fixes documented
3. **Student Notification**: Announced in Skool community
4. **Re-download**: Students can download updated template
5. **Migration Guide**: If changes require action from students

## Contact

- **Security Email**: security@skalers.io
- **General Support**: support@skalers.io
- **GitHub**: @systemstoscale
- **Skool Community**: (link provided to enrolled students)

Thank you for helping keep the AI Employee template secure!

---

**Last Updated**: 2026-02-23
