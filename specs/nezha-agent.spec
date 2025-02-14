Name:           nezha-agent
Version:        codetiger_version
Release:        1%{?dist}
Summary:        哪吒监控agent编译

License:        GPL
URL:            https://gybyt.cn
Source0:        https://github.com/nezhahq/agent/releases/download/v%{version}/nezha-agent_linux_codetiger_arch.zip
Source1:        nezha-agent.service
Source2:        nezha-agent.sh
Source3:        agent.conf

%description

# 编译前准备
%prep
rm -rf %{_builddir}/*
cp %{SOURCE0} %{_builddir}
unzip -d %{name}-%{version} %{SOURCE0}

# 安装后操作
%post
if [ $1 == 1 ]; then
    useradd nezha-agent -s /sbin/nologin || true
    chown -R nezha-agent:nezha-agent /usr/local/nezha
fi

# 安装
%install
%{__mkdir} -p %{buildroot}/usr/local/nezha
cp %{name}-%{version}/nezha-agent %{buildroot}/usr/local/nezha/nezha-agent
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_usr}/lib/systemd/system/nezha-agent.service
%{__install} -p -D -m 0755 %{SOURCE2} %{buildroot}/usr/local/nezha/nezha-agent.sh
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}/usr/local/nezha/agent.conf


# 卸载前准备
%preun
if [ $1 == 0 ]; then
    if [ -f /usr/lib/systemd/system/nezha-agent.service ]; then
    %systemd_preun nezha-agent.service
    fi
fi

# 卸载后步骤
%postun
if [ $1 == 0 ]; then
    userdel nezha-agent || true
    groupdel nezha-agent || true
fi

# 文件列表
%files
%{_usr}/local/nezha/nezha-agent
%{_usr}/local/nezha/nezha-agent.sh
%{_usr}/lib/systemd/system/nezha-agent.service
%config(noreplace) %{_usr}/local/nezha/agent.conf
%doc

%changelog
