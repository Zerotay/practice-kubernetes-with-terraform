resource "kubernetes_secret" "root" {
  metadata {
    name = "root-info"
  }
  data = {
    rootUser = "cm9vdA=="
    rootHost = "JQ=="
    rootPassword = "cm9vdA=="
  }
}
