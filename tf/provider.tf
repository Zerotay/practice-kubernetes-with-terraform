terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
      version = "2.31.0"
    }
    http = {
      source = "hashicorp/http"
    }
  }
}
