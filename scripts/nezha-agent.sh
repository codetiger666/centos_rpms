program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/nezha-agent.spec
  ARCH=amd64
  if [ "${project_arch}" = "x86_64" ]; then
    ARCH=amd64
  fi
  if [ "${project_arch}" = "aarch64" ]; then
    ARCH=arm64
  fi
  sudo sed -i "s/codetiger_arch/${ARCH}/g" specs/nezha-agent.spec
  wget https://github.com/nezhahq/agent/releases/download/v${project_version}/nezha-agent_linux_${ARCH}.zip
  sudo /bin/cp specs/nezha-agent.spec rpm/rpmbuild/SPECS/nezha-agent.spec
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp nezha-agent_linux_${ARCH}.zip rpm/rpmbuild/SOURCES
  sudo /bin/cp nezha/nezha-agent.sh rpm/rpmbuild/SOURCES
  sudo /bin/cp nezha/agent.conf rpm/rpmbuild/SOURCES
  sudo /bin/cp services/nezha-agent.service rpm/rpmbuild/SOURCES
}