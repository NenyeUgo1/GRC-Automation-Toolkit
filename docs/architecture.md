# Architecture

## Overview

The GRC Automation Toolkit is designed as a set of **small, independent modules** that each solve a specific Governance, Risk & Compliance problem:

- `risk_scoring/` – asset/vendor risk scoring
- `policy_tracker/` – policy lifecycle tracking
- `control_mapping/` – framework control mapping
- `vendor_assessment/` – third‑party risk assessment

Each module is:

- **Standalone** – can be run independently
- **Simple** – uses CSV/JSON for input/output
- **Extensible** – logic can be adapted to different organisations

## Design Principles

- **Transparency** – all logic is visible and easy to audit.
- **Simplicity** – minimal dependencies, clear data structures.
- **Practicality** – aligned with real GRC workflows (risk registers, policy registers, vendor assessments).

## Data Flow

- Input: CSV/JSON files representing assets, vendors, policies, or controls.
- Processing: Python scripts apply scoring, mapping, or tracking logic.
- Output: Console output or CSV/JSON suitable for importing into other tools.

## Modules

### Risk Scoring

- Input: `sample_vendor_data.csv`
- Processing: Weighted impact/likelihood model
- Output: Risk score + category

### Policy Tracker

- Input: CLI arguments (policy name, owner, status)
- Processing: Reads/writes `policy_register.csv`
- Output: Updated policy register

### Control Mapping

- Input: `iso_to_nist_mapping.json`
- Processing: Simple mapping expansion
- Output: Human‑readable mapping table

### Vendor Assessment

- Input: Vendor questionnaire responses (CSV)
- Processing: Weighted factor model
- Output: Vendor risk score + level
