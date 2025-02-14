program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/onedrive.spec
  sudo /bin/cp specs/onedrive.spec rpm/rpmbuild/SPECS/onedrive.spec
  wget https://github.com/abraunegg/onedrive/archive/refs/tags/v${project_version}.tar.gz
  mkdir rpm/rpmbuild/SOURCES -p
  tar -xf v${project_version}.tar.gz
  tar -zcvf onedrive-${project_version}.tar.gz onedrive-${project_version}
  sudo /bin/cp onedrive-${project_version}.tar.gz rpm/rpmbuild/SOURCES/onedrive-${project_version}.tar.gz
  sudo /bin/cp onedrive/config rpm/rpmbuild/SOURCES
  sudo /bin/cp onedrive/onedrive.sh rpm/rpmbuild/SOURCES
  sudo /bin/cp services/onedrive.service rpm/rpmbuild/SOURCES
}