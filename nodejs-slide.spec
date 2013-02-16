%define		pkg	slide
Summary:	A flow control lib small enough to fit on in a slide presentation.
Name:		nodejs-%{pkg}
Version:	1.1.3
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/node-slide
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	47514d76854b5896bceaed811f8ae403
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
A flow control lib small enough to fit on in a slide presentation. 
Derived live at Oak.JS

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a package.json lib $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%{nodejs_libdir}/%{pkg}/lib
