Summary: Graphical dvd9 to dvd5 converter
Name: dvd95
Version: 1.6p0
Release: 7%{?dist}
License: GPL+
Group: Applications/Archiving
URL: http://dvd95.sourceforge.net/
Source: http://downloads.sf.net/dvd95/dvd95-%{version}.tar.gz
Patch0: dvd95-1.6p0-desktop.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mplayer
Requires: mencoder
Requires: ffmpeg
BuildRequires: libdvdread-devel >= 0.9.7
BuildRequires: libgnomeui-devel
BuildRequires: mpeg2dec-devel
BuildRequires: mplayer
BuildRequires: mencoder
BuildRequires: ffmpeg
BuildRequires: intltool
# Needed, otherwise translations don't work and the program starts in French
BuildRequires: gettext

%description
DVD95 is a GNOME application to convert DVD9 (8.5G) to DVD5 (4.7G).

It needs no additional packages, an onboard version of vamps and dvdauthor
is used, to be as fast as possible. Interface is pretty simple yo use.
Shrinking factor may be computed for best results, or an adaptive
compression ratio method may be used.

Dvd can be converted to a file tree or an ISO file. The result can be played
with xine, vlc, or mplayer or burned using third party software (k3b).

DVD95 support two copy modes :
 - Without menus, one video title set, multiple audio and subtitles.
 - With menus, one video title set, multiple audio and subtitles.


%prep
%setup -q
%patch0 -p1 -b .desktop


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}"
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/dvd95
%{_datadir}/applications/dvd95.desktop
%{_datadir}/pixmaps/dvd95/


%changelog
* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.6p0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.6p0-6
- Rebuilt for x264/FFmpeg

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.6p0-5
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.6p0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 21 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.6p0-3
- rebuilt

* Thu Aug 12 2010 Matthias Saou <http://freshrpms.net/> 1.6p0-2
- Fix desktop file (#889).

* Wed Aug 11 2010 Matthias Saou <http://freshrpms.net/> 1.6p0-1
- Update to 1.6p0 (#1332).
- Add new (build)requirements : mplayer, mencoder, ffmpeg.

* Wed Jul 10 2009 Matthias Saou <http://freshrpms.net/> 1.5p2-1
- Update to 1.5p2.

* Mon Apr 14 2009 Matthias Saou <http://freshrpms.net/> 1.5p0-1
- Update to 1.5p0 (#546).

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.4p0-4
- rebuild for new F11 features

* Wed Nov 19 2008 Matthias Saou <http://freshrpms.net/> 1.4p0-3
- Update license tag.
- Add gettext build requirement to get english by default (#114).

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.4p0-2
- rebuild for RPM Fusion

* Mon Aug 11 2008 Matthias Saou <http://freshrpms.net/> 1.4p0-1
- Update to 1.4p0.

* Sun May 11 2008 Matthias Saou <http://freshrpms.net/> 1.3p2-1
- Update to 1.3p2.

* Tue Jan  1 2008 Matthias Saou <http://freshrpms.net/> 1.3p1-1
- Update to 1.3p1.
- Replace gtk2-devel with proper libgnomeui-devel build requirement.
- Add missing mpeg2dec-devel build requiremnt.
- Remove empty NEWS file.

* Fri Mar 30 2007 Dag Wieers <dag@wieers.com> - 1.2p0-1
- Initial package. (using DAR)

