%define	pdir	Statistics
%define	pnam	MaxEntropy
%include	/usr/lib/rpm/macros.perl
Summary:	Statistics-MaxEntropy perl module
Summary(pl):	Modu³ perla Statistics-MaxEntropy
Name:		perl-Statistics-MaxEntropy
Version:	0.9
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/ME.wrapper.pl
%{perl_sitelib}/Statistics/*.pm
%{perl_sitelib}/auto/Statistics/Candidates
%{perl_sitelib}/auto/Statistics/MaxEntropy
%{perl_sitelib}/auto/Statistics/SparseVector
%{_mandir}/man[13]/*
