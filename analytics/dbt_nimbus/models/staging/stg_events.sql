{{ config(materialized='view') }}
select
  cast(json_extract_scalar(r, '$.id') as integer) as event_id,
  json_extract_scalar(r, '$.type') as event_type,
  json_extract_scalar(r, '$.repo') as repo,
  json_extract_scalar(r, '$.user') as actor,
  json_extract_scalar(r, '$.ts') as event_ts
from read_json('../../data/bronze/events-00000-of-00001.jsonl') as t(r)
