 HEAD
# File_analyzer
It is a simple Python script that reads files or folders, extracts text from supported document types, filters out invalid documents, and reports word counts.

# Text Analyzer

`text_analyzer.py` is a simple Python script that reads files or folders, extracts text from supported document types, filters out invalid documents, and reports word counts.

## What It Does

- Accepts one or more file paths or folder paths from user input
- Recursively collects files from folders
- Reads plain-text files directly
- Reads `.doc`, `.docx`, `.rtf`, `.rtfd`, `.odt`, `.wordml`, and `.webarchive` files with macOS `textutil`
- Attempts to extract text from `.pdf` files with macOS `mdls`
- Rejects empty documents
- Rejects documents that contain only digits
- Prints:
  - valid documents
  - word counts for each valid document
  - document/count pairs
  - total word count
  - debug information showing what was collected and why files were accepted or rejected

## Requirements

- Python 3
- macOS

This script currently depends on built-in macOS tools:

- `textutil` for Word and rich-text document conversion
- `mdls` for PDF text extraction

## Supported File Types

Plain text types:

- `.txt`
- `.md`
- `.csv`
- `.json`
- `.xml`
- `.html`
- `.htm`
- `.py`
- `.js`
- `.ts`
- `.css`
- `.log`

Rich text / document types:

- `.doc`
- `.docx`
- `.rtf`
- `.rtfd`
- `.odt`
- `.wordml`
- `.webarchive`

PDF:

- `.pdf`

## How To Run

From the project folder:

```bash
python3 text_analyzer.py
```

Then enter file paths or folder paths one at a time:

```text
/Users/shashank/Documents/report.pdf
/Users/shashank/Documents/notes.docx
/Users/shashank/txt
done
```

## Example Output

```text
Files collected: 1
 - sample_test.txt
Loaded: sample_test.txt
Characters extracted: 29
Valid: sample_test.txt
Valid docs:
['hello world from sample file\n']
Word counts:
[5]
Document counts:
[(('sample_test.txt', 'hello world from sample file\n'), 5)]
Total word count:
5
```

## Validation Rules

A document is considered invalid if:

- it is empty after extraction
- it contains only digits

Everything else is treated as valid text.

## Notes

- PDF extraction may fail for scanned PDFs or PDFs without searchable text.
- If a file cannot be read, the script prints an error and continues.
- If a folder is entered, the script searches all files inside it recursively.

## Project Files

- [text_analyzer.py](/Users/shashank/txt/text_analyzer.py:1)
- [README.md](/Users/shashank/txt/README.md:1)
 dc914fe (finis)
