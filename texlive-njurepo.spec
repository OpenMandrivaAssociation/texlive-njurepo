Name:		texlive-njurepo
Version:	50492
Release:	2
Summary:	Reports for Nanjing University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/njurepo
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njurepo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njurepo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njurepo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX document class provides a thesis template for
Nanjing University in order to make it easy to write experiment
reports and homework for the bachelor's curriculum. NJUrepo
stands for Nanjing University versatile Report.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/njurepo
%{_texmfdistdir}/tex/latex/njurepo
%doc %{_texmfdistdir}/doc/latex/njurepo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
