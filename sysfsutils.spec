Summary:	System utilities package
Summary(pl):	Pakiet narzêdzi systemowych
Name:		sysfsutils
Version:	1.3.0
Release:	2
License:	LGPL v2.1/GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz
# Source0-md5:	d11c99271531be3c1e6d36b53968cd2b
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

%description -l pl
Celem tego pakietu jest dostarczenie zestawu narzêdzi do wspó³pracy z
sysfs - wirtualnym systemem plików j±der Linuksa w wersji 2.5+
udostêpniaj±cym drzewo urz±dzeñ systemowych. O ile system plików jest
bardzo u¿ytecznym interfejsem, autorzy zdecydowali siê dostarczyæ
stabilny interfejs programistyczny, u³atwiaj±cy aplikacjom odpytywanie
siê o urz±dzenia systemowe i ich atrybuty.

Ten pakiet zawiera:
- libsysfs - bibliotekê do dostêpu do urz±dzeñ systemowych,
- lsbus - ma³± aplikacjê do odczytywania informacji o szynach
  systemowych,
- systool - aplikacjê do przegl±dania informacji o urz±dzeniach
  systemowych wed³ug szyny, klasy i topologii.

%package devel
Summary:	Header files for sysfs library
Summary(pl):	Pliki nag³ówkowe biblioteki sysfs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for sysfs library.

%description devel -l pl
Pliki nag³ówkowe biblioteki sysfs.

%package static
Summary:	Static sysfs library
Summary(pl):	Statyczna biblioteka sysfs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static sysfs library.

%description static -l pl
Statyczna biblioteka sysfs.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}/sysfs
mv $RPM_BUILD_ROOT%{_includedir}/{*.h,sysfs}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only note, not actual GPL/LGPL texts
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc docs/libsysfs.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/sysfs/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
