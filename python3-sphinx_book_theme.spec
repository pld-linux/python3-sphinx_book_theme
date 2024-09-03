#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	A clean book theme for scientific explanations and documentation with Sphinx
Summary(pl.UTF-8):	Przejrzysty motyw książkowy Sphinksa do opisów i dokumentacji naukowych
Name:		python3-sphinx_book_theme
# 1.1.3 requires Sphinx 5+ and sphinx-theme-builder
# 1.0.1 requires Sphinx 4..6 and sphinx-theme-builder
# 0.3.3 requires Sphinx 3..5 and sphinx-theme-builder
Version:	0.2.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-book-theme/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-book-theme/sphinx-book-theme-%{version}.tar.gz
# Source0-md5:	9760b697e31d20131ba72a55b95deb86
URL:		https://pypi.org/project/sphinx-book-theme/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML
BuildRequires:	python3-Sphinx >= 3
BuildRequires:	python3-Sphinx < 5
BuildRequires:	python3-bs4 >= 4.6.1
BuildRequires:	python3-bs4 < 5
BuildRequires:	python3-docutils >= 0.15
BuildRequires:	python3-docutils < 0.19
%if "%{py3_ver}" == "3.6"
BuildRequires:	python3-importlib_resources >= 3.0
%endif
BuildRequires:	python3-pydata_sphinx_theme >= 0.7.2
BuildRequires:	python3-pydata_sphinx_theme < 0.8
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a lightweight Sphinx theme designed to mimic the look-and-feel
of an interactive book.

%description -l pl.UTF-8
Lekki motyw Sphinksa zaprojektowany tak, aby naśladować interaktywną
książkę.

%prep
%setup -q -n sphinx-book-theme-%{version}

%{__sed} -i -e '/docutils/ s/<0\.17/<0.19/' setup.py

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/sphinx_book_theme
%{py3_sitescriptdir}/sphinx_book_theme-%{version}-py*.egg-info
