# 🛠️ DevOps Toolkit

**A collection of battle‑tested DevOps utilities written in Python, Bash, and Go.**

This repository contains the day‑to‑day automation tools used by our Platform
Engineering team. Each tool is self‑contained, documented, and tested. They are
designed to be copied, adapted, and run directly in any environment – whether
a CI pipeline, a jump host, or your local machine.

## 📂 Repository Structure

```
devops-toolkit/
├── python/
│   ├── aws-cleanup/          # Delete unattached EBS volumes and old snapshots
│   ├── ebs-audit/            # List all EBS volumes with size, type, and attachment
│   ├── iam-audit/            # List IAM users and their access key last used dates
│   ├── cost-report/          # Retrieve current month's AWS cost per service
│   └── log-rotator/          # Rotate log files when they exceed a size threshold
├── bash/
│   ├── backup/               # Simple tar‑based backup script
│   └── service-monitor/      # Check if a systemd service is running, restart if not
├── go/
│   ├── healthcheck/          # HTTP health check against a given URL
│   ├── log-parser/           # Parse log files with a regex pattern
│   └── kube-cleaner/         # Delete failed pods in a Kubernetes namespace
├── .github/workflows/ci.yml  # CI pipeline (tests, linting)
└── docs/                     # Additional documentation (future)
```

## ⚙️ Requirements

- **Python 3.9+** (for Python tools) with `pip`
- **Bash 4+** (for shell scripts)
- **Go 1.21+** (for Go tools)
- **shellcheck** (for linting Bash scripts, optional)
- **AWS credentials** configured (via environment variables, IAM roles, or `~/.aws/credentials`) for the AWS‑related tools.
- **kubectl** and a valid kubeconfig for the `kube-cleaner` tool.

## 🚀 Using the Tools

### Python Tools

Each tool is a standalone Python script. You can run them directly or install
dependencies via `requirements.txt`.

**Example: AWS Cleanup (dry‑run)**
```bash
cd python/aws-cleanup
pip install -r requirements.txt
python aws_cleanup.py --dry-run
# To actually delete: python aws_cleanup.py --execute --days 30
```

**Example: Cost Report**
```bash
cd python/cost-report
pip install -r requirements.txt
python cost_report.py
```

### Bash Tools

Scripts are executable; just run them.

**Backup:**
```bash
./bash/backup/backup.sh /path/to/source /path/to/backup
```

**Service Monitor:**
```bash
./bash/service-monitor/service_monitor.sh nginx
```

### Go Tools

Build and run, or just `go run`.

**Healthcheck:**
```bash
cd go/healthcheck
go run main.go http://example.com/health
```

**Log Parser:**
```bash
cd go/log-parser
go run main.go /var/log/app.log "ERROR|WARN"
```

**Kube Cleaner:**
```bash
cd go/kube-cleaner
go run main.go --namespace staging
```

## 🧪 Running Tests

### Python
```bash
cd python/<tool>
pip install -r requirements.txt
pytest .
```

### Bash
```bash
shellcheck bash/**/*.sh
```

### Go
```bash
cd go/<tool>
go test ./...
```

## 🔄 CI/CD

A GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push:

- **Python tools:** Installs dependencies and executes `pytest`.
- **Bash scripts:** Lints with `shellcheck`.
- **Go tools:** Builds and runs `go test`.

This ensures that all utilities remain functional and follow best practices.

## 🛠️ Contributing

We welcome new utilities that follow the existing pattern:

1. Create a new directory under `python/`, `bash/`, or `go/`.
2. Include a `README.md` in the tool's directory explaining its purpose and usage.
3. Add tests where applicable.
4. Ensure the CI passes.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📄 License

MIT – see [LICENSE](LICENSE).

---

**Built by engineers who fix things before they break.**
```