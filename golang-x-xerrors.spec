# Generated by go2rpm 1
%bcond_without check

# https://github.com/golang/xerrors
%global goipath         golang.org/x/xerrors
%global forgeurl        https://github.com/golang/xerrors
%global commit          5ec99f83aff198f5fbd629d6c8d8eb38a04218ca

%gometa

%global common_description %{expand:
This package holds the transition packages for the new Go 1.13 error values.
See golang.org/design/29934-error-values.}

%global golicenses      LICENSE PATENTS
%global godocs          README

Name:           %{goname}
Version:        0
Release:        1
Summary:        Transition packages for the new Go 1.13 error values
Group:          Development/Other

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
BuildArch:      noarch
BuildRequires:	compiler(go-compiler)

%description
%{common_description}

%prep
%autoseup -n xerrors-5ec99f83aff198f5fbd629d6c8d8eb38a04218ca -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles
