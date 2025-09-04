
import argparse, time, os, csv, random, string
from datetime import datetime
from security.pii import tokenize

def rand_user():
    return "user_" + ''.join(random.choices(string.ascii_lowercase+string.digits, k=6))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rate", type=int, default=10000, help="events per second")
    parser.add_argument("--seconds", type=int, default=10)
    args = parser.parse_args()

    os.makedirs("/usr/app/data", exist_ok=True)
    path = "/usr/app/data/events_latest.csv"
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["event_time","user_id","event_type","amount","payload"])
        total = args.rate * args.seconds
        for i in range(total):
            evt = [
                datetime.utcnow().isoformat(),
                tokenize(rand_user()),
                random.choice(["page_view","purchase","signup"]),
                round(random.random()*100,2),
                "{}",
            ]
            w.writerow(evt)
            if (i+1) % args.rate == 0:
                time.sleep(1)
    print(f"Wrote {total} events to {path}")

if __name__ == "__main__":
    main()
