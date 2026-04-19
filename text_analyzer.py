import functools
import subprocess
from pathlib import Path


TEXT_EXTENSIONS = {
    ".txt",
    ".md",
    ".csv",
    ".json",
    ".xml",
    ".html",
    ".htm",
    ".py",
    ".js",
    ".ts",
    ".css",
    ".log",
}

TEXTUTIL_EXTENSIONS = {
    ".doc",
    ".docx",
    ".rtf",
    ".rtfd",
    ".odt",
    ".wordml",
    ".webarchive",
    ".html",
    ".htm",
}


def normalize(doc):
    return doc.strip().lower()


def is_valid(doc):
    cleaned = normalize(doc)
    if cleaned == "":
        return False
    if cleaned.isdigit():
        return False
    return True


def word_count(doc):
    list_words = doc.split()
    return len(list_words)


def func(docs, funct):
    new_docs = docs.copy()
    return list(map(funct, new_docs))


def read_plain_text(path):
    return path.read_text(encoding="utf-8", errors="ignore")


def read_with_textutil(path):
    result = subprocess.run(
        ["textutil", "-convert", "txt", "-stdout", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        return result.stdout
    return ""


def read_pdf_with_mdls(path):
    result = subprocess.run(
        ["mdls", "-name", "kMDItemTextContent", "-raw", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""

    output = result.stdout.strip()
    if output in {"(null)", ""}:
        return ""
    return output


def extract_text(path):
    suffix = path.suffix.lower()

    if suffix in TEXT_EXTENSIONS:
        return read_plain_text(path)

    if suffix == ".pdf":
        return read_pdf_with_mdls(path)

    if suffix in TEXTUTIL_EXTENSIONS:
        return read_with_textutil(path)

    return read_plain_text(path)


def collect_files():
    files = []

    while True:
        user_input = input("Enter a file or folder path (or 'done' to finish): ").strip()
        if user_input.lower() == "done":
            break
        if user_input == "":
            continue

        path = Path(user_input).expanduser()

        if not path.exists():
            print(f"Skipped: {path} does not exist.")
            continue

        if path.is_file():
            files.append(path)
            continue

        if path.is_dir():
            for item in sorted(path.rglob("*")):
                if item.is_file():
                    files.append(item)
            continue

    return files


def load_documents(files):
    documents = []

    for file_path in files:
        try:
            text = extract_text(file_path)
        except Exception as error:
            print(f"Could not read {file_path}: {error}")
            continue

        print(f"Loaded: {file_path}")
        print(f"Characters extracted: {len(text)}")
        documents.append((str(file_path), text))

    return documents


files = collect_files()
print(f"Files collected: {len(files)}")
for file_path in files:
    print(f" - {file_path}")

documents = load_documents(files)

valid_documents = []
for path, text in documents:
    if is_valid(text):
        print(f"Valid: {path}")
        valid_documents.append((path, text))
    else:
        cleaned = normalize(text)
        if cleaned == "":
            print(f"Rejected: {path} because it is empty after extraction.")
        elif cleaned.isdigit():
            print(f"Rejected: {path} because it only contains digits.")
        else:
            print(f"Rejected: {path} because it did not pass validation.")

valid_docs = [text for _, text in valid_documents]

print("Valid docs:")
print(valid_docs)

valid_wordcount = list(map(word_count, valid_docs))
print("Word counts:")
print(valid_wordcount)

doc_count = list(zip(valid_documents, valid_wordcount))
print("Document counts:")
print(doc_count)

tot_wordcount = functools.reduce(lambda acc, x: acc + x, valid_wordcount, 0)
print("Total word count:")
print(tot_wordcount)
