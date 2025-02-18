Name:           nezha-server
Version:        codetiger_version
Release:        1%{?dist}
Summary:        哪吒监控agent编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/nezhahq/nezha/releases/download/v1.7.4/dashboard-linux-codetiger_arch.zip
Source1:        nezha-server.service
Source2:        nezha-server.sh
Source3:        server.yaml

%description

# 编译前准备
%prep
rm -rf %{_builddir}/*
cp %{SOURCE0} %{_builddir}
unzip -d %{name}-%{version} %{SOURCE0}


# 安装
%install
%{__mkdir} -p %{buildroot}/etc/nezha/data
cp %{name}-%{version}/dashboard-linux-codetiger_arch  %{buildroot}/usr/bin/nezha-server
chmod +x  %{buildroot}/usr/bin/nezha-server
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_usr}/lib/systemd/system/nezha-server.service
%{__install} -p -D -m 0755 %{SOURCE2} %{buildroot}/etc/nezha/nezha-server.sh
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}/etc/nezha/data/config.yaml

# 安装后操作
%post
if [ $1 == 1 ]; then
    groupadd -g 3000 -o nezha || true
    useradd -u 3000 -o nezha -g nezha -s /sbin/nologin || true
    chown -R nezha:nezha /etc/nezha
fi

# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/nezha-server.service ]; then
    %systemd_preun nezha-server.service
    fi
fi

# 卸载后步骤
%postun
if [ $1 == 0 ]; then
    userdel nezha || true
    groupdel nezha || true
fi

# 文件列表
%files
/etc/nezha/nezha-server
/etc/nezha/nezha-server.sh
%{_usr}/lib/systemd/system/nezha-server.service
%config(noreplace) /etc/nezha/data/config.yaml
%doc

%changelog
