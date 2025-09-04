
{{ config(materialized='view') }}
-- Placeholder raw source; in real deployments this would be an external table
select * from (
  select
    current_timestamp as event_time,
    'user_1' as user_id,
    'purchase' as event_type,
    19.99 as amount,
    '{}' as payload
)
