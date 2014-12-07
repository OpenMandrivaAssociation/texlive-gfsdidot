# revision 31978
# category Package
# catalog-ctan /fonts/greek/gfs/gfsdidot
# catalog-date 2013-10-23 14:01:00 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-gfsdidot
Version:	1.0
Release:	10
Summary:	A Greek font based on Didot's work
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfsdidot
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The design of Didot's 1805 Greek typeface was influenced by the
neoclassical ideals of the late 18th century. The font was
brought to Greece at the time of the 1821 Greek Revolution, by
Didot's son, and was very widely used. The present version is
provided by the Greek Font Society. The font supports the Greek
alphabet, and is accompanied by a matching Latin alphabet based
on Zapf's Palatino. LaTeX support is provided, using the OT1,
T1 and LGR encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSDidot-Bold.afm
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSDidot-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSDidot-Italic.afm
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSDidot.afm
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSOlga.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didot.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotdenomnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotec.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotnumnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didottabnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotuecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotusc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gfsudidotmath.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gpdidot.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gpdidoti.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gpdidotusc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gpolga.enc
%{_texmfdistdir}/fonts/map/dvips/gfsdidot/gfsdidot.map
%{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSDidot.otf
%{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSDidotBold.otf
%{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSDidotBoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSDidotItalic.otf
%{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSOlga.otf
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotdenomnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotdenomnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotnumnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotnumnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didottabnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didottabnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotb6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotbi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotbi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidoti6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidoti6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotrg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotsc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotsc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotsco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotsco6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gfsudidotmath8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gfsudidotmath8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/golgai6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/golgai6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/golgaui6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/golgaui6r.tfm
%{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSDidot-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSDidot-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSDidot-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSDidot.pfb
%{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSOlga.pfb
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotb8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotb9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbi8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbi9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbo8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbo9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotdenomnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoti8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoti9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotnumnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoto8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoto9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotrg8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotrg9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsc8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsc9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsco8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsco9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didottabnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotui8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotui9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotb6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotbi6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidoti6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotrg6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotsc6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotsco6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gfsudidotmath8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/golgai6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/golgaui6a.vf
%{_texmfdistdir}/tex/latex/gfsdidot/gfsdidot.sty
%{_texmfdistdir}/tex/latex/gfsdidot/lgrudidot.fd
%{_texmfdistdir}/tex/latex/gfsdidot/omludidot.fd
%{_texmfdistdir}/tex/latex/gfsdidot/ot1udidot.fd
%{_texmfdistdir}/tex/latex/gfsdidot/t1udidot.fd
%{_texmfdistdir}/tex/latex/gfsdidot/uudidotnums.fd
%doc %{_texmfdistdir}/doc/fonts/gfsdidot/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gfsdidot/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gfsdidot/README
%doc %{_texmfdistdir}/doc/fonts/gfsdidot/README.TEXLIVE

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
