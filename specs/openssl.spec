# 自定义clients名称
%define devel openssl-devel
%define libs openssl-libs
Name:           openssl
Epoch:          1
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
./config shared zlib --prefix=/usr  --openssldir=/etc/ssl -Wl,-rpath=/usr/lib64
make -j6

# 安装
%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/local/share/man
rm -rf %{buildroot}/usr/local/share/doc

# 文件列表
%files
%defattr(-,root,root,0755)
%{_usr}/include/openssl/
%{_usr}/lib64/engines-3/afalg.so
%{_usr}/lib64/engines-3/capi.so
%{_usr}/lib64/engines-3/loader_attic.so
%{_usr}/lib64/engines-3/padlock.so
%{_usr}/lib64/libcrypto.a
%{_usr}/lib64/libcrypto.so
%{_usr}/lib64/libcrypto.so.3
%{_usr}/lib64/libssl.a
%{_usr}/lib64/libssl.so
%{_usr}/lib64/libssl.so.3
%{_usr}/lib64/ossl-modules/legacy.so
%{_usr}/lib64/pkgconfig/libcrypto.pc
%{_usr}/lib64/pkgconfig/libssl.pc
%{_usr}/lib64/pkgconfig/openssl.pc
%{_usr}/bin/c_rehash
%{_usr}/bin/openssl
/etc/ssl/ct_log_list.cnf
/etc/ssl/ct_log_list.cnf.dist
/etc/ssl/misc/CA.pl
/etc/ssl/misc/tsget
/etc/ssl/misc/tsget.pl
/etc/ssl/openssl.cnf
/etc/ssl/openssl.cnf.dist

# 文档
%doc

# 更改日志
%changelog
