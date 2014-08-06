Name:           perl-Role-Tiny
Version:        1.003003
Release:        1%{?dist}
Summary:        Roles. Like a nouvelle cuisine portion size slice of Moose
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Role-Tiny/
Source0:        http://cpan.metacpan.org//authors/id/H/HA/HAARG/Role-Tiny-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(Class::Method::Modifiers) >= 1.05
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Class::Method::Modifiers) >= 1.05
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Role::Tiny is a minimalist role composition tool.

%prep
%setup -q -n Role-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 29 2014 David E. Wheeler <david.wheeler@iovation.com> 1.003003-1
- Specfile autogenerated by cpanspec 1.78.