%include	/usr/lib/rpm/macros.perl
Summary:	CGI::Imagemap.pm - imagemap behavior for CGI programs
Summary(pl):	CGI::Imagemap - obs�uga imagemap dla program�w CGI
Name:		perl-CGI-Imagemap
Version:	1.00
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/CGI_Imagemap-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Imagemap allows CGI programmers to place TYPE=IMAGE form fields
on their HTML fill-out forms, with either client-side or server-side
maps emulated.

%description -l pl
Modu� CGI::Imagemap pozwala programistom CGI na umieszczanie p�l z
z TYPE=IMAGE w formularzach HTML z mapami zar�wno po stronie klienta
jak i serwera.

%prep
%setup -q -n CGI_Imagemap-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/CGI/Imagemap.pm
%{_mandir}/man3/*
