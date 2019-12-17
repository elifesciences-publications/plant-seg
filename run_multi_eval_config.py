import glob
import yaml
import subprocess

paths = glob.glob("./evaluation/multicut/_e*.yml")

print(paths)
for path in paths:
    print(path)
    subprocess.run(["python", "./evaluation/evaluation.py", "--config", path])