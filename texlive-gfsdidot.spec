%global tl_name gfsdidot
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Greek font based on Didots work
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfsdidot
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The design of Didot's 1805 Greek typeface was influenced by the
neoclassical ideals of the late 18th century. The font was brought to
Greece at the time of the 1821 Greek Revolution, by Didot's son, and was
very widely used. The present version is provided by the Greek Font
Society. The font supports the Greek alphabet, and is accompanied by a
matching Latin alphabet based on Zapf's Palatino. LaTeX support is
provided, using the OT1, T1, TS1, and LGR encodings.

