%define keepstatic 1

Name:       libusb
Summary:    A library which allows userspace access to USB devices
Version:    0.1.12
Release:    2
Group:      System/Libraries
License:    LGPLv2+
URL:        http://sourceforge.net/projects/libusb/
Source0:    http://prdownloads.sourceforge.net/libusb/%{name}-%{version}.tar.gz
Patch0:     libusb-0.1.12-libusbconfig.patch
Patch1:     libusb-0.1.12-memset.patch
Patch2:     libusb-0.1.12-openat.patch
Patch3:     libusb-0.1.12-wakeups.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This package provides a way for applications to access USB devices.

%package devel
Summary:    Development files for libusb
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb.

%package static
Summary:    Static library for libusb
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}

%description static
This package contains the static library for libusb

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# libusb-0.1.12-libusbconfig.patch
%patch0 -p1
# libusb-0.1.12-memset.patch
%patch1 -p1
# libusb-0.1.12-openat.patch
%patch2 -p1
# libusb-0.1.12-wakeups.patch
%patch3 -p1

%build

%configure  \
    --enable-static

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install 

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} AUTHORS README

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/%{name}*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/%{name}-config
%{_libdir}/pkgconfig/libusb.pc
%{_includedir}/*
%{_libdir}/%{name}*.so

%files static
%defattr(-,root,root,-)
%{_libdir}/%{name}*.a

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
