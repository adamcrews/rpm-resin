Name:		resin
Version:	4.0.40
Release:	1%{?dist}

%define ins_prefix /usr/local/resin
%define __jar_repack %{nil}

Summary:	Resin Web Server
Group:		system
License:	GPLv2
URL:		http://www.caucho.com/download/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz

Requires:	java7
Requires:	openssl

BuildRequires:	make
BuildRequires:  java7
BuildRequires:  java7-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
The Resin Web server binaries and runtime files.

%package docs
Summary:	Resin Web Server Documentation

%description docs
The Resin Web server documentation.

%prep
%setup -q

%build
./configure --prefix=%{ins_prefix} --exec-prefix=%{ins_prefix}
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%post

/sbin/chkconfig --add resin

%preun
if [ "$1" = 0 ]; then
/sbin/service resin stop > /dev/null 2>&1
/sbin/chkconfig --del resin
fi
exit 0

%files
%defattr(-,root,root,-)
/etc/init.d/resin
%dir %{ins_prefix}
%{ins_prefix}/bin
%{ins_prefix}/endorsed
%{ins_prefix}/lib
%{ins_prefix}/libexec64
%{ins_prefix}/project-jars
%config %{ins_prefix}/conf
%config %{ins_prefix}/webapps

%files docs
%docdir %{ins_prefix}/doc
%{ins_prefix}/doc

%changelog
