from datetime import datetime

# Set your countdown target
target_date = datetime(2025, 5, 1)
now = datetime.utcnow()
delta = target_date - now

# Countdown message
countdown_text = f"<!-- countdown start -->\n" \
                 f"## ⏳ Countdown\n\n" \
                 f"**{delta.days} days** left until May 1, 2025 🚀\n" \
                 f"<!-- countdown end -->"

# Read the current README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the countdown block
start = "<!-- countdown start -->"
end = "<!-- countdown end -->"

if start in content and end in content:
    pre = content.split(start)[0]
    post = content.split(end)[1]
    new_content = pre + countdown_text + post

    # Write updated README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
else:
    print("Countdown markers not found in README.md")
