%include	/usr/lib/rpm/macros.perl
Summary:	CGI_Imagemap perl module
Summary(pl):	Modu³ perla CGI_Imagemap
Name:		perl-CGI-Imagemap
Version:	1.00
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI_Imagemap-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Imagemap perl module.

%description -l pl
Modu³ perla CGI-Imagemap.

%prep
%setup -q -n CGI_Imagemap-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/CGI/Imagemap.pm
%{_mandir}/man3/*
