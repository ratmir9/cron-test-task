import uuid


def generate_file_name():
    return str(uuid.uuid4()).replace('-', '')