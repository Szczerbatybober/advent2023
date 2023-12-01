def read_file(file_name) -> list[str]:
    with open(file_name) as f:
        content = f.readlines()
    return [line.strip() for line in content]
