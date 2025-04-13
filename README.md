# Kubernetes in Action: Mastering Container Orchestration 🚀

Welcome to the **Kubernetes in Action: Mastering Container Orchestration** workshop! This hands-on project will guide you through deploying and managing a Flask application on Kubernetes using a variety of native and advanced features.

---

## 🧭 Workshop Overview

This workshop is divided into multiple labs, each focusing on a specific concept or resource within Kubernetes. By the end, you'll have practical experience with deployments, scaling, configuration management, persistent storage, health monitoring, and Helm packaging.

---

## 📚 Labs Summary

| Lab | Title                                             | Focus Areas |
|-----|---------------------------------------------------|-------------|
| 01  | Deploying a Flask Application                     | Deployment, Service |
| 02  | Managing Configuration with ConfigMaps & Secrets  | ConfigMap, Secret |
| 03  | Using Persistent Storage                          | PVC, PV |
| 04  | Auto-scaling with Horizontal Pod Autoscaler       | HPA, Metrics |
| 05  | Readiness & Liveness Probes                       | Health Probes |
| 06  | Packaging with Helm                               | Helm, Templates |

---

## 🛠️ Prerequisites

- Docker
- Kubernetes Cluster (minikube, kind, or cloud-based)
- `kubectl`
- `helm` (for Lab 06)
---

## 🚀 Getting Started

1. Clone this repository:
```bash
git clone https://github.com/your-org/k8s-zero-to-hero-workshop.git
cd k8s-zero-to-hero-workshop
```

2. Choose your lab folder:
```bash
cd labs/lab01-deploy-app
```

3. Follow the instructions in the `README.md` of that lab.

---

## 🧼 Cleanup

To remove all created resources after each lab:
```bash
kubectl delete -f .
```

For Helm:
```bash
helm uninstall flask-app
```

---

## 📘 Additional Resources

- [Kubernetes Docs](https://kubernetes.io/docs/)
- [Helm Docs](https://helm.sh/docs/)
- [Flask Docs](https://flask.palletsprojects.com/)

---

## 🎓 Outcome

By the end of this workshop, you will have:
- Deployed and scaled a containerized app
- Used core Kubernetes concepts
- Managed configuration and secrets securely
- Persisted data across pod restarts
- Monitored and healed apps with probes
- Packaged and deployed apps using Helm
---

Happy Shipping! ⚓
