%define pkgname uuid
Summary:	Ruby interface to Git
Name:		ruby-%{pkgname}
Version:	2.3.1
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	8a9741654c0930849c67c6d6139eec47
URL:		http://github.com/assaf/uuid
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-macaddr
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generates universally unique identifiers (UUIDs) for use in
distributed applications.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uuid
%{ruby_vendorlibdir}/uuid.rb
