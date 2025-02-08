Name:           alist
Version:        codetiger_version
Release:        1%{?dist}
Summary:        alist网盘

License:        GPL
URL:            https://gybyt.cn
Source0:        alist.service
Source1:        alist.sh

%description

# 编译前准备
%prep
rm -rf %{_builddir}/*
cd %{_builddir}
git clone https://github.com/alist-org/alist.git -b vcodetiger_version
sed -i 's/OnlyLocal:         true/OnlyLocal:         false/g' ./alist/drivers/quark_uc/meta.go
git clone --recurse-submodules https://github.com/alist-org/alist-web.git -b codetiger_version
cd alist-web
wget https://crowdin.com/backend/download/project/alist/zh-CN.zip
unzip zh-CN.zip
node ./scripts/i18n.mjs
pnpm install && pnpm build
cp ./dist ../alist/public -ra
cd %{_builddir}/alist
appName="alist"
builtAt="$(date +'%F %T %z')"
goVersion=$(go version | sed 's/go version //')
gitAuthor=$(git show -s --format='format:%aN <%ae>' HEAD)
gitCommit=$(git log --pretty=format:"%h" -1)
version=$(git describe --long --tags --dirty --always)
webVersion=$(wget -qO- -t1 -T2 "https://api.github.com/repos/alist-org/alist-web/releases/latest" | grep "tag_name" | head -n 1 | awk -F ":" '{print $2}' | sed 's/\"//g;s/,//g;s/ //g')
ldflags="\
-w -s \
-X 'github.com/alist-org/alist/v3/internal/conf.BuiltAt=$builtAt' \
-X 'github.com/alist-org/alist/v3/internal/conf.GoVersion=$goVersion' \
-X 'github.com/alist-org/alist/v3/internal/conf.GitAuthor=$gitAuthor' \
-X 'github.com/alist-org/alist/v3/internal/conf.GitCommit=$gitCommit' \
-X 'github.com/alist-org/alist/v3/internal/conf.Version=$version' \
-X 'github.com/alist-org/alist/v3/internal/conf.WebVersion=$webVersion' \
"
go build -ldflags="$ldflags" .
cd %{_builddir}/
mkdir -p %{name}-%{version}
cp ./alist/alist %{name}-%{version}/alist

# 安装前准备
%pre
if [ $1 == 1 ]; then
    id alist &> /dev/null
    if [ $? -ne 0 ]
    then
    useradd alist -s /sbin/nologin 2> /dev/null
    fi
fi

# 安装
%install
%{__mkdir} -p %{buildroot}/usr/local/alist
cp %{name}-%{version}/alist %{buildroot}/usr/local/alist/alist
%{__install} -p -D -m 0644 %{SOURCE0} %{buildroot}%{_usr}/lib/systemd/system/alist.service
%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}/usr/local/alist/alist.sh

# 安装后操作
%post
if [ $1 == 1 ]; then
    chown -R alist:alist /usr/local/alist
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
%{_usr}/lib/systemd/system/alist.service
%doc

%changelog
