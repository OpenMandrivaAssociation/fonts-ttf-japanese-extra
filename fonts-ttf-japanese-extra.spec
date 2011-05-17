Summary:	Japanese TrueType fonts
Name:		fonts-ttf-japanese-extra
Version:	0.20040217
Release:	%mkrel 13
License:	Distributable
URL:		http://sourceforge.jp/projects/mplus-fonts/
Group:		System/Fonts/True type


# Original Kochi fonts include in ascii section non free glyphs, they must
# be removed. Red Hat did it, packages taken from them 

## Original fonts is here
Source0:	%{name}-%{version}.tar.bz2

BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	mkfontscale
Obsoletes:	xtt-fonts
Provides:	xtt-fonts

%description
This Package provides Free Japanese TrueType fonts (alternative Kochi fonts:
kochi-gothic-subst, kochi-mincho-subst)


%prep
%setup -q

%build
tar xfj docs.tar.bz2

%install
rm -fr %buildroot
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/japanese-extra
install -m 755 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/japanese-extra

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/ttf/japanese-extra \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-japanese-extra:pri=50

cd %buildroot/%_datadir/fonts/ttf/japanese-extra/
mkfontscale
cp fonts.scale fonts.dir
cd -

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc COPYING  Changelog  README.ja docs/*
%dir %_datadir/fonts/ttf/japanese-extra/
%config(noreplace) %_datadir/fonts/ttf/japanese-extra/fonts.dir
%config(noreplace) %_datadir/fonts/ttf/japanese-extra/fonts.scale
%_datadir/fonts/ttf/japanese-extra/kochi*
%_sysconfdir/X11/fontpath.d/ttf-japanese-extra:pri=50

