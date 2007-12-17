%define name perl-PerlIO-eol
%define real_name PerlIO-eol
%define version 0.14
%define rel     1

Summary:	PerlIO layer for normalizing line endings
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
Source:         http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/%{real_name}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{real_name}/
BuildRequires:  perl-devel

%description
This perl module enable you to normalize line endings
This layer normalizes any of CR, LF, CRLF and Native into the designated line 
ending. 
It works for both input and output handles.

%prep
%setup -q -n %{real_name}-%{version}


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



