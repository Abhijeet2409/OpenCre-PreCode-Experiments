import subprocess, re

EXCLUDE = re.compile(
    r'^\.github/|\.gitignore$|Dockerfile$|CONTRIBUTING\.md$|package-lock\.json$|CNAME$|_config\.yml$|\.(png|jpg)$'
)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout

diff_files = run(["git", "diff", "--name-status", "HEAD~1", "HEAD"]).split("\n")

print("=== ALL FILES ===")
for line in diff_files:
    if line:
        print(line)

print("=== NON-NOISY FILES ===")
clean_files = []

for line in diff_files:
    if not line: continue
    parts = line.split("\t")
    status, path = parts[0], parts[-1]

# Intentional skipping of deleted files in commit(to align with the proposed approach).
    if status == "D":
        continue  

    if EXCLUDE.search(path):
        continue

    clean_files.append(path)
    print(path)