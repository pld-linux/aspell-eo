Summary:	Esperanto dictionary for aspell
Summary(pl):	S³ownik Esperanto dla aspella
Name:		aspell-eo
Version:	0.50
%define	subv	2
Release:	3
Epoch:		1
License:	GPL (?)
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/eo/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	f84147f5909e1a5f7adb86f27c71eb8c
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Esperanto dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik (lista s³ów) Esperanto dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*
