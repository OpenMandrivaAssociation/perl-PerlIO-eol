%define upstream_name    PerlIO-eol
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	PerlIO layer for normalizing line endings
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This perl module enable you to normalize line endings
This layer normalizes any of CR, LF, CRLF and Native into the designated line 
ending. 
It works for both input and output handles.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
%check 
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/PerlIO
%{perl_vendorarch}/auto/PerlIO
