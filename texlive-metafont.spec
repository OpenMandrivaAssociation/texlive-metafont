Name:		texlive-metafont
Version:	2.718281
Release:	1
Summary:	A system for specifying fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/mf
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metafont.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-metafont.bin
Provides:	tetex-mfwin = %{version}
Provides:	texlive-mfwin = %{version}
Obsoletes:	tetex-mfwin <= 3.0
Conflicts:	tetex-mfwin <= 3.0
Obsoletes:	texlive-mfwin <= 2007
Conflicts:	texlive-mfwin <= 2007
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_mandir}/man1/mf-nowin.1*
%doc %{_texmfdir}/doc/man/man1/mf-nowin.man1.pdf
%doc %{_mandir}/man1/mf.1*
%doc %{_texmfdir}/doc/man/man1/mf.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
