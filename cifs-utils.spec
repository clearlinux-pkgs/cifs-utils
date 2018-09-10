#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDF5BA9D30642D5A0 (cifs-utils@samba.org)
#
Name     : cifs-utils
Version  : 6.8
Release  : 13
URL      : https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-6.8.tar.bz2
Source0  : https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-6.8.tar.bz2
Source99 : https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-6.8.tar.bz2.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: cifs-utils-bin
Requires: cifs-utils-license
Requires: cifs-utils-lib
BuildRequires : Linux-PAM-dev
BuildRequires : keyutils-dev
BuildRequires : krb5-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : sed

%description
This is the release version of cifs-utils, a package of utilities for
doing and managing mounts of the Linux CIFS filesystem. These programs
were originally part of Samba, but have now been split off into a
separate package.

%package bin
Summary: bin components for the cifs-utils package.
Group: Binaries
Requires: cifs-utils-license

%description bin
bin components for the cifs-utils package.


%package dev
Summary: dev components for the cifs-utils package.
Group: Development
Requires: cifs-utils-lib
Requires: cifs-utils-bin
Provides: cifs-utils-devel

%description dev
dev components for the cifs-utils package.


%package lib
Summary: lib components for the cifs-utils package.
Group: Libraries
Requires: cifs-utils-license

%description lib
lib components for the cifs-utils package.


%package license
Summary: license components for the cifs-utils package.
Group: Default

%description license
license components for the cifs-utils package.


%prep
%setup -q -n cifs-utils-6.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536545411
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536545411
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/cifs-utils
cp COPYING %{buildroot}/usr/share/doc/cifs-utils/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cifscreds
/usr/bin/mount.cifs

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/security/pam_cifscreds.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/cifs-utils/COPYING
