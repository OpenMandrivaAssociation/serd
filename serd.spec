%define debug_package %nil

Name:           serd
Version:        0.22.0
Release:        2
Summary:        Lightweight RDF syntax library

%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

Source0:         http://download.drobilla.net/%{name}-%{version}.tar.bz2
URL:            http://drobilla.net/software/
License:        MIT
Group:          System/Libraries

BuildRequires:  waf, pkgconfig

%description
Lightweight C library for RDF syntax which supports reading
and writing Turtle and NTriples. Serd is not intended to be a swiss-army
knife of RDF syntax, but rather is suited to resource limited or
performance critical applications, or situations where a simple
reader/writer with minimal dependencies is ideal
(e.g. in LV2 hosts or plugins).

%files -n %{name}
%defattr(-,root,root,-)
%doc %{_mandir}/man1/serdi.*
%{_bindir}/serdi

#-----------------------------------
%package -n %{lib_name}

Summary:        Lightweight RDF syntax library
Group:          System/Libraries

%description -n %{lib_name}
Lightweight C library for RDF syntax which supports reading
and writing Turtle and NTriples. Serd is not intended to be a swiss-army
knife of RDF syntax, but rather is suited to resource limited or
performance critical applications, or situations where a simple
reader/writer with minimal dependencies is ideal
(e.g. in LV2 hosts or plugins).

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}-%{lib_major}.so.*

#-----------------------------------
%package -n %{lib_name_devel}
Summary:        Headers for the Lightweight RDF syntax library
Group:          System/Libraries
Requires:       %{lib_name} = %{version}-%{release}
Requires:       pkgconfig
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Development files needed to build applications against serd.

%files -n %{lib_name_devel}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}-%{lib_major}.so
%dir %{_includedir}/%{name}-%{lib_major}/%{name}
%{_includedir}/%{name}-%{lib_major}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}-%{lib_major}.pc

#-----------------------------------
%prep
%setup -q
# remove ldconfig
sed -i "/ldconfig/d" wscript

%build
%{__python2} ./waf configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir} CC=%{__cc}
%{__python2} ./waf CC=%{__cc}

%install

./waf install --destdir=%{buildroot}

%clean
