%define name PyXML
%define version 0.6.5
%define release 1

Summary: Python/XML package
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Copyright: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
Vendor: XML-SIG <xml-sig@python.org>
Url: http://www.python.org/sigs/xml-sig/

%description
XML Parsers and API for Python
This version of PyXML was tested with Python 2.0 and 1.5.2.


%prep
%setup

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc ANNOUNCE CREDITS LICENCE README README.dom README.pyexpat README.sgmlop doc demo test
