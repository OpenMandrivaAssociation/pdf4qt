%define oname PDF4QT

Summary:	Shows the periodic system of the elements
Name:		pdf4qt
Version:	1.3.7
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://jakubmelka.github.io/
Source0:	https://github.com/JakubMelka/%{oname}/archive/refs/tags/v%{version}.tar.gz
Source1:	FindLCMS2.cmake
# fix missing link to fontconfig
Patch1:		125.patch
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6TextToSpeech)

%description
Kalzium is an application which will show you some information about the
periodic system of the elements. Therefore you could use it as an
information database.

%files 

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_includedir}/libkdeedu
%{_libdir}/libscience.so

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}


sed "s|lcms2|LCMS2|g" -i Pdf4QtLibCore/CMakeLists.txt
sed "s|lcms|LCMS2|g" -i CMakeLists.txt

cp %SOURCE1 .
#find the local lcms2 module
mod=$PWD

export CC=gcc
export CXX=g++
%cmake \
        -DCMAKE_MODULE_PATH="${mod}" \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
