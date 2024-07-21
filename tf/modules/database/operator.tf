resource "kubernetes_manifest" "mysql-operator" {
  manifest = yamldecode(file("./modules/operator/operator.yml"))
}
resource "kubernetes_manifest" "mysql-crd" {
  manifest = yamldecode(file("./modules/operator/crds.yml"))
}
