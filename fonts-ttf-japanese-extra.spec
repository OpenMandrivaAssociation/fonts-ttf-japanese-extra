Summary:	Free Japanese TrueType fonts
Name:		fonts-ttf-japanese-extra
Version:	0.20040217
Release:	%mkrel 6
License:	Distributable
URL:		http://sourceforge.jp/projects/mplus-fonts/
Group:		System/Fonts/True type


# Original Kochi fonts include in ascii section non free glyphs, they must
# be removed. Red Hat did it, packages taken from them 

## Original fonts is here
Source0:	%{name}-%{version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	freetype-tools
Obsoletes:	xtt-fonts
Provides:	xtt-fonts
Requires(post): fontconfig
Requires(postun): fontconfig

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
/usr/sbin/ttmkfdir > fonts.scale
cp fonts.scale fonts.dir
cd -

%post
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 
fi

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

