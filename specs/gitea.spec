Name:           gitea
Version:        codetiger_version
Release:        1%{?dist}
Summary:        frp编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/go-gitea/gitea/releases/download/v%{version}/gitea
Source1:        gitea.sh
Source2:        config
Source3:        gitea.service
    
Requires:       git openssh-server

%description


# 安装
%install
%{__mkdir} -p %{buildroot}/usr/local/gitea
%{__install} -p -D -m 0755 %{SOURCE0} %{buildroot}%{_usr}/local/gitea/gitea
%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}%{_usr}/local/gitea/gitea.sh
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_usr}/local/gitea/config
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}%{_usr}/lib/systemd/system/gitea.service

# 安装后操作
%post
if [ $1 == 1 ]; then
    groupadd -g 3000 -o gitea || true
    useradd -u 3000 -o gitea -s /sbin/nologin || true
    chown -R gitea:gitea /usr/local/gitea
fi

# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/gitea.service ]; then
    %systemd_preun gitea.service
    fi
fi

# 卸载后步骤
%postun
if [ $1 == 0 ]; then
    userdel gitea || true
    groupdel gitea || true
fi

# 文件列表
%files
%{_usr}/local/gitea/gitea
%{_usr}/local/gitea/gitea.sh
%{_usr}/lib/systemd/system/gitea.service
%config(noreplace) %{_usr}/local/gitea/config
%doc

%changelog