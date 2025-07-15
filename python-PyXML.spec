%define		module	PyXML
Summary:	Python/XML package
Summary(pl.UTF-8):	Pakiet Python/XML
Name:		python-%{module}
Version:	0.8.4
Release:	15
License:	BeOpen Python Open Source License
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pyxml/%{module}-%{version}.tar.gz
# Source0-md5:	1f7655050cebbb664db976405fdba209
Patch0:		%{name}-as_is_keyword_in_py26.patch
Patch1:		%{name}-attrs-contains.patch
URL:		http://pyxml.sourceforge.net/
BuildRequires:	expat-devel >= 1:1.95.8
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
Requires:	expat >= 1:1.95.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PyXML package is a collection of libraries to process XML with
Python. It contains, among other things
- xmlproc: a validating XML parser.
- sgmlop: a C helper module that can speed-up xmllib.py and sgmllib.py
  by a factor of 5.
- PySAX: SAX 1 and SAX2 libraries with drivers for most of the
  parsers.
- 4DOM: A fully compliant DOM Level 2 implementation.
- javadom: An adapter from Java DOM implementations to the standard
  Python DOM binding.
- pulldom: a DOM implementation that supports lazy instantiation of
  nodes.
- marshal: a module with several options for serializing Python
  objects to XML, including WDDX and XML-RPC.
- unicode: a helper module for Python 1.5 users who need conversions
  between UTF-8 and ISO-8859-?.

%description -l pl.UTF-8
Pakiet PyXML jest zestawem bibliotek do obsługi XML-a z poziomu
Pythona. Zawiera między innymi:
- xmlproc: analizator sprawdzający poprawność XML-a;
- sgmlp: pomocniczy moduł w C przyspieszający działanie xmllib.py i
  sgmllib.py pięciokrotnie;
- PySAX: biblioteki SAX1 i SAX2 ze sterownikami do większości
  analizatorów składniowych;
- 4DOM: w pełni kompatybilna implementacja DOM Level 2;
- javadom: adapter z implementacji DOM w Javie do standardowego DOM w
  Pythonie;
- pulldom: implementacja DOM obsługująca leniwe tworzenie instancji
  węzłów;
- marshal: moduł z różnymi opcjami do serializacji obiektów Pythona w
  XML-u, w tym WDDX i XML-RPC;
- unicode: pomocniczy moduł dla użytkowników Pythona 1.5, którzy;
  potrzebują konwersji między UTF-8 a ISO-8859-?.

%package examples
Summary:	Examples of Python/XML
Summary(pl.UTF-8):	Przykłady do Python/XML
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples of Python/XML.

%description examples -l pl.UTF-8
Przykłady do Python/XML.

%prep
%setup -q -n %{module}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%py_build \
	--with-libexpat=%{_prefix} \
	--ldflags=-lexpat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_install

%py_postclean

cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc ANNOUNCE CREDITS LICENCE README* TODO
%attr(755,root,root) %{_bindir}/xmlproc_parse
%attr(755,root,root) %{_bindir}/xmlproc_val
%dir %{py_sitedir}/_xmlplus
%{py_sitedir}/_xmlplus/*.py[co]
%dir %{py_sitedir}/_xmlplus/dom
%{py_sitedir}/_xmlplus/dom/*.py[co]
%dir %{py_sitedir}/_xmlplus/dom/ext
%{py_sitedir}/_xmlplus/dom/ext/*.py[co]
%dir %{py_sitedir}/_xmlplus/dom/ext/reader
%{py_sitedir}/_xmlplus/dom/ext/reader/*.py[co]
%dir %{py_sitedir}/_xmlplus/dom/html
%{py_sitedir}/_xmlplus/dom/html/*.py[co]
%lang(de) %{py_sitedir}/_xmlplus/dom/de
%lang(en_US) %{py_sitedir}/_xmlplus/dom/en_US
%lang(fr) %{py_sitedir}/_xmlplus/dom/fr
%dir %{py_sitedir}/_xmlplus/marshal
%{py_sitedir}/_xmlplus/marshal/*.py[co]
%dir %{py_sitedir}/_xmlplus/parsers
%attr(755,root,root) %{py_sitedir}/_xmlplus/parsers/pyexpat.so
%attr(755,root,root) %{py_sitedir}/_xmlplus/parsers/sgmlop.so
%{py_sitedir}/_xmlplus/parsers/*.py[co]
%dir %{py_sitedir}/_xmlplus/parsers/xmlproc
%{py_sitedir}/_xmlplus/parsers/xmlproc/*.py[co]
%dir %{py_sitedir}/_xmlplus/sax
%{py_sitedir}/_xmlplus/sax/*.py[co]
%dir %{py_sitedir}/_xmlplus/sax/drivers
%{py_sitedir}/_xmlplus/sax/drivers/*.py[co]
%dir %{py_sitedir}/_xmlplus/sax/drivers2
%{py_sitedir}/_xmlplus/sax/drivers2/*.py[co]
%dir %{py_sitedir}/_xmlplus/schema
%{py_sitedir}/_xmlplus/schema/*.py[co]
%dir %{py_sitedir}/_xmlplus/unicode
%{py_sitedir}/_xmlplus/unicode/*.py[co]
%dir %{py_sitedir}/_xmlplus/utils
%attr(755,root,root) %{py_sitedir}/_xmlplus/utils/boolean.so
%{py_sitedir}/_xmlplus/utils/*.py[co]
%dir %{py_sitedir}/_xmlplus/xpath
%{py_sitedir}/_xmlplus/xpath/*.py[co]
%{py_sitedir}/PyXML-%{version}-py*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
