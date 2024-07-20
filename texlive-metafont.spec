Name:		texlive-metafont
Version:	70015
Release:	1
Summary:	A system for specifying fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/mf
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-metafont.bin
Requires:	texlive-modes
%rename tetex-mfwin
%rename texlive-mfwin

%description
The program takes a semi-algorithmic specification of a font,
and produces a bitmap font (whose properties are defined by a
set of parameters of the target device), and a set metrics for
use by TeX. The bitmap output may be converted into a format
directly usable by a device driver, etc., by the tools provided
in the parallel mfware distribution. (Third parties have
developed tools to convert the bitmap output to outline fonts.)
The distribution includes the source of Knuth's Metafont book;
this source is there to read, as an example of writing TeX --
it should not be processed without Knuth's direct permission.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	rm -fr %{_texmfvardir}/web2c/metafont
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metafont
%_texmf_fmtutil_d/metafont
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/metafont <<EOF
#
# from metafont:
mf mf-nowin - -translate-file=cp227.tcx mf.ini
EOF
