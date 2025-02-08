program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/alist.spec
  sudo /bin/cp specs/alist.spec rpm/rpmbuild/SPECS/alist.spec
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp alist/alist.sh rpm/rpmbuild/SOURCES
  sudo /bin/cp services/alist.service rpm/rpmbuild/SOURCES
}