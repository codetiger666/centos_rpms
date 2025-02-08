program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/hysteria.spec
  ARCH=amd64
  if [ "${project_arch}" = "x86_64" ]; then
    ARCH=amd64
  fi
  if [ "${project_arch}" = "aarch64" ]; then
    ARCH=arm64
  fi
  openssl genpkey -algorithm RSA -out server.key
  openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 3650 -nodes -config hysteria/openssl.cnf
  sudo sed -i "s/codetiger_arch/${ARCH}/g" specs/hysteria.spec
  wget https://github.com/apernet/hysteria/releases/download/app%2Fv${project_version}/hysteria-linux-${ARCH}
  sudo /bin/cp specs/hysteria.spec rpm/rpmbuild/SPECS/hysteria.spec
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp hysteria-linux-${ARCH} rpm/rpmbuild/SOURCES/hysteria
  sudo /bin/cp hysteria/hysteria.sh rpm/rpmbuild/SOURCES
  sudo /bin/cp hysteria/config.yaml rpm/rpmbuild/SOURCES
  sudo /bin/cp services/hysteria.service rpm/rpmbuild/SOURCES
  sudo /bin/cp server.key rpm/rpmbuild/SOURCES
  sudo /bin/cp server.crt rpm/rpmbuild/SOURCES
}