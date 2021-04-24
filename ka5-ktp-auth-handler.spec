%define		kdeappsver	21.04.0
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		ktp-auth-handler
Summary:	ktp-auth-handler
Name:		ka5-%{kaname}
Version:	21.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0a3d19eea7a32c6d19297c0da463b2a4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-kaccounts-integration-devel >= %{kdeappsver}
BuildRequires:	ka5-ktp-common-internals-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	libaccounts-qt5-devel >= 1.10
BuildRequires:	libsignon-qt5-devel >= 8.55
BuildRequires:	ninja
BuildRequires:	qca-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-qt5-devel >= 0.9.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Telepathy authentication handler.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/ktp-auth-handler
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.ConfAuthObserver.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.SASLHandler.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.TLSHandler.service
%{_datadir}/telepathy/clients
