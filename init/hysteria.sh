#!/bin/sh

handle_version() {
  echo ${1//app\/v/}
}

handle_version $1