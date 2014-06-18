Name:		resin
Version:	3.1.12
Release:	3%{?dist}

%define ins_prefix /usr/local/resin
%define __jar_repack %{nil}
%define debug_package %{nil}

Summary:	Resin Web Server
Group:		system
License:	GPLv2
URL:		http://www.caucho.com/download/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-makefile.patch
Patch1:		%{name}-%{version}-autoconf.patch

Requires:	java7
Requires:	java7-devel
Requires:	openssl

BuildRequires:	make
BuildRequires:  java7
BuildRequires:  java7-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
# Note this needs both the 32 and 64 bit glibc-devel, but I cannot
# find a way to specify an arch in the BuildRequires
BuildRequires:  glibc-devel
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
The Resin Web server binaries and runtime files.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1 

%build
autoconf
touch NEWS AUTHORS ChangeLog
automake --add-missing
./configure --prefix=%{ins_prefix} --exec-prefix=%{ins_prefix} --with-jni-include="-I/usr/lib/jvm/java-1.7.0-openjdk.x86_64/include -I/usr/lib/jvm/java-1.7.0-openjdk.x86_64/include/linux"
# -I/usr/include/gnu -I /usr/include"
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{ins_prefix}
%{ins_prefix}/bin
%{ins_prefix}/lib
%{ins_prefix}/php
%{ins_prefix}/plugins
%{ins_prefix}/ext-webapp-lib
%{ins_prefix}/libexec
%config %{ins_prefix}/conf
%config %{ins_prefix}/webapps

%changelog
