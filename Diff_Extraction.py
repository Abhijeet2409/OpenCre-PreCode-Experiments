import subprocess
file = "README.md"  # Put the filtered file name from File_Filtering Script Output here.

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout

diff = run(["git", "diff", "HEAD~1", "HEAD", "--", file]).split("\n")

# For simplicity and ensuring minimal script (as per requirment) ,
#  I considered prinitng only cleaned "added" lines from raw diffs.
print("ADDED :")

for l in diff:
    if l.startswith("+") and not l.startswith("+++"): #Cleaning...
        text = l[1:].strip()
        if text:
            print(text)
