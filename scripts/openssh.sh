OPENSSL_VERSION=3.4.1

program_init(){
  # docker exec -i $centos dnf install -y zlib-devel libselinux-devel openssl-devel-$OPENSSL_VERSION
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/openssh.spec
  sudo sed -i "s/codetiger_openssl_version/$OPENSSL_VERSION/g" specs/openssh.spec
  sudo /bin/cp specs/openssh.spec rpm/rpmbuild/SPECS/openssh.spec
  sudo /bin/cp services/sshd.service rpm/rpmbuild/SOURCES
  sudo /bin/cp openssh/sshd_config rpm/rpmbuild/SOURCES
  wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-${project_version}.tar.gz
  wget https://github.com/openssl/openssl/releases/download/openssl-${OPENSSL_VERSION}/openssl-${OPENSSL_VERSION}.tar.gz
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp openssh-${project_version}.tar.gz rpm/rpmbuild/SOURCES/openssh-${project_version}.tar.gz
  sudo /bin/cp openssl-${OPENSSL_VERSION}.tar.gz rpm/rpmbuild/SOURCES/openssl-${OPENSSL_VERSION}.tar.gz
}
