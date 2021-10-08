from pathlib import Path
import subprocess
from tqdm import tqdm

log_files = list(Path(
    "/global/cfs/cdirs/m1759/msalim/perlmutter-site/data/production-cross2/"
).glob("*/*.stdout"))

print(len(log_files))
with open("ns_per_day.csv", "w") as stdout:

    for log_file in tqdm(log_files):
        completed_proc = subprocess.run(
            f"python ns_per_day.py -f {log_file}",
            shell=True,
            stdout=stdout,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
        )

