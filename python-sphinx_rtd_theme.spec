%define module	sphinx_rtd_theme

Name:		python-%{module}
Version:	0.4.3
Release:	%mkrel 3
Summary:	Sphinx theme for readthedocs.org
Group:		Development/Python
License:	MIT
URL:		https://github.com/snide/sphinx_rtd_theme
Source0:	https://pypi.io/packages/source/s/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)

%description
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.

%package -n	python3-%{module}
Summary:	Sphinx theme for readthedocs.org
Group:		Development/Python
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info
