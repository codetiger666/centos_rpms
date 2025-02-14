Name:           onedrive
Version:        codetiger_version
Release:        1%{?dist}
Summary:        onedrive编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/abraunegg/onedrive/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        onedrive.service
Source2:        config
Source3:        onedrive.sh
Source3:        sync_list

BuildRequires:  sqlite-devel     

# 描述
%description
onedrive编译

# 编译前准备
%prep
%setup -q

# 编译
%build
CFLAGS="-fPIC" ./configure  --bindir=/usr/bin
make -j6

# 安装
%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/local/share
rm -rf %{buildroot}/usr/lib/systemd/system/onedrive@.service
rm -rf %{buildroot}/usr/lib/systemd/user/onedrive.service
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/onedrive.service
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}/usr/local/onedrive/conf/config
%{__install} -p -D -m 0644 %{SOURCE4} %{buildroot}/usr/local/onedrive/conf/sync_list
%{__install} -p -D -m 0755 %{SOURCE3} %{buildroot}/usr/local/onedrive/onedrive.sh

# 安装后操作
%post
if [ $1 == 1 ]; then
    groupadd -g 3000 -o onedrive || true
    useradd -u 3000 -o onedrive -g onedrive -s /sbin/nologin || true
    chown -R onedrive:onedrive /usr/local/onedrive
fi

# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/onedrive.service ]; then
    %systemd_preun onedrive.service
    fi
fi

# 卸载后步骤
%postun
if [ $1 == 0 ]; then
    groupdel onedrive || true
    userdel onedrive || true
fi

# 文件列表
%files
%defattr(-,root,root,0755)
%{_usr}/bin/onedrive
%{_usr}/local/etc/logrotate.d/onedrive
%{_usr}/lib/systemd/system/onedrive.service
%{_usr}/local/onedrive/onedrive.sh
%config(noreplace) %{_usr}/local/onedrive/conf/config
%config(noreplace) %{_usr}/local/onedrive/conf/sync_list

# 文档
%doc

# 更改日志
%changelog
