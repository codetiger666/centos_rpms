program_init(){
  ARCH=amd64
  if [ "${project_arch}" = "x86_64" ]; then
    ARCH=amd64
  fi
  if [ "${project_arch}" = "aarch64" ]; then
    ARCH=arm64
  fi
  sudo /bin/cp frp/frpc.service rpm/rpmbuild/SOURCES
  sudo /bin/cp frp/frps.service rpm/rpmbuild/SOURCES
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/frp.spec
  sudo sed -i "s/codetiger_arch/${ARCH}/g" specs/frp.spec
  sudo /bin/cp specs/frp.spec rpm/rpmbuild/SPECS/
  wget https://github.com/fatedier/frp/releases/download/v${project_version}/frp_${project_version}_linux_${ARCH}.tar.gz
  sudo /bin/cp frp_${project_version}_linux_${ARCH}.tar.gz rpm/rpmbuild/SOURCES/
}