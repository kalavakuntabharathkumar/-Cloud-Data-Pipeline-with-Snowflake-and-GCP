
{{ config(materialized='view') }}
select
  cast(event_time as timestamp) as event_time,
  user_id,
  event_type,
  cast(amount as numeric) as amount,
  cast(payload as {{ 'json' if target.type == 'bigquery' else 'variant' }}) as payload
from {{ ref('raw_events') }}
