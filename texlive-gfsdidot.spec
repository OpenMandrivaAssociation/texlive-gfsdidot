Name:		texlive-gfsdidot
Version:	69112
Release:	1
Summary:	A Greek font based on Didot's work
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfsdidot
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidot.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/gfsdidot
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot
%{_texmfdistdir}/fonts/map/dvips/gfsdidot
%{_texmfdistdir}/fonts/opentype/public/gfsdidot
%{_texmfdistdir}/fonts/tfm/public/gfsdidot
%{_texmfdistdir}/fonts/type1/public/gfsdidot
%{_texmfdistdir}/fonts/vf/public/gfsdidot
%{_texmfdistdir}/tex/latex/gfsdidot
%doc %{_texmfdistdir}/doc/fonts/gfsdidot

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
