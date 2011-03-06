Summary:	System utilities package
Summary(pl.UTF-8):	Pakiet narzędzi systemowych
Name:		sysfsutils
%define	org_version	2.1.0
Version:	2.2.0
Release:	1
License:	LGPL v2.1/GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linux-diag/%{name}-%{org_version}.tar.gz
# Source0-md5:	14e7dcd0436d2f49aa403f67e1ef7ddc
Patch0:		%{name}-lsi.patch
URL:		http://linux-diag.sourceforge.net/Sysfsutils.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package's purpose is to provide a set of utilities for
interfacing with sysfs, a virtual filesystem in Linux kernel versions
2.5+ that provides a tree of system devices. While a filesystem is a
very useful interface, the authors decided to provide a stable
programming interface that will hopefully make it easier for
applications to query system devices and their attributes.

This package currently includes:
- libsysfs: a library for accessing system devices.
- lsbus: a small application to query system bus information.
- systool: an application to view system device information by bus,
  class, and topology.

%description -l pl.UTF-8
Celem tego pakietu jest dostarczenie zestawu narzędzi do współpracy z
sysfs - wirtualnym systemem plików jąder Linuksa w wersji 2.5+
udostępniającym drzewo urządzeń systemowych. O ile system plików jest
bardzo użytecznym interfejsem, autorzy zdecydowali się dostarczyć
stabilny interfejs programistyczny, ułatwiający aplikacjom odpytywanie
się o urządzenia systemowe i ich atrybuty.

Ten pakiet zawiera:
- libsysfs - bibliotekę do dostępu do urządzeń systemowych,
- lsbus - małą aplikację do odczytywania informacji o szynach
  systemowych,
- systool - aplikację do przeglądania informacji o urządzeniach
  systemowych według szyny, klasy i topologii.

%package devel
Summary:	Header files for sysfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sysfs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for sysfs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sysfs.

%package static
Summary:	Static sysfs library
Summary(pl.UTF-8):	Statyczna biblioteka sysfs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static sysfs library.

%description static -l pl.UTF-8
Statyczna biblioteka sysfs.

%prep
%setup -q -n %{name}-%{org_version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only note, not actual GPL/LGPL texts
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc docs/libsysfs.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/sysfs

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
