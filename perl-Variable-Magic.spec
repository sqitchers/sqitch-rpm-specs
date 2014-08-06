Name:           perl-Variable-Magic
Version:        0.53
Release:        1%{?dist}
Summary:        Associate user-defined magic to variables from Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Variable-Magic/
Source0:        http://cpan.metacpan.org/authors/id/V/VP/VPIT/Variable-Magic-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Magic is Perl's way of enhancing variables. This mechanism lets the user
add extra data to any variable and hook syntactical operations (such as
access, assignment or destruction) that can be applied to it. With this
module, you can add your own magic to any variable without having to write
a single line of XS.

%prep
%setup -q -n Variable-Magic-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Variable*
%{_mandir}/man3/*

%changelog
* Tue Aug 05 2014 David E. Wheeler <david.wheeler@iovation.com> 0.53-1
- Specfile autogenerated by cpanspec 1.78.
