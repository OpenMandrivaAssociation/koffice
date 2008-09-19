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

%define unstable 0
%{?_unstable: %{expand: %%global unstable 1}}

%if %unstable
%define dont_strip 1
%endif

%define subrel	2

Name: koffice
URL: http://www.koffice.org/
Summary: Set of office applications for KDE
Version: 1.6.3
Release: %mkrel 19
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
BuildRequires: doxygen, graphviz
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
%_datadir/icons/*/*/actions/*
%_datadir/icons/*/*/mimetypes/*
%_bindir/koconverter
%_bindir/kthesaurus
%_libdir/libkdeinit_kthesaurus.*
%_libdir/kde3/kthesaurus.*
%_libdir/kde3/kfile_*
%_libdir/kde3/clipartthumbnail.*
%_libdir/kde3/kofficethumbnail.*
%_libdir/kde3/kodocinfopropspage.*
%_libdir/kde3/kofficescan.*
%_libdir/kde3/libgenerickofilter.*
%_libdir/kde3/libkfolatexexport.*
%_libdir/kde3/libkfomathmlexport.*
%_libdir/kde3/libkfomathmlimport.*
%_libdir/kde3/libkfopngexport.*
%_libdir/kde3/libkounavailpart.*
%_libdir/kde3/libthesaurustool.*
%_libdir/kde3/libxsltexport.*
%_libdir/kde3/libxsltimport.*
%_libdir/kde3/krosspython.*
%_libdir/kde3/krossruby.*
%_datadir/services/kfile_*
%_datadir/applnk/Office/KThesaurus.desktop
%_datadir/applications/kde/koffice.desktop
%dir %_datadir/apps/koffice/
%_datadir/apps/koffice/*
%dir %_datadir/apps/xsltfilter
%_datadir/apps/xsltfilter/*
%dir %_datadir/apps/thesaurus/
%_datadir/apps/thesaurus/*
%_datadir/services/clipartthumbnail.desktop
%_datadir/services/generic_filter.desktop
%_datadir/services/kodocinfopropspage.desktop
%_datadir/services/kofficethumbnail.desktop
%_datadir/services/kounavail.desktop
%_datadir/services/thesaurustool.desktop
%_datadir/services/xslt_export.desktop
%_datadir/services/xslt_import.desktop
%dir %_datadir/servicetypes/
%_datadir/servicetypes/kochart.desktop
%_datadir/servicetypes/kofficepart.desktop
%_datadir/servicetypes/kofilter.desktop
%_datadir/servicetypes/kofilterwrapper.desktop
%_datadir/servicetypes/koplugin.desktop
%_datadir/apps/kross/python
%dir %_datadir/templates/
%_datadir/apps/kofficewidgets/pics/*.png

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
%_libdir/libkrossapi.la
%_libdir/libkrossapi.so.*
%_libdir/libkstore.la
%_libdir/libkwmf.la
%_libdir/libkofficecore.la
%_libdir/libkofficeui.la
%_libdir/libkotext.la
%_libdir/libkopainter.la
%_libdir/libkochart.la
%_libdir/libkowmf.la
%_libdir/libkopalette.la
%_libdir/libkopalette.so.*
%_libdir/libkofficecore.so.*
%_libdir/libkofficeui.so.*
%_libdir/libkotext.so.*
%_libdir/libkopainter.so.*
%_libdir/libkochart.so.*
%_libdir/libkstore.so.*
%_libdir/libkwmf.so.*
%_libdir/libkowmf.so.*
%_libdir/libkoproperty.la
%_libdir/libkoproperty.so.*
%_libdir/libkrossmain.la
%_libdir/libkrossmain.so.*

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
%_datadir/icons/*/*/*/kword.png
%_bindir/kword
%_datadir/applications/kde/kword.desktop
%dir %_datadir/apps/kword
%_datadir/apps/kword/*
%_datadir/services/kwordpart.desktop
%_datadir/services/kwserialletter_classic.desktop
%_datadir/services/kwserialletter_qtsqldb_power.desktop
%_datadir/services/kword_*
%_datadir/services/kwmailmerge_kabc.desktop
%_datadir/services/kwmailmerge_kspread.desktop
%_datadir/servicetypes/kwmailmerge.desktop
%_datadir/apps/xsltfilter/export/kword
%_datadir/apps/konqueror/servicemenus/kword*
%_libdir/kde3/libkword*
%_libdir/kde3/kwmailmerge_*
%_libdir/kde3/libabiwordexport.*
%_libdir/kde3/libabiwordimport.*
%_libdir/kde3/libamiproexport.*
%_libdir/kde3/libamiproimport.*
%_libdir/kde3/libapplixwordimport.*
%_libdir/kde3/libasciiexport.*
%_libdir/kde3/libasciiimport.*
%_libdir/kde3/libdocbookexport.*
%_libdir/kde3/libhtmlexport.*
%_libdir/kde3/libhtmlimport.*
%_libdir/kde3/libmswordimport.*
%_libdir/kde3/libmswriteexport.*
%_libdir/kde3/libmswriteimport.*
%_libdir/kde3/liboowriterexport.*
%_libdir/kde3/liboowriterimport.*
%_libdir/kde3/libpalmdocexport.*
%_libdir/kde3/libpalmdocimport.*
%_libdir/kde3/librtfexport.*
%_libdir/kde3/librtfimport.*
%_libdir/kde3/libwmlexport.*
%_libdir/kde3/libwmlimport.*
%_libdir/kde3/libwpexport.*
%_libdir/kde3/kword*
%_libdir/kde3/libpdfimport.*
%_libdir/kde3/libwpimport.*
%_libdir/libkdeinit_kword.*
%_datadir/templates/TextDocument.desktop
%_datadir/templates/.source/TextDocument.kwt

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
%_libdir/libkwordexportfilters.la
%_libdir/libkwordexportfilters.so.*
%_libdir/libkwmailmerge_interface.la   
%_libdir/libkwmailmerge_interface.so.*
%_libdir/libkwordprivate.la
%_libdir/libkwordprivate.so.*

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
%_datadir/icons/*/*/*/kplato.*
%_bindir/kplato
%_libdir/kde3/kplato.*
%_libdir/kde3/libkplatopart.*
%_libdir/libkdeinit_kplato.*
%_datadir/applications/kde/kplato.desktop
%dir %_datadir/apps/kplato
%_datadir/apps/kplato/*
%_datadir/services/kplatopart.desktop

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
%_datadir/icons/*/*/*/kspread.png
%_bindir/kspread
%_libdir/kde3/krosskspreadcore.*
%_libdir/kde3/kspreadscripting.*
%_libdir/kde3/libexcelimport.*
%_libdir/kde3/libapplixspreadimport.*
%_libdir/kde3/libcsvexport.*
%_libdir/kde3/libcsvimport.*
%_libdir/kde3/libdbaseimport.*
%_libdir/kde3/libgnumericexport.*
%_libdir/kde3/libgnumericimport.*
%_libdir/kde3/libopencalcexport.*
%_libdir/kde3/libopencalcimport.*
%_libdir/kde3/libqproimport.*
%_libdir/kde3/libhancomwordimport.*
%_libdir/kde3/libkspread*
%_libdir/kde3/kspread.*
%_libdir/libkdeinit_kspread.*
%dir %_datadir/apps/kspread/
%_datadir/apps/kspread/*
%_datadir/applications/kde/kspread.desktop
%_datadir/services/kspread*
%_datadir/apps/konqueror/servicemenus/kspread*
%_datadir/templates/SpreadSheet.desktop
%_datadir/templates/.source/SpreadSheet.kst

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
%_datadir/icons/*/*/*/kchart.png
%_bindir/kchart
%_libdir/kde3/kchart.*
%_libdir/kde3/libkchart*
%_libdir/libkdeinit_kchart.*
%dir %_datadir/apps/kchart/
%_datadir/apps/kchart/*
%_datadir/applications/kde/kchart.desktop
%_datadir/services/kchart_*
%_datadir/services/kchartpart.desktop
%_datadir/apps/konqueror/servicemenus/kchart*

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
%_libdir/libkspreadcommon.la
%_libdir/libkspreadcommon.so.*

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
%_libdir/libkchartimageexport.la
%_libdir/libkchartimageexport.so.*
%_libdir/libkdchart.la
%_libdir/libkdchart.so.*
%_libdir/libkchartcommon.la
%_libdir/libkchartcommon.so.*

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
%_datadir/icons/*/*/*/kpresenter.png
%_bindir/kprconverter.pl
%_bindir/kpresenter
%_libdir/libkdeinit_kpresenter.*
%_datadir/services/ole_powerpoint97_import.desktop
%_datadir/services/kpresenter*
%dir %_datadir/apps/kpresenter
%_datadir/apps/kpresenter/*
%_datadir/applications/kde/kpresenter.desktop
%_datadir/services/kprkword.desktop
%_libdir/kde3/libolefilter.*
%_libdir/kde3/libkpresenter*
%_libdir/kde3/libkprkword.*
%_libdir/kde3/libooimpressexport.*
%_libdir/kde3/libooimpressimport.*
%_libdir/kde3/kpresenter.*
%_datadir/templates/Presentation.desktop
%_datadir/templates/.source/Presentation.kpt
%_datadir/apps/konqueror/servicemenus/kpresenter*

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
%_libdir/libkpresenterimageexport.la
%_libdir/libkpresenterimageexport.so.*
%_libdir/libkpresenterprivate.la
%_libdir/libkpresenterprivate.so.*

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
%_datadir/icons/*/*/*/kformula.*
%_bindir/kformula
%_libdir/kde3/libkformulapart.*
%_libdir/kde3/kformula.*
%_libdir/libkdeinit_kformula.*
%dir %_datadir/apps/kformula
%_datadir/apps/kformula/*
%_datadir/applications/kde/kformula.desktop
%_datadir/services/kformula*
%_datadir/apps/konqueror/servicemenus/kformula*

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
%_libdir/libkformulalib.la
%_libdir/libkformulalib.so.*

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
%_datadir/icons/*/*/*/koshell.*
%_bindir/koshell
%_libdir/libkdeinit_koshell.*
%_libdir/kde3/koshell.*
%_datadir/applications/kde/koshell.desktop
%_datadir/config.kcfg/koshell.kcfg
%dir %_datadir/apps/koshell
%_datadir/apps/koshell/*

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
%_datadir/icons/*/*/*/kivio.png
%_bindir/kivio
%_libdir/libkdeinit_kivio.*
%_libdir/kde3/kivio*
%_libdir/kde3/libkivio*
%_libdir/kde3/straight_connector.*
%_datadir/services/kivio*
%_datadir/applications/kde/kivio.desktop
%_datadir/config.kcfg/kivio.kcfg
%dir %_datadir/apps/kivio
%_datadir/apps/kivio/*
%_datadir/apps/konqueror/servicemenus/kivio*

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
%_libdir/libkiviocommon.la
%_libdir/libkiviocommon.so.*

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
%_datadir/icons/*/*/*/karbon.*
%_bindir/karbon
%_libdir/kde3/libkfosvgexport.*
%_libdir/kde3/liboodrawimport.*
%_libdir/kde3/libkarbon*
%_libdir/kde3/libwmfexport.*
%_libdir/kde3/libwmfimport.*
%_libdir/kde3/karbon*
%_libdir/libkdeinit_karbon.*
%dir %_datadir/apps/karbon
%_datadir/apps/karbon/*
%_datadir/services/karbon*
%_datadir/applications/kde/karbon.desktop
%_datadir/servicetypes/karbon_module.desktop
%_datadir/templates/Illustration.desktop  
%_datadir/templates/.source/Illustration.karbon
%_datadir/apps/konqueror/servicemenus/karbon*

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
%_libdir/libkarboncommon.la
%_libdir/libkarboncommon.so.*

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
%_datadir/icons/*/*/*/krita.png
%_bindir/krita
%dir %_datadir/apps/krita
%_datadir/apps/krita/*
%dir %_datadir/apps/kritaplugins
%_datadir/apps/kritaplugins/*
%_libdir/kde3/krosskritacore.*
%_libdir/libkdeinit_krita.*
%_libdir/kde3/libkrita*
%_libdir/kde3/krita*
%if %krita_kjs_compile
%_libdir/kde3/kritakjsembed.*
%endif
%_datadir/services/krita*
%_datadir/servicetypes/krita_*
%_datadir/applnk/.hidden/krita_*
%_datadir/applications/kde/krita.desktop
%_datadir/apps/konqueror/servicemenus/krita*

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
%_libdir/libkrita*.so.*
%_libdir/libkrita*.la

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
%_datadir/icons/*/*/*/kexi.*
%_bindir/kexi
%_bindir/ksqlite
%_bindir/ksqlite2
%_bindir/ksqlite2to3
%_bindir/kexi_*
%_bindir/krossrunner
%_libdir/libkdeinit_kexi.*
%_libdir/kde3/kexi*
%_libdir/kde3/libkspreadkexiimport.*
%_libdir/kde3/kformdesigner_*
%dir %_datadir/apps/kexi
%_datadir/apps/kexi/*
%_datadir/mimelnk/application/x-kexi-connectiondata.desktop
%_datadir/services/kexi
%_datadir/services/kexidb*
%_datadir/services/keximigrate*
%_datadir/services/kformdesigner
%_datadir/applications/kde/kexi.desktop
%_datadir/servicetypes/widgetfactory.desktop
%_datadir/locale/*/*/kexi*
%_datadir/services/kspread_kexi_import.desktop
%_datadir/mimelnk/application/x-kexiproject-*
%_datadir/servicetypes/kexi*
%_datadir/config/kexirc
%_datadir/config/magic/kexi.magic
%_libdir/kde3/krosskexiapp.*
%_libdir/kde3/krosskexidb.*
%_datadir/apps/konqueror/servicemenus/kexi*

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
%_libdir/libkexi*.la
%_libdir/libkexi*.so.*
%_libdir/libkformdesigner.la
%_libdir/libkformdesigner.so.*

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
%_datadir/icons/*/*/*/kudesigner.*
%_bindir/kudesigner
%_bindir/kugar
%_libdir/libkdeinit_kudesigner.*
%_libdir/libkdeinit_kugar.*
%_libdir/kde3/libkudesign*
%_libdir/kde3/libkugar*
%_libdir/kde3/kudesigner*
%_libdir/kde3/kugar.*
%_datadir/icons/*/*/*/kugar.png
%dir %_datadir/apps/kugar
%_datadir/apps/kugar/*
%dir %_datadir/apps/kudesigner
%_datadir/apps/kudesigner/*
%_datadir/services/kugar_kugar_import.desktop
%_datadir/services/kugarpart.desktop
%_datadir/applications/kde/kugar.desktop
%_datadir/applications/kde/kudesigner.desktop

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
%_libdir/libkudesignercore.la*
%_libdir/libkudesignercore.so*
%_libdir/libkugarlib.la
%_libdir/libkugarlib.so.*

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
%_libdir/*.so
%exclude %_libdir/libkudesignercore.so
%_includedir/*
%if %compile_apidox
%doc %_docdir/*/*/koffice-apidocs
%endif
%exclude %_libdir/libkdeinit_*

#--------------------------------------------------------------------

%prep

%setup -q 
%patch0 -p0 -b .categories
%patch1 -p0 -b .cve_kpdf
%patch2 -p0 -b .cve_kpdf
%patch3 -p1 -b .cve-2008-1693

%build
export QTDIR=%{qt3dir}
export KDEDIR=%_prefix

%configure2_5x \
%if %unstable
	--enable-debug=full \
%else
	--disable-debug \
%endif
%if %use_enable_final
	--enable-final \
%else
	--disable-final \
%endif
	--disable-static \
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif
	--disable-rpath \
%if ! %use_python
    --without-python \
%endif
	--with-xinerama 

%make

%if %compile_apidox
make apidox
%endif

%install
rm -fr %buildroot

%makeinstall

perl -pi -e "s|Icon=kudesigner|Icon=text_tools_section.png|" %buildroot/%_datadir/applications/kde/kudesigner.desktop
perl -pi -e "s|Icon=kthesaurus|Icon=office_accessories_section.png|" %buildroot/%_datadir/applnk/Office/KThesaurus.desktop

rm -f %buildroot/%_datadir/apps/kontour/kpartplugins/scan-kontour.rc
rm -f %buildroot/%_datadir/mimelnk/image/x-raw.desktop

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



