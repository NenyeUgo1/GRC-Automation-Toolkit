import csv
import os
import sys
from datetime import datetime

POLICY_FILE = "policy_register.csv"
FIELDNAMES = ["policy_name", "version", "owner", "last_updated", "status"]


def init_register():
    if not os.path.exists(POLICY_FILE):
        with open(POLICY_FILE, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_policies():
    init_register()
    with open(POLICY_FILE, newline="") as csvfile:
        return list(csv.DictReader(csvfile))


def save_policies(policies):
    with open(POLICY_FILE, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(policies)


def update_policy(policy_name, owner="Unknown", status="Draft"):
    policies = load_policies()
    for policy in policies:
        if policy["policy_name"].lower() == policy_name.lower():
            version = int(policy["version"]) + 1
            policy["version"] = str(version)
            policy["owner"] = owner
            policy["last_updated"] = datetime.utcnow().isoformat()
            policy["status"] = status
            save_policies(policies)
            print(f"Updated policy '{policy_name}' to version {version}")
            return

    # If not found, create new
    new_policy = {
        "policy_name": policy_name,
        "version": "1",
        "owner": owner,
        "last_updated": datetime.utcnow().isoformat(),
        "status": status,
    }
    policies.append(new_policy)
    save_policies(policies)
    print(f"Created new policy '{policy_name}' with version 1")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python policy_tracker.py <policy_name> [owner] [status]")
        sys.exit(1)

    policy_name = sys.argv[1]
    owner = sys.argv[2] if len(sys.argv) > 2 else "Unknown"
    status = sys.argv[3] if len(sys.argv) > 3 else "Draft"
    update_policy(policy_name, owner, status)
