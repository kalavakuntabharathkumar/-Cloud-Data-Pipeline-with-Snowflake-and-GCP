
terraform {
  required_providers {
    snowflake = {
      source = "Snowflake-Labs/snowflake"
      version = "~> 0.96"
    }
  }
  required_version = ">= 1.5.0"
}

provider "snowflake" {}

resource "snowflake_warehouse" "wf" {
  name = "NIMBUSFLOW_WH"
  warehouse_size = "XSMALL"
  auto_suspend = 60
  auto_resume  = true
}

resource "snowflake_database" "db" {
  name = "NIMBUSFLOW_DB"
}

resource "snowflake_schema" "demo" {
  database = snowflake_database.db.name
  name     = "DEMO"
}

output "warehouse" { value = snowflake_warehouse.wf.name }
output "database" { value = snowflake_database.db.name }
output "schema"    { value = snowflake_schema.demo.name }
