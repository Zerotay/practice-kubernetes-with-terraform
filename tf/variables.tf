variable "aws_region" {
  description = "The AWS region to create resources in."
  type        = string
  default     = "us-west-2"
}

variable "cluster_name" {
  description = "The name of the EKS cluster."
  type        = string
  default     = "example-eks-cluster"
}

variable "subnet_ids" {
  description = "A list of subnet IDs for the EKS cluster."
  type        = list(string)
  default     = ["subnet-0bb1c79de3EXAMPLE", "subnet-0bb1c79de3EXAMPLE"]
}

