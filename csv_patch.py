# csv_patch.py
import csv, sys

CSV = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
new_row = ["Linus Torvalds", "torvalds@linux.org", 1970]

with open(CSV, "a", newline="") as f:
    csv.writer(f).writerow(new_row)
print("✅ Row added to", CSV)
