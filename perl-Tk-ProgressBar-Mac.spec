#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tk
%define	pnam	ProgressBar-Mac
Summary:	Tk::ProgressBar::Mac - a blue, 3-D Macintosh Classic progress bar
Name:		perl-Tk-ProgressBar-Mac
Version:	1.2
Release:	0.3
# same as perl (REMOVE THIS LINE IF NOT TRUE)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	38922bce1c20a3e098022c6f2787c633
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This widget provides a dynamic image that looks just like a Mac OS 9
progress bar. Packed around it are four Frames, north, south, east and
west, within which you can stuff additional widgets. For example, see
how Tk::Copy::Mac uses several Labels and a CollapsableFrame widget to
create a reasonable facsimile of a Macintosh copy dialog.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/Tk/ProgressBar
%{perl_vendorlib}/Tk/ProgressBar/Mac.pm
%{_mandir}/man3/*
