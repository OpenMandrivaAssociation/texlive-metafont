%global tl_name metafont
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.71828182
Release:	%{tl_revision}.1
Summary:	A system for specifying fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/knuth/dist/mf
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kpathsea)
Requires:	texlive(metafont.bin)
Requires:	texlive(modes)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The program takes a programmatic specification of a font, and produces a
bitmap font (whose properties are defined by a set of parameters of the
target device), and metrics for use by TeX. The bitmap output may be
converted into a format directly usable by a device driver, etc., by the
tools provided in the parallel mfware distribution. Third parties have
developed tools to convert the bitmap output to outline fonts. The
distribution includes the source of Knuth's Metafont book; this source
is there to read, as an example of writing TeX -- it should not be
processed without Knuth's direct permission. The mailing list tex-
fonts@math.utah.edu is the best for general discussion of Metafont
usage; the tex-k@tug.org list is best for bug reports about building the
software, etc.

