# The MIT License (MIT)
# 
# Copyright (c) 2013 Tomasz Olszak <olszak.tomasz@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

Name:       qt5-qtquickcontrols
Summary:    Qt Quick Controls
Version:    5.2.0
Release:    0
Group:      Base/Libraries
License:    LGPL-2.1+ or GPL-3.0
URL:        http://qt.digia.com
Source0:    %{name}-%{version}.tar.xz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Quick Controls library

#### Build section

%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/share/qt5
touch .git # To make sure syncqt is used

%qmake5
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake5_install

#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

#### File section

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Controls
%{_libdir}/qt5/qml/QtQuick/Layouts
