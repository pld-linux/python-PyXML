
%define short_name PyXML

Summary:	Python/XML package
Summary(pl):	Pakiet Python/XML
Name:		python-%{short_name}
Version:	0.6.6
Release:	1
License:	Python
Vendor:		XML-SIG <xml-sig@python.org>
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Source0:	http://prdownloads.sourceforge.net/pyxml/%{short_name}-%{version}.tar.gz
URL:		http://pyxml.sourceforge.net/
%requires_eq	python
BuildRequires:	python >= 2.0
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%include /usr/lib/rpm/macros.python

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
Pakiet PyXML jest zestawem bibliotek do obs≥ugi XML z poziomu Pythona.
Zawiera miÍdzy innymi:
 - xmlproc: parser sprawdzaj±cy poprawno∂Ê XML
 - sgmlp: pomocniczy modu≥ w C przyspieszaj±cy dzia≥anie xmllib.py
   i sgmllib.py piÍciokrotnie
 - PySAX: biblioteki SAX1 i SAX2 z driverami do wiÍkszo∂ci parserÛw
 - 4DOM: w pe≥ni kompatybilna implementacja DOM Level 2
 - javadom: adapter z implementacji DOM w Javie do standardowego DOM
   w Pythonie
 - pulldom: implementacja DOM obs≥uguj±ca leniwe tworzenie instancji
   wÍz≥Ûw
 - marshal: modu≥ z rÛønymi opcjami do serializacji obiektÛw Pythona
   w XML, w tym WDDX i XML-RPC
 - unicode: pomocniczy modu≥ dla uøytkownikÛw Pythona 1.5, ktÛrzy
   potrzebuj± konwersji miÍdzy UTF-8 a ISO-8859-?.
 
%package examples
Summary:	Examples of Python/XML
Summary(pl):	Przyk≥ady do Python/XML
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
%requires_eq	python
Requires:	%{name} = %{version}

%description examples
Examples of Python/XML.

%description examples -l pl
Przyk≥ady do Python/XML.

%prep
%setup -q -n %{short_name}-%{version}

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
