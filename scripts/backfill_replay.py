
import argparse, os, shutil
from datetime import datetime, timedelta

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=7)
    args = parser.parse_args()
    os.makedirs("backfills", exist_ok=True)
    for d in range(args.days):
        day = (datetime.utcnow() - timedelta(days=d)).strftime("%Y-%m-%d")
        dst = f"backfills/events_{day}.csv"
        shutil.copyfile("data/events_latest.csv", dst)
        print("Created", dst)

if __name__ == "__main__":
    main()
