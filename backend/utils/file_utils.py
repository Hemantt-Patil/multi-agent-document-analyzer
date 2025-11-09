def save_file(file_content: bytes, filename: str):
    with open(filename, "wb") as f:
        f.write(file_content)
