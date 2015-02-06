%define upstream_name    PerlIO-eol
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.140.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 556071
- rebuild for perl 5.12

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 406178
- rebuild using %%perl_convert_version

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.14-2mdv2008.1
+ Revision: 152171
- rebuild for new perl
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 0.14-1mdv2008.0
+ Revision: 20949
- update to 0.14


* Fri Dec 09 2005 Michael Scherer <misc@mandriva.org> 0.13-4mdk
- Rebuild
- use mkrel
- use check

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.13-3mdk
- Rebuild for new perl

* Fri Oct 29 2004 Michael Scherer <misc@mandrake.org> 0.13-2mdk 
- BuildRequires

* Sun Oct 24 2004 Michael Scherer <misc@mandrake.org> 0.13-1mdk
- First Mandrakelinux package

