import subprocess

commands = [
    ["git", "--version"],
    ["git", "status"],
    ["git", "remote", "-v"]
]

for cmd in commands:
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
    except Exception as e:
        print("ERROR:", str(e))
    print("-" * 40)
