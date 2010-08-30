
%define gitrev 053e94b
%define gitauthor assaf
%define gitname uuid

Summary:	Ruby interface to Git
Name:		ruby-uuid
Version:	2.3.1
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/%{gitauthor}-%{gitname}-v%{version}-0-g%{gitrev}.tar.gz
# Source0-md5:	0d4aebbd649d4ca30a96edc1fa46ea1d
URL:		http://github.com/assaf/uuid
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
Requires:	ruby-macaddr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generates universally unique identifiers (UUIDs) for use in
distributed applications.

%prep
%setup -q -n %{gitauthor}-%{gitname}-%{gitrev}
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/uuid.rb
%attr(755,root,root) %{_bindir}/uuid
