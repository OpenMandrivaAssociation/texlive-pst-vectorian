# revision 28801
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-vectorian
# catalog-date 2013-01-11 11:15:33 +0100
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-pst-vectorian
Version:	0.4
Release:	2
Summary:	Printing ornaments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-vectorian
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vectorian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vectorian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses PStricks to draw ornaments (a substantial
repertoire of ornaments is provided).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-vectorian/psvectorian.pro
%{_texmfdistdir}/tex/latex/pst-vectorian/psvectorian.sty
%doc %{_texmfdistdir}/doc/latex/pst-vectorian/README
%doc %{_texmfdistdir}/doc/latex/pst-vectorian/psvectorian.pdf
%doc %{_texmfdistdir}/doc/latex/pst-vectorian/psvectorian.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
