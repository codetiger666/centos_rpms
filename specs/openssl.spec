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
rm -rf %{buildroot}/usr/local/share/doc

# 文件列表
%files
%defattr(-,root,root,0755)
%{_usr}/local/include/openssl/
%{_usr}/local/codetiger_lib/cmake/OpenSSL/OpenSSLConfig.cmake
%{_usr}/local/codetiger_lib/cmake/OpenSSL/OpenSSLConfigVersion.cmake
%{_usr}/local/codetiger_lib/engines-3/afalg.so
%{_usr}/local/codetiger_lib/engines-3/capi.so
%{_usr}/local/codetiger_lib/engines-3/loader_attic.so
%{_usr}/local/codetiger_lib/engines-3/padlock.so
%{_usr}/local/codetiger_lib/libcrypto.a
%{_usr}/local/codetiger_lib/libcrypto.so
%{_usr}/local/codetiger_lib/libcrypto.so.3
%{_usr}/local/codetiger_lib/libssl.a
%{_usr}/local/codetiger_lib/libssl.so
%{_usr}/local/codetiger_lib/libssl.so.3
%{_usr}/local/codetiger_lib/ossl-modules/legacy.so
%{_usr}/local/codetiger_lib/pkgconfig/libcrypto.pc
%{_usr}/local/codetiger_lib/pkgconfig/libssl.pc
%{_usr}/local/codetiger_lib/pkgconfig/openssl.pc
%{_usr}/local/bin/c_rehash
%{_usr}/local/bin/openssl
%{_usr}/local/ssl/ct_log_list.cnf
%{_usr}/local/ssl/ct_log_list.cnf.dist
%{_usr}/local/ssl/misc/CA.pl
%{_usr}/local/ssl/misc/tsget
%{_usr}/local/ssl/misc/tsget.pl
%{_usr}/local/ssl/openssl.cnf
%{_usr}/local/ssl/openssl.cnf.dist

# 文档
%doc

# 更改日志
%changelog
