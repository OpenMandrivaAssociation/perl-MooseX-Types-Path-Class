%define upstream_name    MooseX-Types-Path-Class
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A Path::Class type library for Moose
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::MOP)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Path::Class)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


