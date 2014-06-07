Summary:	xscope - X Window Protocol viewer
Summary(pl.UTF-8):	xscope - podglądacz protokołu X Window
Name:		xorg-app-xscope
Version:	1.4.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xscope-%{version}.tar.bz2
# Source0-md5:	ad80eb4ec8d807eb542c4e790c90e848
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xscope sits in-between an X11 client and an X11 server and prints the
contents of each request, reply, error, or event that is communicated
between them. This information can be useful in debugging and
performance tuning of X11 servers and clients.

%description -l pl.UTF-8
Program xscope umiejscawia się między klientem a serwerem X11 i
wypisuje zawartość każdego żądania, odpowiedzi, błędu i zdarzenia,
które jest przesyłane między nimi. Informacje te mogą być przydatne
przy diagnostyce i poprawianiu wydajności serwerów i klientów X11.

%prep
%setup -q -n xscope-%{version}

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xscope
%{_mandir}/man1/xscope.1*
