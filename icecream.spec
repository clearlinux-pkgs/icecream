#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : icecream
Version  : 1.2
Release  : 2
URL      : https://github.com/icecc/icecream/archive/1.2/icecream-1.2.tar.gz
Source0  : https://github.com/icecc/icecream/archive/1.2/icecream-1.2.tar.gz
Source1  : iceccd.service
Source2  : icecream-scheduler.service
Summary  : icecc is a library for connecting to icecc schedulers
Group    : Development/Tools
License  : GPL-2.0
Requires: icecream-bin = %{version}-%{release}
Requires: icecream-libexec = %{version}-%{release}
Requires: icecream-license = %{version}-%{release}
Requires: icecream-services = %{version}-%{release}
BuildRequires : libcap-ng-dev
BuildRequires : lzo-dev

%description
NOTE: Although icecream will compile on some non-Linux systems,
it depends critically on Linux' /proc/ structures and will fail
at runtime until somebody figures out how to emulate the "ticks"
form of process accounting in there.

%package bin
Summary: bin components for the icecream package.
Group: Binaries
Requires: icecream-libexec = %{version}-%{release}
Requires: icecream-license = %{version}-%{release}
Requires: icecream-services = %{version}-%{release}

%description bin
bin components for the icecream package.


%package dev
Summary: dev components for the icecream package.
Group: Development
Requires: icecream-bin = %{version}-%{release}
Provides: icecream-devel = %{version}-%{release}

%description dev
dev components for the icecream package.


%package libexec
Summary: libexec components for the icecream package.
Group: Default
Requires: icecream-license = %{version}-%{release}

%description libexec
libexec components for the icecream package.


%package license
Summary: license components for the icecream package.
Group: Default

%description license
license components for the icecream package.


%package services
Summary: services components for the icecream package.
Group: Systemd services

%description services
services components for the icecream package.


%prep
%setup -q -n icecream-1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542241689
%autogen --disable-static --with-man=no
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1542241689
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/icecream
cp COPYING %{buildroot}/usr/share/package-licenses/icecream/COPYING
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/iceccd.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/icecream-scheduler.service
## install_append content
set clang clang++ x86_64-generic-linux-c++ x86_64-generic-linux-gcc x86_64-generic-linux-g++
for f; do
ln -sf /usr/bin/icecc %{buildroot}/usr/libexec/icecc/bin/$f
done
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/icecc
/usr/bin/icecc-create-env
/usr/bin/icecc-scheduler
/usr/bin/icecc-test-env
/usr/bin/iceccd
/usr/bin/icerun

%files dev
%defattr(-,root,root,-)
/usr/include/icecc/comm.h
/usr/include/icecc/job.h
/usr/include/icecc/logging.h
/usr/lib64/pkgconfig/icecc.pc

%files libexec
%defattr(-,root,root,-)
/usr/libexec/icecc/bin/c++
/usr/libexec/icecc/bin/cc
/usr/libexec/icecc/bin/clang
/usr/libexec/icecc/bin/clang++
/usr/libexec/icecc/bin/g++
/usr/libexec/icecc/bin/gcc
/usr/libexec/icecc/bin/x86_64-generic-linux-c++
/usr/libexec/icecc/bin/x86_64-generic-linux-g++
/usr/libexec/icecc/bin/x86_64-generic-linux-gcc
/usr/libexec/icecc/compilerwrapper
/usr/libexec/icecc/icecc-create-env

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/icecream/COPYING

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/iceccd.service
/usr/lib/systemd/system/icecream-scheduler.service
