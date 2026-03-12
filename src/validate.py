#!/usr/bin/env python3


def is_morphologika(file: list[str]) -> bool:
    # Instantiate dictionary with required headers as keys and False as values
    required_headers = {
        "[individuals]": False,
        "[landmarks]": False,
        "[dimensions]": False,
        "[names]": False,
        "[rawpoints]": False,
    }

    # Loop through lines
    for line in file:
        if line.strip() in required_headers.keys():
            # Update dictionary value to True for the corresponding header
            required_headers[line.strip()] = True
            # Break if all required headers have been found
            if all(required_headers.values()):
                return True

    # If not all required headers were found, return False
    return False
