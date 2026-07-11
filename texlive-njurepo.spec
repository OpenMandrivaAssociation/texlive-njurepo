%global tl_name njurepo
%global tl_revision 50492

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	Reports for Nanjing University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/njurepo
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/njurepo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/njurepo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/njurepo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX document class provides a thesis template for Nanjing
University in order to make it easy to write experiment reports and
homework for the bachelor's curriculum. NJUrepo stands for Nanjing
University versatile Report.

