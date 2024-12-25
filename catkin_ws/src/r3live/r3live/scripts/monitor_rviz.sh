#!/bin/bash
# 监控 RViz 进程的脚本
# 该脚本会不断检查 RViz 是否在运行，并在其崩溃或退出时重启它

RVIZ_COMMAND="rviz -d /home/cijh/catkin_ws/src/r3live/config/rviz/r3live_rviz_config.rviz"

LOG_FILE="/tmp/rviz_monitor.log"

echo "Starting RViz monitoring..." | tee -a $LOG_FILE

while true; do
    # 检查 RViz 是否正在运行
    if ! pgrep -x "rviz" > /dev/null; then
        echo "$(date): RViz not running. Restarting RViz..." | tee -a $LOG_FILE

        # 启动 RViz 并将输出重定向到日志文件
        $RVIZ_COMMAND > /tmp/rviz_output.log 2>&1 &

        # 记录新启动的进程 ID
        RVIZ_PID=$!
        echo "$(date): RViz started with PID: $RVIZ_PID" | tee -a $LOG_FILE
    fi
    # 等待 5 秒后再次检查
    sleep 5
done


