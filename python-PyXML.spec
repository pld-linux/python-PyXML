%include /usr/lib/rpm/macros.python

%define module PyXML

Summary:	Python/XML package
Summary(pl):	Pakiet Python/XML
Name:		python-%{module}
Version:	0.7
Release:	2
License:	Python
Vendor:		XML-SIG <xml-sig@python.org>
Group:		Development/Libraries
Source0:	http://prdownloads.sourceforge.net/pyxml/%{module}-%{version}.tar.gz
URL:		http://pyxml.sourceforge.net/
BuildRequires:	python >= 2.2
BuildRequires:	rpm-pythonprov
%requires_eq	python
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
Group:		Development/Libraries
%requires_eq	python
Requires:	%{name} = %{version}

%description examples
Examples of Python/XML.

%description examples -l pl
Przyk³ady do Python/XML.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}" python setup.py build --with-libexpat=%{_prefix} --ldflags=-lexpat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_examplesdir}/%{name}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--record=INSTALLED_FILES

cp -a demo $RPM_BUILD_ROOT/%{_examplesdir}/%{name}

gzip -9fn ANNOUNCE CREDITS LICENCE README README.dom README.pyexpat README.sgmlop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc test
%{py_sitedir}/_xmlplus
%attr(755,root,root) %{_bindir}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
