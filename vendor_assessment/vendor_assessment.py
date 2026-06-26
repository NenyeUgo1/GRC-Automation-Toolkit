import csv
import sys

FACTORS = {
    "data_sensitivity": 0.4,
    "vendor_criticality": 0.3,
    "security_maturity": 0.2,
    "compliance_alignment": 0.1,
}


def calculate_vendor_risk(row):
    score = 0
    for factor, weight in FACTORS.items():
        value = float(row.get(factor, 0))
        score += value * weight
    return score * 10  # scale to 0–100


def categorize(score):
    if score < 20:
        return "Low"
    elif score < 40:
        return "Medium"
    elif score < 70:
        return "High"
    else:
        return "Critical"


def process_vendors(input_file):
    with open(input_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        print("Vendor,Risk Score,Risk Level")
        for row in reader:
            name = row.get("vendor_name", "Unknown")
            score = calculate_vendor_risk(row)
            level = categorize(score)
            print(f"{name},{score:.1f},{level}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vendor_assessment.py <vendor_csv>")
        sys.exit(1)
    process_vendors(sys.argv[1])
