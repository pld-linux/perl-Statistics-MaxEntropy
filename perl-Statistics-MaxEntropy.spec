%include	/usr/lib/rpm/macros.perl
Summary:	Statistics-MaxEntropy perl module
Summary(pl):	Modu³ perla Statistics-MaxEntropy
Name:		perl-Statistics-MaxEntropy
Version:	0.9
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Statistics/Statistics-MaxEntropy-%{version}.tar.gz
Patch:		perl-Statistics-MaxEntropy-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics-MaxEntropy perl module. 

%description -l pl
Modu³ perla Statistics-MaxEntropy.

%prep
%setup -q -n Statistics-MaxEntropy-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Statistics/MaxEntropy
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        Changes README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,GNU_GPL.txt,GNU_LGPL.txt,INSTALL.txt}.gz
%attr(755,root,root) %{_bindir}/ME.wrapper.pl

%{perl_sitelib}/Statistics/*.pm
%{perl_sitelib}/auto/Statistics/Candidates
%{perl_sitelib}/auto/Statistics/MaxEntropy
%{perl_sitelib}/auto/Statistics/SparseVector
%{perl_sitearch}/auto/Statistics/MaxEntropy

%{_mandir}/man[13]/*
