# 自定义clients名称
%define devel openssl-devel
%define libs openssl-libs
Name:           openssl
Version:        codetiger_version
Release:        1%{?dist}
Summary:        openssl编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/openssl/openssl/releases/download/openssl-codetiger_version/openssl-codetiger_version.tar.gz

# 别名 用来代替openssl-devel openssl-devel
Provides: %{libs} = %{version}
Provides: %{devel} = %{version}

BuildRequires:  zlib-devel gcc
Requires: zlib

# 描述
%description
openssl编译

%prep
%setup -q

# 编译
%build
./config shared zlib
make -j6

# 安装
%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/local/share/man

# 文件列表
%files
%defattr(-,root,root,0755)

# 文档
%doc

# 更改日志
%changelog
