%define _requires_exceptions devel\(libtwopigen\)\\|devel\(libgvrender\)\\|devel\(libcdt\)\\|devel\(libdotgen\)\\|devel\(libcommon\)\\|devel\(libpathplan\)\\|devel\(libneatogen\)\\|devel\(libcircogen\)\\|devel\(libgraph\)\\|devel\(libdotneato\)\\|devel\(libfdpgen\)\\|devel\(libpack\)

%define lib_name_orig %mklibname koffice
%define lib_major 2
%define lib_name %lib_name_orig%lib_major

%define lib_name_orig_kexi %mklibname kexi
%define lib_major_kexi 0
%define lib_name_kexi %lib_name_orig_kexi%lib_major_kexi

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define use_python 1

%define compile_apidox 0

%define krita_kjs_compile 0

Name: koffice
URL: http://www.koffice.org/
Summary: Set of office applications for KDE
Version: 1.6.3
Release: %mkrel 20
Epoch: 11
Source: %name-%version.tar.bz2
Patch0: koffice-1.6.2-fix-desktopfiles.patch
Patch1: koffice-xpdf-CVE-2007-3387.diff
Patch2: koffice-1.6.3-xpdf2-CVE-2007-4352-5392-5393.diff
Patch3: koffice-1.6.2-ubu-CVE-2008-1693.patch
Group: Office
License: GPLv2+
BuildRoot: %_tmppath/%name-%version-kde3-%release-root
BuildRequires: libx11-devel	
BuildRequires: libarts-devel 
BuildRequires: db1-devel 
BuildRequires: diffutils
BuildRequires: freetype2-devel 
BuildRequires: gettext
BuildRequires: binutils-devel 
BuildRequires: bzip2-devel
BuildRequires: libjpeg-devel 
BuildRequires: mng-devel 
BuildRequires: png-devel
BuildRequires: mktemp 
BuildRequires: python-devel
BuildRequires: readline-devel 
BuildRequires: rpm-build 
BuildRequires: texinfo 
BuildRequires: zlib1-devel
BuildRequires: libxslt-devel 
BuildRequires: libxml2-devel >= 2.4.28-2mdk
BuildRequires: kdelibs-devel >= 3.2-13mdk
BuildRequires: kde3-macros
BuildRequires: wv2-devel
BuildRequires: imagemagick-devel 
BuildRequires: libjbig-devel
BuildRequires: aspell-devel >= 0.50.2 
BuildRequires: ruby-devel
BuildRequires: libexif-devel 
BuildRequires: libOpenEXR-devel 
BuildRequires: postgresql-devel 
BuildRequires: libpqxx-devel
BuildRequires: automake1.7
BuildRequires: autoconf2.5
BuildRequires: libart_lgpl-devel
BuildRequires: mysql-devel
BuildRequires: libwpd-devel
BuildRequires: libpoppler-qt-devel
%if %krita_kjs_compile
BuildRequires: kjsembed-devel
%else
BuildConflicts: kjsembed-devel
%endif
%if %compile_apidox
BuildRequires: doxygen
BuildRequires: graphviz
%endif
Conflicts:	koffice <= 1.3-10mdk

Requires:	%name-kword
Requires:	%name-kchart
Requires:	%name-kspread
Requires:	%name-karbon
Requires:	%name-kugar
Requires:	%name-kpresenter
Requires:	%name-kivio
Requires:	%name-kformula
Requires:	%name-koshell
Requires:	%name-kexi
Requires:	%name-krita
Requires:	%name-kplato

%description
Office applications for the K Desktop Environment.

KOffice contains:
   * KWord: word processor
   * KSpread: spreadsheet
   * KPresenter: presentations
   * KChart: chart generator
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

%package common
Group: Office
Summary: Common files for koffice applications
Conflicts: %lib_name <= 1.3-10mdk
Obsoletes: %lib_name
Obsoletes: koffice-progs
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: kexi <= 0.1-0.beta4.3mdk
Conflicts: %lib_name-progs < 11:1.6.3-18
Requires: wordnet
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils
Requires: koffice-l10n

%description common
Common files for koffice applications.

%files common
%defattr(-,root,root)
%doc %_docdir/*/*/koffice
%doc %_docdir/*/*/thesaurus
%_kde3_iconsdir/*/*/actions/*
%_kde3_iconsdir/*/*/mimetypes/*
%_kde3_bindir/koconverter
%_kde3_bindir/kthesaurus
%_kde3_libdir/libkdeinit_kthesaurus.*
%_kde3_libdir/kde3/kthesaurus.*
%_kde3_libdir/kde3/kfile_*
%_kde3_libdir/kde3/clipartthumbnail.*
%_kde3_libdir/kde3/kofficethumbnail.*
%_kde3_libdir/kde3/kodocinfopropspage.*
%_kde3_libdir/kde3/kofficescan.*
%_kde3_libdir/kde3/libgenerickofilter.*
%_kde3_libdir/kde3/libkfolatexexport.*
%_kde3_libdir/kde3/libkfomathmlexport.*
%_kde3_libdir/kde3/libkfomathmlimport.*
%_kde3_libdir/kde3/libkfopngexport.*
%_kde3_libdir/kde3/libkounavailpart.*
%_kde3_libdir/kde3/libthesaurustool.*
%_kde3_libdir/kde3/libxsltexport.*
%_kde3_libdir/kde3/libxsltimport.*
%_kde3_libdir/kde3/krosspython.*
%_kde3_libdir/kde3/krossruby.*
%_kde3_datadir/services/kfile_*
%_kde3_datadir/applnk/Office/KThesaurus.desktop
%_kde3_datadir/applications/kde/koffice.desktop
%dir %_kde3_appsdir/koffice/
%_kde3_appsdir/koffice/*
%dir %_kde3_appsdir/xsltfilter
%_kde3_appsdir/xsltfilter/*
%dir %_kde3_appsdir/thesaurus/
%_kde3_appsdir/thesaurus/*
%_kde3_datadir/services/clipartthumbnail.desktop
%_kde3_datadir/services/generic_filter.desktop
%_kde3_datadir/services/kodocinfopropspage.desktop
%_kde3_datadir/services/kofficethumbnail.desktop
%_kde3_datadir/services/kounavail.desktop
%_kde3_datadir/services/thesaurustool.desktop
%_kde3_datadir/services/xslt_export.desktop
%_kde3_datadir/services/xslt_import.desktop
%dir %_kde3_datadir/servicetypes/
%_kde3_datadir/servicetypes/kochart.desktop
%_kde3_datadir/servicetypes/kofficepart.desktop
%_kde3_datadir/servicetypes/kofilter.desktop
%_kde3_datadir/servicetypes/kofilterwrapper.desktop
%_kde3_datadir/servicetypes/koplugin.desktop
%_kde3_appsdir/kross/python
%dir %_kde3_datadir/templates/
%_kde3_appsdir/kofficewidgets/pics/*.png

#--------------------------------------------------------------------

%package -n %lib_name-common
Group: Development/KDE and Qt
Summary: Library files for Koffice
Conflicts: %lib_name <= 1.3-10mdk
Obsoletes: %lib_name
Conflicts: koffice <= %epoch:1.2.1-9mdk
Obsoletes: %lib_name-progs < 11:1.6.3-18

%description -n %lib_name-common
Library files for Koffice.

%post -n %lib_name-common -p /sbin/ldconfig
%postun -n %lib_name-common -p /sbin/ldconfig

%files -n %lib_name-common
%defattr(-,root,root)
%_kde3_libdir/libkrossapi.la
%_kde3_libdir/libkrossapi.so.*
%_kde3_libdir/libkstore.la
%_kde3_libdir/libkwmf.la
%_kde3_libdir/libkofficecore.la
%_kde3_libdir/libkofficeui.la
%_kde3_libdir/libkotext.la
%_kde3_libdir/libkopainter.la
%_kde3_libdir/libkochart.la
%_kde3_libdir/libkowmf.la
%_kde3_libdir/libkopalette.la
%_kde3_libdir/libkopalette.so.*
%_kde3_libdir/libkofficecore.so.*
%_kde3_libdir/libkofficeui.so.*
%_kde3_libdir/libkotext.so.*
%_kde3_libdir/libkopainter.so.*
%_kde3_libdir/libkochart.so.*
%_kde3_libdir/libkstore.so.*
%_kde3_libdir/libkwmf.so.*
%_kde3_libdir/libkowmf.so.*
%_kde3_libdir/libkoproperty.la
%_kde3_libdir/libkoproperty.so.*
%_kde3_libdir/libkrossmain.la
%_kde3_libdir/libkrossmain.so.*

#--------------------------------------------------------------------

%package kword
Summary: Word processor for koffice
Group: Graphical desktop/KDE
Requires: koffice-common = %epoch:%version-%release
Provides: kword
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-kword < 11:1.6.3-18
Requires: wordnet
Requires: %name-kformula
Provides: %name-apps

%description kword
Kword is a word processor for kde project

%post kword
%update_menus
%{update_desktop_database}

%postun kword
%clean_menus
%{clean_desktop_database}

%files kword
%defattr(-,root,root)
%doc %_docdir/*/*/kword
%_kde3_iconsdir/*/*/*/kword.png
%_kde3_bindir/kword
%_kde3_datadir/applications/kde/kword.desktop
%dir %_kde3_appsdir/kword
%_kde3_appsdir/kword/*
%_kde3_datadir/services/kwordpart.desktop
%_kde3_datadir/services/kwserialletter_classic.desktop
%_kde3_datadir/services/kwserialletter_qtsqldb_power.desktop
%_kde3_datadir/services/kword_*
%_kde3_datadir/services/kwmailmerge_kabc.desktop
%_kde3_datadir/services/kwmailmerge_kspread.desktop
%_kde3_datadir/servicetypes/kwmailmerge.desktop
%_kde3_appsdir/xsltfilter/export/kword
%_kde3_appsdir/konqueror/servicemenus/kword*
%_kde3_libdir/kde3/libkword*
%_kde3_libdir/kde3/kwmailmerge_*
%_kde3_libdir/kde3/libabiwordexport.*
%_kde3_libdir/kde3/libabiwordimport.*
%_kde3_libdir/kde3/libamiproexport.*
%_kde3_libdir/kde3/libamiproimport.*
%_kde3_libdir/kde3/libapplixwordimport.*
%_kde3_libdir/kde3/libasciiexport.*
%_kde3_libdir/kde3/libasciiimport.*
%_kde3_libdir/kde3/libdocbookexport.*
%_kde3_libdir/kde3/libhtmlexport.*
%_kde3_libdir/kde3/libhtmlimport.*
%_kde3_libdir/kde3/libmswordimport.*
%_kde3_libdir/kde3/libmswriteexport.*
%_kde3_libdir/kde3/libmswriteimport.*
%_kde3_libdir/kde3/liboowriterexport.*
%_kde3_libdir/kde3/liboowriterimport.*
%_kde3_libdir/kde3/libpalmdocexport.*
%_kde3_libdir/kde3/libpalmdocimport.*
%_kde3_libdir/kde3/librtfexport.*
%_kde3_libdir/kde3/librtfimport.*
%_kde3_libdir/kde3/libwmlexport.*
%_kde3_libdir/kde3/libwmlimport.*
%_kde3_libdir/kde3/libwpexport.*
%_kde3_libdir/kde3/kword*
%_kde3_libdir/kde3/libpdfimport.*
%_kde3_libdir/kde3/libwpimport.*
%_kde3_libdir/libkdeinit_kword.*
%_kde3_datadir/templates/TextDocument.desktop
%_kde3_datadir/templates/.source/TextDocument.kwt

#--------------------------------------------------------------------

%package -n %lib_name-kword
Group:		Development/KDE and Qt
Summary:	Libraries files for KWord
Conflicts:	koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-progs < 11:1.6.3-18

%description -n %lib_name-kword
Libraries file for KWord

%post -n %lib_name-kword -p /sbin/ldconfig
%postun -n %lib_name-kword -p /sbin/ldconfig

%files -n %lib_name-kword
%defattr(-,root,root)
%_kde3_libdir/libkwordexportfilters.la
%_kde3_libdir/libkwordexportfilters.so.*
%_kde3_libdir/libkwmailmerge_interface.la   
%_kde3_libdir/libkwmailmerge_interface.so.*
%_kde3_libdir/libkwordprivate.la
%_kde3_libdir/libkwordprivate.so.*

#--------------------------------------------------------------------

%package kplato
Summary: A new project management application for koffice
Group: Graphical desktop/KDE
Requires: koffice-common = %epoch:%version-%release
Provides: kplato
Conflicts: koffice <= %epoch:1.2.1-9mdk
Provides: %name-apps
Obsoletes: %lib_name-kplato

%description kplato
A new project management application for koffice.

%post kplato
%update_menus
%{update_desktop_database}

%postun kplato
%clean_menus
%{update_desktop_database}

%files kplato
%defattr(-,root,root)
%doc %_docdir/*/*/kplato
%_kde3_iconsdir/*/*/*/kplato.*
%_kde3_bindir/kplato
%_kde3_libdir/kde3/kplato.*
%_kde3_libdir/kde3/libkplatopart.*
%_kde3_libdir/libkdeinit_kplato.*
%_kde3_datadir/applications/kde/kplato.desktop
%dir %_kde3_appsdir/kplato
%_kde3_appsdir/kplato/*
%_kde3_datadir/services/kplatopart.desktop

#--------------------------------------------------------------------

%package kspread
Summary:	SpreadSheet for koffice
Group:		Graphical desktop/KDE
Requires: koffice-common = %epoch:%version-%release
Provides:	kspread
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-spread < 11:1.6.3-18
Provides:   %name-apps

%description kspread
KSpread is a spreadsheet for kde project

%post kspread
%update_menus
%{update_desktop_database}


%postun kspread
%clean_menus
%{clean_desktop_database}

%files kspread
%defattr(-,root,root)
%doc %_docdir/*/*/kspread
%_kde3_iconsdir/*/*/*/kspread.png
%_kde3_bindir/kspread
%_kde3_libdir/kde3/krosskspreadcore.*
%_kde3_libdir/kde3/kspreadscripting.*
%_kde3_libdir/kde3/libexcelimport.*
%_kde3_libdir/kde3/libapplixspreadimport.*
%_kde3_libdir/kde3/libcsvexport.*
%_kde3_libdir/kde3/libcsvimport.*
%_kde3_libdir/kde3/libdbaseimport.*
%_kde3_libdir/kde3/libgnumericexport.*
%_kde3_libdir/kde3/libgnumericimport.*
%_kde3_libdir/kde3/libopencalcexport.*
%_kde3_libdir/kde3/libopencalcimport.*
%_kde3_libdir/kde3/libqproimport.*
%_kde3_libdir/kde3/libhancomwordimport.*
%_kde3_libdir/kde3/libkspread*
%_kde3_libdir/kde3/kspread.*
%_kde3_libdir/libkdeinit_kspread.*
%dir %_kde3_appsdir/kspread/
%_kde3_appsdir/kspread/*
%_kde3_datadir/applications/kde/kspread.desktop
%_kde3_datadir/services/kspread*
%_kde3_appsdir/konqueror/servicemenus/kspread*
%_kde3_datadir/templates/SpreadSheet.desktop
%_kde3_datadir/templates/.source/SpreadSheet.kst

#--------------------------------------------------------------------

%package kchart
Summary: Chart for koffice
Group: Graphical desktop/KDE
Obsoletes: %name-progs
Requires: koffice-common = %epoch:%version-%release
Provides: kchart
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-kchart < 11:1.6.3-18
Provides: %name-apps

%description kchart
KChart is a chart for kde project

%post kchart
%update_menus
%{update_desktop_database}

%postun kchart
%clean_menus
%{clean_desktop_database}

%files kchart
%defattr(-,root,root)
%doc %_docdir/HTML/en/kchart
%_kde3_iconsdir/*/*/*/kchart.png
%_kde3_bindir/kchart
%_kde3_libdir/kde3/kchart.*
%_kde3_libdir/kde3/libkchart*
%_kde3_libdir/libkdeinit_kchart.*
%dir %_kde3_appsdir/kchart/
%_kde3_appsdir/kchart/*
%_kde3_datadir/applications/kde/kchart.desktop
%_kde3_datadir/services/kchart_*
%_kde3_datadir/services/kchartpart.desktop
%_kde3_appsdir/konqueror/servicemenus/kchart*

#--------------------------------------------------------------------

%package -n %lib_name-kspread
Group: Development/KDE and Qt
Summary: Libraries files for KSpread
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-progs < 11:1.6.3-18
Conflicts: %lib_name-kchart < 11:1.6.3-18

%description -n %lib_name-kspread
Libraries file for KSpread

%post -n %lib_name-kspread -p /sbin/ldconfig
%postun -n %lib_name-kspread -p /sbin/ldconfig

%files -n %lib_name-kspread
%defattr(-,root,root)
%_kde3_libdir/libkspreadcommon.la
%_kde3_libdir/libkspreadcommon.so.*

#--------------------------------------------------------------------

%package -n %lib_name-kchart
Group: Development/KDE and Qt
Summary: Libraries files for KChart
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-kspread < 11:1.6.3-18
Conflicts: %lib_name-progs < 11:1.6.3-18

%description -n %lib_name-kchart
Libraries file for KChart.

%post -n %lib_name-kchart -p /sbin/ldconfig
%postun -n %lib_name-kchart -p /sbin/ldconfig

%files -n %lib_name-kchart
%defattr(-,root,root)
%_kde3_libdir/libkchartimageexport.la
%_kde3_libdir/libkchartimageexport.so.*
%_kde3_libdir/libkdchart.la
%_kde3_libdir/libkdchart.so.*
%_kde3_libdir/libkchartcommon.la
%_kde3_libdir/libkchartcommon.so.*

#--------------------------------------------------------------------

%package kpresenter
Summary:	Presentation for koffice
Group:		Graphical desktop/KDE
Requires: koffice-common = %epoch:%version-%release
Provides:	kpresenter
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-kpresenter < 11:1.6.3-18
Requires:   %name-kformula
Requires:	xdg-utils
Provides:   %name-apps

%description kpresenter
KPresenter is a presentation for kde project.

%post kpresenter
%update_menus
%{update_desktop_database}

%postun kpresenter
%clean_menus
%{clean_desktop_database}


%files kpresenter
%defattr(-,root,root)
%doc %_docdir/*/*/kpresenter
%_kde3_iconsdir/*/*/*/kpresenter.png
%_kde3_bindir/kprconverter.pl
%_kde3_bindir/kpresenter
%_kde3_libdir/libkdeinit_kpresenter.*
%_kde3_datadir/services/ole_powerpoint97_import.desktop
%_kde3_datadir/services/kpresenter*
%dir %_kde3_appsdir/kpresenter
%_kde3_appsdir/kpresenter/*
%_kde3_datadir/applications/kde/kpresenter.desktop
%_kde3_datadir/services/kprkword.desktop
%_kde3_libdir/kde3/libolefilter.*
%_kde3_libdir/kde3/libkpresenter*
%_kde3_libdir/kde3/libkprkword.*
%_kde3_libdir/kde3/libooimpressexport.*
%_kde3_libdir/kde3/libooimpressimport.*
%_kde3_libdir/kde3/kpresenter.*
%_kde3_datadir/templates/Presentation.desktop
%_kde3_datadir/templates/.source/Presentation.kpt
%_kde3_appsdir/konqueror/servicemenus/kpresenter*

#--------------------------------------------------------------------

%package -n %lib_name-kpresenter
Group: Development/KDE and Qt
Summary: Libraries files for KPresenter
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-progs < 11:1.6.3-18

%description -n %lib_name-kpresenter
Libraries file for KPresenter

%post -n %lib_name-kpresenter -p /sbin/ldconfig
%postun -n %lib_name-kpresenter -p /sbin/ldconfig

%files -n %lib_name-kpresenter
%defattr(-,root,root)
%_kde3_libdir/libkpresenterimageexport.la
%_kde3_libdir/libkpresenterimageexport.so.*
%_kde3_libdir/libkpresenterprivate.la
%_kde3_libdir/libkpresenterprivate.so.*

#--------------------------------------------------------------------

%package kformula
Summary:	Formula for koffice
Group:		Graphical desktop/KDE
Requires:	%name-common = %epoch:%version-%release
Provides:	kformula
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-kformula < 11:1.6.3-18
Provides:   %name-apps

%description kformula
KFormula is a formula for kde project.

%post kformula
%update_menus
%{update_desktop_database}


%postun kformula
%clean_menus
%{clean_desktop_database}


%files kformula
%defattr(-,root,root)
%doc %_docdir/*/*/kformula
%_kde3_iconsdir/*/*/*/kformula.*
%_kde3_bindir/kformula
%_kde3_libdir/kde3/libkformulapart.*
%_kde3_libdir/kde3/kformula.*
%_kde3_libdir/libkdeinit_kformula.*
%dir %_kde3_appsdir/kformula
%_kde3_appsdir/kformula/*
%_kde3_datadir/applications/kde/kformula.desktop
%_kde3_datadir/services/kformula*
%_kde3_appsdir/konqueror/servicemenus/kformula*

#--------------------------------------------------------------------

%package -n %lib_name-kformula
Group: Development/KDE and Qt
Summary: Libraries files for KFormula
Requires: fonts-ttf-latex
Conflicts: %lib_name-progs < 11:1.6.3-18

Conflicts:  koffice <= %epoch:1.2.1-9mdk

%description -n %lib_name-kformula
Libraries file for KFormula

%post -n %lib_name-kformula -p /sbin/ldconfig
%postun -n %lib_name-kformula -p /sbin/ldconfig

%files -n %lib_name-kformula
%defattr(-,root,root)
%_kde3_libdir/libkformulalib.la
%_kde3_libdir/libkformulalib.so.*

#--------------------------------------------------------------------

%package koshell
Summary:	Koshell for koffice
Group:		Graphical desktop/KDE
Requires: koffice-common = %epoch:%version-%release
Provides:	koshell
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-progs < 11:1.6.3-18
Provides:   %name-apps
Obsoletes: %lib_name-koshell

%description koshell
Koshell for kde project.

%post koshell
%update_menus

%postun koshell
%clean_menus


%files koshell
%defattr(-,root,root)
%doc %_docdir/*/*/koshell
%_kde3_iconsdir/*/*/*/koshell.*
%_kde3_bindir/koshell
%_kde3_libdir/libkdeinit_koshell.*
%_kde3_libdir/kde3/koshell.*
%_kde3_datadir/applications/kde/koshell.desktop
%_kde3_datadir/config.kcfg/koshell.kcfg
%dir %_kde3_appsdir/koshell
%_kde3_appsdir/koshell/*

#--------------------------------------------------------------------

%package kivio
Summary:	Diagramme for koffice
Group:		Graphical desktop/KDE
Requires: koffice-common = %epoch:%version-%release
Provides:	kivio
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-kivio < 11:1.6.3-18
Provides:   %name-apps

%description kivio
Kivio is a diagramme for kde project.

%post kivio
%update_menus
%{update_desktop_database}


%postun kivio
%clean_menus
%{update_desktop_database}

%files kivio
%defattr(-,root,root)
%doc %_docdir/*/*/kivio
%_kde3_iconsdir/*/*/*/kivio.png
%_kde3_bindir/kivio
%_kde3_libdir/libkdeinit_kivio.*
%_kde3_libdir/kde3/kivio*
%_kde3_libdir/kde3/libkivio*
%_kde3_libdir/kde3/straight_connector.*
%_kde3_datadir/services/kivio*
%_kde3_datadir/applications/kde/kivio.desktop
%_kde3_datadir/config.kcfg/kivio.kcfg
%dir %_kde3_appsdir/kivio
%_kde3_appsdir/kivio/*
%_kde3_appsdir/konqueror/servicemenus/kivio*

#--------------------------------------------------------------------

%package -n %lib_name-kivio
Group: Development/KDE and Qt
Summary: Libraries files for kivio
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-progs < 11:1.6.3-18

%description -n %lib_name-kivio
Libraries file for kivio

%post -n %lib_name-kivio -p /sbin/ldconfig
%postun -n %lib_name-kivio -p /sbin/ldconfig

%files -n %lib_name-kivio
%defattr(-,root,root)
%_kde3_libdir/libkiviocommon.la
%_kde3_libdir/libkiviocommon.so.*

#--------------------------------------------------------------------

%package karbon
Summary:	Scalable drawing for koffice
Group:		Graphical desktop/KDE
Requires:	%name-common = %epoch:%version-%release
Provides:	karbon
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-karbon < 11:1.6.3-18
Provides:   %name-apps

%description karbon
Karbon is a scalable drawing for kde project.

%post karbon
%update_menus
%{update_desktop_database}


%postun karbon
%clean_menus
%{update_desktop_database}


%files karbon
%defattr(-,root,root)
%doc %_docdir/*/*/karbon
%_kde3_iconsdir/*/*/*/karbon.*
%_kde3_bindir/karbon
%_kde3_libdir/kde3/libkfosvgexport.*
%_kde3_libdir/kde3/liboodrawimport.*
%_kde3_libdir/kde3/libkarbon*
%_kde3_libdir/kde3/libwmfexport.*
%_kde3_libdir/kde3/libwmfimport.*
%_kde3_libdir/kde3/karbon*
%_kde3_libdir/libkdeinit_karbon.*
%dir %_kde3_appsdir/karbon
%_kde3_appsdir/karbon/*
%_kde3_datadir/services/karbon*
%_kde3_datadir/applications/kde/karbon.desktop
%_kde3_datadir/servicetypes/karbon_module.desktop
%_kde3_datadir/templates/Illustration.desktop  
%_kde3_datadir/templates/.source/Illustration.karbon
%_kde3_appsdir/konqueror/servicemenus/karbon*

#--------------------------------------------------------------------

%package -n %lib_name-karbon
Group: Development/KDE and Qt
Summary: Libraries files for KArbon
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-progs < 11:1.6.3-18

%description -n %lib_name-karbon
Libraries file for KArbon

%post -n %lib_name-karbon -p /sbin/ldconfig
%postun -n %lib_name-karbon -p /sbin/ldconfig

%files -n %lib_name-karbon
%defattr(-,root,root)
%_kde3_libdir/libkarboncommon.la
%_kde3_libdir/libkarboncommon.so.*

#--------------------------------------------------------------------

%package krita
Summary: A pixel-based image manipulation program
Group: Graphical desktop/KDE
Requires: koffice-common = %epoch:%version-%release
Provides: krita
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-krita < 11:1.6.3-18
Provides: %name-apps
Obsoletes: krita-plugins
Obsoletes: %lib_name-krita-kjsembed

%description krita
Krita is a pixel-based image manipulation program.

%post krita
%update_menus
%{update_desktop_database}

%postun krita
%clean_menus
%{update_desktop_database}

%files krita
%defattr(-,root,root)
%doc %_docdir/*/*/krita
%_kde3_iconsdir/*/*/*/krita.png
%_kde3_bindir/krita
%dir %_kde3_appsdir/krita
%_kde3_appsdir/krita/*
%dir %_kde3_appsdir/kritaplugins
%_kde3_appsdir/kritaplugins/*
%_kde3_libdir/kde3/krosskritacore.*
%_kde3_libdir/libkdeinit_krita.*
%_kde3_libdir/kde3/libkrita*
%_kde3_libdir/kde3/krita*
%if %krita_kjs_compile
%_kde3_libdir/kde3/kritakjsembed.*
%endif
%_kde3_datadir/services/krita*
%_kde3_datadir/servicetypes/krita_*
%_kde3_datadir/applnk/.hidden/krita_*
%_kde3_datadir/applications/kde/krita.desktop
%_kde3_appsdir/konqueror/servicemenus/krita*

#--------------------------------------------------------------------

%package -n %lib_name-krita
Group:		Development/KDE and Qt
Summary:	Libraries files for Krita
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-progs < 11:1.6.3-18

%description -n %lib_name-krita
Libraries file for Krita

%post -n %lib_name-krita -p /sbin/ldconfig
%postun -n %lib_name-krita -p /sbin/ldconfig

%files -n %lib_name-krita
%defattr(-,root,root)
%_kde3_libdir/libkrita*.so.*
%_kde3_libdir/libkrita*.la

#--------------------------------------------------------------------

%package kexi
Summary:    An integrated environment for managing data
Group:	    Graphical desktop/KDE
Requires: koffice-common = %epoch:%version-%release
Provides:   kexi >= %epoch:%version-%release
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Obsoletes:  kexi <= 0.1-0.beta5.5mdk	
Provides:   %name-apps
Requires:   keximdb 

%description kexi
Kexi is an integrated environment for managing data.

%post kexi
%update_menus
%{update_desktop_database}

%postun kexi
%clean_menus
%{update_desktop_database}

%files kexi
%defattr(-,root,root)
%doc %_docdir/*/*/kexi
%_kde3_iconsdir/*/*/*/kexi.*
%_kde3_bindir/kexi
%_kde3_bindir/ksqlite
%_kde3_bindir/ksqlite2
%_kde3_bindir/ksqlite2to3
%_kde3_bindir/kexi_*
%_kde3_bindir/krossrunner
%_kde3_libdir/libkdeinit_kexi.*
%_kde3_libdir/kde3/kexi*
%_kde3_libdir/kde3/libkspreadkexiimport.*
%_kde3_libdir/kde3/kformdesigner_*
%dir %_kde3_appsdir/kexi
%_kde3_appsdir/kexi/*
%_kde3_datadir/mimelnk/application/x-kexi-connectiondata.desktop
%_kde3_datadir/services/kexi
%_kde3_datadir/services/kexidb*
%_kde3_datadir/services/keximigrate*
%_kde3_datadir/services/kformdesigner
%_kde3_datadir/applications/kde/kexi.desktop
%_kde3_datadir/servicetypes/widgetfactory.desktop
%_kde3_datadir/locale/*/*/kexi*
%_kde3_datadir/services/kspread_kexi_import.desktop
%_kde3_datadir/mimelnk/application/x-kexiproject-*
%_kde3_datadir/servicetypes/kexi*
%_kde3_datadir/config/kexirc
%_kde3_datadir/config/magic/kexi.magic
%_kde3_libdir/kde3/krosskexiapp.*
%_kde3_libdir/kde3/krosskexidb.*
%_kde3_appsdir/konqueror/servicemenus/kexi*

#--------------------------------------------------------------------

%package -n %lib_name-kexi
Group:		Development/KDE and Qt
Summary:	Libraries files for Kexi
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Obsoletes: %lib_name_kexi <= 0.1-0.beta5.5mdk	
Provides: %lib_name_kexi
Conflicts: %lib_name-progs < 11:1.6.3-18

%description -n %lib_name-kexi
Libraries file for Kexi

%post -n %lib_name-kexi -p /sbin/ldconfig
%postun -n %lib_name-kexi -p /sbin/ldconfig

%files -n %lib_name-kexi
%defattr(-,root,root)
%_kde3_libdir/libkexi*.la
%_kde3_libdir/libkexi*.so.*
%_kde3_libdir/libkformdesigner.la
%_kde3_libdir/libkformdesigner.so.*

#--------------------------------------------------------------------

%package kugar
Summary: Kugar for koffice
Group: Graphical desktop/KDE
Requires: %name-common = %epoch:%version-%release
Provides: kugar
Conflicts: koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-kugar < 11:1.6.3-18
Provides: %name-apps

%description kugar
Kugar for kde project.

%post kugar
%update_menus
%{update_desktop_database}

%postun kugar
%clean_menus
%{update_desktop_database}

%files kugar
%defattr(-,root,root)
%doc %_docdir/*/*/kugar
%_kde3_iconsdir/*/*/*/kudesigner.*
%_kde3_bindir/kudesigner
%_kde3_bindir/kugar
%_kde3_libdir/libkdeinit_kudesigner.*
%_kde3_libdir/libkdeinit_kugar.*
%_kde3_libdir/kde3/libkudesign*
%_kde3_libdir/kde3/libkugar*
%_kde3_libdir/kde3/kudesigner*
%_kde3_libdir/kde3/kugar.*
%_kde3_iconsdir/*/*/*/kugar.png
%dir %_kde3_appsdir/kugar
%_kde3_appsdir/kugar/*
%dir %_kde3_appsdir/kudesigner
%_kde3_appsdir/kudesigner/*
%_kde3_datadir/services/kugar_kugar_import.desktop
%_kde3_datadir/services/kugarpart.desktop
%_kde3_datadir/applications/kde/kugar.desktop
%_kde3_datadir/applications/kde/kudesigner.desktop

#--------------------------------------------------------------------

%package -n %lib_name-kugar
Group:		Development/KDE and Qt
Summary:	Libraries files for Kugar
Conflicts:  koffice <= %epoch:1.2.1-9mdk
Conflicts: %lib_name-progs < 11:1.6.3-18

%description -n %lib_name-kugar
Libraries file for Kugar

%post -n %lib_name-kugar -p /sbin/ldconfig
%postun -n %lib_name-kugar -p /sbin/ldconfig

%files -n %lib_name-kugar
%defattr(-,root,root)
%_kde3_libdir/libkudesignercore.la*
%_kde3_libdir/libkudesignercore.so*
%_kde3_libdir/libkugarlib.la
%_kde3_libdir/libkugarlib.so.*

#--------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Development files for koffice
Conflicts: koffice <= %epoch:1.2.1-9mdk
Obsoletes: %lib_name-krita-devel
Obsoletes: %lib_name-kexi-devel
Obsoletes: %lib_name-kugar-devel
Obsoletes: %lib_name-progs-devel
Obsoletes: %lib_name-kword-devel
Obsoletes: %lib_name-kspread-devel
Obsoletes: %lib_name-kpresenter-devel
Obsoletes: %lib_name-kformula-devel
Obsoletes: %lib_name-kivio-devel
Obsoletes: %lib_name-karbon-devel
Requires: %lib_name-common = %epoch:%{version}-%{release}
Requires: %lib_name-krita = %epoch:%version
Requires: %lib_name-kexi = %epoch:%version
Requires: %lib_name-kugar = %epoch:%version
Requires: %lib_name-common = %epoch:%version
Requires: %lib_name-kword = %epoch:%version
Requires: %lib_name-kspread = %epoch:%version
Requires: %lib_name-kpresenter = %epoch:%version
Requires: %lib_name-kformula = %epoch:%version
Requires: %lib_name-kivio = %epoch:%version
Requires: %lib_name-karbon = %epoch:%version

%description devel
Development files for koffice.

%files devel
%defattr(-,root,root)
%_kde3_libdir/*.so
%exclude %_kde3_libdir/libkudesignercore.so
%_kde3_includedir/*
%if %compile_apidox
%doc %_docdir/*/*/koffice-apidocs
%endif
%exclude %_kde3_libdir/libkdeinit_*

#--------------------------------------------------------------------

%prep

%setup -q 
%patch0 -p0 -b .categories
%patch1 -p0 -b .cve_kpdf
%patch2 -p0 -b .cve_kpdf
%patch3 -p1 -b .cve-2008-1693

%build
export QTDIR=%{qt3dir}
export KDEDIR=%_kde3_prefix

%configure_kde3 --disable-static 

%make

%if %compile_apidox
make apidox
%endif

%install
rm -fr %buildroot

%makeinstall

perl -pi -e "s|Icon=kudesigner|Icon=text_tools_section.png|" %buildroot/%_kde3_datadir/applications/kde/kudesigner.desktop
perl -pi -e "s|Icon=kthesaurus|Icon=office_accessories_section.png|" %buildroot/%_kde3_datadir/applnk/Office/KThesaurus.desktop

rm -f %buildroot/%_kde3_appsdir/kontour/kpartplugins/scan-kontour.rc
rm -f %buildroot/%_kde3_datadir/mimelnk/image/x-raw.desktop

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



