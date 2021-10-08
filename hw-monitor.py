import psutil
import subprocess
from datetime import datetime, timedelta
import time

start = datetime.now()
end = start + timedelta(hours=2)

# SET THESE ACCORDINGLY:
py_exe = '/global/homes/m/msalim/m1759/CryoEM-GB-workflow/venv/bin/python'
nodes = ['nid001465', 'nid001813', 'nid002316', 'nid002372', 'nid002861']

cpu_cmd = f"{py_exe} -c 'from psutil import cpu_percent; print(cpu_percent(percpu=True))'"

while datetime.now() < end:
    time.sleep(15)
    for hostname in nodes:
        cmd = subprocess.run(f"ssh {hostname} nvidia-smi", shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding="utf-8")
        now = datetime.now().isoformat()
        percentages = [w for w in cmd.stdout.split() if w.endswith('%')]
        for gid, pct in enumerate(percentages):
            print(f"{hostname} GPU {gid} {now} {pct}")

        cmd = subprocess.run(f"ssh {hostname} {cpu_cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding="utf-8")
        now = datetime.now().isoformat()
        print(f"{hostname} CPU {now} {cmd.stdout.strip()}")