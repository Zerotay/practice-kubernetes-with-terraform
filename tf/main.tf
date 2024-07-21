provider "kubernetes" {
  config_path = "~/.kube/config"
  # config_context = "my-context"
}

resource "kubernetes_daemonset" "api-server" {
  metadata {
    name = "api-server-daemon"
    labels = {
      app = "api-server-daemon"
    }
  }
  spec {
    selector {
      match_labels = {
        app = "api-server-daemon"
      }
    }
    template {
      metadata {
        labels = {
          app = "api-server-daemon"
        }
      }
      spec {
        container {
          name = "api-server-daemon"
          image = "zerotay/api-server:v1.0.0"
          port {
            container_port = 8080
          }
        }
      }
    }
  }
}
module "database" {
  source = "./modules/database/"
}


