%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-ixblue-ins-driver
Version:        0.1.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ixblue_ins_driver package

License:        MIT
URL:            http://wiki.ros.org/ixblue_ins_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-diagnostic-updater
Requires:       ros-noetic-ixblue-ins-msgs
Requires:       ros-noetic-ixblue-stdbin-decoder
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
BuildRequires:  boost-devel
BuildRequires:  libpcap-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-diagnostic-msgs
BuildRequires:  ros-noetic-diagnostic-updater
BuildRequires:  ros-noetic-ixblue-ins-msgs
BuildRequires:  ros-noetic-ixblue-stdbin-decoder
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The iXblue_ins_driver package

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Oct 27 2020 Laure LE BRETON <laure.le-breton@ixblue.com> - 0.1.4-1
- Autogenerated by Bloom

* Thu Sep 03 2020 Laure LE BRETON <laure.le-breton@ixblue.com> - 0.1.3-1
- Autogenerated by Bloom

