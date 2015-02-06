Summary: New mail notification utility
Name: kbiff
Version: 4.0
Release: 2
Source0: http://prdownloads.sourceforge.net/kbiff/%{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/KDE
Url: http://www.kbiff.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: kdelibs4-devel

%description
KBiff is a "biff", or new mail notification utility. It is highly configurable
but very easy to use and set up. It tries to combine the best of the features
of most of the "other" biff programs out there. KBiff supports all major
mailbox formats: mbox (Berkely style), maildir, mh, POP3, IMAP4 and NNTP.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %name --with-html

%clean
rm -fr %buildroot

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_libdir/*.so
%_kde_applicationsdir/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*
%_kde_mandir/man1/*.1*


%changelog
* Tue Mar 22 2011 Funda Wang <fwang@mandriva.org> 4.0-1mdv2011.0
+ Revision: 647500
- new version 4.0
- Created package structure for kbiff.



* Mon Aug 28 2006 Laurent MONTEL <lmontel@mandriva.com> 3.8-2mdk
- xdg menu

* Mon Oct 17 2005 Laurent MONTEL <lmontel@mandriva.com> 3.8-1mdk
- 3.8.0

* Mon Jul 12 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.7.1-4mdk
- Fix File section

* Fri Jul 08 2005 Laurent MONTEL <lmontel@mandriva.com> 3.7.1-3mdk
- Rebuild

* Wed May 04 2005 Laurent MONTEL <lmontel@mandriva.com> 3.7.1-2mdk
- Fix build under x86_64

* Fri Jun 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.7.1-1mdk
- 3.7.1

* Fri Jun  4 2004  <lmontel@n2.mandrakesoft.com> 3.7-3mdk
- Rebuild

* Mon Feb 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.7-2mdk
- Rebuild

* Wed Nov 12 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 3.7-1mdk
- 3.7

* Thu Jul 17 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 3.6.3-3mdk
- Rebuild

* Thu Jun 05 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 3.6.3-2mdk
- cross compile
- configure with libdir, mandir, xinerama, fpic, gnu-ld
- rm -rf $RPM_BUILD_ROOT in %%install
- use %%makeinstall_std macro
- actually build in %%build stage

* Fri Nov 08 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.6.3-1mdk
- 3.6.3

* Sun Nov 03 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.6.2-1mdk
- 3.6.2

* Wed Aug 14 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.6.1-4mdk
- Rebuild against gcc-3.2

* Sat Jul 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.6.1-3mdk
- Rebuild against gcc-3.2

* Sat Jun 01 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.6.1-2mdk
- Rebuild

* Thu May 23 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.6.1-1mdk
- Update code for kde3.0

* Sat Jan 05 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.5.4-3mdk
- Add missing files
- Make rpmlint happy

* Wed Jan 2 2002 Stefan van der Eijk <stefan@eijk.nu> 3.5.4-2mdk
- BuildRequires: arts

* Fri Nov 09 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.5.4-1mdk
- Update code (3.5.4)

* Mon Nov  5 2001 Stefan van der Eijk <stefan@eijk.nu> 3.5.2-2mdk
- BuildRequires revisited

* Wed Oct 24 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.5.2-1mdk
- Update code (3.5.2)

* Fri Oct 19 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.5.1-1mdk
- Update code (3.5.1)

* Thu Sep 18 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.5-1mdk
- Update code (3.5)

* Thu Sep 12 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.2-2mdk
- Rebuild

* Tue May 22 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.2-1mdk
- Update code (3.4.2)

* Tue Apr 10 2001 David BAUDENS <baudens@mandrakesoft.com> 3.4-4mdk
- Move KDE menu entry in %%_datadir/applnk
- Use more macro
- Don't delete usefull links for documentation
- Rebuild against latest GCC

* Sat Mar 31 2001 David BAUDENS <baudens@mandrakesoft.com> 3.4-3mdk
- Fix BuildRequires for non %%ix86 architectures

* Wed Mar 28 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4-2mdk
- Add build requires

* Tue Mar 27 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4-1mdk
- Update code

* Fri Mar 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- Update code

* Wed Mar 14 2001 David BAUDENS <baudens@mandrakesoft.com> 3.3.1-2mdk
- Rebuild agains Qt 2.3.0

* Thu Jan 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- Update code

* Thu Dec 07 2000 Laurent Montel <lmontel@mandrakesoft.com> 3.3-2mdk
- Fix package

* Mon Nov 22 2000 Laurent Montel <lmontel@mandrakesoft.com> 3.3-1mdk
- Initial package fix compile with gcc-2.96
