Summary: New mail notification utility
Name: kbiff
Version: 4.0
Release: %mkrel 1
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
