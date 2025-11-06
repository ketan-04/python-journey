import datetime
import subprocess

# Ask user for the message
message = input("Enter your progress update message: ")

# Get today's date
today = datetime.datetime.now().strftime("%d %b %Y")

# Line to add
line = f"- ✅ {today} — {message}\n"

# Read existing README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.readlines()

# Find where "## 💬 Progress Log" is and insert after it
for i, line_content in enumerate(content):
    if "## 💬 Progress Log" in line_content:
        content.insert(i + 1, line)
        break
else:
    # If no progress section found, add at end
    content.append("\n## 💬 Progress Log\n")
    content.append(line)

# Write back updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(content)

# Git commands
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", message])
subprocess.run(["git", "push"])

print("\n✅ Progress updated and pushed to GitHub!")
