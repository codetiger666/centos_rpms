Name:           hysteria
Version:        codetiger_version
Release:        1%{?dist}
Summary:        hysteria编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/apernet/hysteria/releases/download/app%2Fvcodetiger_version/hysteria
Source1:        config.yaml
Source2:        hysteria.sh
Source3:        server.key
Source4:        server.crt
Source5:        hysteria.service

%description


# 安装
%install
%{__mkdir} -p %{buildroot}/usr/local/hysteria
%{__install} -p -D -m 0755 %{SOURCE0} %{buildroot}%{_usr}/local/hysteria/hysteria
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_usr}/local/hysteria/config.yaml
%{__install} -p -D -m 0755 %{SOURCE2} %{buildroot}%{_usr}/local/hysteria/hysteria.sh
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}%{_usr}/local/hysteria/server.key
%{__install} -p -D -m 0644 %{SOURCE4} %{buildroot}%{_usr}/local/hysteria/server.crt
%{__install} -p -D -m 0644 %{SOURCE5} %{buildroot}%{_usr}/lib/systemd/system/hysteria.service

# 安装后操作
%post
if [ $1 == 1 ]; then
    useradd hysteria -s /sbin/nologin || true
    chown -R hysteria:hysteria /usr/local/hysteria
fi

# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/hysteria.service ]; then
    %systemd_preun hysteria.service
    fi
fi

# 卸载后步骤
%postun
if [ $1 == 0 ]; then
    userdel hysteria || true
    groupdel hysteria || true
fi

# 文件列表
%files
%{_usr}/local/hysteria/hysteria
%{_usr}/local/hysteria/hysteria.sh
%{_usr}/local/hysteria/server.key
%{_usr}/local/hysteria/server.crt
%{_usr}/lib/systemd/system/hysteria.service
%config(noreplace) %{_usr}/local/hysteria/config.yaml
%doc

%changelog