program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/gitea.spec
  ARCH=amd64
  if [ "${project_arch}" = "x86_64" ]; then
    ARCH=amd64
  fi
  if [ "${project_arch}" = "aarch64" ]; then
    ARCH=arm64
  fi
  sudo sed -i "s/codetiger_arch/${ARCH}/g" specs/gitea.spec
  wget https://github.com/go-gitea/gitea/releases/download/v${project_version}/gitea-${project_version}-linux-${ARCH}
  sudo /bin/cp specs/gitea.spec rpm/rpmbuild/SPECS/gitea.spec
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp gitea-${project_version}-linux-${ARCH} rpm/rpmbuild/SOURCES/gitea
  sudo /bin/cp services/gitea.service rpm/rpmbuild/SOURCES
  sudo /bin/cp gitea/gitea.sh rpm/rpmbuild/SOURCES
  sudo /bin/cp gitea/config rpm/rpmbuild/SOURCES
}