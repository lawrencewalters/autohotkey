from typing import Dict

def extract(filename: str) -> Dict:
    """Given a filename (full path if necessary), read the key-value pairs, and return as a Dict. File should have `token_name` and `pin`"""
    creds = {}

    try:
        with open(filename) as credentials_file:
            for line in credentials_file:
                name, var = line.partition("=")[::2]
                creds[name.strip()] = var.strip()
    except:
        raise ValueError("Some issue with your password file 'credentials.txt', please fix")
    return creds