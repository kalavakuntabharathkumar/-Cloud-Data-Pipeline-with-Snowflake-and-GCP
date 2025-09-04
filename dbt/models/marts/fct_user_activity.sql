
{{ config(materialized='table') }}
select
  user_id,
  count(*) as event_count,
  sum(amount) as revenue
from {{ ref('stg_events') }}
group by 1
