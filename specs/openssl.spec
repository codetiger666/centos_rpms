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

BuildRequires:  zlib-devel gcc
Requires: zlib
Requires: openssl-libs = %{epoch}:%{version}

# 描述
%description
openssl编译
# 子包openssl-libs定义

%package -n openssl-libs
Summary:      openssl-libs

%description
openssl-libs编译

# 子包openssl-devel定义
%package -n openssl-devel
Summary:      openssl-devel
Requires: openssl = %{epoch}:%{version}

%description
openssl-devel编译

%prep
%setup -q

# 编译
%build
./config shared zlib --prefix=/usr  --openssldir=/etc/ssl --libdir=/usr/lib64
make -j6

# 安装
%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/share/man
rm -rf %{buildroot}/usr/share/doc
rm -rf %{buildroot}/etc/ssl

# 文件列表
%files
%defattr(-,root,root,0755)
%{_usr}/bin/c_rehash
%{_usr}/bin/openssl

# 子包openssl-libs文件列表
%files -n openssl-libs
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

# 子包openssl-devel文件列表
%files -n openssl-devel
%{_usr}/include/openssl/
%{_usr}/lib64/pkgconfig/libcrypto.pc
%{_usr}/lib64/pkgconfig/libssl.pc
%{_usr}/lib64/pkgconfig/openssl.pc

# 文档
%doc

# 更改日志
%changelog
