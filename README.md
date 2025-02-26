# Log Extraction Tool

## Overview
This tool efficiently extracts log entries for a given date from a large log file.

## Setup
1. Clone the repository:

2. Build the index:

3. Extract logs using the optimized script:

4. If you don't have an index, use the simple extractor:

## Files
- `extract_logs.py` - Reads the file line-by-line (slow but simple)
- `build_index.py` - Builds an index for fast retrieval
- `extract_logs_fast.py` - Uses the index for quick searches
- `index.json` - Stores index data for fast lookups