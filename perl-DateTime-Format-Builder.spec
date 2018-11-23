#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-Format-Builder
Version  : 0.81
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Builder-0.81.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Builder-0.81.tar.gz
Summary  : 'Create DateTime parser classes and objects.'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-DateTime-Format-Builder-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Class::Data::Inheritable)
BuildRequires : perl(Class::Factory::Util)
BuildRequires : perl(Class::Singleton)
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Format::Strptime)
BuildRequires : perl(DateTime::Locale)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(Exception::Class)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::DeprecationManager)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
This archive contains the distribution DateTime-Format-Builder,
version 0.81:
Create DateTime parser classes and objects.

%package dev
Summary: dev components for the perl-DateTime-Format-Builder package.
Group: Development
Provides: perl-DateTime-Format-Builder-devel = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-Builder package.


%package license
Summary: license components for the perl-DateTime-Format-Builder package.
Group: Default

%description license
license components for the perl-DateTime-Format-Builder package.


%prep
%setup -q -n DateTime-Format-Builder-0.81

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Builder
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Builder/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/DateTime/Format/Builder.pm
/usr/lib/perl5/vendor_perl/5.28.0/DateTime/Format/Builder/Parser.pm
/usr/lib/perl5/vendor_perl/5.28.0/DateTime/Format/Builder/Parser/Dispatch.pm
/usr/lib/perl5/vendor_perl/5.28.0/DateTime/Format/Builder/Parser/Quick.pm
/usr/lib/perl5/vendor_perl/5.28.0/DateTime/Format/Builder/Parser/Regex.pm
/usr/lib/perl5/vendor_perl/5.28.0/DateTime/Format/Builder/Parser/Strptime.pm
/usr/lib/perl5/vendor_perl/5.28.0/DateTime/Format/Builder/Parser/generic.pm
/usr/lib/perl5/vendor_perl/5.28.0/DateTime/Format/Builder/Tutorial.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::Builder.3
/usr/share/man/man3/DateTime::Format::Builder::Parser.3
/usr/share/man/man3/DateTime::Format::Builder::Parser::Dispatch.3
/usr/share/man/man3/DateTime::Format::Builder::Parser::Quick.3
/usr/share/man/man3/DateTime::Format::Builder::Parser::Regex.3
/usr/share/man/man3/DateTime::Format::Builder::Parser::Strptime.3
/usr/share/man/man3/DateTime::Format::Builder::Parser::generic.3
/usr/share/man/man3/DateTime::Format::Builder::Tutorial.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-Builder/LICENSE
