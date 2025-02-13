#!/bin/sh

handle_version() {
  echo $(curl https://api.github.com/repos/openssh/openssh-portable/tags | jq -r '.[0].name' | sed 's/V_\([0-9]*\)_\([0-9]*\)_P\([0-9]*\)/\1.\2p\3/')
}

handle_version
