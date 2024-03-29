Summary:	Command-line utility for audio files
Summary(pl.UTF-8):	Narzędzie linii poleceń dla plików dźwiękowych
Name:		dagger
Version:	0.3.2
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://freewarepoint.de/dagger/%{name}-%{version}.tar.gz
# Source0-md5:	c482a7bca5d7e1ffa2157358734956d3
URL:		http://freewarepoint.de/dagger/
Requires:	id3v2 >= 0.1.11
Requires:	python-devel >= 1:2.3
Requires:	vorbis-tools >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dagger is a small command-line utility for Unix/Linux written in
Python which tags and renames audio-files. Currently supported formats
are MP3 and Ogg Vorbis. dagger's configuration file supports different
profiles with their own sets of options.

%description -l pl.UTF-8
dagger jest małym narzędziem linii poleceń napisanym w Pythonie dla
środowiska Unix/Linux służącym do ustawiania znaczników i zmiany nazw
plików dźwiękowych. Aktualnie obsługiwanymi formatami są MP3 i Ogg
Vorbis. Plik konfiguracyjny daggera umożliwia ustawienie różnych
profili z własnym zestawem opcji.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

mv daggerrc daggerrc-example
install %{name} $RPM_BUILD_ROOT%{_bindir}
cp -r man/man* $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog README daggerrc-example
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*.[15]*
