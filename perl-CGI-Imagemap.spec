%include	/usr/lib/rpm/macros.perl
Summary:	CGI::Imagemap.pm - imagemap behavior for CGI programs
Name:		perl-CGI-Imagemap
Version:	1.00
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/CGI/CGI_Imagemap-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Imagemap allows CGI programmers to place TYPE=IMAGE form fields
on their HTML fill-out forms, with either client-side or server-side
maps emulated.

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
