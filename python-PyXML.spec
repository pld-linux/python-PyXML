%define short_name PyXML
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)

Summary:	Python/XML package
Name:		python-%{short_name}
Version:	0.6.5
Release:	2
Source0:	ftp://ftp.sf.net/pub/sourceforge/pyxml/%{short_name}-%{version}.tar.gz
Copyright:	UNKNOWN
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
BuildRequires:	python >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Vendor:		XML-SIG <xml-sig@python.org>
Url:		http://www.python.org/sigs/xml-sig/

%description
XML Parsers and API for Python This version of PyXML was tested with
Python 2.0 and 1.5.2.

%package examples
Summary: examples of Python/XML
Group: Development/Libraries

%description examples
examples of Python/XML

%prep
%setup -q -n %{short_name}-%{version}

%build
CFLAGS="%{rpmcflags}" python setup.py build -- --with-libexpat=/usr --ldflags=-lexpat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_examplesdir}/%{name}
python setup.py install -- --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
cp -a demo $RPM_BUILD_ROOT/%{_examplesdir}/%{name}

gzip -9fn ANNOUNCE CREDITS LICENCE README README.dom README.pyexpat README.sgmlop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCE,CREDITS,LICENCE,README,README.dom,README.pyexpat,README.sgmlop}.gz doc test

%{python_sitepkgsdir}/_xmlplus
%attr(755,root,root) %{_bindir}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
