#!/bin/bash
PROGRAM_PATH=$(dirname "$(realpath "$0")")
APP_NAME=gitea
CONF=$PROGRAM_PATH/config

source $PROGRAM_PATH/config

case "$1" in
start)
    ${APP_NAME} web --work-path $WORK_PATH --config $WORK_PATH/conf/app.ini -p $WORK_PORT > ${PROGRAM_PATH}/${APP_NAME}.log 2>&1 &
    echo $! > $PROGRAM_PATH/$APP_NAME.pid
    ;;
stop)
    if [ -e ${PROGRAM_PATH}/${APP_NAME}.pid ];then
        kill $(cat ${PROGRAM_PATH}/${APP_NAME}.pid)
        rm $PROGRAM_PATH/$APP_NAME.pid
    fi
    ;;
status)
    if [ -e ${PROGRAM_PATH}/${APP_NAME}.pid ];then
        echo "${APP_NAME} is runing..."
    else
        echo "${APP_NAME} is not runing..."
    fi
    ;;
restart)
    $0 stop
    $0 start
    ;;
*)
  echo "Usage: $0 {start|stop|status|restart}"
esac
# 正常退出程序
exit 0