#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	CGI::Imagemap - imagemap behavior for CGI programs
Summary(pl.UTF-8):   CGI::Imagemap - obsługa imagemap dla programów CGI
Name:		perl-CGI-Imagemap
Version:	1.00
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/CGI_Imagemap-%{version}.tar.gz
# Source0-md5:	063fcbb84efb0237accf4bc740ced608
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Imagemap allows CGI programmers to place TYPE=IMAGE form fields
on their HTML fill-out forms, with either client-side or server-side
maps emulated.

%description -l pl.UTF-8
Moduł CGI::Imagemap pozwala programistom CGI na umieszczanie pól z
z TYPE=IMAGE w formularzach HTML z mapami zarówno po stronie klienta
jak i serwera.

%prep
%setup -q -n CGI_Imagemap-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/CGI/Imagemap.pm
%{_mandir}/man3/*
