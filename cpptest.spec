Name:           cpptest
Version:        1.1.1
Release:        9%{?dist}
Summary:        A portable and powerful and simple unit testing framework for C++

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://%{name}.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         cpptest-1.1.0-libcpptest_pc_in.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  doxygen

#Fix RHBZ 925192
Patch1: cpptest-aarch64.patch

%description
CppTest is a portable and powerful, yet simple, unit testing framework
for handling automated tests in C++. The focus lies on usability and
extendability.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}, pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .libcpptest_pc_in
%patch1 -p1
%build
%configure --disable-static --enable-doc
make %{?_smp_mflags} V=1


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Not useful. Aready present in html and images folder
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/html/screenshot*png
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/html/index.html
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/html/html-example.html


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc NEWS COPYING AUTHORS ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.1.1-9
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.1-8
- Mass rebuild 2013-12-27

* Wed May 01 2013 Dan Mashal <dan.mashal@fedoraproject.org> -1.1.1-7
-Add patch for aarch64 

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 05 2010 Rakesh Pandit <rakesh@fedoraproject.org> 1.1.1-1
- Updated to 1.1.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.1.0-3
- Remove check section.

* Tue Mar 17 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.1.0-2
- Commented testsuite. Patched .pc file, fixed spacing and tab mix
- Removed image folder in %%doc

* Fri Mar 06 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.1.0-1
- Initial package
