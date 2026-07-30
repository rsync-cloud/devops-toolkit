#!/bin/bash
set -euo pipefail
# Service monitor – checks if a process is running, restarts if down
SERVICE="${1:-}"
if [[ -z "$SERVICE" ]]; then
    echo "Usage: $0 <service-name>"
    exit 1
fi

if pgrep -x "$SERVICE" > /dev/null; then
    echo "Service $SERVICE is running."
else
    echo "Service $SERVICE is down. Attempting restart..."
    sudo systemctl restart "$SERVICE" || true
    if pgrep -x "$SERVICE" > /dev/null; then
        echo "Service $SERVICE restarted successfully."
    else
        echo "Failed to restart $SERVICE."
        exit 2
    fi
fi
