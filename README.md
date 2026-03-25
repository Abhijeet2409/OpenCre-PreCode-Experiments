# OpenCRE Pre-Code Experiments (Scraper & Indexer - Module A)

These experiments were performed locally on the OWASP ASVS repository to validate key assumptions before building the full pipeline.

## Goal
To validate efficient extraction of meaningful repository changes.

## Experiments

### 1. Noise Filtering Pattern
A regex-based exclusion pattern was derived from repository analysis to filter common non-meaningful files (e.g., configuration files, metadata, and images):

```
^(
  \.github/ |
  \.gitignore$ |
  Dockerfile$ |
  CONTRIBUTING\.md$ |
  package-lock\.json$ |
  CNAME$ |
  _config\.yml$ |
  .*\.(png|jpg)$
)
```

Additional patterns (e.g., `.html`, `README.md`, `index.md`) were considered during analysis but not included, as they may contain meaningful content relevant to the indexing process.

---

### 2. File Filtering Script
- Uses `git diff --name-status` to detect file-level changes between the latest commits.
- Applies regex-based filtering to exclude non-meaningful files (e.g., `.github/`, config files, images).
- Outputs a clean list of relevant files for further processing.

#### Terminal Output
```
=== ALL FILES ===
M 5.0/en/0x01-Frontispiece.md
M README.md

=== NON-NOISY FILES ===
5.0/en/0x01-Frontispiece.md
README.md
```

---

### 3. Clean Diff Extraction Script
- Takes filtered files from the previous step as input; integration is automated in the full pipeline.
- Extracts line-level changes using `git diff`.
- Cleans raw diff output by removing metadata and symbols.


#### Terminal Output
```
ADDED:
The project is led by the three project leaders Daniel Cuthbert, Josh Grossman, and Elar Lang.
```

---


