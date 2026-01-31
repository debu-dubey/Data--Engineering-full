import subprocess
import os

def run_step(script_path):
    print(f'Running {script_path}')
    result = subprocess.run(["python3",script_path], capture_output = True, text = True)
    if result.returncode == 0:
        print(f"Script {script_path} successfully executed")
    else:
        print(f"Error executing {script_path}")
        print(result.stderr)


pipeline_steps = [
    "data_generation.py",
    "Bronze/load_to_sql.py",
    "Silver/transform_silver.py",
    "Gold/transform_gold.py"
]


for step in pipeline_steps:
    run_step(step)