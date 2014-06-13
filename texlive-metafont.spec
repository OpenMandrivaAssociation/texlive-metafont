# revision 29764
# category Package
# catalog-ctan /systems/knuth/dist/mf
# catalog-date 2012-08-30 22:47:45 +0200
# catalog-license knuth
# catalog-version 2.718281
Name:		texlive-metafont
Version:	2.718281
Release:	12
Summary:	A system for specifying fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/mf
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-metafont.bin
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
%{_texmfdistdir}/metafont/base/expr.mf
%{_texmfdistdir}/metafont/base/io.mf
%{_texmfdistdir}/metafont/base/mf.mf
%{_texmfdistdir}/metafont/base/null.mf
%{_texmfdistdir}/metafont/base/plain.mf
%{_texmfdistdir}/metafont/config/cmmf.ini
%{_texmfdistdir}/metafont/config/mf.ini
%{_texmfdistdir}/metafont/misc/3test.mf
%{_texmfdistdir}/metafont/misc/6test.mf
%{_texmfdistdir}/metafont/misc/mode2dpi.mf
%{_texmfdistdir}/metafont/misc/mode2dpixy.mf
%{_texmfdistdir}/metafont/misc/modename.mf
%{_texmfdistdir}/metafont/misc/modes.mf
%{_texmfdistdir}/metafont/misc/ps2mfbas.mf
%{_texmfdistdir}/metafont/misc/rtest.mf
%{_texmfdistdir}/metafont/misc/test.mf
%{_texmfdistdir}/metafont/misc/waits.mf
%{_texmfdistdir}/metafont/misc/ztest.mf
%_texmf_fmtutil_d/metafont
%doc %{_mandir}/man1/mf-nowin.1*
%doc %{_texmfdistdir}/doc/man/man1/mf-nowin.man1.pdf
%doc %{_mandir}/man1/mf.1*
%doc %{_texmfdistdir}/doc/man/man1/mf.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

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
