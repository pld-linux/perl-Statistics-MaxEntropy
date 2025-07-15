#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Statistics
%define		pnam	MaxEntropy
Summary:	MaxEntropy - Perl5 module for Maximum Entropy Modeling and Feature Induction
Summary(pl.UTF-8):	MaxEntropy - moduł do modelowania największej entropii i indukcji cech
Name:		perl-Statistics-MaxEntropy
Version:	0.9
Release:	15
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b1f7972596653b423e5d65fc7e29f2ee
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Statistics-MaxEntropy/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-perldoc
%endif
Requires:	perl-perldoc
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

%description -l pl.UTF-8
Ten moduł jest implementacją algorytmów uogólnionego i ulepszonego
iteracyjnego skalowania (GIS, IIS) oraz algorytmu indukcji cech (FI -
Feature Induction), zdefiniowanych przez Darrocha i Ratcliffa w 1972
roku oraz Della Pietra i innych w 1997. Celem algorytmów skalujących
jest znalezienie maksymalnego rozproszenia entropii zadanej zbiorem
zdarzeń i (opcjonalnie) początkowym rozproszeniem. Można podać także
zbiór cech-kandydatów; wtedy może być zastosowany algorytm FI do
odnalezienia i dodanie cech-kandydatów, które dają największy zysk w
sensie odchylenia Kullbacka-Leiblera kiedy są dodane do aktualnego
zbioru cech.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p0

# kill insecure /tmp usage and possible conflict with another users' builds
install -d tmp
%{__perl} -pi -e 's@"/tmp"@"tmp"@' t/0[01]*

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README *txt
%attr(755,root,root) %{_bindir}/ME.wrapper.pl
%{perl_vendorlib}/Statistics/*.pm
# empty autosplit.ix files
#%%{perl_vendorlib}/auto/Statistics/Candidates
#%%{perl_vendorlib}/auto/Statistics/MaxEntropy
#%%{perl_vendorlib}/auto/Statistics/SparseVector
%{_mandir}/man[13]/*
