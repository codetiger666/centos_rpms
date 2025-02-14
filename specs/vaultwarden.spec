Name:           vaultwarden
Version:        codetiger_version
Release:        1%{?dist}
Summary:        vaultwarden编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/czyt/vaultwarden-binary/releases/download/codetiger_version-extracted/vaultwarden
Source1:        vaultwarden.sh
Source2:        .env
Source3:        vaultwarden.service
Source4:        web-vault

%description


# 安装
%install
%{__mkdir} -p %{buildroot}/usr/local/vaultwarden
%{__install} -p -D -m 0755 %{SOURCE0} %{buildroot}%{_usr}/local/vaultwarden/vaultwarden
%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}%{_usr}/local/vaultwarden/vaultwarden.sh
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_usr}/local/vaultwarden/.env
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}%{_usr}/lib/systemd/system/vaultwarden.service
/bin/cp -ra %{SOURCE4} %{buildroot}/usr/local/vaultwarden

# 安装后操作
%post
if [ $1 == 1 ]; then
    groupadd -g 3000 -o vaultwarden || true
    useradd -u 3000 -g vaultwarden -o vaultwarden -s /sbin/nologin || true
    chown -R vaultwarden:vaultwarden /usr/local/vaultwarden
fi

# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/vaultwarden.service ]; then
    %systemd_preun vaultwarden.service
    fi
fi

# 卸载后步骤
%postun
if [ $1 == 0 ]; then
    userdel vaultwarden || true
    groupdel vaultwarden || true
fi

# 文件列表
%files
%{_usr}/local/vaultwarden/vaultwarden
%{_usr}/local/vaultwarden/vaultwarden.sh
%{_usr}/local/vaultwarden/web-vault/
%{_usr}/lib/systemd/system/vaultwarden.service
%config(noreplace) %{_usr}/local/vaultwarden/.env
%doc

%changelog