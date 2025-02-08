program_init(){
  sudo sed -i "s/codetiger_version/${project_version}/g" specs/vaultwarden.spec
  ARCH=amd64
  if [ "${project_arch}" = "x86_64" ]; then
    ARCH=amd64
  fi
  if [ "${project_arch}" = "aarch64" ]; then
    ARCH=arm64
  fi
  wget https://github.com/czyt/vaultwarden-binary/releases/download/${project_version}-extracted/vaultwarden-linux-${ARCH}-extracted.zip
  sudo /bin/cp specs/vaultwarden.spec rpm/rpmbuild/SPECS/vaultwarden.spec
  mkdir rpm/rpmbuild/SOURCES -p
  unzip vaultwarden-linux-${ARCH}-extracted.zip -d extracted
  sudo /bin/cp extracted/vaultwarden rpm/rpmbuild/SOURCES
  sudo /bin/cp -ra extracted/web-vault rpm/rpmbuild/SOURCES
  sudo /bin/cp services/vaultwarden.service rpm/rpmbuild/SOURCES
  sudo /bin/cp vaultwarden/vaultwarden.sh rpm/rpmbuild/SOURCES
  sudo /bin/cp vaultwarden/.env rpm/rpmbuild/SOURCES
}