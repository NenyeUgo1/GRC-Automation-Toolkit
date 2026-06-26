import csv
import sys

RISK_LEVELS = [
    (0, 20, "Low"),
    (21, 40, "Medium"),
    (41, 70, "High"),
    (71, 100, "Critical"),
]


def calculate_risk_score(impact, likelihood):
    """
    Simple weighted risk scoring model:
    risk_score = (impact * 0.6) + (likelihood * 0.4)
    impact and likelihood are expected to be integers between 0 and 10.
    """
    return (impact * 0.6) + (likelihood * 0.4)


def categorize_risk(score):
    for low, high, label in RISK_LEVELS:
        if low <= score <= high:
            return label
    return "Unknown"


def process_csv(input_file):
    with open(input_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        print("Asset/Vendor,Risk Score,Risk Level")
        for row in reader:
            name = row.get("name", "Unknown")
            impact = float(row.get("impact", 0))
            likelihood = float(row.get("likelihood", 0))
            score = calculate_risk_score(impact, likelihood) * 10  # scale to 0–100
            level = categorize_risk(score)
            print(f"{name},{score:.1f},{level}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python risk_scoring.py <input_csv>")
        sys.exit(1)
    process_csv(sys.argv[1])
