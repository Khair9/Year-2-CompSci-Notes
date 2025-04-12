from datetime import datetime

# Define exam dates
exams = {
    "P2T": "2025-05-01",
    "Alg & Data": "2025-05-02",
    "OOSE": "2025-05-12",
    "Econ": "2025-05-14",
    "WAD": "2025-05-19",
}

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

now = datetime.utcnow()
new_lines = []
in_table = False
header_handled = False

for line in lines:
    # Skip and remove countdown block (optional)
    if "<!-- countdown start -->" in line:
        new_lines.append("<!-- countdown start -->\n")
        new_lines.append("<!-- countdown end -->\n")
        continue

    # Detect table header
    if "| Subject" in line:
        in_table = True
        header_handled = False
        new_lines.append("| Subject       | Time Left      | Percentage of Grade |\n")
        continue

    # Table separator line (e.g. |--------|------|------|)
    if in_table and not header_handled and "-" in line:
        new_lines.append("|---------------|----------------|----------|\n")
        header_handled = True
        continue

    # Update table rows
    if in_table and "|" in line and header_handled:
        parts = [p.strip() for p in line.strip().split("|")]
        if len(parts) >= 4:
            subject = parts[1]
            progress = parts[3]
            if subject in exams:
                exam_date = datetime.strptime(exams[subject], "%Y-%m-%d")
                days_left = (exam_date - now).days
                time_left = f"in {days_left} days" if days_left >= 0 else "done"
            else:
                time_left = "TBD"
            new_line = f"| {subject:<13} | {time_left:<14} | {progress:<8} |\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    else:
        # End of table
        in_table = False
        new_lines.append(line)

# Save updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
