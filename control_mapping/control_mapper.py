import json
import os

MAPPING_FILE = "iso_to_nist_mapping.json"


def load_mapping():
    if not os.path.exists(MAPPING_FILE):
        print(f"Mapping file '{MAPPING_FILE}' not found.")
        return {}
    with open(MAPPING_FILE) as f:
        return json.load(f)


def print_mapping(mapping):
    print("ISO 27001 Control,NIST CSF / Other Framework Controls")
    for iso_control, mapped_controls in mapping.items():
        mapped_str = "; ".join(mapped_controls)
        print(f"{iso_control},{mapped_str}")


if __name__ == "__main__":
    mapping = load_mapping()
    if mapping:
        print_mapping(mapping)
