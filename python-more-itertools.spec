%global sum     More routines for operating on iterables, beyond itertools

Name:           python-more-itertools
Version:        2.5.0
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/erikrose/more-itertools
Source0:        https://github.com/erikrose/more-itertools/archive/%{version}.tar.gz

BuildArch:      noarch


%description
%{sum}

%package -n python2-more-itertools
Summary:        %sum

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-setuptools
Requires:       python-six


%description -n python2-more-itertools
%{sum}


%prep
%autosetup -n more-itertools-%{version}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%license LICENSE


%files -n python2-more-itertools
%{python2_sitelib}/more_itertools-%{version}-py*.egg-info
%{python2_sitelib}/more_itertools


%changelog
* Thu Mar 16 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 2.5.0-1
- Initial packaging
