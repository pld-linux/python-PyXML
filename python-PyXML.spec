%include	/usr/lib/rpm/macros.python

%define module PyXML

Summary:	Python/XML package
Summary(pl):	Pakiet Python/XML
Name:		python-%{module}
Version:	0.8.3
Release:	2
License:	BeOpen Python Open Source License
Vendor:		XML-SIG <xml-sig@python.org>
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyxml/%{module}-%{version}.tar.gz
# Source0-md5:	7083d950064ce90840d9ed48c818dc85
URL:		http://pyxml.sourceforge.net/
BuildRequires:	expat-devel >= 1.95.4
BuildRequires:	python >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PyXML package is a collection of libraries to process XML with
Python. It contains, among other things
- xmlproc: a validating XML parser.
- sgmlop: a C helper module that can speed-up xmllib.py and sgmllib.py
  by a factor of 5.
- PySAX: SAX 1 and SAX2 libraries with drivers for most of the
  parsers.
- 4DOM: A fully compliant DOM Level 2 implementation
- javadom: An adapter from Java DOM implementations to the standard
  Python DOM binding.
- pulldom: a DOM implementation that supports lazy instantiation of
  nodes.
- marshal: a module with several options for serializing Python
  objects to XML, including WDDX and XML-RPC.
- unicode: a helper module for Python 1.5 users who need conversions
  between UTF-8 and ISO-8859-?.

%description -l pl
Pakiet PyXML jest zestawem bibliotek do obs³ugi XML z poziomu Pythona.
Zawiera miêdzy innymi:
- xmlproc: parser sprawdzaj±cy poprawno¶æ XML
- sgmlp: pomocniczy modu³ w C przyspieszaj±cy dzia³anie xmllib.py i
  sgmllib.py piêciokrotnie
- PySAX: biblioteki SAX1 i SAX2 z driverami do wiêkszo¶ci parserów
- 4DOM: w pe³ni kompatybilna implementacja DOM Level 2
- javadom: adapter z implementacji DOM w Javie do standardowego DOM w
  Pythonie
- pulldom: implementacja DOM obs³uguj±ca leniwe tworzenie instancji
  wêz³ów
- marshal: modu³ z ró¿nymi opcjami do serializacji obiektów Pythona w
  XML, w tym WDDX i XML-RPC
- unicode: pomocniczy modu³ dla u¿ytkowników Pythona 1.5, którzy
  potrzebuj± konwersji miêdzy UTF-8 a ISO-8859-?.

%package examples
Summary:	Examples of Python/XML
Summary(pl):	Przyk³ady do Python/XML
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description examples
Examples of Python/XML.

%description examples -l pl
Przyk³ady do Python/XML.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build \
	--with-libexpat=%{_prefix} \
	--ldflags=-lexpat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

cp -a demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc test ANNOUNCE CREDITS LICENCE README README* TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/_xmlplus

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
