#!/bin/sh

handle_version() {
  echo $1 | sed 's/V_\([0-9]*\)_[0-9]*_P\([0-9]*\)/\1.\2p\2/'
}

handle_version $1