Summary:	Simple terminal UI for git commands
Name:		lazygit
Version:	0.57.0
Release:	1
License:	MIT
Group:		Development/Tools
#Source0Download: https://github.com/lazygit/lazygit/releases
Source0:	https://github.com/jesseduffield/lazygit/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3d80f8a6991f0426f8a7730ee65c4569
URL:		https://github.com/jesseduffield/lazygit
BuildRequires:	golang >= 1.25.0
BuildRequires:	rpmbuild(macros) >= 2.009
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	_debugsource_packages

%description
Simple terminal UI for git commands.

%prep
%setup -q

%{__mkdir_p} .go-cache

%build
%__go build -v -mod=vendor -o bin/lazygit

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

cp -p bin/lazygit $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/lazygit
