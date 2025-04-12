from datetime import datetime

# Mapping of subjects to their exam dates
exams = {
    "P2T": "2025-05-01",
    "Alg & Data": "2025-05-02",
    "OOSE": "2025-05-12",
    "Econ": "2025-05-14",
    "WAD": "2025-05-19",
}

# Load README
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

now = datetime.utcnow()
new_lines = []
in_table = False

for line in lines:
    # Skip and later replace the countdown block (optional)
    if "<!-- countdown start -->" in line:
        new_lines.append("<!-- countdown start -->\n")
        new_lines.append("<!-- countdown end -->\n")
        continue

    if "| Subject" in line:
        in_table = True
        new_lines.append("| Subject       | Time Left      | Progress |\n")
        continue

    if in_table and "|" in line and not line.startswith("| Subject"):
        parts = line.strip().split("|")
        if len(parts) < 4:
            new_lines.append(line)
            continue

        subject = parts[1].strip()
        date_str = exams.get(subject)
        if date_str:
            exam_date = datetime.strptime(date_str, "%Y-%m-%d")
            days_left = (exam_date - now).days
            time_left = f"in {days_left} days" if days_left >= 0 else "done"
        else:
            time_left = "TBD"

        new_line = f"| {subject:<13} | {time_left:<14} | {parts[3].strip()}      |\n"
        new_lines.append(new_line)
    else:
        new_lines.append(line)

# Write updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
