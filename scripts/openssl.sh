program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/openssl.spec
  ARCH=amd64
  if [ "${project_arch}" = "x86_64" ]; then
    sudo sed -i "s/codetiger_lib/lib64/g" specs/openssl.spec
  fi
  if [ "${project_arch}" = "aarch64" ]; then
    sudo sed -i "s/codetiger_lib/lib/g" specs/openssl.spec
  fi
  wget https://github.com/openssl/openssl/releases/download/openssl-${project_version}/openssl-${project_version}.tar.gz
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp openssl-${project_version}.tar.gz rpm/rpmbuild/SOURCES/openssl-${project_version}.tar.gz
}
