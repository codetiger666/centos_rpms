Name:           alist
Version:        codetiger_version
Release:        1%{?dist}
Summary:        alist网盘

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/AlistGo/alist/releases/download/v%{version}/alist-linux-codetiger_arch.tar.gz
Source1:        alist.service
Source2:        alist.sh
Source3:        config
Source4:        config.json

%description

# 编译前准备
%prep
rm -rf %{_builddir}/*
cp %{SOURCE0} %{_builddir}
tar -xf %{SOURCE0}


# 安装
%install
%{__mkdir} -p %{buildroot}/usr/local/alist/data
cp alist %{buildroot}/usr/local/alist/alist
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_usr}/lib/systemd/system/alist.service
%{__install} -p -D -m 0755 %{SOURCE2} %{buildroot}/usr/local/alist/alist.sh
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}/usr/local/alist/config
%{__install} -p -D -m 0644 %{SOURCE4} %{buildroot}/usr/local/alist/data/config.json


# 安装后操作
%post
if [ $1 == 1 ]; then
    useradd -u 3000 -o alist || true
    chown -R alist:3000 /usr/local/alist
fi

# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/alist.service ]; then
    %systemd_preun alist.service
    fi
fi

# 卸载后步骤
%postun
if [ $1 == 0 ]; then
    userdel alist 2> /dev/null
    groupdel alist 2> /dev/null
fi

# 文件列表
%files
%{_usr}/local/alist/alist
%{_usr}/local/alist/alist.sh
%{_usr}/local/alist/config
%{_usr}/local/alist/data/config.json
%{_usr}/lib/systemd/system/alist.service
%doc

%changelog
