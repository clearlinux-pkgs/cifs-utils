#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDF5BA9D30642D5A0 (cifs-utils@samba.org)
#
Name     : cifs-utils
Version  : 7.0
Release  : 29
URL      : https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-7.0.tar.bz2
Source0  : https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-7.0.tar.bz2
Source1  : https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-7.0.tar.bz2.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: cifs-utils-bin = %{version}-%{release}
Requires: cifs-utils-lib = %{version}-%{release}
Requires: cifs-utils-license = %{version}-%{release}
Requires: cifs-utils-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : keyutils-dev
BuildRequires : krb5-dev
BuildRequires : libcap-ng-dev
BuildRequires : pypi-docutils
BuildRequires : sed
BuildRequires : talloc-dev

%description
This is the release version of cifs-utils, a package of utilities for
doing and managing mounts of the Linux CIFS filesystem. These programs
were originally part of Samba, but have now been split off into a
separate package.

%package bin
Summary: bin components for the cifs-utils package.
Group: Binaries
Requires: cifs-utils-license = %{version}-%{release}

%description bin
bin components for the cifs-utils package.


%package dev
Summary: dev components for the cifs-utils package.
Group: Development
Requires: cifs-utils-lib = %{version}-%{release}
Requires: cifs-utils-bin = %{version}-%{release}
Provides: cifs-utils-devel = %{version}-%{release}
Requires: cifs-utils = %{version}-%{release}

%description dev
dev components for the cifs-utils package.


%package lib
Summary: lib components for the cifs-utils package.
Group: Libraries
Requires: cifs-utils-license = %{version}-%{release}

%description lib
lib components for the cifs-utils package.


%package license
Summary: license components for the cifs-utils package.
Group: Default

%description license
license components for the cifs-utils package.


%package man
Summary: man components for the cifs-utils package.
Group: Default

%description man
man components for the cifs-utils package.


%prep
%setup -q -n cifs-utils-7.0
cd %{_builddir}/cifs-utils-7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660261198
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%reconfigure --disable-static ROOTSBINDIR=/usr/bin
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1660261198
rm -rf %{buildroot}
## install_prepend content
mkdir -p %{buildroot}/sbin
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/cifs-utils
cp %{_builddir}/cifs-utils-%{version}/COPYING %{buildroot}/usr/share/package-licenses/cifs-utils/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cifs.upcall
/usr/bin/cifscreds
/usr/bin/mount.cifs
/usr/bin/mount.smb3
/usr/bin/smb2-quota
/usr/bin/smbinfo

%files dev
%defattr(-,root,root,-)
/usr/include/cifsidmap.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/security/pam_cifscreds.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cifs-utils/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cifscreds.1
/usr/share/man/man1/smb2-quota.1
/usr/share/man/man1/smbinfo.1
/usr/share/man/man8/cifs.upcall.8
/usr/share/man/man8/mount.cifs.8
/usr/share/man/man8/mount.smb3.8
/usr/share/man/man8/pam_cifscreds.8
