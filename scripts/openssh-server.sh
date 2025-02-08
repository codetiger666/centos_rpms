OPENSSL_VERSION=3.4.0

program_init(){
  # docker exec -i $centos dnf install -y zlib-devel libselinux-devel openssl-devel-$OPENSSL_VERSION
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/openssh-server.spec
  sudo sed -i "s/codetiger_openssl_version/$OPENSSL_VERSION/g" specs/openssh-server.spec
  sudo /bin/cp specs/openssh-server.spec rpm/rpmbuild/SPECS/openssh-server.spec
  sudo /bin/cp services/sshd.service rpm/rpmbuild/SOURCES
  sudo /bin/cp openssh/sshd_config rpm/rpmbuild/SOURCES
  wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-${project_version}.tar.gz
  wget https://github.com/openssl/openssl/releases/download/openssl-${OPENSSL_VERSION}/openssl-${OPENSSL_VERSION}.tar.gz
  tar -zxvf openssh-${project_version}.tar.gz
  mv openssh-${project_version} openssh-server-${project_version}
  tar -zcvf openssh-server-${project_version}.tar.gz openssh-server-${project_version}
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp openssh-server-${project_version}.tar.gz rpm/rpmbuild/SOURCES/openssh-server-${project_version}.tar.gz
  sudo /bin/cp openssl-${OPENSSL_VERSION}.tar.gz rpm/rpmbuild/SOURCES/openssl-${OPENSSL_VERSION}.tar.gz
}