%define major	0
%define libname	%mklibname afpclient %{major}
%define devname	%mklibname afpclient -d

Summary:	An open source client for Apple Filing Protocol
Name:		afpfs-ng
Version:	0.8.2
Release:	3
License:	GPLv2+
Group:		Networking/File transfer
Url:		https://sites.google.com/site/alexthepuffin/home
# https://github.com/simonvetter/afpfs-ng
Source0:	https://github.com/simonvetter/afpfs-ng/raw/master/afpfs-ng-%{version}.tar.gz

BuildRequires:	readline-devel
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(ncurses)

BuildRequires:	gcc-c++, gcc, gcc-cpp

%description
afpfs-ng is a client for the Apple Filing Protocol (AFP) which will let
you mount and access shared volumes from Mac OS X (or netatalk).

There is a FUSE-based client which lets you mount a remote filesystem.

There is also a simple, command-line AFP client; think about it as an
FTP client for AFP.

%package -n %{libname}
Summary:	Shared library of %{name}
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with libafpclient, an Apple Filing Protocol (AFP) client library.

%package -n %{devname}
Summary:	Development headers for libafpclient
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	afpclient-devel = %{EVRD}

%description -n %{devname}
This package contains the headers needed to compile programs that use
libafpclient, an Apple Filing Protocol (AFP) client library.

%prep
%autosetup -p1 -n %{name}
touch README
sed -i -e 's,identify.c,,' lib/Makefile.am
autoreconf -fiv

%build
%configure --disable-static
%make

%install
%makeinstall_std

%files
%doc docs/*.txt docs/README
%{_bindir}/afp*
%{_bindir}/mount_afp
%{_mandir}/man1/*afp*.1*

%files -n %{libname}
%{_libdir}/libafpclient.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/%{name}

