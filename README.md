# OpenCRE Pre-Code Experiments

This repository contains pre-code experiments conducted for the OpenCRE GSoC project (Scraper & Indexer - Module A).

These experiments were performed locally on the OWASP ASVS repository to validate key assumptions before building the full pipeline.

## Experiments

### 1. File Filtering
- Uses `git diff --name-status` to detect file-level changes between the latest commits.
- Applies regex-based filtering to exclude non-meaningful files (e.g., `.github/`, config files, images).
- Outputs a clean list of relevant files for further processing.
  
## Terminal Output
=== ALL FILES ===
M       5.0/en/0x01-Frontispiece.md
M       README.md
=== NON-NOISY FILES ===
5.0/en/0x01-Frontispiece.md
README.md


### 2. Diff Extraction
- Takes filtered files from the previous step as input (currently provided manually).
- Extracts line-level changes using `git diff`.
- Cleans raw diff output by removing metadata and symbols.
- Focuses on extracting meaningful added content

## Terminal Output 
ADDED :
The project is led by the three project leaders [Daniel Cuthbert](https://github.com/danielcuthbert), [Josh Grossman](https://github.com/tghosth), and [Elar Lang](https://github.com/elarlang).

## Goal
To validate efficient extraction of meaningful repository changes.
