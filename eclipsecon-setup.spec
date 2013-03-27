%global __requires_exclude osgi*
%global __provides_exclude osgi*

Name:           eclipsecon-setup
Version:        1.0
Release:	1%{?dist}
Summary:        Linux Tools Project bundles and example projects for tutorial.

License:        EPL
URL:            http://www.eclipse.org/linuxtools
Source0:	%{name}-%{version}.tar.gz

BuildRequires:  unzip

BuildArch: noarch

# .eclipse folder may be architecture specific
#ExclusiveArch:  x86_64

%description
This contains a the Linux Tools Project bundles as well as the set of
sample projects to be used for EclipseCon Boston 2013.


%prep
%setup -q


%build


%install
install -dm 755 %{buildroot}%{_javadir}/%{name}
install -dm 755 %{buildroot}%{_datadir}/doc/%{name}
# Linux Tools Project P2 Repository
cp -rp repository-linuxtools %{buildroot}%{_javadir}/%{name}
# Custom Feature that automatically includes the features we want
cp -rp repository-eclipsecon %{buildroot}%{_javadir}/%{name}
cp -rp examples %{buildroot}%{_datadir}/doc/%{name}
#cp -rp .eclipse %{buildroot}%{_javadir}/%{name}
#cp -rp workspace %{buildroot}%{_javadir}/%{name}


%files
%{_javadir}/%{name}
%{_datadir}/doc/%{name}


%changelog
* Wed Mar 13 2013 Roland Grunberg <rgrunber@redhat.com> 1.0-1
- Initial packaging.
