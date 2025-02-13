program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/alist.spec
  ARCH=amd64
  if [ "${project_arch}" = "x86_64" ]; then
    ARCH=amd64
  fi
  if [ "${project_arch}" = "aarch64" ]; then
    ARCH=arm64
  fi
  wget https://github.com/AlistGo/alist/releases/download/v${project_version}/alist-linux-${ARCH}.tar.gz
  sudo /bin/cp specs/alist.spec rpm/rpmbuild/SPECS/alist.spec
  sudo sed -i "s/codetiger_arch/${ARCH}/g" specs/alist.spec
  tar -xf alist-linux-${ARCH}.tar.gz -C alist-${project_version}
  tar -zcvf alist-${project_version}.tar.gz alist-${project_version}
  sudo /bin/cp alist-${project_version}.tar.gz rpm/rpmbuild/SOURCES
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp alist/alist.sh rpm/rpmbuild/SOURCES
  sudo /bin/cp alist/config rpm/rpmbuild/SOURCES
  sudo /bin/cp alist/config.json rpm/rpmbuild/SOURCES
  sudo /bin/cp services/alist.service rpm/rpmbuild/SOURCES
}