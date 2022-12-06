def get_file_obj(filename: str):
    fh = open(f"inputs/{filename}", "r")
    return fh
