%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	MaxEntropy
Summary:	MaxEntropy - Perl5 module for Maximum Entropy Modeling and Feature Induction
Name:		perl-Statistics-MaxEntropy
Version:	0.9
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an implementation of the Generalised and Improved Iterative
Scaling (GIS, IIS) algorithms and the Feature Induction (FI) algorithm
as defined in (B<Darroch and Ratcliff 1972>) and (B<Della Pietra et
al. 1997>). The purpose of the scaling algorithms is to find the maximum
entropy distribution given a set of events and (optionally) an initial
distribution. Also a set of candidate features may be specified; then
the FI algorithm may be applied to find and add the candidate feature(s)
that give the largest `gain' in terms of Kullback Leibler divergence
when it is added to the current set of features.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
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
