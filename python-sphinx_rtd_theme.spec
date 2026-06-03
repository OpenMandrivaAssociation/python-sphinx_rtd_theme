%define module sphinx_rtd_theme

Name:		python-sphinx_rtd_theme
Summary:	Sphinx theme for readthedocs.org
Version:	3.1.0
Release:	1
Group:		Development/Python
License:	MIT AND Apache-2.0 AND OFL-1.1
URL:		https://github.com/readthedocs/sphinx_rtd_theme
Source0:	https://github.com/readthedocs/sphinx_rtd_theme/archive/%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	fdupes
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)


# Renamed 2025-12-19 after 6.0
%rename python-sphinx-rtd-theme

%description
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.

%prep -a
# Remove bundled egg info
rm -rf %{module}.egg-info

# Remove upper bounds on docutils
sed -i 's:docutils >0.18,<0.23:docutils >0.18:g' setup.cfg

# Fix line endings
sed -i 's/\r//g' OFL-License.txt

# We cannot build the Javascript from source at this time, due to many missing
# dependencies.  Convince the build script to skip building the Javascript and
# go on to the python.
mkdir -p build/lib/%{module}/static/js
cp -p sphinx_rtd_theme/static/js/badge_only.js build/lib/%{module}/static/js
cp -p sphinx_rtd_theme/static/js/theme.js build/lib/%{module}/static/js

%install -a
# Fix dupes.
%fdupes %{buildroot}%{python_sitelib}/%{module}/static

%files
%doc README.rst
%license LICENSE OFL-License.txt
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
