from pathlib import Path

def file_readers():
    src  = Path.cwd()
    all_content = {}

    ignor = {'.git', 'venv', '.venv'}

    for files_path in src.rglob("*"):
        
        if files_path.is_dir():
            continue

        if any(part in ignor for part in files_path.parts):
            continue
        try:
            content = files_path.read_text(encoding='utf-8')
            path = files_path.relative_to(src)

            all_content[str(path)] = content
        except (UnicodeDecodeError, PermissionError):
            continue

    return all_content
