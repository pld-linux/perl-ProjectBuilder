#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	ProjectBuilder
%include	/usr/lib/rpm/macros.perl
Summary:	ProjectBuilder
Name:		perl-ProjectBuilder
Version:	0.11.3
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ProjectBuilder/%{pdir}-%{version}.tar.gz
# Source0-md5:	eaca1edcfbf6e2c1603ab071a803f9f3
URL:		http://search.cpan.org/dist/ProjectBuilder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProjectBuilder helps you build various packages directly from your
project sources. In order to work correctly, it relies on a certain
number of configuration files. Most of these configuration parameters
can be setup in all the configuration files, however, they generally
make more sense in a specific one, which is indicated. There are
mainly 4 configuration files, the one in the home directory of the
user (used first), the one from the project (use in second), the one
in the VM/VE hosting directory, and the one provided by the tool in
/etc/pb or /usr/local/etc/pb (lastly).

%prep
%setup -q -n %{pdir}-%{version}

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
%doc AUTHORS ChangeLog INSTALL NEWS README
%attr(755,root,root) %{_bindir}/pbdistrocheck
%{_mandir}/man1/pbdistrocheck.1p*
%{_mandir}/man3/ProjectBuilder::*.3pm*
%{perl_vendorlib}/ProjectBuilder
