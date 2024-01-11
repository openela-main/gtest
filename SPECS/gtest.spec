Summary:        Google C++ testing framework
Name:           gtest
Version:        1.8.0
Release:        5%{?dist}
License:        BSD and ASL2.0
URL:            https://github.com/google/googletest
Source0:        https://github.com/google/googletest/archive/release-%{version}.tar.gz
# Install into lib64 if needed
Patch0:         gtest-1.8.0-libdir.patch
# https://github.com/google/googletest/issues/845
Patch1:         gtest-1.8.0-null-pointer.patch
# https://github.com/google/googletest/issues/930
# https://bugzilla.redhat.com/show_bug.cgi?id=1513522
Patch2:         gtest-1.8.0-fix-double-free-with-shared-libs.patch
# Fedora-specific patches
## Set libversion for libraries to version of gtest
## WARNING: must be rediffed for each version bump
Patch100:       gtest-1.8.0-libversion.patch
BuildRequires:  cmake
BuildRequires:  python3-devel
%description
Framework for writing C++ tests on a variety of platforms (GNU/Linux,
Mac OS X, Windows, Windows CE, and Symbian). Based on the xUnit
architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, various options for running the tests, and XML test report
generation.

%package     -n gtest-devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description -n gtest-devel
This package contains development files for %{name}.

%package     -n gmock
Summary:        Google C++ Mocking Framework
%description -n gmock
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++s
specifics in mind, Google C++ Mocking Framework (or Google Mock for
short) is a library for writing and using C++ mock classes.

Google Mock:

 o lets you create mock classes trivially using simple macros,
 o supports a rich set of matchers and actions,
 o handles unordered, partially ordered, or completely ordered
   expectations,
 o is extensible by users, and
 o works on Linux, Mac OS X, Windows, Windows Mobile, minGW, and
   Symbian.

%package     -n gmock-devel
Summary:        Development files for gmock
Requires:       gmock = %{version}-%{release}
%description -n gmock-devel
This package contains development files for gmock.

%prep
%autosetup -p1 -n googletest-release-%{version}

%build
mkdir build && cd build
%cmake -DBUILD_SHARED_LIBS=ON \
       -DPYTHON_EXECUTABLE=%{__python3} \
       -Dgtest_build_tests=ON ..
make %{?_smp_mflags}

%install
cd build
%make_install

%check
cd build
make test

%files
%license googletest/LICENSE
%{_libdir}/libgtest.so.%{version}
%{_libdir}/libgtest_main.so.%{version}

%files -n gtest-devel
%doc googletest/{CHANGES,CONTRIBUTORS,README.md}
%doc googletest/docs/
%doc googletest/samples
%{_includedir}/gtest/
%{_libdir}/libgtest.so
%{_libdir}/libgtest_main.so

%files -n gmock
%license googlemock/LICENSE
%{_libdir}/libgmock.so.%{version}
%{_libdir}/libgmock_main.so.%{version}

%files -n gmock-devel
%doc googlemock/{CHANGES,CONTRIBUTORS,README.md}
%doc googlemock/docs/
%{_includedir}/gmock/
%{_libdir}/libgmock.so
%{_libdir}/libgmock_main.so

%changelog
* Thu Jul 19 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-5
- Fix license field to accurately represent the content

* Fri Jun 29 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.8.0-4
- Change to Python 3 as a build dependency

* Wed Feb 14 2018 Neal Gompa <ngompa13@gmail.com> - 1.8.0-3
- Add patch to fix gmock segfaults (rhbz#1513522)
- Add patch to properly version the libraries
- Move the documentation to the right place
- Drop unneeded ldconfig scriptlets:
    https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets
- Some clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Dan Cermak <dan.cermak@cgc-instruments.com> - 1.8.0-1
- 1.8.0
- Merge gtest and gmock (rhbz#1314927)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.7.0-8
- Use patch from Jonathan Wakely to fix opt issue (rhbz#1408291)

* Wed Dec 21 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.7.0-7
- Disable C++ compiler optimization to fix FTBFS (BZ#1406937).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.7.0-4
- rebuilt for gcc-5.0.0-0.22.fc23

* Mon Feb 23 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.7.0-3
- Rebuild for gcc5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Terje Rosten <terje.rosten@ntnu.no> - 1.7.0-1
- 1.7.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Rex Dieter <rdieter@fedoraproject.org> 1.6.0-3
- use %%cmake macro, fix %%check, use RPM_BULID_ROOT consistently

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 28 2012 Akira TAGOH <tagoh@redhat.com> - 1.6.0-1
- New upstream release.
- Using autotools is not supported in upstream anymore. switching to cmake.
- undefined reference issues seems gone now. (#813825)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 15 2011 Akira TAGOH <tagoh@redhat.com> j- 1.5.0-5
- Fix FTBFS issue; update libtool files instead of disabling rpath things.

* Sun Mar 20 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-4
- add patch from Dan Horák to let 'make check' work 

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-2
- add python to buildreq 

* Wed Jan 12 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.5.0-1
- 1.5.0
- some cleanup

* Thu Aug 26 2010 Dan Horák <dan[at]danny.cz> - 1.4.0-2
- added workaround for linking the tests on Fedora >= 13 (#564953, #599865)

* Sat Nov 14 2009 Debarshi Ray <rishi@fedoraproject.org> - 1.4.0-1
- Version bump to 1.4.0.
  * New feature: the event listener API.
  * New feature: test shuffling.
  * New feature: the XML report format is closer to junitreport and can
    be parsed by Hudson now.
  * New feature: elapsed time for the tests is printed by default.
  * New feature: comes with a TR1 tuple implementation such that Boost
    is no longer needed for Combine().
  * New feature: EXPECT_DEATH_IF_SUPPORTED macro and friends.
  * New feature: the Xcode project can now produce static gtest libraries in
    addition to a framework.
  * Compatibility fixes for gcc and minGW.
  * Bug fixes and implementation clean-ups.

* Fri Jul 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 1.3.0-2.20090601svn257
- Autorebuild for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.0-1
- Version bump to 1.3.0.
  * New feature: ability to use Google Test assertions in other testing
    frameworks.
  * New feature: ability to run disabled test via
    --gtest_also_run_disabled_tests.
  * New feature: the --help flag for printing the usage.
  * New feature: access to Google Test flag values in user code.
  * New feature: a script that packs Google Test into one .h and one .cc file
    for easy deployment.
  * New feature: support for distributing test functions to multiple machines
    (requires support from the test runner).
  * Bug fixes and implementation clean-ups.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 05 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.0.0-1
- Initial build.
