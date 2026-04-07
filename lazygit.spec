Summary:	Simple terminal UI for git commands
Name:		lazygit
Version:	0.61.0
Release:	1
License:	MIT
Group:		Development/Tools
#Source0Download: https://github.com/jesseduffield/lazygit/releases
Source0:	https://github.com/jesseduffield/lazygit/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	db41eb89e2a5c32f0a38c15d1b3c2fe9
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
