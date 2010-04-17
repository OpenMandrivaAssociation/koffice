%define lib_name_orig %mklibname koffice2
%define lib_major 2
%define lib_name %lib_name_orig%lib_major

%define use_python 1
%define compile_apidox 0

Name: koffice
URL: http://www.koffice.org/
Summary: Set of office applications for KDE
Version: 2.1.82
Release: %mkrel 1
Epoch: 11
Source: http://fr2.rpmfind.net/linux/KDE/stable/koffice-%version/src/%name-%version.tar.bz2
Patch0: koffice-2.1.81-fix-build.patch
Patch1: koffice-2.1.81-krita_disable_painterlyframework.patch
Patch2: koffice-2.1.81-dsolinking.patch
Patch3: koffice-2.1.81-ascii_import_crash.patch
Group: Office
License: GPL
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: lcms-devel
BuildRequires: qca2-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel
BuildRequires: libOpenEXR-devel
BuildRequires: QtShiva-devel
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
BuildRequires: GraphicsMagick-devel
BuildRequires: opengtl-devel >= 0.9.13
BuildRequires: mysql-static-devel
BuildRequires: kdegraphics4-devel
BuildRequires: libtiff-devel
BuildRequires: wv2-devel >= 0.4.2
BuildRequires: getfem++
BuildRequires: xbase-devel
BuildRequires: ctemplate-devel
BuildRequires: freetds-devel
BuildRequires: sqlite-devel
%if %compile_apidox
BuildRequires: graphviz
BuildRequires: doxygen
%endif
Requires: kword
Requires: kspread
Requires: karbon
Requires: kpresenter
Requires: krita
Requires: kplato
Requires: kchart
Requires: kformula
Obsoletes: koshell
Obsoletes: kugar
Obsoletes: kivio
Obsoletes: koffice-kivio < 1.6.3-20
Obsoletes: koffice2 < 1:1.9.95.4

%description
Office applications for the K Desktop Environment.

KOffice contains:
   * KWord: word processor
   * KSpread: spreadsheet
   * KPresenter: presentations
   * KChart: diagram generator
   * Some filters (Excel 97, Winword 97/2000, etc.)
   * karbon: the scalable vector drawing application for KDE.
   * krita: painting and image editing application.
   * kplato: a project management.

%files

#--------------------------------------------------------------------

%package core
Group: Office
Summary: Set of office applications for KDE
Suggests: wordnet
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Provides: koffice2-core = %epoch:%version-%release
Obsoletes: %{_lib}kopainter5 < 1.9.95-0.738034.1
Obsoletes: koffice2-core <= 11:1.9.95.3-0.766453.5
Obsoletes: koffice-common < 11:1.6.3-20
Obsoletes: koshell
Obsoletes: kugar
Obsoletes: kplatowork
Obsoletes: kivio
Conflicts: koffice-kspread < 11:1.6.3-20
Conflicts: koffice-kpresenter < 11:1.6.3-20
Conflicts: koffice-karbon < 11:1.6.3-20
Conflicts: koffice-kchart < 11:1.6.3-20
Conflicts: koffice-kword < 11:1.6.3-20
Conflicts: koffice-devel < 11:1.9.98.1-3
Conflicts: kchart < 11:1.9.98.2-4
Requires: kdebase4-runtime

%description core
Common files for Koffice

%files core
%defattr(-,root,root)
%_kde_datadir/applications/kde4/koffice.desktop
%_kde_datadir/kde4/services/spellcheck.desktop
%_kde_libdir/kde4/spellcheck.so
%_kde_libdir/kde4/libkarbonpdfimport.so
%_kde_libdir/kde4/karbonfiltereffects.so
%_kde_libdir/kde4/libicalendarexport.so
%_kde_libdir/kde4/libpowerpointimport.so
%_kde_libdir/kde4/paragraphtool.so
%dir %_kde_appsdir/koffice
%_kde_appsdir/koffice/autocorrect
%_kde_appsdir/koffice/koffice_shell.rc
%_kde_appsdir/koffice/icons/*/*/*/*
%_kde_appsdir/koffice/icons/*.png
%_kde_datadir/mime/packages/msooxml-all.xml
%_kde_iconsdir/oxygen/scalable/actions/shape-choose.svgz
%_kde_iconsdir/oxygen/*/actions/table.*
%_kde_iconsdir/oxygen/32x32/actions/shape-choose.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-chart.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-connection.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-formula.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-image.png
%_kde_iconsdir/oxygen/32x32/actions/x-shape-text.png
%_kde_iconsdir/oxygen/16x16/actions/object-align-horizontal-center-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-align-horizontal-left-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-align-horizontal-right-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-align-vertical-bottom-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-align-vertical-bottom-top-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-align-vertical-center-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-align-vertical-top-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-group-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-ungroup-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-order-back-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-order-front-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-order-lower-koffice.png
%_kde_iconsdir/oxygen/16x16/actions/object-order-raise-koffice.png
%_kde_iconsdir/hicolor/16x16/actions/black.png
%_kde_iconsdir/hicolor/16x16/actions/highlight.png
%_kde_iconsdir/hicolor/16x16/actions/pen.png
%_kde_datadir/kde4/services/ServiceMenus/kchart_konqi.desktop
%_kde_appsdir/musicshape
%_kde_appsdir/koproperty
%_kde_datadir/kde4/services/autocorrect.desktop
%_kde_datadir/kde4/services/changecase.desktop
%_kde_datadir/kde4/services/defaulttools.desktop
%_kde_datadir/kde4/services/divineproportionshape.desktop
%_kde_datadir/kde4/services/generic_filter.desktop
%_kde_datadir/kde4/services/kofficedockers.desktop
%_kde_datadir/kde4/services/kofficethumbnail.desktop
%_kde_datadir/kde4/services/kounavail.desktop
%_kde_datadir/kde4/services/musicshape.desktop
%_kde_datadir/kde4/services/pathshapes.desktop
%_kde_datadir/kde4/services/pictureshape.desktop
%_kde_datadir/kde4/services/textshape.desktop
%_kde_datadir/kde4/services/textvariables.desktop
%_kde_datadir/kde4/services/artistictextshape.desktop
%_kde_datadir/kde4/services/Filterkpr2odf.desktop
%_kde_datadir/kde4/services/kopabackgroundtool.desktop
%_kde_datadir/kde4/services/paragraphtool.desktop
%_kde_datadir/kde4/services/kolcmsengine.desktop
%_kde_datadir/kde4/services/vectorshape.desktop
%_kde_datadir/kde4/services/videoshape.desktop
%_kde_datadir/kde4/servicetypes/filtereffect.desktop
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
%_kde_datadir/kde4/servicetypes/textvariableplugin.desktop
%exclude %_kde_datadir/templates/.source/Presentation.kpt
%exclude %_kde_datadir/templates/.source/SpreadSheet.kst
%exclude %_kde_datadir/templates/.source/TextDocument.kwt
%exclude %_kde_datadir/templates/Illustration.desktop
%exclude %_kde_datadir/templates/Presentation.desktop
%exclude %_kde_datadir/templates/SpreadSheet.desktop
%exclude %_kde_datadir/templates/TextDocument.desktop
%_kde_libdir/kde4/autocorrect.so
%_kde_libdir/kde4/libasciiexport.so
%_kde_libdir/kde4/libasciiimport.so
%_kde_libdir/kde4/changecase.so
%_kde_libdir/kde4/defaulttools.so
%_kde_libdir/kde4/divineproportionshape.so
%_kde_libdir/kde4/kofficedockers.so
%_kde_libdir/kde4/kofficescan.so
%_kde_libdir/kde4/kofficethumbnail.so
%_kde_libdir/kde4/libabiwordexport.so
%_kde_libdir/kde4/musicshape.so
%_kde_libdir/kde4/pathshapes.so
%_kde_libdir/kde4/pictureshape.so
%_kde_libdir/kde4/textshape.so
%_kde_libdir/kde4/textvariables.so
%_kde_libdir/kde4/artistictextshape.so
%_kde_libdir/kde4/libFilterkpr2odf.so
%_kde_libdir/kde4/kopabackgroundtool.so
%_kde_libdir/kde4/kolcmsengine.so
%_kde_libdir/kde4/libdocximport.so
%_kde_libdir/kde4/libkspreadhtmlimport.so
%_kde_libdir/kde4/libpptximport.so
%_kde_libdir/kde4/libxlsximport.so
%_kde_libdir/kde4/vectorshape.so
%_kde_libdir/kde4/videoshape.so
%_kde_bindir/kthesaurus
%_kde_datadir/applications/kde4/KThesaurus.desktop
%_kde_datadir/kde4/services/thesaurustool.desktop
%_kde_datadir/apps/koffice/thesaurus/thesaurus.txt
%_kde_libdir/kde4/thesaurustool.so
%_kde_libdir/libkdeinit4_kthesaurus.so
%_kde_bindir/koconverter
%_kde_docdir/HTML/en/koffice
%_kde_docdir/HTML/en/thesaurus
%_kde_docdir/HTML/en/kivio
# Those are installed despite their parent packages are available
%exclude %_kde_datadir/kde4/services/ServiceMenus/kivio_konqi.desktop

#--------------------------------------------------------------------

%define libkoreport_major 6
%define libkoreport %mklibname koreport %libkoreport_major

%package -n %libkoreport
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkoreport
Koffice 2 core library.

%files -n %libkoreport
%defattr(-,root,root)
%_kde_libdir/libkoreport.so.%{libkoreport_major}*

#--------------------------------------------------------------------

%define libkokross_major 6
%define libkokross %mklibname kokross %libkokross_major

%package -n %libkokross
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkokross
Koffice 2 core library.

%files -n %libkokross
%defattr(-,root,root)
%_kde_libdir/libkokross.so.%libkokross_major
%_kde_libdir/libkokross.so.%libkokross_major.0.0

#--------------------------------------------------------------------

%define libkomain_major 6
%define libkomain %mklibname komain %libkomain_major

%package -n %libkomain
Summary: Koffice 2 core library
Group: System/Libraries
Requires: koffice-l10n

%description -n %libkomain
Koffice 2 core library.

%files -n %libkomain
%defattr(-,root,root)
%_kde_libdir/libkomain.so.%libkomain_major
%_kde_libdir/libkomain.so.%libkomain_major.0.0

#--------------------------------------------------------------------

%define libkopageapp_major 6
%define libkopageapp %mklibname kopageapp %libkopageapp_major

%package -n %libkopageapp
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkopageapp
Koffice 2 core library.

%files -n %libkopageapp
%defattr(-,root,root)
%_kde_libdir/libkopageapp.so.%libkopageapp_major
%_kde_libdir/libkopageapp.so.%libkopageapp_major.0.0

#--------------------------------------------------------------------

%define libkotext_major 6
%define libkotext %mklibname kotext %libkotext_major

%package -n %libkotext
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkotext
Koffice 2 core library.

%files -n %libkotext
%defattr(-,root,root)
%_kde_libdir/libkotext.so.%libkotext_major
%_kde_libdir/libkotext.so.%libkotext_major.0.0

#--------------------------------------------------------------------

%define libkowmf_major 6
%define libkowmf %mklibname kowmf %libkowmf_major

%package -n %libkowmf
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkowmf
Koffice 2 core library.

%files -n %libkowmf
%defattr(-,root,root)
%_kde_libdir/libkowmf.so.%libkowmf_major
%_kde_libdir/libkowmf.so.%libkowmf_major.0.0

#--------------------------------------------------------------------

%define libkoodf_major 6
%define libkoodf %mklibname koodf %libkoodf_major

%package -n %libkoodf
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkoodf
Koffice 2 core library.

%files -n %libkoodf
%defattr(-,root,root)
%_kde_libdir/libkoodf.so.%libkoodf_major
%_kde_libdir/libkoodf.so.%libkoodf_major.0.0

#--------------------------------------------------------------------

%define libkwmf_major 6
%define libkwmf %mklibname kwmf %libkwmf_major

%package -n %libkwmf
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkwmf
Koffice 2 core library.

%files -n %libkwmf
%defattr(-,root,root)
%_kde_libdir/libkwmf.so.%libkwmf_major
%_kde_libdir/libkwmf.so.%libkwmf_major.0.0

#--------------------------------------------------------------------

%define libflake_major 6
%define libflake %mklibname flake %libflake_major

%package -n %libflake
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libflake
Koffice 2 core library.

%files -n %libflake
%defattr(-,root,root)
%_kde_libdir/libflake.so.%libflake_major
%_kde_libdir/libflake.so.%libflake_major.0.0

#--------------------------------------------------------------------
%define libpigmentcms_major 6
%define libpigmentcms %mklibname pigmentcms %libpigmentcms_major

%package -n %libpigmentcms
Summary: Koffice 2 core library
Group: System/Libraries
Obsoletes:   %{_lib}libpigmentpigment1 < 1:1.9.95.3-0.766453.1
Obsoletes:   %{_lib}libpigmentcms1 < 1:1.9.95.3-0.766453.1
Obsoletes:   %{_lib}libpigmentcms1 < 1:1.9.95.3-0.766453.1

%description -n %libpigmentcms
Koffice 2 core library.

%files -n %libpigmentcms
%defattr(-,root,root)
%_kde_libdir/libpigmentcms.so.%libpigmentcms_major
%_kde_libdir/libpigmentcms.so.%libpigmentcms_major.0.0

#--------------------------------------------------------------------
%if 0
%define libkformdesigner_major 6
%define libkformdesigner %mklibname kformdesigner %libkformdesigner_major

%package -n %libkformdesigner
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkformdesigner
Koffice 2 core library.

%files -n %libkformdesigner
%defattr(-,root,root)
%_kde_libdir/libkformdesigner.so.%libkformdesigner_major
%_kde_libdir/libkformdesigner.so.%libkformdesigner_major.0.0
%endif
#--------------------------------------------------------------------

%define libkochart_major 6
%define libkochart %mklibname kochart %libkochart_major

%package -n %libkochart
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkochart
Koffice 2 core library.

%files -n %libkochart
%defattr(-,root,root)
%_kde_libdir/libkochart.so.%libkochart_major
%_kde_libdir/libkochart.so.%libkochart_major.0.0

#--------------------------------------------------------------------

%package -n kword
Summary:	Word processor for koffice2
Group:		Graphical desktop/KDE
Requires:	%name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Requires:	wordnet
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
%{update_desktop_database}

%postun -n kword
%{clean_desktop_database}

%files -n kword
%defattr(-,root,root)
%_kde_bindir/kword
%_kde_iconsdir/*/*/apps/kword.png
%_kde_datadir/applications/kde4/kword.desktop
%_kde_datadir/kde4/services/ServiceMenus/kword_konqi.desktop
%_kde_configdir/kwordrc
%_kde_appsdir/kword
%_kde_appsdir/xsltfilter/export/kword/xslfo/*
%_kde_datadir/kde4/services/kword_*
%_kde_datadir/kde4/services/krossmodulekword.desktop
%_kde_datadir/kde4/services/kwordpart.desktop
%_kde_datadir/kde4/services/xslt_export.desktop
%_kde_datadir/kde4/services/xslt_import.desktop
%_kde_libdir/kde4/krossmodulekword.so
%_kde_libdir/kde4/libkwordkword1dot3import.so
%_kde_libdir/kde4/libkwordpart.so
%_kde_libdir/kde4/libabiwordimport.so
%_kde_libdir/kde4/libamiproexport.so
%_kde_libdir/kde4/libamiproimport.so
%_kde_libdir/kde4/libapplixspreadimport.so
%_kde_libdir/kde4/libapplixwordimport.so
%_kde_libdir/kde4/libcsvexport.so
%_kde_libdir/kde4/libcsvimport.so
%_kde_libdir/kde4/libdbaseimport.so
%_kde_libdir/kde4/libdocbookexport.so
%_kde_libdir/kde4/libgenerickofilter.so
%_kde_libdir/kde4/libgnumericexport.so
%_kde_libdir/kde4/libgnumericimport.so
%_kde_libdir/kde4/libhancomwordimport.so
%_kde_libdir/kde4/libhtmlexport.so
%_kde_libdir/kde4/libhtmlimport.so
%_kde_libdir/kde4/libkounavailpart.so
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
%_kde_libdir/kde4/libmswordodf_import.so
%_kde_libdir/libkdeinit4_kword.so

#--------------------------------------------------------------------

%define kwordexportfilters_major 6
%define libkwordexportfilters %mklibname kwordexportfilters %kwordexportfilters_major

%package -n %libkwordexportfilters
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkwordexportfilters
Koffice 2 core library.

%files -n %libkwordexportfilters
%defattr(-,root,root)
%_kde_libdir/libkwordexportfilters.so.%kwordexportfilters_major
%_kde_libdir/libkwordexportfilters.so.%kwordexportfilters_major.0.0

#--------------------------------------------------------------------

%define kwordprivate_major 6
%define libkwordprivate %mklibname kwordprivate %kwordprivate_major

%package -n %libkwordprivate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkwordprivate
Koffice 2 core library.

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
Obsoletes:      kplatowork
Obsoletes:      %{_lib}kplatoworkprivat5 < 1:1.9.95.3-1
Obsoletes:      %name-kplato <= 11:1.9.95.3-0.766453.5
Provides:       %name-kplato = %epoch:%version-%release
Obsoletes:      koffice2-kplato < 1:1.9.95.3-0.766453.6
Provides:       koffice2-kplato = %epoch:%version-%release

%description -n kplato
A new project management application for koffice2.

%post -n kplato
%{update_desktop_database}

%postun -n kplato
%{update_desktop_database}


%files -n kplato
%defattr(-,root,root)
%_kde_bindir/kplato
%_kde_bindir/kplatowork
%_kde_datadir/applications/kde4/kplato.desktop
%_kde_datadir/applications/kde4/kplatowork.desktop
%_kde_appsdir/kplatowork
%_kde_appsdir/kplato
%_kde_datadir/config/kplatorc
%_kde_libdir/libkdeinit4_kplato.so
%_kde_libdir/libkdeinit4_kplatowork.so
%_kde_libdir/kde4/krossmodulekplato.so
%_kde_libdir/kde4/libkplatopart.so
%_kde_libdir/kde4/libkplatoworkpart.so
%_kde_datadir/kde4/services/kplatopart.desktop
%_kde_datadir/kde4/services/krossmodulekplato.desktop
%_kde_datadir/kde4/services/kplato_icalendar_export.desktop
%_kde_datadir/kde4/services/kplatoworkpart.desktop
%_kde_datadir/kde4/servicetypes/kplato_schedulerplugin.desktop
%_kde_iconsdir/hicolor/*/*/*kplato*
%_kde_datadir/config.kcfg/kplatosettings.kcfg                                   
%_kde_datadir/config/kplatoworkrc

#--------------------------------------------------------------------

%define chartshapelib_major 6
%define libchartshapelib %mklibname chartshapelib %chartshapelib_major

%package -n %libchartshapelib
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libchartshapelib
Koffice 2 core library.

%files -n %libchartshapelib
%defattr(-,root,root)
%_kde_libdir/libchartshapelib.so.%chartshapelib_major
%_kde_libdir/libchartshapelib.so.%chartshapelib_major.0.0


#--------------------------------------------------------------------
%define kplatomodels_major 6
%define  libkplatomodels %mklibname kplatomodels %kplatomodels_major

%package -n %libkplatomodels
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatomodels
Koffice 2 core library.

%files -n %libkplatomodels
%defattr(-,root,root)
%_kde_libdir/libkplatomodels.so.%kplatomodels_major
%_kde_libdir/libkplatomodels.so.%kplatomodels_major.0.0

#-------------------------------------------------------------------

%define  kplatokernel_major 6
%define  libkplatokernel %mklibname kplatokernel %kplatokernel_major

%package -n %libkplatokernel
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatokernel
Koffice 2 core library.

%files -n %libkplatokernel
%defattr(-,root,root)
%_kde_libdir/libkplatokernel.so.%kplatokernel_major
%_kde_libdir/libkplatokernel.so.%kplatokernel_major.0.0

#--------------------------------------------------------------------

%define kplatoprivate_major 6
%define libkplatoprivate %mklibname kplatoprivate %kplatoprivate_major

%package -n %libkplatoprivate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoprivate
Koffice 2 core library.

%files -n %libkplatoprivate
%defattr(-,root,root)
%_kde_libdir/libkplatoprivate.so.%kplatoprivate_major
%_kde_libdir/libkplatoprivate.so.%kplatoprivate_major.0.0

#--------------------------------------------------------------------

%define kplatoui_major 6
%define libkplatoui %mklibname kplatoui %kplatoui_major

%package -n %libkplatoui
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoui
Koffice 2 core library.

%files -n %libkplatoui
%defattr(-,root,root)
%_kde_libdir/libkplatoui.so.%kplatoui_major
%_kde_libdir/libkplatoui.so.%kplatoui_major.0.0

#--------------------------------------------------------------------

%define kplatoworkapp_major 6
%define libkplatoworkapp %mklibname kplatoworkapp %kplatoworkapp_major

%package -n %libkplatoworkapp
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoworkapp
Koffice 2 core library.

%files -n %libkplatoworkapp
%defattr(-,root,root)
%_kde_libdir/libkplatoworkapp.so.%kplatoworkapp_major
%_kde_libdir/libkplatoworkapp.so.%kplatoworkapp_major.0.0
#--------------------------------------------------------------------

%define kplatoworkfactory_major 6
%define libkplatoworkfactory %mklibname kplatoworkfactory %kplatoworkfactory_major

%package -n %libkplatoworkfactory
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoworkfactory
Koffice 2 core library.

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
Conflicts:      kword < 11:2.1.0-4

%description -n kspread
KSpread is a spreadsheet for kde project

%post -n kspread
%{update_desktop_database}


%postun -n kspread
%{clean_desktop_database}

%files -n kspread
%defattr(-,root,root)
%_kde_bindir/kspread
%_kde_libdir/kde4/krossmodulekspread.so
%_kde_libdir/kde4/libkspreadhtmlexport.so
%_kde_libdir/kde4/libkspreadlatexexport.so
%_kde_libdir/kde4/libkspreadpart.so
%_kde_libdir/kde4/libkspreadsolver.so
%_kde_libdir/kde4/kspread*
%_kde_libdir/kde4/spreadsheetshape.so
%_kde_libdir/kde4/libexcelimport.so
%_kde_libdir/libkdeinit4_kspread.so
%_kde_iconsdir/hicolor/*/apps/kspread.png
%_kde_datadir/applications/kde4/kspread.desktop
%_kde_datadir/kde4/services/ServiceMenus/kspread_konqi.desktop
%_kde_appsdir/kspread
%_kde_datadir/config/kspreadrc
%_kde_datadir/config.kcfg/kspread.kcfg
%_kde_docdir/HTML/en/kspread
%_kde_datadir/kde4/services/krossmodulekspread.desktop
%_kde_datadir/kde4/services/kspread*.desktop
%_kde_datadir/kde4/servicetypes/kspread_plugin.desktop
%_kde_datadir/kde4/services/spreadsheetshape.desktop

#--------------------------------------------------------------------

%define kspread_major 6
%define libkspreadcommon %mklibname kspreadcommon %kspread_major

%package -n %libkspreadcommon
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkspreadcommon
Koffice 2 core library.

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
%{update_desktop_database}

%postun -n kpresenter
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
%_kde_libdir/kde4/kpresentereventactions.so 
%_kde_libdir/kde4/kpresentertoolanimation.so
%_kde_libdir/kde4/kprvariables.so
%_kde_libdir/libkdeinit4_kpresenter.so
%_kde_datadir/applications/kde4/kpresenter.desktop
%_kde_datadir/kde4/services/ServiceMenus/kpresenter_konqi.desktop
%_kde_appsdir/kpresenter
%_kde_datadir/config/kpresenterrc
%_kde_iconsdir/hicolor/*/apps/kpresenter.png
%_kde_datadir/kde4/services/kpresenterpart.desktop
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
%_kde_datadir/kde4/services/kpresenter_powerpoint_import.desktop
%_kde_datadir/kde4/services/kpresenter_pptx_import.desktop
%_kde_datadir/kde4/services/kprvariables.desktop
%_kde_datadir/kde4/servicetypes/kpr_pageeffect.desktop
%_kde_datadir/kde4/servicetypes/kpr_shapeanimation.desktop
%_kde_docdir/HTML/en/kpresenter

#--------------------------------------------------------------------

%define kpresenterprivate_major 6
%define libkpresenterprivate %mklibname kpresenterprivate %kpresenterprivate_major

%package -n %libkpresenterprivate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkpresenterprivate
Koffice 2 core library.

%files -n %libkpresenterprivate
%defattr(-,root,root)
%_kde_libdir/libkpresenterprivate.so.%kpresenterprivate_major
%_kde_libdir/libkpresenterprivate.so.%kpresenterprivate_major.0.0

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
Conflicts:	%name-core < 11:1.9.98.2-4

%description -n kchart
Kchart is a chart and diagram drawing program.

%post -n kchart
%{update_desktop_database}


%postun -n kchart
%{update_desktop_database}

%files -n kchart
%defattr(-,root,root)
%_kde_libdir/kde4/chartshape.so
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
%{_kde_appsdir}/kchart
%{_kde_iconsdir}/hicolor/*/apps/kchart.png
%_kde_docdir/HTML/en/kchart

#--------------------------------------------------------------------

%define  kdchart_major 6
%define  libkdchart %mklibname kdchart  %kdchart_major

%package -n %libkdchart
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkdchart
Koffice 2 core library.

%files -n %libkdchart
%defattr(-,root,root)
%_kde_libdir/libkdchart.so.%kdchart_major
%_kde_libdir/libkdchart.so.%kdchart_major.0.0

#--------------------------------------------------------------------

%define  kchartcommon_major 6
%define  libkchartcommon %mklibname kchartcommon %kchartcommon_major

%package -n %libkchartcommon
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkchartcommon
Koffice 2 core library.

%files -n %libkchartcommon
%defattr(-,root,root)
%_kde_libdir/libkchartcommon.so.%kchartcommon_major
%_kde_libdir/libkchartcommon.so.%kchartcommon_major.0.0

#--------------------------------------------------------------------

%package -n katelier
Summary: Krita and karbon meta package
Group: Graphical desktop/KDE
Requires: krita = %{epoch}:%{version}-%{release}
Requires: karbon = %{epoch}:%{version}-%{release}

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
%{update_desktop_database}

%postun -n krita
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
%_kde_datadir/applications/kde4/krita_exr.desktop
%_kde_datadir/applications/kde4/krita_gif.desktop
%_kde_datadir/applications/kde4/krita_jp2.desktop
%_kde_datadir/applications/kde4/krita_ppm.desktop
%_kde_datadir/applications/kde4/krita_psd.desktop
%_kde_datadir/applications/kde4/krita_xcf.desktop
%_kde_datadir/kde4/services/ServiceMenus/krita_konqi.desktop
%_kde_datadir/kde4/services/*krita*.desktop
%_kde_datadir/kde4/servicetypes/*krita*.desktop
%_kde_iconsdir/hicolor/*/apps/krita.png
%_kde_appsdir/krita
%_kde_appsdir/kritaplugins
%_kde_configdir/kritarc
%_kde_datadir/color/icc/krita/*.icm
%_kde_datadir/color/icc/pigment/*.icm
%_kde_datadir/kde4/servicetypes/pigment.desktop
%_kde_appsdir/pigmentcms
%_kde_datadir/mime/packages/krita_ora.xml

#--------------------------------------------------------------------

%define  libkritaui_major 6
%define  libkritaui %mklibname kritaui  %libkritaui_major

%package -n %libkritaui
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritaui
Koffice 2 core library.

%files -n %libkritaui
%defattr(-,root,root)
%_kde_libdir/libkritaui.so.%libkritaui_major
%_kde_libdir/libkritaui.so.%libkritaui_major.0.0

#--------------------------------------------------------------------

%define  libkritaimage_major 6
%define  libkritaimage %mklibname kritaimage  %libkritaimage_major

%package -n %libkritaimage
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritaimage
Koffice 2 core library.

%files -n %libkritaimage
%defattr(-,root,root)
%_kde_libdir/libkritaimage.so.%libkritaimage_major
%_kde_libdir/libkritaimage.so.%libkritaimage_major.0.0

#--------------------------------------------------------------------

%define  libkritalibbrush_major 6
%define  libkritalibbrush %mklibname kritalibbrush  %libkritalibbrush_major

%package -n %libkritalibbrush
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritalibbrush
Koffice 2 core library.

%files -n %libkritalibbrush
%defattr(-,root,root)
%_kde_libdir/libkritalibbrush.so.%{libkritalibbrush_major}*

#--------------------------------------------------------------------

%define  libkritalibpaintop_major 6
%define  libkritalibpaintop %mklibname kritalibpaintop  %libkritalibpaintop_major

%package -n %libkritalibpaintop
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkritalibpaintop
Koffice 2 core library.

%files -n %libkritalibpaintop
%defattr(-,root,root)
%_kde_libdir/libkritalibpaintop.so.%{libkritalibpaintop_major}*

#--------------------------------------------------------------------

%define  libkoplugin_major 6
%define  libkoplugin %mklibname koplugin  %libkoplugin_major

%package -n %libkoplugin
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkoplugin
Koffice 2 core library.

%files -n %libkoplugin
%defattr(-,root,root)
%_kde_libdir/libkoplugin.so.%{libkoplugin_major}*

#--------------------------------------------------------------------
#
%define  libkowidgets_major 6
%define  libkowidgets %mklibname kowidgets  %libkowidgets_major
#
%package -n %libkowidgets
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkowidgets
Koffice 2 core library.

%files -n %libkowidgets
%defattr(-,root,root)
%_kde_libdir/libkowidgets.so.%{libkowidgets_major}*

#--------------------------------------------------------------------
%if 0
%define  libkplatoworkapp_major 6
%define  libkplatoworkapp %mklibname kplatoworkapp  %libkplatoworkapp_major

%package -n %libkplatoworkapp
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoworkapp
Koffice 2 core library.

%files -n %libkplatoworkapp
%defattr(-,root,root)
%_kde_libdir/libkplatoworkapp.so.%{libkplatoworkapp_major}*

#--------------------------------------------------------------------

%define  libkplatoworkfactory_major 6
%define  libkplatoworkfactory %mklibname kplatoworkfactory  %libkplatoworkfactory_major

%package -n %libkplatoworkfactory
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkplatoworkfactory
Koffice 2 core library.

%files -n %libkplatoworkfactory
%defattr(-,root,root)
%_kde_libdir/libkplatoworkfactory.so.%{libkplatoworkfactory_major}*

#--------------------------------------------------------------------

%define  libkrossmodulekrita_major 6
%define  libkrossmodulekrita %mklibname krossmodulekrita  %libkrossmodulekrita_major

%package -n %libkrossmodulekrita
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkrossmodulekrita
Koffice 2 core library.

%files -n %libkrossmodulekrita
%defattr(-,root,root)
%_kde_libdir/libkrossmodulekrita.so.%{libkrossmodulekrita_major}*
%endif

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
%{update_desktop_database}


%postun -n karbon
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
%_kde_libdir/kde4/libkarbonsvgimport.so
%_kde_libdir/kde4/libwmfexport.so
%_kde_libdir/kde4/libwmfimport.so
%_kde_libdir/kde4/libkarbon1ximport.so
%_kde_libdir/kde4/karbon_refinepathplugin.so
%_kde_libdir/kde4/karbon_roundcornersplugin.so
%_kde_libdir/libkdeinit4_karbon.so
%_kde_datadir/applications/kde4/karbon.desktop
%_kde_configdir/karbonrc
%_kde_appsdir/karbon
%_kde_datadir/kde4/services/ServiceMenus/karbon_konqi.desktop
%_kde_docdir/HTML/en/karbon
%_kde_datadir/kde4/services/karbon*.desktop
%_kde_datadir/kde4/servicetypes/karbon_module.desktop
%exclude %_kde_datadir/templates/.source/Illustration.karbon

#--------------------------------------------------------------------

%define  karboncommon_major 6
%define  libkarboncommon %mklibname karboncommon  %karboncommon_major

%package -n %libkarboncommon
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkarboncommon
Koffice 2 core library.

%files -n %libkarboncommon
%defattr(-,root,root)
%_kde_libdir/libkarboncommon.so.%karboncommon_major
%_kde_libdir/libkarboncommon.so.%karboncommon_major.0.0

#--------------------------------------------------------------------

%define  karbonui_major 6
%define  libkarbonui %mklibname karbonui  %karbonui_major

%package -n %libkarbonui
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkarbonui
Koffice 2 core library.

%files -n %libkarbonui
%defattr(-,root,root)
%_kde_libdir/libkarbonui.so.%karbonui_major
%_kde_libdir/libkarbonui.so.%karbonui_major.0.0

#--------------------------------------------------------------------

%package -n kformula
Summary:        Formula Editor for koffice2
Group:          Graphical desktop/KDE
Requires:       %name-core = %{epoch}:%{version}-%{release}
URL:            http://www.koffice.org/
Provides:       %name-kformula = %epoch:%version-%release
Conflicts:      koffice-core < 11:2.0.91

%description -n kformula
Kformula is a formula editor for kde project.

%files -n kformula
%defattr(-,root,root)
%_kde_bindir/kformula
%_kde_libdir/libkdeinit_kformula.so
%_kde_libdir/kde4/formulashape.so
%_kde_libdir/kde4/libkformulapart.so
%_kde_datadir/applications/kde4/kformula.desktop
%_kde_datadir/apps/formulashape
%_kde_datadir/apps/kformula
%_kde_iconsdir/*/*/*/kformula.png
%_kde_datadir/kde4/services/ServiceMenus/kformula_konqi.desktop
%_kde_datadir/kde4/services/formulashape.desktop
%_kde_datadir/kde4/services/kformulapart.desktop
%_kde_docdir/HTML/en/kformula

#--------------------------------------------------------------------

%define libkformulalib_major 6
%define libkformulalib %mklibname kformulalib %libkformulalib_major

%package -n %libkformulalib
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkformulalib
Koffice 2 core library.

%files -n %libkformulalib
%defattr(-,root,root)
%_kde_libdir/libkformulalib.so.%libkformulalib_major
%_kde_libdir/libkformulalib.so.%libkformulalib_major.0.0

#--------------------------------------------------------------------

%define libkformulaprivate_major 6
%define libkformulaprivate %mklibname kformulaprivate %libkformulaprivate_major

%package -n %libkformulaprivate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkformulaprivate
Koffice 2 core library.

%files -n %libkformulaprivate
%defattr(-,root,root)
%_kde_libdir/libkformulaprivate.so.%{libkformulaprivate_major}*

#--------------------------------------------------------------------

%package -n kexi
Summary:    An integrated environment for managing data
Group:      Graphical desktop/KDE
Requires:   koffice-core = %epoch:%version-%release
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Obsoletes:  kexi <= 0.1-0.beta5.5mdk    
Provides:   %name-apps

%description -n kexi
Kexi is an integrated environment for managing data.

%post -n kexi
%{update_desktop_database}

%postun -n kexi
%{update_desktop_database}

%files -n kexi
%defattr(-,root,root)
%{_kde_bindir}/kexi
%{_kde_appsdir}/kexi
%{_kde_datadir}/config/kexirc
%{_kde_services}/kexi
%{_kde_services}/kexidb_mysqldriver.desktop
%{_kde_services}/kexidb_pqxxsqldriver.desktop
%{_kde_services}/kexidb_xbasedriver.desktop
%{_kde_services}/keximigrate_kspread.desktop
%{_kde_services}/keximigrate_mdb.desktop
%{_kde_services}/keximigrate_mysql.desktop
%{_kde_services}/keximigrate_pqxx.desktop
%{_kde_services}/keximigrate_sybase.desktop
%{_kde_services}/keximigrate_txt.desktop
%{_kde_services}/kexirelationdesignshape.desktop
%{_kde_services}/kformdesigner
%{_kde_servicetypes}/widgetfactory.desktop
%{_kde_servicetypes}/kexidb_driver.desktop
%{_kde_servicetypes}/kexihandler.desktop
%{_kde_servicetypes}/keximigration_driver.desktop
%{_kde_applicationsdir}/kexi.desktop
%{_kde_libdir}/kde4/kformdesigner_containers.so
%{_kde_libdir}/kde4/kformdesigner_kexidbwidgets.so
%{_kde_libdir}/kde4/kformdesigner_stdwidgets.so
%{_kde_libdir}/kde4/kexidb_mysqldriver.so
%{_kde_libdir}/kde4/kexidb_pqxxsqldriver.so
%{_kde_libdir}/kde4/kexidb_xbasedriver.so
%{_kde_libdir}/kde4/kexidb_sqlite3driver.so
%{_kde_libdir}/kde4/kexihandler_csv_importexport.so
%{_kde_libdir}/kde4/kexihandler_form.so
%{_kde_libdir}/kde4/kexihandler_migration.so
%{_kde_libdir}/kde4/kexihandler_query.so
%{_kde_libdir}/kde4/kexihandler_script.so
%{_kde_libdir}/kde4/kexihandler_table.so
%{_kde_libdir}/kde4/keximigrate_kspread.so
%{_kde_libdir}/kde4/keximigrate_mdb.so
%{_kde_libdir}/kde4/keximigrate_mysql.so
%{_kde_libdir}/kde4/keximigrate_pqxx.so
%{_kde_libdir}/kde4/keximigrate_sybase.so
%{_kde_libdir}/kde4/keximigrate_txt.so
%{_kde_libdir}/kde4/kexirelationdesignshape.so
%{_kde_libdir}/kde4/krossmodulekexidb.so
%{_kde_libdir}/kde4/kexihandler_report.so

#--------------------------------------------------------------------
   
%define libkexicore_major 6
%define libkexicore %mklibname kexicore %libkexicore_major
   
%package -n %libkexicore
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexicore
Koffice 2 core library.

%files -n %libkexicore
%defattr(-,root,root)
%_kde_libdir/libkexicore.so.%{libkexicore_major}*

#--------------------------------------------------------------------

%define libkexidatatable_major 6 
%define libkexidatatable %mklibname kexidatatable %libkexidatatable_major

%package -n %libkexidatatable
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexidatatable
Koffice 2 core library.

%files -n %libkexidatatable
%defattr(-,root,root)
%_kde_libdir/libkexidatatable.so.%{libkexidatatable_major}*

#--------------------------------------------------------------------

%define libkexidb_major 6
%define libkexidb %mklibname kexidb %libkexidb_major

%package -n %libkexidb
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexidb
Koffice 2 core library.

%files -n %libkexidb
%defattr(-,root,root)
%_kde_libdir/libkexidb.so.%{libkexidb_major}*

#--------------------------------------------------------------------

%define libkexiextendedwidgets_major 6
%define libkexiextendedwidgets %mklibname kexiextendedwidgets %libkexiextendedwidgets_major

%package -n %libkexiextendedwidgets
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexiextendedwidgets
Koffice 2 core library.

%files -n %libkexiextendedwidgets
%defattr(-,root,root)
%_kde_libdir/libkexiextendedwidgets.so.%{libkexiextendedwidgets_major}*

#--------------------------------------------------------------------

%define libkexiformutils_major 6 
%define libkexiformutils %mklibname kexiformutils %libkexiformutils_major

%package -n %libkexiformutils
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexiformutils
Koffice 2 core library.

%files -n %libkexiformutils
%defattr(-,root,root)
%_kde_libdir/libkexiformutils.so.%{libkexiformutils_major}*

#--------------------------------------------------------------------

%define libkeximain_major 6
%define libkeximain %mklibname keximain %libkeximain_major

%package -n %libkeximain
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkeximain
Koffice 2 core library.

%files -n %libkeximain
%defattr(-,root,root)
%_kde_libdir/libkeximain.so.%{libkeximain_major}*

#--------------------------------------------------------------------

%define libkeximigrate_major 6
%define libkeximigrate %mklibname keximigrate %libkeximigrate_major

%package -n %libkeximigrate
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkeximigrate
Koffice 2 core library.

%files -n %libkeximigrate
%defattr(-,root,root)
%_kde_libdir/libkeximigrate.so.%{libkeximigrate_major}*

#--------------------------------------------------------------------

%define libkexirelationsview_major 6
%define libkexirelationsview %mklibname kexirelationsview %libkexirelationsview_major

%package -n %libkexirelationsview
Summary: Koffice 2 core library
Group: System/Libraries

%description -n %libkexirelationsview
Koffice 2 core library.

%files -n %libkexirelationsview
%defattr(-,root,root)
%_kde_libdir/libkexirelationsview.so.%{libkexirelationsview_major}*

#--------------------------------------------------------------------

%define libkexiutils_major 6
%define libkexiutils %mklibname kexiutils %libkexiutils_major
   
%package -n %libkexiutils
Summary: Koffice 2 core library
Group: System/Libraries
   
%description -n %libkexiutils
Koffice 2 core library.
   
%files -n %libkexiutils
%defattr(-,root,root)
%_kde_libdir/libkexiutils.so.%{libkexiutils_major}*

#-------------------------------------------------------------------- 

%define libwv2_major 4
%define libwv2 %mklibname wv2 %libwv2_major
   
%package -n %libwv2
Summary: Koffice 2 core library
Group: System/Libraries
   
%description -n %libwv2
Koffice 2 core library.
   
%files -n %libwv2
%defattr(-,root,root)
%_kde_libdir/libwv2.so.%{libwv2_major}*

#--------------------------------------------------------------------

%define libmsooxml_major 6
%define libmsooxml %mklibname msooxml %libmsooxml_major
   
%package -n %libmsooxml
Summary: Koffice 2 core library
Group: System/Libraries
   
%description -n %libmsooxml
Koffice 2 core library.
   
%files -n %libmsooxml
%defattr(-,root,root)
%_kde_libdir/libmsooxml.so.%{libmsooxml_major}*

#--------------------------------------------------------------------

%define libkrossmodulekrita_major 6
%define libkrossmodulekrita %mklibname krossmodulekrita %libkrossmodulekrita_major
   
%package -n %libkrossmodulekrita
Summary: Koffice 2 core library
Group: System/Libraries
   
%description -n %libkrossmodulekrita
Koffice 2 core library.
   
%files -n %libkrossmodulekrita
%defattr(-,root,root)
%_kde_libdir/libkrossmodulekrita.so.%{libkrossmodulekrita_major}*

#--------------------------------------------------------------------

%define libkoproperty_major 6
%define libkoproperty %mklibname koproperty %libkoproperty_major
   
%package -n %libkoproperty
Summary: Koffice 2 core library
Group: System/Libraries
   
%description -n %libkoproperty
Koffice 2 core library.
   
%files -n %libkoproperty
%defattr(-,root,root)
%_kde_libdir/libkoproperty.so.%{libkoproperty_major}*

#--------------------------------------------------------------------

%define libkformdesigner_major 6
%define libkformdesigner %mklibname kformdesigner %libkformdesigner_major
   
%package -n %libkformdesigner
Summary: Koffice 2 core library
Group: System/Libraries
   
%description -n %libkformdesigner
Koffice 2 core library.
   
%files -n %libkformdesigner
%defattr(-,root,root)
%_kde_libdir/libkformdesigner.so.%{libkformdesigner_major}*

#--------------------------------------------------------------------

%package -n f-office
Summary:    Fremantle Office viewer
Group:      Graphical desktop/KDE
Requires:   koffice-core = %epoch:%version-%release
Provides:   %name-apps

%description -n f-office
Fremantle Office viewer

%files -n f-office
%defattr(-,root,root)
%{_kde_bindir}/FreOffice
%{_kde_datadir}/applications/hildon/FreOffice.desktop
%{_kde_datadir}/dbus-1/services/com.nokia.FreOffice.service
%{_kde_iconsdir}/hicolor/*/hildon
%{_kde_iconsdir}/hicolor/*/apps/freoffice.png

#--------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files for developing koffice2 applications
Requires: %libkokross = %{epoch}:%{version}-%{release}
Requires: %libkomain = %{epoch}:%{version}-%{release}
Requires: %libkopageapp = %{epoch}:%{version}-%{release}
Requires: %libkotext = %{epoch}:%{version}-%{release}
Requires: %libkowmf = %{epoch}:%{version}-%{release}
Requires: %libkoodf = %{epoch}:%{version}-%{release}
Requires: %libkwmf = %{epoch}:%{version}-%{release}
Requires: %libflake = %{epoch}:%{version}-%{release}
Requires: %libpigmentcms = %{epoch}:%{version}-%{release}
Requires: %libkochart = %{epoch}:%{version}-%{release}
Requires: %libkwordexportfilters = %{epoch}:%{version}-%{release}
Requires: %libkwordprivate = %{epoch}:%{version}-%{release}
Requires: %libchartshapelib = %{epoch}:%{version}-%{release}
Requires: %libkspreadcommon = %{epoch}:%{version}-%{release}
Requires: %libkpresenterprivate = %{epoch}:%{version}-%{release}
Requires: %libkdchart = %{epoch}:%{version}-%{release}
Requires: %libkchartcommon = %{epoch}:%{version}-%{release}
Requires: %libkritaui = %{epoch}:%{version}-%{release}
Requires: %libkritaimage = %{epoch}:%{version}-%{release}
Requires: %libkritalibbrush = %{epoch}:%{version}-%{release}
Requires: %libkritalibpaintop = %{epoch}:%{version}-%{release}
Requires: %libkarboncommon = %{epoch}:%{version}-%{release}
Requires: %libkarbonui = %{epoch}:%{version}-%{release}
Requires: %libkoreport = %{epoch}:%{version}-%{release}
Requires: %libkoplugin = %{epoch}:%{version}-%{release}
Requires: %libkowidgets = %{epoch}:%{version}-%{release}
Requires: %libkformulalib = %{epoch}:%{version}-%{release}
Requires: %libkformulaprivate = %{epoch}:%{version}-%{release}
Requires: %name-core = %{epoch}:%{version}-%{release}
Provides: %name-devel = %{epoch}:%{version}-%{release}
Obsoletes: %lib_name-devel
Conflicts: koffice2-kchart < 1.9.95-0.738534.3
Conflicts: karbon < 11:1.9.95.8-3
Conflicts: kchart < 11:1.9.95.8-3
Conflicts: kivio < 11:1.9.95.8-3
Conflicts: kplato < 11:1.9.95.8-3
Conflicts: kpresenter < 11:1.9.95.8-3
Conflicts: krita < 11:1.9.95.8-3
Conflicts: kspread < 11:1.9.95.8-3
Conflicts: koffice-core < 11:1.9.98.5-3
Conflicts: kword < 11:1.9.95.8-3
Obsoletes: koffice2-devel < 1:1.9.95.3-0.766453.6
Provides: koffice2-devel = %epoch:%version-%release

%description devel
Header files needed for developing koffice2 applications.

%files devel
%defattr(-,root,root)
%_kde_bindir/wv2-config
%_kde_appsdir/cmake/*/*
%_kde_libdir/wvWare
%_kde_includedir/*
%_kde_libdir/libchartshapelib.so
%_kde_libdir/libflake.so
%_kde_libdir/libkarboncommon.so
%_kde_libdir/libkarbonui.so
%_kde_libdir/libkchartcommon.so
%_kde_libdir/libkdchart.so
%_kde_libdir/libkochart.so
%_kde_libdir/libkokross.so
%_kde_libdir/libkomain.so
%_kde_libdir/libkoodf.so
%_kde_libdir/libkopageapp.so
%_kde_libdir/libkotext.so
%_kde_libdir/libkowmf.so
%_kde_libdir/libkpresenterprivate.so
%_kde_libdir/libkritaimage.so
%_kde_libdir/libkritaui.so
%_kde_libdir/libkspreadcommon.so
%_kde_libdir/libkwmf.so
%_kde_libdir/libkwordexportfilters.so
%_kde_libdir/libkwordprivate.so
%_kde_libdir/libkplatokernel.so
%_kde_libdir/libkplatomodels.so
%_kde_libdir/libkplatoprivate.so
%_kde_libdir/libkplatoui.so
%_kde_libdir/libkplatoworkapp.so
%_kde_libdir/libkplatoworkfactory.so
%_kde_libdir/libkoreport.so
%_kde_libdir/libpigmentcms.so
%_kde_libdir/libkritalibpaintop.so
%_kde_libdir/libkritalibbrush.so
%_kde_libdir/libkoplugin.so
%_kde_libdir/libkowidgets.so
%_kde_libdir/libkformulalib.so
%_kde_libdir/libkformulaprivate.so
%_kde_libdir/libkexicore.so
%_kde_libdir/libkexidatatable.so
%_kde_libdir/libkexidb.so
%_kde_libdir/libkexiextendedwidgets.so
%_kde_libdir/libkexiformutils.so
%_kde_libdir/libkexiguiutils.so
%_kde_libdir/libkexiguiutils.so.6
%_kde_libdir/libkexiguiutils.so.6.0.0
%_kde_libdir/libkeximain.so
%_kde_libdir/libkeximigrate.so
%_kde_libdir/libkexirelationsview.so
%_kde_libdir/libkexiutils.so
%_kde_libdir/libkformdesigner.so
%_kde_libdir/libkoproperty.so
%_kde_libdir/libkrossmodulekrita.so
%_kde_libdir/libmsooxml.so
%_kde_libdir/libwv2.la
%_kde_libdir/libwv2.so
#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0
%patch1 -p1 -b .krita_disable_painterlyframework
%patch2 -p1 -b .dsolinking
%patch3 -p2 -b .ascii_import_crash

%build
%cmake_kde4 \
	-DBUILD_xbase=FALSE \
	-DFreeTDS_LIBRARIES=-lsybdb \
    -DBUILD_kchart=TRUE -DBUILD_koreport=TRUE

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
