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



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.20040217-13mdv2011.0
+ Revision: 675571
- br fontconfig for fc-query used in new rpm-setup-build

* Mon Dec 06 2010 Funda Wang <fwang@mandriva.org> 0.20040217-12mdv2011.0
+ Revision: 611718
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.20040217-11mdv2010.1
+ Revision: 494144
- fc-cache is now called by an rpm filetrigger

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.20040217-10mdv2010.0
+ Revision: 428846
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.20040217-9mdv2009.0
+ Revision: 245259
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.20040217-7mdv2008.1
+ Revision: 170837
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.20040217-6mdv2008.0
+ Revision: 48743
- fontpath.d conversion (#31756)
- minor cleanups

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 0.20040217-5mdv2008.0
+ Revision: 43075
- use %%mkrel


* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 0.20040217-4mdk
- Don't package fontconfig cache file
- Fix prereq

* Sun Jun 27 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.20040217-3mdk
- rename (this is the old fonts-ttf-japanese-0.20040217-2mdk)

* Mon Apr 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.20040217-2mdk
- fix buildrequires
- don't use () around commands, it will make rpm-build not exit on errors within the braces
- don't list files twice

* Wed Feb 18 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.20020727-4mdk
- from UTUMI Hirosi <utuhiro78@yahoo.co.jp>: initial build
  (old Kochis have license problems. This is a package of "alternative" Kochis)

* Fri Jul 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.20020727-4mdk
- rebuild
- fix obsolete-not-provided (rpmlint)

* Tue Feb 18 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 0.2.20020727-3mdk
- proper use of fc-cache

