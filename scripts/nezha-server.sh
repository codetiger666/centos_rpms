program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/nezha-server.spec
  ARCH=amd64
  if [ "${project_arch}" = "x86_64" ]; then
    ARCH=amd64
  fi
  if [ "${project_arch}" = "aarch64" ]; then
    ARCH=arm64
  fi
  sudo sed -i "s/codetiger_arch/${ARCH}/g" specs/nezha-server.spec
  wget https://github.com/nezhahq/nezha/releases/download/v${project_version}/dashboard-linux-${ARCH}.zip
  sudo /bin/cp specs/nezha-agent.spec rpm/rpmbuild/SPECS/nezha-server.spec
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp dashboard-linux-${ARCH}.zip rpm/rpmbuild/SOURCES
  sudo /bin/cp nezha/nezha-server.sh rpm/rpmbuild/SOURCES
  sudo /bin/cp nezha/server.yaml rpm/rpmbuild/SOURCES
  sudo /bin/cp services/nezha-server.service rpm/rpmbuild/SOURCES
}