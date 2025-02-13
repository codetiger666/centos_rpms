program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/openssl.spec
  wget https://github.com/openssl/openssl/releases/download/openssl-${project_version}/openssl-${project_version}.tar.gz
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp openssl-${project_version}.tar.gz rpm/rpmbuild/SOURCES/openssl-${project_version}.tar.gz
}
