def check_file_extension(content, extensions):
    return any(content.endswith(ext) for ext in extensions)