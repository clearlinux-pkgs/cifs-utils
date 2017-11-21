#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5AFDBFB270F3B981 (cifs-utils@samba.org)
#
Name     : cifs-utils
Version  : 6.7
Release  : 10
URL      : https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-6.7.tar.bz2
Source0  : https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-6.7.tar.bz2
Source99 : https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-6.7.tar.bz2.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: cifs-utils-bin
Requires: cifs-utils-lib
Requires: cifs-utils-doc
BuildRequires : Linux-PAM-dev
BuildRequires : keyutils-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
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


%package doc
Summary: doc components for the cifs-utils package.
Group: Documentation

%description doc
doc components for the cifs-utils package.


%package lib
Summary: lib components for the cifs-utils package.
Group: Libraries

%description lib
lib components for the cifs-utils package.


%prep
%setup -q -n cifs-utils-6.7

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490193678
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1490193678
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/security/pam_cifscreds.so
