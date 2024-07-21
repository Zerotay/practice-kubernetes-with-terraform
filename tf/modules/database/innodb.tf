resource "kubernetes_manifest" "innodb" {
  manifest = {
    "apiVersion" = "mysql.oracle.com/v2"
    "kind" = "InnoDBCluster"
    "metadata" = {
      "name" = "inno-db"
    }
    "spec" = {
      "secretName" = "root-info"
      "tlsUseSelfSigned" = true
      "instances" = 3
      "router"= {
        "instances"= 1
      }
    }
  }
}
