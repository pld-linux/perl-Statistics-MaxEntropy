#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	MaxEntropy
Summary:	MaxEntropy - Perl5 module for Maximum Entropy Modeling and Feature Induction
Summary(pl):	MaxEntropy - modu� do modelowania najwi�kszej entropii i indukcji cech
Name:		perl-Statistics-MaxEntropy
Version:	0.9
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an implementation of the Generalised and Improved
Iterative Scaling (GIS, IIS) algorithms and the Feature Induction (FI)
algorithm as defined in (Darroch and Ratcliff 1972) and (Della Pietra
et al. 1997). The purpose of the scaling algorithms is to find the
maximum entropy distribution given a set of events and (optionally) an
initial distribution. Also a set of candidate features may be
specified; then the FI algorithm may be applied to find and add the
candidate feature(s) that give the largest `gain' in terms of Kullback
Leibler divergence when it is added to the current set of features.

%description -l pl
Ten modu� jest implementacj� algorytm�w uog�lnionego i ulepszonego
iteracyjnego skalowania (GIS, IIS) oraz algorytmu indukcji cech (FI -
Feature Induction), zdefiniowanych przez Darrocha i Ratcliffa w 1972
roku oraz Della Pietra i innych w 1997. Celem algorytm�w skaluj�cych
jest znalezienie maksymalnego rozproszenia entropii zadanej zbiorem
zdarze� i (opcjonalnie) pocz�tkowym rozproszeniem. Mo�na poda� tak�e
zbi�r cech-kandydat�w; wtedy mo�e by� zastosowany algorytm FI do
odnalezienia i dodanie cech-kandydat�w, kt�re daj� najwi�kszy zysk w
sensie odchylenia Kullbacka-Leiblera kiedy s� dodane do aktualnego
zbioru cech.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README *txt
%attr(755,root,root) %{_bindir}/ME.wrapper.pl
%{perl_sitelib}/Statistics/*.pm
# empty autosplit.ix files
#%{perl_sitelib}/auto/Statistics/Candidates
#%{perl_sitelib}/auto/Statistics/MaxEntropy
#%{perl_sitelib}/auto/Statistics/SparseVector
%{_mandir}/man[13]/*
