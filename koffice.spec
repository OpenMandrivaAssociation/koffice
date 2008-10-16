%define _requires_exceptions devel\(libtwopigen\)\\|devel\(libgvrender\)\\|devel\(libcdt\)\\|devel\(libdotgen\)\\|devel\(libcommon\)\\|devel\(libpathplan\)\\|devel\(libneatogen\)\\|devel\(libcircogen\)\\|devel\(libgraph\)\\|devel\(libdotneato\)\\|devel\(libfdpgen\)\\|devel\(libpack\)

%define lib_name_orig %mklibname koffice2
%define lib_major 2
%define lib_name %lib_name_orig%lib_major
%define lib_name_orig_kexi %mklibname kexi
%define lib_major_kexi 0
%define lib_name_kexi %mklibname kexi %lib_major_kexi

%define use_python 1
%define compile_apidox 0

Name: koffice
URL: http://www.koffice.org/
Summary: Set of office applications for KDE
Version: 1.9.98.1
Release: %mkrel 2
Epoch: 11
Source: %name-%version.tar.bz2
Patch1: koffice-1.9.95.4-disable-gmagick.patch
Patch2: koffice-1.9.95.8-fix-desktopfiles.patch
Group: Office
License: GPL
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: lcms-devel
BuildRequires: qca2-devel
BuildRequires: libwpd-devel
BuildRequires: libOpenEXR-devel
BuildRequires: libexif-devel
BuildRequires: libexiv-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libxslt-devel
BuildRequires: libxml2-utils
BuildRequires: boost-devel
BuildRequires: libpoppler-qt4-devel
BuildRequires: libjbig-devel
BuildRequires: libxml2-devel >= 2.4.28-2mdk
BuildRequires: python-devel
BuildRequires: readline-devel
BuildRequires: libpqxx-devel
BuildRequires: postgresql-devel
BuildRequires: eigen2
BuildRequires: pstoedit
BuildRequires: mysql-devel
BuildRequires: jpeg-devel
BuildRequires: qimageblitz-devel
BuildRequires: gsl-devel
BuildRequires: qca2-devel
BuildRequires: glpk-devel
BuildRequires: mesaglut-devel
BuildRequires: glew-devel
#BuildRequires: GraphicsMagick-devel
BuildRequires: mysql-static-devel
BuildRequires: kdegraphics4-devel
BuildRequires: libtiff-devel
BuildRequires: wv2-devel
BuildRequires: getfem++
BuildRequires: xbase-devel
BuildRequires: ctemplate-devel
BuildRequires: freetds-devel
%if %compile_apidox
BuildRequires: doxygen, graphviz
%endif

Requires: kword
Requires: kspread
Requires: karbon
Requires: kugar
Requires: kpresenter
#Requires: kivio
#Requires: kformula
Requires: koshell
#Requires: kexi
Requires: krita
Requires: kplato
Requires: kchart

%description
Office applications for the K Desktop Environment.

KOffice contains:
   * KWord: word processor
   * KSpread: spreadsheet
   * KPresenter: presentations
   * KChart: diagram generator
   * Kugar: A tool for generating business quality reports.
   * Kivio: A Visio(r)-style flowcharting application.
   * Kexi: an integrated environment for managing data
   * Some filters (Excel 97, Winword 97/2000, etc.)
   * karbon: the scalable vector drawing application for KDE.
   * kformula:  a formula editor for KOffice.
   * krita: painting and image editing application.
   * koshell
   * kplato: a project management.

%files

#--------------------------------------------------------------------

%package core
Group: Office
Summary: Set of office applications for KDE
Requires: wordnet
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: %{_lib}kopainter5 < 1.9.95-0.738034.1
Obsoletes: koffice2-core <= 11:1.9.95.3-0.766453.5
Obsoletes: koffice-common < 11:1.6.3-20
Provides: koffice2-core = %epoch:%version-%release
Conflicts: koffice-kspread < 11:1.6.3-20
Conflicts: koffice-kpresenter < 11:1.6.3-20
Conflicts: koffice-karbon < 11:1.6.3-20
Conflicts: koffice-kchart < 11:1.6.3-20
Conflicts: koffice-kword < 11:1.6.3-20
Requires: kdebase4-runtime

%description core
Common files for Koffice

%files core
%defattr(-,root,root)
%_kde_datadir/applications/kde4/koffice.desktop

%_kde_datadir/kde4/services/spellcheck.desktop
%_kde_libdir/kde4/kofficesimpletextedit.so
%_kde_libdir/kde4/spellcheck.so
%_kde_libdir/kde4/libkarbonsvgimport.so

%_kde_appsdir/koffice/icons/*/*/*/*
%_kde_appsdir/koffice/icons/*.png
#%_kde_iconsdir/hicolor/*/actions/abs.png
#%_kde_iconsdir/hicolor/*/actions/brackets.png
#%_kde_iconsdir/hicolor/*/actions/frac.png
#%_kde_iconsdir/hicolor/*/actions/gsub.png
#%_kde_iconsdir/hicolor/*/actions/gsup.png
#%_kde_iconsdir/hicolor/*/actions/int.png
#%_kde_iconsdir/hicolor/*/actions/lsub.png
#%_kde_iconsdir/hicolor/*/actions/lsup.png
#%_kde_iconsdir/hicolor/*/actions/matrix.png
#%_kde_iconsdir/hicolor/*/actions/multiline.png
#%_kde_iconsdir/hicolor/*/actions/onetwomatrix.png
#%_kde_iconsdir/hicolor/*/actions/over.png
#%_kde_iconsdir/hicolor/*/actions/paren.png
#%_kde_iconsdir/hicolor/*/actions/prod.png
#%_kde_iconsdir/hicolor/*/actions/rsub.png
#%_kde_iconsdir/hicolor/*/actions/rsup.png
#%_kde_iconsdir/hicolor/*/actions/sqrt.png
#%_kde_iconsdir/hicolor/*/actions/sum.png
#%_kde_iconsdir/hicolor/*/actions/under.png
#%_kde_iconsdir/hicolor/22x22/actions/inscol.png
#%_kde_iconsdir/hicolor/22x22/actions/insrow.png
#%_kde_iconsdir/hicolor/22x22/actions/remcol.png
#%_kde_iconsdir/hicolor/22x22/actions/remrow.png
%_kde_iconsdir/hicolor/*/mimetypes/*
%_kde_iconsdir/oxygen/*/actions/table.*
%_kde_iconsdir/oxygen/22x22/actions/aoleft.png
%_kde_iconsdir/oxygen/22x22/actions/object-arrange-back.png
%_kde_iconsdir/oxygen/22x22/actions/object-arrange-front.png
%_kde_iconsdir/oxygen/22x22/actions/object-arrange-lower.png
%_kde_iconsdir/oxygen/22x22/actions/object-arrange-raise.png
%_kde_iconsdir/oxygen/32x32/actions/shape-choose.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-chart.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-connection.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-formula.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-image.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-text.png
%_kde_appsdir/koffice

%_kde_datadir/kde4/services/ServiceMenus/kchart_konqi.desktop
%_kde_appsdir/musicshape
%_kde_datadir/kde4/services/autocorrect.desktop
%_kde_datadir/kde4/services/changecase.desktop
%_kde_datadir/kde4/services/clipartthumbnail.desktop
%_kde_datadir/kde4/services/defaulttools.desktop
%_kde_datadir/kde4/services/divineproportionshape.desktop
%_kde_datadir/kde4/services/generic_filter.desktop
#%_kde_datadir/kde4/services/kformdesigner/kformdesigner_containers.desktop
#%_kde_datadir/kde4/services/kformdesigner/kformdesigner_stdwidgets.desktop
%_kde_datadir/kde4/services/kodocinfopropspage.desktop
%_kde_datadir/kde4/services/koffice_graya_u16_plugin.desktop
%_kde_datadir/kde4/services/kofficedockers.desktop
%_kde_datadir/kde4/services/kofficegrayaplugin.desktop
%_kde_datadir/kde4/services/kofficethumbnail.desktop
%_kde_datadir/kde4/services/kounavail.desktop
%_kde_datadir/kde4/services/musicshape.desktop
%_kde_datadir/kde4/services/pathshapes.desktop
%_kde_datadir/kde4/services/pictureshape.desktop
%_kde_datadir/kde4/services/textshape.desktop
%_kde_datadir/kde4/services/textvariables.desktop
%_kde_datadir/kde4/services/kofficesimpletextedit.desktop
%_kde_datadir/kde4/services/artistictextshape.desktop
%_kde_datadir/kde4/services/Filterkpr2odf.desktop
%_kde_datadir/kde4/services/paragraphtool.desktop
%_kde_datadir/kde4/services/kopabackgroundtool.desktop
%_kde_datadir/kde4/servicetypes/scripteventaction.desktop
%_kde_datadir/kde4/servicetypes/flakedevice.desktop
%_kde_datadir/kde4/servicetypes/pigmentextension.desktop
%_kde_datadir/kde4/servicetypes/flake.desktop
%_kde_datadir/kde4/servicetypes/flakeshape.desktop
%_kde_datadir/kde4/servicetypes/flaketool.desktop
%_kde_datadir/kde4/servicetypes/inlinetextobject.desktop
%_kde_datadir/kde4/servicetypes/kochart.desktop
%_kde_datadir/kde4/servicetypes/kofficedocker.desktop
%_kde_datadir/kde4/servicetypes/kofficepart.desktop
%_kde_datadir/kde4/servicetypes/kofilter.desktop
%_kde_datadir/kde4/servicetypes/kofilterwrapper.desktop
%_kde_datadir/kde4/servicetypes/koplugin.desktop
%_kde_datadir/kde4/servicetypes/texteditingplugin.desktop
#%_kde_datadir/kde4/servicetypes/widgetfactory.desktop
%_kde_datadir/kde4/servicetypes/textvariableplugin.desktop
%_kde_datadir/templates/.source/Presentation.kpt
%_kde_datadir/templates/.source/SpreadSheet.kst
%_kde_datadir/templates/.source/TextDocument.kwt
%_kde_datadir/templates/Illustration.desktop
%_kde_datadir/templates/Presentation.desktop
%_kde_datadir/templates/SpreadSheet.desktop
%_kde_datadir/templates/TextDocument.desktop

%_kde_libdir/kde4/autocorrect.so
%_kde_libdir/kde4/libasciiexport.so
%_kde_libdir/kde4/libasciiimport.so
%_kde_libdir/kde4/changecase.so
%_kde_libdir/kde4/clipartthumbnail.so
%_kde_libdir/kde4/defaulttools.so
%_kde_libdir/kde4/divineproportionshape.so
#%_kde_libdir/kde4/formulashape.so
#%_kde_libdir/kde4/kformdesigner_containers.so
#%_kde_libdir/kde4/kformdesigner_stdwidgets.so
%_kde_libdir/kde4/kodocinfopropspage.so
%_kde_libdir/kde4/koffice_graya_u16_plugin.so
%_kde_libdir/kde4/kofficedockers.so
%_kde_libdir/kde4/kofficegrayau8plugin.so
%_kde_libdir/kde4/kofficescan.so
%_kde_libdir/kde4/kofficethumbnail.so
%_kde_libdir/kde4/libabiwordexport.so
%_kde_libdir/kde4/musicshape.so
%_kde_libdir/kde4/pathshapes.so
%_kde_libdir/kde4/pictureshape.so
%_kde_libdir/kde4/textshape.so
%_kde_libdir/kde4/textvariables.so
%_kde_libdir/kde4/libmswordimport.so
%_kde_libdir/kde4/artistictextshape.so
%_kde_libdir/kde4/libFilterkpr2odf.so
%_kde_libdir/kde4/libmswordodf_import.so
%_kde_libdir/kde4/paragraphtool.so
%_kde_libdir/kde4/kopabackgroundtool.so

%_kde_bindir/kthesaurus
%_kde_datadir/applications/kde4/KThesaurus.desktop
%_kde_datadir/kde4/services/thesaurustool.desktop
%_kde_datadir/apps/koffice/thesaurus/thesaurus.txt
%_kde_libdir/kde4/thesaurustool.so
%_kde_libdir/libkdeinit4_kthesaurus.so

%_kde_bindir/koconverter

%_kde_docdir/HTML/en/kchart

%_kde_docdir/HTML/en/koffice

%_kde_docdir/HTML/en/thesaurus

#--------------------------------------------------------------------

%define libkoguiutils_major 5
%define libkoguiutils %mklibname koguiutils %libkoguiutils_major

%package -n %libkoguiutils
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkoguiutils
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkoguiutils -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkoguiutils -p /sbin/ldconfig
%endif

%files -n %libkoguiutils
%defattr(-,root,root)
%_kde_libdir/libkoguiutils.so.%libkoguiutils_major
%_kde_libdir/libkoguiutils.so.%libkoguiutils_major.0.0

#--------------------------------------------------------------------

%define libkokross_major 5
%define libkokross %mklibname kokross %libkokross_major

%package -n %libkokross
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkokross
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkokross -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkokross -p /sbin/ldconfig
%endif

%files -n %libkokross
%defattr(-,root,root)
%_kde_libdir/libkokross.so.%libkokross_major
%_kde_libdir/libkokross.so.%libkokross_major.0.0

#--------------------------------------------------------------------

%define libkomain_major 5
%define libkomain %mklibname komain %libkomain_major

%package -n %libkomain
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkomain
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkomain -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkomain -p /sbin/ldconfig
%endif

%files -n %libkomain
%defattr(-,root,root)
%_kde_libdir/libkomain.so.%libkomain_major
%_kde_libdir/libkomain.so.%libkomain_major.0.0

#--------------------------------------------------------------------

%define libkopageapp_major 5
%define libkopageapp %mklibname kopageapp %libkopageapp_major

%package -n %libkopageapp
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkopageapp
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkopageapp -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopageapp -p /sbin/ldconfig
%endif

%files -n %libkopageapp
%defattr(-,root,root)
%_kde_libdir/libkopageapp.so.%libkopageapp_major
%_kde_libdir/libkopageapp.so.%libkopageapp_major.0.0

#--------------------------------------------------------------------
%if 0
%define libkoproperty_major 5
%define libkoproperty %mklibname koproperty %libkoproperty_major

%package -n %libkoproperty
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkoproperty
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkoproperty -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkoproperty -p /sbin/ldconfig
%endif

%files -n %libkoproperty
%defattr(-,root,root)
%_kde_libdir/libkoproperty.so.%libkoproperty_major
%_kde_libdir/libkoproperty.so.%libkoproperty_major.0.0
%endif
#--------------------------------------------------------------------

%define libkoresources_major 5
%define libkoresources %mklibname koresources %libkoresources_major

%package -n %libkoresources
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkoresources
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkoresources -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkoresources -p /sbin/ldconfig
%endif

%files -n %libkoresources
%defattr(-,root,root)
%_kde_libdir/libkoresources.so.%libkoresources_major
%_kde_libdir/libkoresources.so.%libkoresources_major.0.0

#--------------------------------------------------------------------

%define libkotext_major 5
%define libkotext %mklibname kotext %libkotext_major

%package -n %libkotext
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkotext
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkotext -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkotext -p /sbin/ldconfig
%endif

%files -n %libkotext
%defattr(-,root,root)
%_kde_libdir/libkotext.so.%libkotext_major
%_kde_libdir/libkotext.so.%libkotext_major.0.0

#--------------------------------------------------------------------

%define libkowmf_major 5
%define libkowmf %mklibname kowmf %libkowmf_major

%package -n %libkowmf
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkowmf
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkowmf -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkowmf -p /sbin/ldconfig
%endif

%files -n %libkowmf
%defattr(-,root,root)
%_kde_libdir/libkowmf.so.%libkowmf_major
%_kde_libdir/libkowmf.so.%libkowmf_major.0.0

#--------------------------------------------------------------------

%define libkoodf_major 5
%define libkoodf %mklibname koodf %libkoodf_major

%package -n %libkoodf
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkoodf
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkoodf -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkoodf -p /sbin/ldconfig
%endif

%files -n %libkoodf
%defattr(-,root,root)
%_kde_libdir/libkoodf.so.%libkoodf_major
%_kde_libdir/libkoodf.so.%libkoodf_major.0.0

#--------------------------------------------------------------------

%define libkostore_major 5
%define libkostore %mklibname kostore %libkostore_major

%package -n %libkostore
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkostore
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkostore -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkostore -p /sbin/ldconfig
%endif

%files -n %libkostore
%defattr(-,root,root)
%_kde_libdir/libkostore.so.%libkostore_major
%_kde_libdir/libkostore.so.%libkostore_major.0.0

#--------------------------------------------------------------------

%define libkwmf_major 5
%define libkwmf %mklibname kwmf %libkwmf_major

%package -n %libkwmf
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkwmf
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkwmf -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkwmf -p /sbin/ldconfig
%endif

%files -n %libkwmf
%defattr(-,root,root)
%_kde_libdir/libkwmf.so.%libkwmf_major
%_kde_libdir/libkwmf.so.%libkwmf_major.0.0

#--------------------------------------------------------------------

%define libflake_major 5
%define libflake %mklibname flake %libflake_major

%package -n %libflake
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libflake
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libflake -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libflake -p /sbin/ldconfig
%endif

%files -n %libflake
%defattr(-,root,root)
%_kde_libdir/libflake.so.%libflake_major
%_kde_libdir/libflake.so.%libflake_major.0.0

#--------------------------------------------------------------------
%define libpigmentcms_major 5
%define libpigmentcms %mklibname pigmentcms %libpigmentcms_major

%package -n %libpigmentcms
Summary: Koffice 2 core library
Group: System/Libraries
Obsoletes:   %{_lib}libpigmentpigment1 < 1:1.9.95.3-0.766453.1
Obsoletes:   %{_lib}libpigmentcms1 < 1:1.9.95.3-0.766453.1
Obsoletes:   %{_lib}libpigmentcms1 < 1:1.9.95.3-0.766453.1

%description -n %libpigmentcms
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libpigmentcms -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libpigmentcms -p /sbin/ldconfig
%endif

%files -n %libpigmentcms
%defattr(-,root,root)
%_kde_libdir/libpigmentcms.so.%libpigmentcms_major
%_kde_libdir/libpigmentcms.so.%libpigmentcms_major.0.0

#--------------------------------------------------------------------
%if 0
%define libkformdesigner_major 5
%define libkformdesigner %mklibname kformdesigner %libkformdesigner_major

%package -n %libkformdesigner
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkformdesigner
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkformdesigner -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkformdesigner -p /sbin/ldconfig
%endif

%files -n %libkformdesigner
%defattr(-,root,root)
%_kde_libdir/libkformdesigner.so.%libkformdesigner_major
%_kde_libdir/libkformdesigner.so.%libkformdesigner_major.0.0
%endif
#--------------------------------------------------------------------

%define libkochart_major 5
%define libkochart %mklibname kochart %libkochart_major

%package -n %libkochart
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkochart
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkochart -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkochart -p /sbin/ldconfig
%endif

%files -n %libkochart
%defattr(-,root,root)
%_kde_libdir/libkochart.so.%libkochart_major
%_kde_libdir/libkochart.so.%libkochart_major.0.0

#--------------------------------------------------------------------

%define libkoffice_graya_u16_major 5
%define libkoffice_graya_u16 %mklibname koffice_graya_u16 %libkoffice_graya_u16_major

%package -n %libkoffice_graya_u16
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkoffice_graya_u16
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkoffice_graya_u16 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkoffice_graya_u16 -p /sbin/ldconfig
%endif

%files -n %libkoffice_graya_u16
%defattr(-,root,root)
%_kde_libdir/libkoffice_graya_u16.so.%libkoffice_graya_u16_major
%_kde_libdir/libkoffice_graya_u16.so.%libkoffice_graya_u16_major.0.0

#--------------------------------------------------------------------

%define libkofficegrayau8colorspace_major 5
%define libkofficegrayau8colorspace %mklibname kofficegrayau8colorspace %libkofficegrayau8colorspace_major

%package -n %libkofficegrayau8colorspace
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkofficegrayau8colorspace
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkofficegrayau8colorspace -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkofficegrayau8colorspace -p /sbin/ldconfig
%endif

%files -n %libkofficegrayau8colorspace
%defattr(-,root,root)
%_kde_libdir/libkofficegrayau8colorspace.so.%libkofficegrayau8colorspace_major
%_kde_libdir/libkofficegrayau8colorspace.so.%libkofficegrayau8colorspace_major.0.0

#--------------------------------------------------------------------

%package      devel
Group:		Development/KDE and Qt
Summary:	Header files for developing koffice2 applications
Requires:       %name-core = %{epoch}:%{version}-%{release}
Provides:       %name-devel = %{epoch}:%{version}-%{release}
Obsoletes:	%lib_name-devel
Conflicts:      koffice2-kchart < 1.9.95-0.738534.3
Conflicts:	karbon < 11:1.9.95.8-3
Conflicts:	kchart < 11:1.9.95.8-3
Conflicts:	kformula < 11:1.9.95.8-3
Conflicts:	kivio < 11:1.9.95.8-3
Conflicts:	kplato < 11:1.9.95.8-3
Conflicts:	kpresenter < 11:1.9.95.8-3
Conflicts:	krita < 11:1.9.95.8-3
Conflicts:	kspread < 11:1.9.95.8-3
Conflicts:	koffice-core < 11:1.9.95.8-3
Conflicts:	kword < 11:1.9.95.8-3
Obsoletes:      koffice2-devel < 1:1.9.95.3-0.766453.6
Provides:       koffice2-devel = %epoch:%version-%release

%description devel
Header files needed for developing koffice2 applications.

%if %mdkversion < 200900
%post devel -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun devel -p /sbin/ldconfig
%endif

%files devel
%defattr(-,root,root)
%_kde_appsdir/cmake/*/*
%_kde_includedir/*
%_kde_libdir/libchartshapelib.so
%_kde_libdir/libflake.so
%_kde_libdir/libkarboncommon.so
%_kde_libdir/libkarbonui.so
%_kde_libdir/libkchartcommon.so
%_kde_libdir/libkdchart.so
#%_kde_libdir/libkexicore.so
#%_kde_libdir/libkexidatatable.so
#%_kde_libdir/libkexidb.so
#%_kde_libdir/libkexiextendedwidgets.so
#%_kde_libdir/libkexiformutils.so
#%_kde_libdir/libkexiguiutils.so
#%_kde_libdir/libkeximain.so
#%_kde_libdir/libkeximigrate.so
#%_kde_libdir/libkexirelationsview.so
#%_kde_libdir/libkexisql3.so
#%_kde_libdir/libkexiutils.so
#%_kde_libdir/libkformdesigner.so
#%_kde_libdir/libkformulalib.so
#%_kde_libdir/libkformulaprivate.so
%_kde_libdir/libkisexiv2.so
#%_kde_libdir/libkivioprivate.so
%_kde_libdir/libkochart.so
%_kde_libdir/libkoffice_graya_u16.so
%_kde_libdir/libkofficegrayau8colorspace.so
%_kde_libdir/libkoguiutils.so
%_kde_libdir/libkokross.so
%_kde_libdir/libkomain.so
%_kde_libdir/libkoodf.so
%_kde_libdir/libkopageapp.so
#%_kde_libdir/libkoproperty.so
%_kde_libdir/libkoresources.so
%_kde_libdir/libkotext.so
%_kde_libdir/libkowmf.so
%_kde_libdir/libkplatokernel.so
%_kde_libdir/libkplatomodels.so
%_kde_libdir/libkplatoprivate.so
%_kde_libdir/libkplatoui.so
%_kde_libdir/libkplatoworkapp.so
%_kde_libdir/libkplatoworkfactory.so
%_kde_libdir/libkpresenterprivate.so
%_kde_libdir/libkrita_xyz_u16.so
%_kde_libdir/libkritabasicdynamiccoloringprogram.so
%_kde_libdir/libkritabasicdynamicshapeprogram.so
%_kde_libdir/libkritadynamicbrush.so
%_kde_libdir/libkritagrayscale.so
%_kde_libdir/libkritaimage.so
%_kde_libdir/libkritaui.so
%_kde_libdir/libkrossmodulekrita.so
%_kde_libdir/libkspreadcommon.so
#%_kde_libdir/libkstore.so
%_kde_libdir/libkwmf.so
%_kde_libdir/libkwordexportfilters.so
%_kde_libdir/libkwordprivate.so
%_kde_libdir/libpigmentcms.so
%_kde_libdir/libkostore.so
%_kde_libdir/libkritalibpaintop.so
%_kde_libdir/libKritaRulerAssistantCommon.so

#--------------------------------------------------------------------

%package -n kword
Summary:	Word processor for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Requires:	wordnet
#Requires:       kformula
Provides:	%name-apps
Provides:       kword2
Obsoletes:      %name-kword <= 11:1.9.95.3-0.766453.5
Provides:       %name-kword = %epoch:%version-%release
Obsoletes:      koffice2-kword < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kword = %epoch:%version-%release
Conflicts:	koffice-common < 11:1.6.3-20

%description -n kword
Kword is a word processor for kde project

%post -n kword
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}

%postun -n kword
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{clean_desktop_database}

%files -n kword
%defattr(-,root,root)
%_kde_bindir/kword
%_kde_iconsdir/*/*/apps/kword.png
%_kde_datadir/applications/kde4/kword.desktop
%_kde_datadir/kde4/services/ServiceMenus/kword_konqi.desktop
%_kde_appsdir/kword
%_kde_appsdir/xsltfilter/export/kword/xslfo/*
%_kde_datadir/kde4/services/kword_*
%_kde_datadir/kde4/services/krossmodulekword.desktop
%_kde_datadir/kde4/services/kwordpart.desktop
%_kde_datadir/kde4/services/xslt_export.desktop
%_kde_datadir/kde4/services/xslt_import.desktop
%_kde_datadir/kde4/servicetypes/kwmailmerge.desktop
%_kde_libdir/kde4/krossmodulekword.so
%_kde_libdir/kde4/libkwordkword1dot3import.so
%_kde_libdir/kde4/libkwordpart.so
%_kde_libdir/kde4/libabiwordimport.so
%_kde_libdir/kde4/libamiproexport.so
%_kde_libdir/kde4/libamiproimport.so
%_kde_libdir/kde4/libapplixspreadimport.so
%_kde_libdir/kde4/libapplixwordimport.so
#%_kde_libdir/kde4/libasciiexport.so
#%_kde_libdir/kde4/libasciiimport.so
%_kde_libdir/kde4/libcsvexport.so
%_kde_libdir/kde4/libcsvimport.so
%_kde_libdir/kde4/libdbaseimport.so
%_kde_libdir/kde4/libdocbookexport.so
%_kde_libdir/kde4/libexcelimport.so
%_kde_libdir/kde4/libgenerickofilter.so
%_kde_libdir/kde4/libgnumericexport.so
%_kde_libdir/kde4/libgnumericimport.so
%_kde_libdir/kde4/libhancomwordimport.so
%_kde_libdir/kde4/libhtmlexport.so
%_kde_libdir/kde4/libhtmlimport.so
%_kde_libdir/kde4/libkounavailpart.so
%_kde_libdir/kde4/libmswriteexport.so
%_kde_libdir/kde4/libmswriteimport.so
%_kde_libdir/kde4/liboowriterexport.so
%_kde_libdir/kde4/liboowriterimport.so
%_kde_libdir/kde4/libopencalcexport.so
%_kde_libdir/kde4/libopencalcimport.so
%_kde_libdir/kde4/libpalmdocexport.so
%_kde_libdir/kde4/libpalmdocimport.so
%_kde_libdir/kde4/libqproimport.so
%_kde_libdir/kde4/librtfexport.so
%_kde_libdir/kde4/librtfimport.so
%_kde_libdir/kde4/libwmlexport.so
%_kde_libdir/kde4/libwmlimport.so
%_kde_libdir/kde4/libwpexport.so
%_kde_libdir/kde4/libwpimport.so
%_kde_libdir/kde4/libxsltexport.so
%_kde_libdir/kde4/libxsltimport.so
%_kde_libdir/libkdeinit4_kword.so
%_kde_docdir/HTML/en/kword

#--------------------------------------------------------------------

%define kwordexportfilters_major 5
%define libkwordexportfilters %mklibname kwordexportfilters %kwordexportfilters_major

%package -n %libkwordexportfilters
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkwordexportfilters
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkwordexportfilters -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkwordexportfilters -p /sbin/ldconfig
%endif

%files -n %libkwordexportfilters
%defattr(-,root,root)
%_kde_libdir/libkwordexportfilters.so.%kwordexportfilters_major
%_kde_libdir/libkwordexportfilters.so.%kwordexportfilters_major.0.0

#--------------------------------------------------------------------

%define kwordprivate_major 5
%define libkwordprivate %mklibname kwordprivate %kwordprivate_major

%package -n %libkwordprivate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkwordprivate
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkwordprivate -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkwordprivate -p /sbin/ldconfig
%endif

%files -n %libkwordprivate
%defattr(-,root,root)
%_kde_libdir/libkwordprivate.so.%kwordprivate_major
%_kde_libdir/libkwordprivate.so.%kwordprivate_major.0.0

#--------------------------------------------------------------------

%package -n kplato
Summary:	A new project management application for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Provides:       %name-apps
Provides:       kplato2
Obsoletes:      %{_lib}kplatoworkprivat5 < 1:1.9.95.3-1
Obsoletes:      %name-kplato <= 11:1.9.95.3-0.766453.5
Provides:       %name-kplato = %epoch:%version-%release
Obsoletes:      koffice2-kplato < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kplato = %epoch:%version-%release

%description -n kplato
A new project management application for koffice2.

%post -n kplato
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}

%postun -n kplato
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}


%files -n kplato
%defattr(-,root,root)
%_kde_bindir/kplato
%_kde_bindir/kplatowork
%_kde_datadir/applications/kde4/kplato.desktop
%_kde_datadir/applications/kde4/kplatowork.desktop
%_kde_appsdir/kplato
%_kde_datadir/config/kplatorc
%_kde_libdir/libkdeinit4_kplato.so
%_kde_libdir/kde4/libkplatoworkpart.so
%_kde_libdir/kde4/krossmodulekplato.so
%_kde_libdir/kde4/libkplatopart.so
%_kde_libdir/libkdeinit4_kplatowork.so
%_kde_datadir/kde4/services/kplatopart.desktop
%_kde_datadir/kde4/services/kplatoworkpart.desktop
%_kde_datadir/kde4/services/krossmodulekplato.desktop
%_kde_iconsdir/hicolor/*/*/kplato*.*

%_kde_appsdir/kplatowork

%_kde_docdir/HTML/en/kplato

#--------------------------------------------------------------------

%define chartshapelib_major 5
%define libchartshapelib %mklibname chartshapelib %chartshapelib_major

%package -n %libchartshapelib
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libchartshapelib
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libchartshapelib -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libchartshapelib -p /sbin/ldconfig
%endif

%files -n %libchartshapelib
%defattr(-,root,root)
%_kde_libdir/libchartshapelib.so.%chartshapelib_major
%_kde_libdir/libchartshapelib.so.%chartshapelib_major.0.0


#--------------------------------------------------------------------

%define kplatomodels_major 5
%define  libkplatomodels %mklibname kplatomodels %kplatomodels_major

%package -n %libkplatomodels
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatomodels
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkplatomodels -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkplatomodels -p /sbin/ldconfig
%endif

%files -n %libkplatomodels
%defattr(-,root,root)
%_kde_libdir/libkplatomodels.so.%kplatomodels_major
%_kde_libdir/libkplatomodels.so.%kplatomodels_major.0.0

#-------------------------------------------------------------------

%define  kplatokernel_major 5
%define  libkplatokernel %mklibname kplatokernel %kplatokernel_major

%package -n %libkplatokernel
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatokernel
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkplatokernel -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkplatokernel -p /sbin/ldconfig
%endif

%files -n %libkplatokernel
%defattr(-,root,root)
%_kde_libdir/libkplatokernel.so.%kplatokernel_major
%_kde_libdir/libkplatokernel.so.%kplatokernel_major.0.0

#--------------------------------------------------------------------

%define kplatoprivate_major 5
%define libkplatoprivate %mklibname kplatoprivate %kplatoprivate_major

%package -n %libkplatoprivate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoprivate
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkplatoprivate -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkplatoprivate -p /sbin/ldconfig
%endif

%files -n %libkplatoprivate
%defattr(-,root,root)
%_kde_libdir/libkplatoprivate.so.%kplatoprivate_major
%_kde_libdir/libkplatoprivate.so.%kplatoprivate_major.0.0

#--------------------------------------------------------------------

%define kplatoui_major 5
%define libkplatoui %mklibname kplatoui %kplatoui_major

%package -n %libkplatoui
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoui
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkplatoui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkplatoui -p /sbin/ldconfig
%endif

%files -n %libkplatoui
%defattr(-,root,root)
%_kde_libdir/libkplatoui.so.%kplatoui_major
%_kde_libdir/libkplatoui.so.%kplatoui_major.0.0

#--------------------------------------------------------------------

%define kplatoworkapp_major 5
%define libkplatoworkapp %mklibname kplatoworkapp %kplatoworkapp_major

%package -n %libkplatoworkapp
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoworkapp
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkplatoworkapp -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkplatoworkapp -p /sbin/ldconfig
%endif

%files -n %libkplatoworkapp
%defattr(-,root,root)
%_kde_libdir/libkplatoworkapp.so.%kplatoworkapp_major
%_kde_libdir/libkplatoworkapp.so.%kplatoworkapp_major.0.0

#--------------------------------------------------------------------

%define kplatoworkfactory_major 5
%define libkplatoworkfactory %mklibname kplatoworkfactory %kplatoworkfactory_major

%package -n %libkplatoworkfactory
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoworkfactory
Koffice 2 core library.

%if %mdkversion < 200900
%post -n   %libkplatoworkfactory -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkplatoworkfactory -p /sbin/ldconfig
%endif

%files -n %libkplatoworkfactory
%defattr(-,root,root)
%_kde_libdir/libkplatoworkfactory.so.%kplatoworkfactory_major
%_kde_libdir/libkplatoworkfactory.so.%kplatoworkfactory_major.0.0

#--------------------------------------------------------------------


%package -n kspread
Summary:	SpreadSheet for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Provides:       %name-apps
Provides:       kspread2
Obsoletes:      %name-kspread <= 11:1.9.95.3-0.766453.5
Provides:       %name-kspread = %epoch:%version-%release
Obsoletes:      koffice2-kspread < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kspread = %epoch:%version-%release

%description -n kspread
KSpread is a spreadsheet for kde project

%post -n kspread
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}


%postun -n kspread
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{clean_desktop_database}

%files -n kspread
%defattr(-,root,root)
%_kde_bindir/kspread
%_kde_libdir/kde4/krossmodulekspread.so
%_kde_libdir/kde4/libkspreadhtmlexport.so
#%_kde_libdir/kde4/libkspreadinsertcalendar.so
%_kde_libdir/kde4/libkspreadlatexexport.so
%_kde_libdir/kde4/libkspreadpart.so
%_kde_libdir/kde4/libkspreadsolver.so
%_kde_libdir/kde4/kspread*
%_kde_libdir/kde4/spreadsheetshape.so
%_kde_libdir/libkdeinit4_kspread.so

%_kde_iconsdir/hicolor/*/apps/kspread.png

%_kde_datadir/applications/kde4/kspread.desktop
%_kde_datadir/kde4/services/ServiceMenus/kspread_konqi.desktop
%_kde_appsdir/kspread
%_kde_datadir/config.kcfg/kspread.kcfg
%_kde_docdir/HTML/en/kspread

%_kde_datadir/kde4/services/krossmodulekspread.desktop
%_kde_datadir/kde4/services/kspread*.desktop
%_kde_datadir/kde4/servicetypes/kspread_plugin.desktop
%_kde_datadir/kde4/services/spreadsheetshape.desktop

#--------------------------------------------------------------------

%define kspread_major 5
%define libkspreadcommon %mklibname kspreadcommon %kspread_major

%package -n %libkspreadcommon
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkspreadcommon
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkspreadcommon -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkspreadcommon -p /sbin/ldconfig
%endif

%files -n %libkspreadcommon
%defattr(-,root,root)
%_kde_libdir/libkspreadcommon.so.%kspread_major
%_kde_libdir/libkspreadcommon.so.%kspread_major.0.0

#--------------------------------------------------------------------

%package -n kpresenter
Summary:	Presentation for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
#Requires:       kformula
Requires:	xdg-utils
Provides:       %name-apps
Provides:       kpresenter2
Obsoletes:      %name-kpresenter <= 11:1.9.95.3-0.766453.5
Provides:       %name-kpresenter = %epoch:%version-%release
Obsoletes:      koffice2-kpresenter < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kpresenter = %epoch:%version-%release

%description -n kpresenter
KPresenter is a presentation for kde project.

%post -n kpresenter
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}

%postun -n kpresenter
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{clean_desktop_database}


%files -n kpresenter
%defattr(-,root,root)
%_kde_bindir/kpresenter
%_kde_libdir/kde4/libkpresenterpart.so
%_kde_libdir/kde4/kpr_pageeffect_barwipe.so
%_kde_libdir/kde4/kpr_pageeffect_clockwipe.so
%_kde_libdir/kde4/kpr_pageeffect_edgewipe.so
%_kde_libdir/kde4/kpr_pageeffect_iriswipe.so
%_kde_libdir/kde4/kpr_pageeffect_matrixwipe.so
%_kde_libdir/kde4/kpr_pageeffect_slidewipe.so
%_kde_libdir/kde4/kpr_shapeanimation_example.so
%_kde_libdir/kde4/libpowerpointimport.so
%_kde_libdir/kde4/kpresentereventactions.so 
%_kde_libdir/kde4/kpresentertoolanimation.so
%_kde_libdir/libkdeinit4_kpresenter.so
%_kde_datadir/applications/kde4/kpresenter.desktop
%_kde_datadir/kde4/services/ServiceMenus/kpresenter_konqi.desktop
%_kde_appsdir/kpresenter
%_kde_iconsdir/hicolor/*/apps/kpresenter.png
%_kde_datadir/kde4/services/kpresenterpart.desktop
%_kde_datadir/kde4/services/kpresenter_powerpoint_import.desktop
%_kde_datadir/kde4/services/kpresentereventactions.desktop
%_kde_datadir/kde4/servicetypes/presentationeventaction.desktop
%_kde_datadir/kde4/services/kpr_pageeffect_barwipe.desktop
%_kde_datadir/kde4/services/kpr_pageeffect_clockwipe.desktop
%_kde_datadir/kde4/services/kpr_pageeffect_edgewipe.desktop
%_kde_datadir/kde4/services/kpr_pageeffect_iriswipe.desktop
%_kde_datadir/kde4/services/kpr_pageeffect_matrixwipe.desktop
%_kde_datadir/kde4/services/kpr_pageeffect_slidewipe.desktop
%_kde_datadir/kde4/services/kpr_shapeanimation_example.desktop
%_kde_datadir/kde4/services/kpresentertoolanimation.desktop
%_kde_datadir/kde4/servicetypes/kpr_pageeffect.desktop
%_kde_datadir/kde4/servicetypes/kpr_shapeanimation.desktop

%_kde_docdir/HTML/en/kpresenter

#--------------------------------------------------------------------

%define kpresenterprivate_major 5
%define libkpresenterprivate %mklibname kpresenterprivate %kpresenterprivate_major

%package -n %libkpresenterprivate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkpresenterprivate
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkpresenterprivate -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkpresenterprivate -p /sbin/ldconfig
%endif

%files -n %libkpresenterprivate
%defattr(-,root,root)
%_kde_libdir/libkpresenterprivate.so.%kpresenterprivate_major
%_kde_libdir/libkpresenterprivate.so.%kpresenterprivate_major.0.0

#--------------------------------------------------------------------
%package -n kformula
Summary:	Formula for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Provides:       %name-apps
Provides:       kformula2
Obsoletes:      %name-kformula <= 11:1.9.95.3-0.766453.5
Provides:       %name-kformula = %epoch:%version-%release
Obsoletes:      koffice2-kformula < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kformula = %epoch:%version-%release

%description -n kformula
KFormula is a formula for kde project.

%post -n kformula
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}


%postun -n kformula
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{clean_desktop_database}


%files -n kformula
%defattr(-,root,root)
%if 0
%_kde_bindir/kformula
%_kde_libdir/kde4/libkformulapart.so
%_kde_libdir/libkdeinit4_kformula.so
%_kde_datadir/applications/kde4/kformula.desktop
%_kde_appsdir/formulashape
%_kde_appsdir/kformula
%_kde_datadir/kde4/services/ServiceMenus/kformula_konqi.desktop
%_kde_iconsdir/hicolor/*/apps/kformula.png
%_kde_datadir/kde4/services/kformulapart.desktop
%endif
%_kde_docdir/HTML/en/kformula

#--------------------------------------------------------------------
%if 0
%define kformulalib_major 5
%define libkformulalib %mklibname kformulalib %kformulalib_major

%package -n %libkformulalib
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkformulalib
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkformulalib -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkformulalib -p /sbin/ldconfig
%endif

%files -n %libkformulalib
%defattr(-,root,root)
%_kde_libdir/libkformulalib.so.5
%_kde_libdir/libkformulalib.so.5.0.0

#--------------------------------------------------------------------

%define kformulaprivate_major 5
%define  libkformulaprivate %mklibname kformulaprivate %kformulaprivate_major

%package -n %libkformulaprivate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkformulaprivate
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkformulaprivate -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkformulaprivate -p /sbin/ldconfig
%endif

%files -n %libkformulaprivate
%defattr(-,root,root)
%_kde_libdir/libkformulaprivate.so.%kformulaprivate_major
%_kde_libdir/libkformulaprivate.so.%kformulaprivate_major.0.0
%endif
#--------------------------------------------------------------------

%package -n koshell
Summary:	Koshell for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Provides:       %name-apps
Provides:       koshell2
Obsoletes:      %name-koshell <= 11:1.9.95.3-0.766453.5
Provides:       %name-koshell = %epoch:%version-%release
Obsoletes:      koffice2-koshell < 1:1.9.95.3-0.766453.6
Provides:       koffice2-koshell = %epoch:%version-%release

%description -n koshell
Koshell for kde project.

%if %mdkversion < 200900
%post -n koshell -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n koshell -p /sbin/ldconfig
%endif


%files -n koshell
%defattr(-,root,root)
%_kde_docdir/HTML/en/koshell

#--------------------------------------------------------------------

%package -n kivio
Summary:	Diagramme for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Provides:       %name-apps
Provides:       kivio2
Obsoletes:      %name-kivio <= 11:1.9.95.3-0.766453.5
Provides:       %name-kivio = %epoch:%version-%release
Obsoletes:      koffice2-kivio < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kivio = %epoch:%version-%release

%description -n kivio
Kivio is a diagramme for kde project.

%post -n kivio
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}


%postun -n kivio
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}

%files -n kivio
%defattr(-,root,root)
%if 0
%_kde_bindir/kivio
%_kde_libdir/kde4/libkiviopart.so
%_kde_libdir/libkdeinit4_kivio.so
%_kde_datadir/applications/kde4/kivio.desktop
%_kde_appsdir/kivio
%_kde_datadir/kde4/services/ServiceMenus/kivio_konqi.desktop
%_kde_datadir/kde4/services/kiviopart.desktop
%endif
%_kde_docdir/HTML/en/kivio

#--------------------------------------------------------------------
%if 0
%define  kivioprivate_major 5
%define  libkivioprivate %mklibname kivioprivate  %kivioprivate_major 

%package -n %libkivioprivate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkivioprivate
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkivioprivate -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkivioprivate -p /sbin/ldconfig
%endif

%files -n %libkivioprivate
%defattr(-,root,root)
%_kde_libdir/libkivioprivate.so.%kivioprivate_major 
%_kde_libdir/libkivioprivate.so.%kivioprivate_major.0.0
%endif
#--------------------------------------------------------------------

%package -n kchart
Summary:        Chart and diagram drawing
Group:          Graphical desktop/KDE
Requires:       %name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Provides:       %name-apps
Provides:       kchart2
Obsoletes:      %name-kchart <= 11:1.9.95.3-0.766453.5
Provides:       %name-kchart = %epoch:%version-%release
Obsoletes:      koffice2-kchart < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kchart = %epoch:%version-%release

%description -n kchart
Kchart is a chart and diagram drawing program.

%post -n kchart
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}


%postun -n kchart
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}

%files -n kchart
%defattr(-,root,root)
%{_kde_bindir}/kchart

%_kde_libdir/kde4/chartshape.so
%_kde_libdir/kde4/libkchartpart.so
%_kde_libdir/libkdeinit4_kchart.so
%_kde_libdir/kde4/libkchartgenericimageexport.so
%_kde_libdir/kde4/libkchartsvgexport.so

%{_kde_datadir}/kde4/services/chartshape.desktop
%{_kde_datadir}/kde4/services/kchartpart.desktop
%{_kde_datadir}/kde4/services/kchart_bmp_export.desktop
%{_kde_datadir}/kde4/services/kchart_jpeg_export.desktop
%{_kde_datadir}/kde4/services/kchart_mng_export.desktop
%{_kde_datadir}/kde4/services/kchart_png_export.desktop
%{_kde_datadir}/kde4/services/kchart_svg_export.desktop
%{_kde_datadir}/kde4/services/kchart_xbm_export.desktop
%{_kde_datadir}/kde4/services/kchart_xpm_export.desktop

%{_kde_datadir}/applications/kde4/kchart.desktop
%{_kde_datadir}/config.kcfg/kchart.kcfg
%{_kde_appsdir}/kchart
%{_kde_iconsdir}/hicolor/*/apps/kchart.png

#--------------------------------------------------------------------

%define  kdchart_major 5
%define  libkdchart %mklibname kdchart  %kdchart_major

%package -n %libkdchart
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkdchart
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkdchart -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdchart -p /sbin/ldconfig
%endif

%files -n %libkdchart
%defattr(-,root,root)
%_kde_libdir/libkdchart.so.%kdchart_major
%_kde_libdir/libkdchart.so.%kdchart_major.0.0

#--------------------------------------------------------------------

%define  kchartcommon_major 5
%define  libkchartcommon %mklibname kchartcommon %kchartcommon_major

%package -n %libkchartcommon
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkchartcommon
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkchartcommon -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkchartcommon -p /sbin/ldconfig
%endif

%files -n %libkchartcommon
%defattr(-,root,root)
%_kde_libdir/libkchartcommon.so.%kchartcommon_major
%_kde_libdir/libkchartcommon.so.%kchartcommon_major.0.0

#--------------------------------------------------------------------

%define  kisexiv2_major 5
%define  libkisexiv2 %mklibname kisexiv2 %kisexiv2_major

%package -n %libkisexiv2
Summary:   Koffice 2 core library
Group:     System/Libraries
Conflicts: koffice2-krita < 1.9.95-0.738534.3 

%description -n %libkisexiv2
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkisexiv2 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkisexiv2 -p /sbin/ldconfig
%endif

%files -n %libkisexiv2
%defattr(-,root,root)
%_kde_libdir/libkisexiv2.so.%kisexiv2_major
%_kde_libdir/libkisexiv2.so.%kisexiv2_major.0.0

#--------------------------------------------------------------------

%package -n katelier
Summary: Krita and karbon meta package
Group: Graphical desktop/KDE
Requires: krita
Requires: karbon

%description -n katelier
Krita and karbon meta package

%files -n katelier
%defattr(-,root,root,-)

#--------------------------------------------------------------------

%package -n krita
Summary:        A pixel-based image manipulation program
Group:          Graphical desktop/KDE
URL:            http://www.koffice.org/
Requires:	    %name-core = %{epoch}:%{version}-%{release}
Provides:       %name-apps
Provides:       krita2
Obsoletes:      %name-krita < 11:1.9.95.4-1
Provides:       %name-krita = %epoch:%version-%release
Obsoletes:      koffice2-krita < 11:1.9.95.4-1
Provides:       koffice2-krita = %epoch:%version-%release

Obsoletes:      %{_lib}kritafilterslistdynamicprogram5 < 1:1.9.92-0.710350.1
Obsoletes:      %{_lib}krita_gray_u165 < 1:1.9.92-0.710350.1
Obsoletes:      %{_lib}kritargbf32hdr5 < 11:1.9.95.4-1

%description -n krita
Krita is a pixel-based image manipulation program.

%post -n krita
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}

%postun -n krita
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}

%files -n krita
%defattr(-,root,root)
%_kde_bindir/krita
%_kde_libdir/kde4/*krita*
%_kde_libdir/libkdeinit4_krita.so
%_kde_datadir/applications/kde4/krita.desktop
%_kde_datadir/applications/kde4/krita_jpeg.desktop
%_kde_datadir/applications/kde4/krita_png.desktop
%_kde_datadir/applications/kde4/krita_bmp.desktop
%_kde_datadir/applications/kde4/krita_ora.desktop
%_kde_datadir/applications/kde4/krita_pdf.desktop
%_kde_datadir/applications/kde4/krita_tiff.desktop
%_kde_datadir/applications/kde4/krita_raw.desktop
%_kde_datadir/kde4/services/ServiceMenus/krita_konqi.desktop
%_kde_datadir/kde4/services/*krita*.desktop
%_kde_datadir/kde4/servicetypes/*krita*.desktop
%_kde_iconsdir/hicolor/*/apps/krita.png
%_kde_appsdir/krita
%_kde_appsdir/kritaplugins

%_kde_datadir/color/icc/krita/*.icm
%_kde_datadir/color/icc/pigment/*.icm
%_kde_datadir/kde4/servicetypes/pigment.desktop
%_kde_datadir/mime/packages/krita_ora.xml

%_kde_docdir/HTML/en/krita

#--------------------------------------------------------------------

%define  libkrita_xyz_u16_major 5
%define  libkrita_xyz_u16 %mklibname krita_xyz_u16  %libkrita_xyz_u16_major

%package -n %libkrita_xyz_u16
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkrita_xyz_u16
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkrita_xyz_u16 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkrita_xyz_u16 -p /sbin/ldconfig
%endif

%files -n %libkrita_xyz_u16
%defattr(-,root,root)
%_kde_libdir/libkrita_xyz_u16.so.%{libkrita_xyz_u16_major}*

#--------------------------------------------------------------------


%define  kritabasicdynamiccoloringprogram_major 5
%define  libkritabasicdynamiccoloringprogram  %mklibname kritabasicdynamiccoloringprogram  %kritabasicdynamiccoloringprogram_major

%package -n %libkritabasicdynamiccoloringprogram
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritabasicdynamiccoloringprogram
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkritabasicdynamiccoloringprogram -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkritabasicdynamiccoloringprogram -p /sbin/ldconfig
%endif

%files -n %libkritabasicdynamiccoloringprogram
%defattr(-,root,root)
%_kde_libdir/libkritabasicdynamiccoloringprogram.so.%{kritabasicdynamiccoloringprogram_major}*

#--------------------------------------------------------------------

%define  kritabasicdynamicshapeprogram_major 5
%define  libkritabasicdynamicshapeprogram %mklibname kritabasicdynamicshapeprogram  %kritabasicdynamicshapeprogram_major

%package -n %libkritabasicdynamicshapeprogram
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritabasicdynamicshapeprogram
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkritabasicdynamicshapeprogram -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkritabasicdynamicshapeprogram -p /sbin/ldconfig
%endif

%files -n %libkritabasicdynamicshapeprogram
%defattr(-,root,root)
%_kde_libdir/libkritabasicdynamicshapeprogram.so.%{kritabasicdynamicshapeprogram_major}*

#--------------------------------------------------------------------

%define  libkritaui_major 5
%define  libkritaui %mklibname kritaui  %libkritaui_major

%package -n %libkritaui
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritaui
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkritaui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkritaui -p /sbin/ldconfig
%endif

%files -n %libkritaui
%defattr(-,root,root)
%_kde_libdir/libkritaui.so.%libkritaui_major
%_kde_libdir/libkritaui.so.%libkritaui_major.0.0

#--------------------------------------------------------------------

%define  kritadynamicbrush_major 5
%define  libkritadynamicbrush %mklibname kritadynamicbrush  %kritadynamicbrush_major

%package -n %libkritadynamicbrush
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritadynamicbrush
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkritadynamicbrush -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkritadynamicbrush -p /sbin/ldconfig
%endif

%files -n %libkritadynamicbrush
%defattr(-,root,root)
%_kde_libdir/libkritadynamicbrush.so.%kritadynamicbrush_major
%_kde_libdir/libkritadynamicbrush.so.%kritadynamicbrush_major.0.0

#--------------------------------------------------------------------

%define  libkrossmodulekrita_major 5
%define  libkrossmodulekrita %mklibname krossmodulekrita %libkrossmodulekrita_major

%package -n %libkrossmodulekrita
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkrossmodulekrita
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkrossmodulekrita -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkrossmodulekrita -p /sbin/ldconfig
%endif

%files -n %libkrossmodulekrita
%defattr(-,root,root)
%_kde_libdir/libkrossmodulekrita.so.%libkrossmodulekrita_major
%_kde_libdir/libkrossmodulekrita.so.%libkrossmodulekrita_major.0.0

#--------------------------------------------------------------------
# TODO Find the missing BuildRequire
#define  libkritafilterslistdynamicprogram_major 5
#define  libkritafilterslistdynamicprogram %mklibname kritafilterslistdynamicprogram  %libkritafilterslistdynamicprogram_major
#
#%package -n %libkritafilterslistdynamicprogram
#Summary: Koffice 2 core library
#Group: System/Libraries
#
#%description -n %libkritafilterslistdynamicprogram
#Koffice 2 core library.
#
#%post -n %libkritafilterslistdynamicprogram -p /sbin/ldconfig
#%postun -n %libkritafilterslistdynamicprogram -p /sbin/ldconfig
#
#%files -n %libkritafilterslistdynamicprogram
#%defattr(-,root,root)
#%_kde_libdir/libkritafilterslistdynamicprogram.so.%libkritafilterslistdynamicprogram_major
#%_kde_libdir/libkritafilterslistdynamicprogram.so.%libkritafilterslistdynamicprogram_major.0.0
#
#--------------------------------------------------------------------

%define  libkritagrayscale_major 5
%define  libkritagrayscale %mklibname kritagrayscale  %libkritagrayscale_major

%package -n %libkritagrayscale
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritagrayscale
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkritagrayscale -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkritagrayscale -p /sbin/ldconfig
%endif

%files -n %libkritagrayscale
%defattr(-,root,root)
%_kde_libdir/libkritagrayscale.so.5
%_kde_libdir/libkritagrayscale.so.5.0.0

#--------------------------------------------------------------------

%define  libkritaimage_major 5
%define  libkritaimage %mklibname kritaimage  %libkritaimage_major

%package -n %libkritaimage
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritaimage
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkritaimage -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkritaimage -p /sbin/ldconfig
%endif

%files -n %libkritaimage
%defattr(-,root,root)
%_kde_libdir/libkritaimage.so.%libkritaimage_major
%_kde_libdir/libkritaimage.so.%libkritaimage_major.0.0

#--------------------------------------------------------------------

%define  libkritalibpaintop_major 5
%define  libkritalibpaintop %mklibname kritalibpaintop  %libkritalibpaintop_major

%package -n %libkritalibpaintop
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritalibpaintop
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkritalibpaintop -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkritalibpaintop -p /sbin/ldconfig
%endif

%files -n %libkritalibpaintop
%defattr(-,root,root)
%_kde_libdir/libkritalibpaintop.so.%{libkritalibpaintop_major}*

#--------------------------------------------------------------------

%package -n karbon
Summary:	Scalable drawing for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Provides:       %name-apps
Provides:       karbon2
Obsoletes:      %name-karbon <= 11:1.9.95.3-0.766453.5
Provides:       %name-karbon = %epoch:%version-%release
Obsoletes:      koffice2-karbon < 1:1.9.95.3-0.766453.6
Provides:       koffice2-karbon = %epoch:%version-%release

%description -n karbon
Karbon is a scalable drawing for kde project.

%post -n karbon
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}


%postun -n karbon
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}


%files -n karbon
%defattr(-,root,root)
%_kde_bindir/karbon
%_kde_libdir/kde4/karbon_flattenpathplugin.so
%_kde_libdir/kde4/karbon_whirlpinchplugin.so
%_kde_libdir/kde4/karbontools.so
%_kde_libdir/kde4/libkarbonpart.so
%_kde_libdir/kde4/libkarbonpngexport.so
%_kde_libdir/kde4/libkarbonsvgexport.so
%_kde_libdir/kde4/libkarbonepsimport.so
%_kde_libdir/kde4/libwmfexport.so
%_kde_libdir/kde4/libwmfimport.so
%_kde_libdir/kde4/libkarbon1ximport.so
%_kde_libdir/kde4/karbon_refinepathplugin.so
%_kde_libdir/kde4/karbon_roundcornersplugin.so
%_kde_libdir/kde4/karbondockersplugin.so
%_kde_libdir/libkdeinit4_karbon.so
%_kde_datadir/applications/kde4/karbon.desktop
%_kde_appsdir/karbon
%_kde_datadir/kde4/services/ServiceMenus/karbon_konqi.desktop

%_kde_docdir/HTML/en/karbon

%_kde_datadir/kde4/services/karbon*.desktop
%_kde_datadir/kde4/servicetypes/karbon_module.desktop
%_kde_datadir/templates/.source/Illustration.karbon

#--------------------------------------------------------------------

%define  karboncommon_major 5
%define  libkarboncommon %mklibname karboncommon  %karboncommon_major

%package -n %libkarboncommon
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkarboncommon
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkarboncommon -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkarboncommon -p /sbin/ldconfig
%endif

%files -n %libkarboncommon
%defattr(-,root,root)
%_kde_libdir/libkarboncommon.so.%karboncommon_major
%_kde_libdir/libkarboncommon.so.%karboncommon_major.0.0

#--------------------------------------------------------------------

%define  karbonui_major 5
%define  libkarbonui %mklibname karbonui  %karbonui_major

%package -n %libkarbonui
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkarbonui
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkarbonui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkarbonui -p /sbin/ldconfig
%endif

%files -n %libkarbonui
%defattr(-,root,root)
%_kde_libdir/libkarbonui.so.%karbonui_major
%_kde_libdir/libkarbonui.so.%karbonui_major.0.0

#--------------------------------------------------------------------

%package -n kexi
Summary:    An integrated environment for managing data
Group:	    Graphical desktop/KDE
Requires:   %name-core = %{epoch}:%{version}-%{release}
URL:        http://www.koffice.org/
Provides:   %name-apps
Provides:   kexi2
Obsoletes:      %{_lib}kexisql2 < 1:1.9.95-0.738534.2
Obsoletes:      %name-kexi <= 11:1.9.95.3-0.766453.5
Provides:       %name-kexi = %epoch:%version-%release
Obsoletes:      koffice2-kexi < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kexi = %epoch:%version-%release

%description -n kexi
Karbon is an integrated environment for managing data.

%post -n kexi
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}

%postun -n kexi
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_desktop_database}

%files -n kexi
%defattr(-,root,root)
%if 0
%_kde_bindir/kexi
%_kde_bindir/ksqlite
%_kde_bindir/ksqlite2to3

%_kde_libdir/kde4/kexidb_mysqldriver.so
%_kde_libdir/kde4/kexidb_pqxxsqldriver.so
%_kde_libdir/kde4/keximigrate_pqxx.so
%_kde_libdir/kde4/kexidb_sqlite3driver.so
%_kde_libdir/kde4/kexidb_xbasedriver.so
%_kde_libdir/kde4/kexihandler_csv_importexport.so
%_kde_libdir/kde4/kexihandler_form.so
%_kde_libdir/kde4/kexihandler_migration.so
%_kde_libdir/kde4/kexihandler_query.so
%_kde_libdir/kde4/kexihandler_relation.so
%_kde_libdir/kde4/kexihandler_table.so
%_kde_libdir/kde4/keximigrate_mysql.so
%_kde_libdir/kde4/keximigrate_sybase.so
%_kde_libdir/kde4/kexihandler_script.so
%_kde_libdir/kde4/pgzkexireportpart2.so
%_kde_libdir/kde4/kformdesigner_kexidbwidgets.so
%_kde_libdir/kde4/krossmodulekexidb.so
%_kde_datadir/applications/kde4/kexi.desktop
%_kde_appsdir/kexi
%_kde_datadir/kde4/services/ServiceMenus/kexi_konqi.desktop
%_kde_datadir/config/kexirc
%endif
%_kde_docdir/HTML/en/kexi
%if 0
%_kde_datadir/kde4/services/kexi/*.desktop
%_kde_datadir/kde4/services/kexidb_mysqldriver.desktop
%_kde_datadir/kde4/services/kexidb_pqxxsqldriver.desktop
%_kde_datadir/kde4/services/keximigrate_pqxx.desktop
%_kde_datadir/kde4/services/kexidb_sqlite3driver.desktop
%_kde_datadir/kde4/services/keximigrate_mysql.desktop
%_kde_datadir/kde4/services/keximigrate_sybase.desktop
%_kde_datadir/kde4/services/kexidb_xbasedriver.desktop
%_kde_datadir/kde4/services/kformdesigner/kformdesigner_kexidbfactory.desktop
%_kde_datadir/kde4/servicetypes/kexidb_driver.desktop
%_kde_datadir/kde4/servicetypes/kexihandler.desktop
%_kde_datadir/kde4/servicetypes/keximigration_driver.desktop

#--------------------------------------------------------------------

%define  libkexicore_major 5
%define  libkexicore %mklibname kexicore %libkexicore_major

%package -n %libkexicore
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexicore
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkexicore -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkexicore -p /sbin/ldconfig
%endif

%files -n %libkexicore
%defattr(-,root,root)
%_kde_libdir/libkexicore.so.%libkexicore_major
%_kde_libdir/libkexicore.so.%libkexicore_major.0.0

#--------------------------------------------------------------------

%define  libkexidatatable_major 5
%define  libkexidatatable %mklibname kexidatatable %libkexidatatable_major

%package -n %libkexidatatable
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexidatatable
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkexidatatable -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkexidatatable -p /sbin/ldconfig
%endif

%files -n %libkexidatatable
%defattr(-,root,root)
%_kde_libdir/libkexidatatable.so.%libkexidatatable_major
%_kde_libdir/libkexidatatable.so.%libkexidatatable_major.0.0

#--------------------------------------------------------------------

%define  libkexidb_major 5
%define  libkexidb %mklibname kexidb %libkexidb_major

%package -n %libkexidb
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexidb
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkexidb -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkexidb -p /sbin/ldconfig
%endif

%files -n %libkexidb
%defattr(-,root,root)
%_kde_libdir/libkexidb.so.%libkexidb_major
%_kde_libdir/libkexidb.so.%libkexidb_major.0.0

#--------------------------------------------------------------------

%define  libkexiextendedwidgets_major 5
%define  libkexiextendedwidgets %mklibname kexiextendedwidgets %libkexiextendedwidgets_major

%package -n %libkexiextendedwidgets
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexiextendedwidgets
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkexiextendedwidgets -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkexiextendedwidgets -p /sbin/ldconfig
%endif

%files -n %libkexiextendedwidgets
%defattr(-,root,root)
%_kde_libdir/libkexiextendedwidgets.so.%libkexiextendedwidgets_major.0.0

#--------------------------------------------------------------------

%define  libkexiformutils_major 5
%define  libkexiformutils %mklibname kexiformutils %libkexiformutils_major

%package -n %libkexiformutils
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexiformutils
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkexiformutils -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkexiformutils -p /sbin/ldconfig
%endif

%files -n %libkexiformutils
%defattr(-,root,root)
%_kde_libdir/libkexiformutils.so.%libkexiformutils_major
%_kde_libdir/libkexiformutils.so.%libkexiformutils_major.0.0
#--------------------------------------------------------------------

%define  libkexiguiutils_major 5
%define  libkexiguiutils %mklibname kexiguiutils %libkexiguiutils_major

%package -n %libkexiguiutils
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexiguiutils
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkexiguiutils -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkexiguiutils -p /sbin/ldconfig
%endif

%files -n %libkexiguiutils
%defattr(-,root,root)
%_kde_libdir/libkexiguiutils.so.%libkexiguiutils_major
%_kde_libdir/libkexiguiutils.so.%libkexiguiutils_major.0.0
#--------------------------------------------------------------------

%define  libkeximain_major 5
%define  libkeximain %mklibname keximain %libkeximain_major

%package -n %libkeximain
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkeximain
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkeximain -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkeximain -p /sbin/ldconfig
%endif

%files -n %libkeximain
%defattr(-,root,root)
%_kde_libdir/libkeximain.so.%libkeximain_major
%_kde_libdir/libkeximain.so.%libkeximain_major.0.0

#--------------------------------------------------------------------

%define  libkeximigrate_major 5
%define  libkeximigrate %mklibname keximigrate %libkeximigrate_major

%package -n %libkeximigrate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkeximigrate
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkeximigrate -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkeximigrate -p /sbin/ldconfig
%endif

%files -n %libkeximigrate
%defattr(-,root,root)
%_kde_libdir/libkeximigrate.so.%libkeximigrate_major
%_kde_libdir/libkeximigrate.so.%libkeximigrate_major.0.0

#--------------------------------------------------------------------

%define  libkexirelationsview_major 5
%define  libkexirelationsview %mklibname kexirelationsview %libkexirelationsview_major

%package -n %libkexirelationsview
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexirelationsview
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkexirelationsview -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkexirelationsview -p /sbin/ldconfig
%endif

%files -n %libkexirelationsview
%defattr(-,root,root)
%_kde_libdir/libkexirelationsview.so.%libkexirelationsview_major
%_kde_libdir/libkexirelationsview.so.%libkexirelationsview_major.0.0

#--------------------------------------------------------------------

%define  libkexisql3_major 3
%define  libkexisql3 %mklibname kexisql3 %libkexisql3_major

%package -n %libkexisql3
Summary:    Koffice 2 core library
Group:      System/Libraries
Obsoletes:  %{_lib}koffice2-kexi < 11:1.6.3-20

%description -n %libkexisql3
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkexisql3 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkexisql3 -p /sbin/ldconfig
%endif

%files -n %libkexisql3
%defattr(-,root,root)
%_kde_libdir/libkexisql3.so.%libkexisql3_major
%_kde_libdir/libkexisql3.so.%libkexisql3_major.2.8

#--------------------------------------------------------------------

%define  libkexiutils_major 5
%define  libkexiutils %mklibname kexiutils %libkexiutils_major

%package -n %libkexiutils
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexiutils
Koffice 2 core library.

%if %mdkversion < 200900
%post -n %libkexiutils -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkexiutils -p /sbin/ldconfig
%endif

%files -n %libkexiutils
%defattr(-,root,root)
%_kde_libdir/libkexiutils.so.%libkexiutils_major
%_kde_libdir/libkexiutils.so.%libkexiutils_major.0.0
%endif
#--------------------------------------------------------------------

%package -n kugar
Summary:	Kugar for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Provides:       %name-apps
Provides:       kugar2
Obsoletes:      %name-kugar <= 11:1.9.95.3-0.766453.5
Provides:       %name-kugar = %epoch:%version-%release
Obsoletes:      koffice2-kugar < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kugar = %epoch:%version-%release

Obsoletes:      %{_lib}kudesignercore5 <  1:1.9.94-0.726770.1
Obsoletes:      %{_lib}kugarlib5 < 1:1.9.94-0.726770.1

%description -n kugar
Kugar for kde project.

%post -n kugar
%if %mdkversion < 200900
/sbin/ldconfig
%{update_desktop_database}
%endif

%postun -n kugar
%if %mdkversion < 200900
/sbin/ldconfig
%{update_desktop_database}
%endif
%files -n kugar
%defattr(-,root,root)
%_kde_docdir/HTML/en/kugar

#--------------------------------------------------------------------

%prep

%setup -q -n %name-%version
%patch1 -p0
#patch2 -p0

%build
# (Anssi 06/2008) FreeTDS_LIBRARIES is needed with recent freetds, otherwise
# it fails on missing libtds.so that has been removed in this version.
%cmake_kde4 \
	-DBUILD_xbase=FALSE \
	-DFreeTDS_LIBRARIES=-lsybdb

%make
%if %compile_apidox
make apidox
%endif

%install
rm -fr %buildroot

%makeinstall_std -C build

%if %compile_apidox
make install-apidox DESTDIR=%buildroot/
list=`ls -d */ -1`;
echo $list;
for i in $list ; do
	cd $i;
		if grep '^include .*Doxyfile.am' Makefile.am; then
			echo "installing apidox from $i" ;	
			make install-apidox DESTDIR=%buildroot/ ; 
		fi
	cd ../;
done;
%endif

%clean
rm -fr %buildroot
