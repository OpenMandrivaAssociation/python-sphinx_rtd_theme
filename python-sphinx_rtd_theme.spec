%define module	sphinx_rtd_theme

Name:		python-%{module}
Version:	1.0.0
Release:	3
Summary:	Sphinx theme for readthedocs.org
Group:		Development/Python
License:	MIT
URL:		https://github.com/snide/sphinx_rtd_theme
Source0:	https://pypi.io/packages/source/s/%{module}/%{module}-%{version}.tar.gz
Patch0:		sphinx_rtd_theme-1.0.0-docutils-0.18.patch
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)

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
