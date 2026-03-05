# Lessons Learned

*Things your AI system has learned from mistakes. When something breaks, add the fix here so it never happens again.*

## Format

```
### [Short title]
**Problem:** What went wrong
**Fix:** What solved it
**Rule:** The rule to follow going forward
```

## Lessons

### Example: API key formatting
**Problem:** API key had a trailing space, causing auth failures
**Fix:** Trimmed whitespace from .env values
**Rule:** Never add spaces around `=` in .env files. Always trim values.
