#!/bin/bash
# Script to view logs easily
# Usage: ./view_logs.sh [log_type]

LOG_DIR="logs"

# Create logs directory if it doesn't exist
mkdir -p $LOG_DIR

case "$1" in
    "error"|"errors")
        echo "=== ERROR LOG ==="
        if [ -f "$LOG_DIR/errors.log" ]; then
            tail -n 100 $LOG_DIR/errors.log
        else
            echo "No error log found"
        fi
        ;;
    "access")
        echo "=== ACCESS LOG ==="
        if [ -f "$LOG_DIR/access.log" ]; then
            tail -n 100 $LOG_DIR/access.log
        else
            echo "No access log found"
        fi
        ;;
    "app"|"main")
        echo "=== APPLICATION LOG ==="
        if [ -f "$LOG_DIR/report_generator.log" ]; then
            tail -n 100 $LOG_DIR/report_generator.log
        else
            echo "No application log found"
        fi
        ;;
    "all")
        echo "=== ALL LOGS ==="
        tail -n 50 $LOG_DIR/*.log 2>/dev/null || echo "No logs found"
        ;;
    "follow"|"f")
        echo "=== FOLLOWING ALL LOGS (Ctrl+C to exit) ==="
        tail -f $LOG_DIR/*.log
        ;;
    "service")
        echo "=== SYSTEMD SERVICE LOGS ==="
        sudo journalctl -u report-generator -n 100 --no-pager
        ;;
    "service-follow"|"sf")
        echo "=== FOLLOWING SERVICE LOGS (Ctrl+C to exit) ==="
        sudo journalctl -u report-generator -f
        ;;
    *)
        echo "Usage: $0 [log_type]"
        echo ""
        echo "Log types:"
        echo "  error, errors    - View error log"
        echo "  access           - View access log"
        echo "  app, main        - View application log"
        echo "  all              - View all logs"
        echo "  follow, f        - Follow all logs (live)"
        echo "  service          - View systemd service logs"
        echo "  service-follow, sf - Follow systemd service logs (live)"
        echo ""
        echo "Examples:"
        echo "  $0 error         # View error log"
        echo "  $0 follow        # Follow all logs"
        echo "  $0 service-follow # Follow service logs"
        ;;
esac

