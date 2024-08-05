%define module	sphinx_rtd_theme

Name:		python-%{module}
Version:	2.0.0
Release:	2
Summary:	Sphinx theme for readthedocs.org
Group:		Development/Python
License:	MIT
URL:		https://github.com/snide/sphinx_rtd_theme
Source0:	https://pypi.io/packages/source/s/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)

%patchlist
sphinx_rtd_theme-docutils-0.21.patch

%description
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.

%prep
%autosetup -p1 -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info
