%define prefix /usr/local/nginx
Name:          openresty
Version:        codetiger_version
Release:        1%{?dist}
Summary:        openresty编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://openresty.org/download/%{name}-%{version}.tar.gz
Source1:        nginx.conf
Source2:        nginx.service
Source3:        default.conf

BuildRequires:  pcre pcre-devel openssl-devel gcc gd libxslt-devel libxml2-devel geoip-devel libatomic_ops-devel libstdc++ perl-ExtUtils-Embed gd-devel
Requires:       pcre openssl cmake gcc libxml2 libxslt gd geoip libstdc++ perl

# 描述
%description
openresty自编译

# 编译前准备
%prep
%setup -q

# 编译
%build
CFLAGS="-fPIC" ./configure --prefix=/usr/local/nginx --sbin-path=/usr/sbin/nginx --conf-path=/usr/local/nginx/nginx.conf --pid-path=/var/run/nginx.pid --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --lock-path=/var/lock/nginx.lock --with-luajit --with-http_gunzip_module --with-pcre --with-pcre-jit --with-http_perl_module --with-ld-opt="-Wl,-E" --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-http_addition_module --with-http_xslt_module --with-http_image_filter_module --with-http_geoip_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gzip_static_module --with-http_auth_request_module --with-http_random_index_module --with-select_module --with-poll_module --with-file-aio --with-http_degradation_module --with-libatomic --http-client-body-temp-path=/var/tmp/nginx/client_body --http-proxy-temp-path=/var/tmp/nginx/proxy --http-fastcgi-temp-path=/var/tmp/nginx/fastcgi --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi --http-scgi-temp-path=/var/tmp/nginx/scgi --add-module=/opt/nginx-upstream-dynamic-servers --add-module=/opt/ngx_upstream_jdomain -j6
make -j6

# 安装
%install
make install DESTDIR=%{buildroot}
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{prefix}/nginx.conf
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}%{prefix}/conf.d/default.conf
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_usr}/lib/systemd/system/nginx.service

# 安装前准备
%pre
if [ $1 == 1 ]; then
   useradd nginx -s /sbin/nologin || true
fi

# 安装后操作
%post
if [ $1 == 1 ]; then
    mkdir -p /var/tmp/nginx/proxy
    mkdir -p /var/tmp/nginx/client_body
    mkdir -p /var/tmp/nginx/proxy_cache
    mkdir -p /var/tmp/nginx/uwsgi
    mkdir -p /var/tmp/nginx/proxy_cache/enginx
    mkdir -p /var/tmp/nginx/fastcgi
    mkdir -p /var/tmp/nginx/scgi
    mkdir -p /var/tmp/nginx/proxy_temp
    chown -R nginx:nginx /var/tmp/nginx
    mkdir -p /var/log/nginx
    chown -R nginx:nginx /var/log/nginx
    mkdir -p /usr/local/nginx/conf.d
fi

# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/nginx.service ]; then
    %systemd_preun nginx.service
    fi
fi

# 卸载后步骤
%postun
if [ $1 == 0 ]; then
    rm -rf /var/tmp/nginx/proxy
    rm -rf /var/tmp/nginx/client_body
    rm -rf /usr/lib/systemd/system/nginx.service
    rm -rf /var/tmp/nginx
    rm -rf /var/log/nginx
    userdel nginx || true
    groupdel nginx || true
fi

# 文件列表
%files
%defattr(-,root,root,0755)
%{_usr}/lib64/perl5/perllocal.pod
%{_usr}/local/lib64/perl5/codetiger_perl_version/auto/nginx/.packlist
%{_usr}/local/lib64/perl5/codetiger_perl_version/auto/nginx/nginx.so
%{_usr}/local/lib64/perl5/codetiger_perl_version/nginx.pm
%{_usr}/local/share/man/man3/nginx.3pm
%{_sbindir}/nginx
%{_usr}/local/nginx/
%{_usr}/lib/systemd/system/nginx.service
# 文档
%doc

# 更改日志
%changelog