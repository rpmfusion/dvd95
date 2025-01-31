Summary: Graphical dvd9 to dvd5 converter
Name: dvd95
Version: 1.7p0
Release: 21%{?dist}
License: GPL-2.0-or-later
URL: http://dvd95.sourceforge.net/
Source: https://sourceforge.net/code-snapshots/git/d/dv/dvd95/code.git/dvd95-code-01dd592f7a8352d61fd5d8faa75463ebfd954980.zip
Patch0: dvd95-1.6p0-desktop.patch
Patch1: dvd95-hardening.patch
Patch2: dvd95-format-security.patch
# Patch for c99 confirmant, fix for
# -Werror=implicit-function-declaration, -Werror=incompatible-pointer-types
Patch3: dvd95-include-type-cat-c99.patch
# Patch for C23 strict function prototype
Patch4: dvd95-c23-function-prototype.patch
# Patch for C23 to avoid bool keyword
Patch5: dvd95-c23-avoid-bool-keyword.patch

Requires: mplayer
Requires: mencoder
Requires: ffmpeg

BuildRequires: desktop-file-utils
BuildRequires: libdvdread-devel >= 0.9.7
BuildRequires: libgnomeui-devel
BuildRequires: libmpeg2-devel
BuildRequires: mplayer
BuildRequires: mencoder
BuildRequires: ffmpeg
BuildRequires: intltool libtool
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
%setup -q -n dvd95-code-01dd592f7a8352d61fd5d8faa75463ebfd954980
%patch -P0 -p1 -b .desktop
%patch -P1 -p1 -b .hardening
%patch -P2 -p1 -b .format-security
%patch -P3 -p1 -b .c99
%patch -P4 -p1 -b .c23_proto
%patch -P5 -p1 -b .c23_bool
autoreconf -i

%build
%configure
%make_build


%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/dvd95.desktop
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/dvd95
%{_datadir}/applications/dvd95.desktop
%{_datadir}/pixmaps/dvd95/


%changelog
* Fri Jan 31 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7p0-21
- Support C23 strict function prototype
- Support C23, remove bool keyword usage

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.7p0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 16 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7p0-19
- Fix FTBFS with c99, -Werror=implicit-function-declaration
  -Werror=incompatible-pointer-types

* Thu Aug 01 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.7p0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.7p0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.7p0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.7p0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.7p0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7p0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7p0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Leigh Scott <leigh123linux@gmail.com> - 1.7p0-11
- Rebuild for new libdvdread

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7p0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7p0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.7p0-8
- rebuild for libdvdread ABI bump

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7p0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7p0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.7p0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.7p0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.7p0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.7p0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 10 2016 Sérgio Basto <sergio@serjux.com> - 1.7p0-1
- Update dvd95 to 1.7p0 last git version

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

* Fri Jul 10 2009 Matthias Saou <http://freshrpms.net/> 1.5p2-1
- Update to 1.5p2.

* Tue Apr 14 2009 Matthias Saou <http://freshrpms.net/> 1.5p0-1
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

