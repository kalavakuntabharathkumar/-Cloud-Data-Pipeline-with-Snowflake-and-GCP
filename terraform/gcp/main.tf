
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.5.0"
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "lake" {
  name     = "${var.project_id}-nimbusflow-lake"
  location = var.region
  uniform_bucket_level_access = true
}

resource "google_service_account" "dataflow" {
  account_id   = "nimbusflow-dataflow"
  display_name = "NimbusFlow Dataflow SA"
}

resource "google_bigquery_dataset" "demo" {
  dataset_id = var.bq_dataset
  location   = "US"
}

variable "project_id" {}
variable "region" { default = "us-central1" }
variable "bq_dataset" { default = "nimbusflow_demo" }
