#!/usr/bin/env python3
import argparse, json, os, pathlib, time
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def parse_jsonl(line: str):
    d = json.loads(line)
    d['ingest_time'] = time.time()
    return d

def run(input_path: str, dest_dir: str):
    pathlib.Path(dest_dir).mkdir(parents=True, exist_ok=True)
    options = PipelineOptions(["--runner=DirectRunner"])
    with beam.Pipeline(options=options) as p:
        rows = (p
            | "Read" >> beam.io.ReadFromText(input_path)
            | "Parse" >> beam.Map(parse_jsonl)
        )
        # Write as newline-delimited JSON (bronze)
        _ = (rows
             | "Format" >> beam.Map(json.dumps)
             | "Write" >> beam.io.WriteToText(os.path.join(dest_dir, "events"), file_name_suffix=".jsonl", num_shards=1))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--dest", required=True)
    args = ap.parse_args()
    run(args.source, args.dest)
