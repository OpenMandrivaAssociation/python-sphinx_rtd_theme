%define module	sphinx_rtd_theme

Name:		python-%{module}
Version:	3.0.2
Release:	3
Summary:	Sphinx theme for readthedocs.org
Group:		Development/Python
License:	MIT
URL:		https://github.com/snide/sphinx_rtd_theme
Source0:	https://pypi.io/packages/source/s/%{module}/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)

# Renamed 2025-12-19 after 6.0
%rename python-sphinx-rtd-theme

%patchlist
sphinx_rtd_theme-3.0.2-sphinx9.0-docutils0.22.patch

%description
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info
