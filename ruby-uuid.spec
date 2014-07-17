%define pkgname uuid
Summary:	Ruby interface to Git
Name:		ruby-%{pkgname}
Version:	2.3.7
Release:	2
License:	MIT
Group:		Development/Tools
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	749430cac002a05e99d7ae0fb835f78a
Patch0:	nogems.patch
URL:		http://github.com/assaf/uuid
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-macaddr >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generates universally unique identifiers (UUIDs) for use in
distributed applications.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%{__sed} -i -e 's,@VERSION@,%{version},' lib/uuid.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/uuid.rb
