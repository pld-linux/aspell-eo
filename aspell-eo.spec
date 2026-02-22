Summary:	Esperanto dictionary for aspell
Summary(pl.UTF-8):	Słownik Esperanto dla aspella
Name:		aspell-eo
Version:	2.1.20000225a
%define	subv	2
Release:	3
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/eo/aspell6-eo-%{version}-%{subv}.tar.bz2
# Source0-md5:	455719c49ffeb51b204767de6e1d9ef6
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Esperanto dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik (lista słów) Esperanto dla aspella.

%prep
%setup -q -n aspell6-eo-%{version}-%{subv}

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
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
