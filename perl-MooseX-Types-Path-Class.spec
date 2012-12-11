%define upstream_name    MooseX-Types-Path-Class
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A Path::Class type library for Moose
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(Path::Class)
BuildArch:	noarch

%description
MooseX::Types::Path::Class creates common the Moose manpage types,
coercions and option specifications useful for dealing with the Path::Class
manpage objects as the Moose manpage attributes.

Coercions (see the Moose::Util::TypeConstraints manpage) are made from both
'Str' and 'ArrayRef' to both the Path::Class::Dir manpage and the
Path::Class::File manpage objects. If you have the MooseX::Getopt manpage
installed, the Getopt option type ("=s") will be added for both the
Path::Class::Dir manpage and the Path::Class::File manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 655139
- rebuild for updated spec-helper

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 380995
- adding missing buildrequires:
- import perl-MooseX-Types-Path-Class


* Fri May 29 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist

