import subprocess

with open("git_test_out.txt", "w") as f:
    try:
        res = subprocess.run(["git", "--version"], capture_output=True, text=True)
        f.write(f"STDOUT: {res.stdout}\n")
        f.write(f"STDERR: {res.stderr}\n")
    except Exception as e:
        f.write(f"ERROR: {str(e)}\n")
