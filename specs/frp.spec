Name:           frp
Version:        codetiger_version
Release:        1%{?dist}
Summary:        frp编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/fatedier/frp/releases/download/v%{version}/%{name}_%{version}_linux_codetiger_arch.tar.gz
Source1:        frpc.service
Source2:        frps.service
    

%description

# 编译前准备
%prep
rm -rf %{_builddir}/*
cp %{SOURCE0} %{_builddir}
tar xf %{SOURCE0}
mv frp_%{version}_linux_codetiger_arch %{name}-%{version}

# 安装
%install
%{__mkdir} -p %{buildroot}/usr/local/frp
cp %{name}-%{version}/frpc* %{buildroot}/usr/local/frp
cp %{name}-%{version}/frps* %{buildroot}/usr/local/frp
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_usr}/lib/systemd/system/frpc.service
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_usr}/lib/systemd/system/frps.service

# 安装后操作
%post
if [ $1 == 1 ]; then
    useradd frp -s /sbin/nologin || true
    chown -R alist:alist /usr/local/frp
fi

# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/frp.service ]; then
    %systemd_preun frp.service
    fi
fi

# 卸载后步骤
%postun
if [ $1 == 0 ]; then
    userdel frp || true
    groupdel frp || true
fi

# 文件列表
%files
%{_usr}/local/frp/frpc
%{_usr}/local/frp/frps
%{_usr}/lib/systemd/system/frpc.service
%{_usr}/lib/systemd/system/frps.service
%config(noreplace) %{_usr}/local/frp/frpc.toml
%config(noreplace) %{_usr}/local/frp/frps.toml
%doc

%changelog