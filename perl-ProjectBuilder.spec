#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	ProjectBuilder
%include	/usr/lib/rpm/macros.perl
Summary:	Perl module providing multi-OSes (Linux/Solaris/...) Continuous Packaging
Name:		perl-ProjectBuilder
Version:	0.12.1
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	ftp://ftp.project-builder.org/src/%{pdir}-%{version}.tar.gz
# Source0-md5:	2f31609146aab2e8f597df1b938df3f7
#URL:		http://search.cpan.org/dist/ProjectBuilder/
URL:		http://www.project-builder.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProjectBuilder is a Perl module providing set of functions to help
develop packages for projects and deal with different Operating
systems (Linux distributions, Solaris, ...). It implements a
Continuous Packaging approach.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/pb
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README
%dir %{_sysconfdir}/pb
%attr(755,root,root) %{_bindir}/pbdistrocheck
%{_mandir}/man1/pbdistrocheck.1p*
%{_mandir}/man3/ProjectBuilder::*.3pm*
%{perl_vendorlib}/ProjectBuilder
