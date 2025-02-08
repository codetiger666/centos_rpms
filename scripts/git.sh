PCRE_VERSION=5

program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/git.spec
  sudo sed -i "s/codetiger_perl_version/${PCRE_VERSION}/g" specs/git.spec
  wget https://www.kernel.org/pub/software/scm/git/git-${project_version}.tar.gz
  sudo /bin/cp specs/git.spec rpm/rpmbuild/SPECS/git.spec
  docker exec -i $centos dnf remove -y openssh*
  docker exec -i $centos dnf install -y openssh-server
  mkdir rpm/rpmbuild/SOURCES -p
  sudo /bin/cp git-${project_version}.tar.gz rpm/rpmbuild/SOURCES
}