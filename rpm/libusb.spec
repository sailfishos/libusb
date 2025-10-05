Name: libusb
Epoch: 1
Version: 0.1.7
Release: 1
Summary: A library which allows userspace access to USB devices
License: LGPLv2+
URL: https://github.com/sailfishos/libusb/
Source0: libusb-%{version}.tar.bz2
Patch0: libusb-config-multilib.patch
BuildRequires:  gcc
BuildRequires: libusb1-devel

%description
This package provides a way for applications to access USB devices.
Legacy libusb-0.1 is no longer supported by upstream, therefore content of this
package was replaced by libusb-compat. It provides compatibility layer allowing
applications written for libusb-0.1 to work with libusb-1.0.

%package devel
Summary: Development files for libusb
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files, libraries and documentation needed to
develop applications that use libusb-0.1. However new applications should use
libusb-1.0 library instead of this one.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -p1 -n libusb-%{version}/libusb-compat-0.1

%build
%autogen --disable-static
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libusb.la
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} AUTHORS ChangeLog NEWS README

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libusb-0.1.so.*

%files devel
%{_includedir}/usb.h
%{_libdir}/libusb.so
%{_libdir}/pkgconfig/libusb.pc
%{_bindir}/libusb-config

%files doc
%{_docdir}/%{name}-%{version}
