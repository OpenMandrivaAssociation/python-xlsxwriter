Name:		python-xlsxwriter
Version:	3.2.9
Release:	1
Summary:	A Python module for creating Excel XLSX files
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://pypi.org/project/xlsxwriter/
Source0:	xlsxwriter-3.2.9.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
A Python module for creating Excel XLSX files.

%files
%{py_sitedir}/*
%{_bindir}/vba_extract.py
