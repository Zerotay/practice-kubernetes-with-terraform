# output "cluster_endpoint" {
#   description = "The endpoint for the EKS API server."
#   value       = aws_eks_cluster.example.endpoint
# }

# output "cluster_certificate_authority_data" {
#   description = "The base64 encoded certificate data required to communicate with the cluster."
#   value       = aws_eks_cluster.example.certificate_authority[0].data
# }

# output "cluster_name" {
#   description = "The name of the EKS cluster."
#   value       = aws_eks_cluster.example.name
# }

output "kuber-test" {
   value = path.root
   description = "What is this"
}

