#
# This is 2013.1.2 release
#
%global release_name havana

Name:		openstack-neutron
Version:	2013.2
Release:	0.3.b2%{?dist}
Provides:	openstack-quantum = %{version}-%{release}
Obsoletes:	openstack-quantum < 2013.2-0.3.b2

Summary:	OpenStack Networking Service

Group:		Applications/System
License:	ASL 2.0
URL:		http://launchpad.net/neutron/

#Source0:	http://launchpad.net/neutron/%{release_name}/%{version}/+download/neutron-%{version}.tar.gz
Source0:	http://launchpad.net/neutron/%{release_name}/%{release_name}-2/+download/neutron-%{version}.b2.tar.gz
Source1:	neutron.logrotate
Source2:	neutron-sudoers
Source4:	neutron-server-setup
Source5:	neutron-node-setup
Source6:	neutron-dhcp-setup
Source7:	neutron-l3-setup

Source10:	neutron-server.init
Source20:	neutron-server.upstart
Source11:	neutron-linuxbridge-agent.init
Source21:	neutron-linuxbridge-agent.upstart
Source12:	neutron-openvswitch-agent.init
Source22:	neutron-openvswitch-agent.upstart
Source13:	neutron-ryu-agent.init
Source23:	neutron-ryu-agent.upstart
Source14:	neutron-nec-agent.init
Source24:	neutron-nec-agent.upstart
Source15:	neutron-dhcp-agent.init
Source25:	neutron-dhcp-agent.upstart
Source16:	neutron-l3-agent.init
Source26:	neutron-l3-agent.upstart
Source17:	neutron-metadata-agent.init
Source27:	neutron-metadata-agent.upstart
Source18:	neutron-ovs-cleanup.init
Source28:	neutron-ovs-cleanup.upstart
Source19:	neutron-lbaas-agent.init
Source29:	neutron-lbaas-agent.upstart
Source30:	neutron-mlnx-agent.init
Source40:	neutron-mlnx-agent.upstart

#
# patches_base=2013.2.b2
#
Patch0001: 0001-use-parallel-installed-versions-in-RHEL6.patch

BuildArch:	noarch

BuildRequires:	python2-devel
BuildRequires:	python-setuptools
# Build require these parallel versions
# as setup.py build imports neutron.openstack.common.setup
# which will then check for these
BuildRequires:	python-sqlalchemy0.7
BuildRequires:	python-webob1.0
BuildRequires:	python-paste-deploy1.5
BuildRequires:	python-routes1.12
BuildRequires:	dos2unix
BuildRequires:	python-pbr
BuildRequires:	python-d2to1


Requires:	python-neutron = %{version}-%{release}
Requires:	openstack-utils
Requires:	python-keystone
Requires:	python-pbr

Requires(post):		chkconfig
Requires(postun):	initscripts
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(pre):		shadow-utils

# dnsmasq is not a hard requirement, but is currently the only option
# when neutron-dhcp-agent is deployed.
Requires:	dnsmasq


%description
Quantum is a virtual network service for Openstack. Just like
OpenStack Nova provides an API to dynamically request and configure
virtual servers, Quantum provides an API to dynamically request and
configure virtual networks. These networks connect "interfaces" from
other OpenStack services (e.g., virtual NICs from Nova VMs). The
Quantum API supports extensions to provide advanced network
capabilities (e.g., QoS, ACLs, network monitoring, etc.)


%package -n python-neutron
Summary:	Quantum Python libraries
Group:		Applications/System

Provides:	python-quantum = %{version}-%{release}
Obsoletes:	python-quantum < 2013.2-0.3.b2

Requires:	MySQL-python
Requires:	python-alembic
Requires:	python-amqplib
Requires:	python-anyjson
Requires:	python-eventlet
Requires:	python-greenlet
Requires:	python-httplib2
Requires:	python-iso8601
Requires:	python-kombu
Requires:	python-lxml
Requires:	python-paste-deploy1.5
Requires:	python-routes1.12
Requires:	python-sqlalchemy0.7
Requires:	python-webob1.0
Requires:	python-netaddr
Requires:	python-oslo-config
Requires:	python-qpid
Requires:	python-neutronclient
Requires:	sudo

%description -n python-neutron
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron Python library.


%package -n openstack-neutron-bigswitch
Summary:	Quantum Big Switch plugin
Group:		Applications/System

Provides:	openstack-quantum-bigswitch = %{version}-%{release}
Obsoletes:	openstack-quantum-bigswitch < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-bigswitch
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the FloodLight Openflow Controller or the Big Switch
Networks Controller.


%package -n openstack-neutron-brocade
Summary:	Quantum Brocade plugin
Group:		Applications/System

Provides:	openstack-quantum-brocade = %{version}-%{release}
Obsoletes:	openstack-quantum-brocade < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-brocade
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Brocade VCS switches running NOS.


%package -n openstack-neutron-cisco
Summary:	Quantum Cisco plugin
Group:		Applications/System

Provides:	openstack-quantum-cisco = %{version}-%{release}
Obsoletes:	openstack-quantum-cisco < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}
Requires:	python-configobj


%description -n openstack-neutron-cisco
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Cisco UCS and Nexus.


%package -n openstack-neutron-hyperv
Summary:	Quantum Hyper-V plugin
Group:		Applications/System

Provides:	openstack-quantum-hyperv = %{version}-%{release}
Obsoletes:	openstack-quantum-hyperv < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-hyperv
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Microsoft Hyper-V.


%package -n openstack-neutron-linuxbridge
Summary:	Quantum linuxbridge plugin
Group:		Applications/System

Provides:	openstack-quantum-linuxbridge = %{version}-%{release}
Obsoletes:	openstack-quantum-linuxbridge < 2013.2-0.3.b2

Requires:	bridge-utils
Requires:	openstack-neutron = %{version}-%{release}
Requires:	python-pyudev


%description -n openstack-neutron-linuxbridge
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks as VLANs using Linux bridging.


%package -n openstack-neutron-midonet
Summary:	Quantum MidoNet plugin
Group:		Applications/System

Provides:	openstack-quantum-midonet = %{version}-%{release}
Obsoletes:	openstack-quantum-midonet < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-midonet
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using MidoNet from Midokura.


%package -n openstack-neutron-ml2
Summary:	Quantum ML2 plugin
Group:		Applications/System

Provides:	openstack-quantum-ml2 = %{version}-%{release}
Obsoletes:	openstack-quantum-ml2 < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-ml2
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains a neutron plugin that allows the use of drivers
to support separately extensible sets of network types and the mechanisms
for accessing those types.


%package -n openstack-neutron-mellanox
Summary:	Quantum Mellanox plugin
Group:		Applications/System

Provides:	openstack-quantum-mellanox = %{version}-%{release}
Obsoletes:	openstack-quantum-mellanox < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-mellanox
This plugin implements Quantum v2 APIs with support for Mellanox embedded
switch functionality as part of the VPI (Ethernet/InfiniBand) HCA.


%package -n openstack-neutron-nicira
Summary:	Quantum Nicira plugin
Group:		Applications/System

Provides:	openstack-quantum-nicira = %{version}-%{release}
Obsoletes:	openstack-quantum-nicira < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-nicira
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Nicira NVP.


%package -n openstack-neutron-openvswitch
Summary:	Quantum openvswitch plugin
Group:		Applications/System

Provides:	openstack-quantum-openvswitch = %{version}-%{release}
Obsoletes:	openstack-quantum-openvswitch < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}
Requires:	openvswitch


%description -n openstack-neutron-openvswitch
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Open vSwitch.


%package -n openstack-neutron-plumgrid
Summary:	Quantum PLUMgrid plugin
Group:		Applications/System

Provides:	openstack-quantum-plumgrid = %{version}-%{release}
Obsoletes:	openstack-quantum-plumgrid < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-plumgrid
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the PLUMgrid platform.


%package -n openstack-neutron-ryu
Summary:	Quantum Ryu plugin
Group:		Applications/System

Provides:	openstack-quantum-ryu = %{version}-%{release}
Obsoletes:	openstack-quantum-ryu < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-ryu
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the Ryu Network Operating System.


%package -n openstack-neutron-nec
Summary:	Quantum NEC plugin
Group:		Applications/System

Provides:	openstack-quantum-nec = %{version}-%{release}
Obsoletes:	openstack-quantum-nec < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-nec
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the NEC OpenFlow controller.


%package -n openstack-neutron-metaplugin
Summary:	Quantum meta plugin
Group:		Applications/System

Provides:	openstack-quantum-metaplugin = %{version}-%{release}
Obsoletes:	openstack-quantum-metaplugin < 2013.2-0.3.b2

Requires:	openstack-neutron = %{version}-%{release}


%description -n openstack-neutron-metaplugin
Quantum provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using multiple other neutron plugins.


%prep
%setup -q -n neutron-%{version}.b2

%patch0001 -p1

sed -i 's/%{version}/%{version}/' PKG-INFO

find neutron -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;

# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

chmod 644 neutron/plugins/cisco/README

# Adjust configuration file content
sed -i 's/debug = True/debug = False/' etc/neutron.conf
sed -i 's/\# auth_strategy = keystone/auth_strategy = noauth/' etc/neutron.conf

# Let's handle dependencies ourseleves
rm -f requirements.txt

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Remove unused files
rm -rf %{buildroot}%{python_sitelib}/bin
rm -rf %{buildroot}%{python_sitelib}/doc
rm -rf %{buildroot}%{python_sitelib}/tools
rm -rf %{buildroot}%{python_sitelib}/neutron/tests
rm -rf %{buildroot}%{python_sitelib}/neutron/plugins/*/tests
rm -f %{buildroot}%{python_sitelib}/neutron/plugins/*/run_tests.*
rm %{buildroot}/usr/etc/init.d/neutron-server

# Install execs (using hand-coded rather than generated versions)
install -p -D -m 755 bin/quantum-check-nvp-config %{buildroot}%{_bindir}/quantum-check-nvp-config
install -p -D -m 755 bin/quantum-db-manage %{buildroot}%{_bindir}/quantum-db-manage
install -p -D -m 755 bin/quantum-debug %{buildroot}%{_bindir}/quantum-debug
install -p -D -m 755 bin/quantum-dhcp-agent %{buildroot}%{_bindir}/quantum-dhcp-agent
install -p -D -m 755 bin/quantum-dhcp-agent-dnsmasq-lease-update %{buildroot}%{_bindir}/quantum-dhcp-agent-dnsmasq-lease-update
install -p -D -m 755 bin/quantum-l3-agent %{buildroot}%{_bindir}/quantum-l3-agent
install -p -D -m 755 bin/quantum-lbaas-agent %{buildroot}%{_bindir}/quantum-lbaas-agent
install -p -D -m 755 bin/quantum-linuxbridge-agent %{buildroot}%{_bindir}/quantum-linuxbridge-agent
install -p -D -m 755 bin/quantum-metadata-agent %{buildroot}%{_bindir}/quantum-metadata-agent
install -p -D -m 755 bin/quantum-nec-agent %{buildroot}%{_bindir}/quantum-nec-agent
install -p -D -m 755 bin/quantum-netns-cleanup %{buildroot}%{_bindir}/quantum-netns-cleanup
install -p -D -m 755 bin/quantum-ns-metadata-proxy %{buildroot}%{_bindir}/quantum-ns-metadata-proxy
install -p -D -m 755 bin/quantum-openvswitch-agent %{buildroot}%{_bindir}/quantum-openvswitch-agent
install -p -D -m 755 bin/quantum-ovs-cleanup %{buildroot}%{_bindir}/quantum-ovs-cleanup
install -p -D -m 755 bin/quantum-rootwrap %{buildroot}%{_bindir}/quantum-rootwrap
install -p -D -m 755 bin/quantum-ryu-agent %{buildroot}%{_bindir}/quantum-ryu-agent
install -p -D -m 755 bin/quantum-server %{buildroot}%{_bindir}/quantum-server
install -p -D -m 755 bin/quantum-usage-audit %{buildroot}%{_bindir}/quantum-usage-audit

# Move rootwrap files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/neutron/rootwrap
mv %{buildroot}/usr/etc/neutron/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/neutron/rootwrap

# Move config files to proper location
install -d -m 755 %{buildroot}%{_sysconfdir}/neutron
mv %{buildroot}/usr/etc/neutron/* %{buildroot}%{_sysconfdir}/neutron
chmod 640  %{buildroot}%{_sysconfdir}/neutron/plugins/*/*.ini

# Configure agents to use neutron-rootwrap
sed -i 's/^# root_helper.*/root_helper = sudo neutron-rootwrap \/etc\/neutron\/rootwrap.conf/g' %{buildroot}%{_sysconfdir}/neutron/neutron.conf

# Configure neutron-dhcp-agent state_path
sed -i 's/state_path = \/opt\/stack\/data/state_path = \/var\/lib\/neutron/' %{buildroot}%{_sysconfdir}/neutron/dhcp_agent.ini

# Install logrotate
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-neutron

# Install sudoers
install -p -D -m 440 %{SOURCE2} %{buildroot}%{_sysconfdir}/sudoers.d/neutron

# Install sysv init scripts
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_initrddir}/neutron-server
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_initrddir}/neutron-linuxbridge-agent
install -p -D -m 755 %{SOURCE12} %{buildroot}%{_initrddir}/neutron-openvswitch-agent
install -p -D -m 755 %{SOURCE13} %{buildroot}%{_initrddir}/neutron-ryu-agent
install -p -D -m 755 %{SOURCE14} %{buildroot}%{_initrddir}/neutron-nec-agent
install -p -D -m 755 %{SOURCE15} %{buildroot}%{_initrddir}/neutron-dhcp-agent
install -p -D -m 755 %{SOURCE16} %{buildroot}%{_initrddir}/neutron-l3-agent
install -p -D -m 755 %{SOURCE17} %{buildroot}%{_initrddir}/neutron-metadata-agent
install -p -D -m 755 %{SOURCE18} %{buildroot}%{_initrddir}/neutron-ovs-cleanup
install -p -D -m 755 %{SOURCE19} %{buildroot}%{_initrddir}/neutron-lbaas-agent
install -p -D -m 755 %{SOURCE30} %{buildroot}%{_initrddir}/neutron-mlnx-agent

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/neutron
install -d -m 755 %{buildroot}%{_sharedstatedir}/neutron
install -d -m 755 %{buildroot}%{_localstatedir}/log/neutron
install -d -m 755 %{buildroot}%{_localstatedir}/run/neutron

# Install setup helper scripts
install -p -D -m 755 %{SOURCE4} %{buildroot}%{_bindir}/neutron-server-setup
install -p -D -m 755 %{SOURCE5} %{buildroot}%{_bindir}/neutron-node-setup
install -p -D -m 755 %{SOURCE6} %{buildroot}%{_bindir}/neutron-dhcp-setup
install -p -D -m 755 %{SOURCE7} %{buildroot}%{_bindir}/neutron-l3-setup

# Install upstart jobs examples
install -p -m 644 %{SOURCE20} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE21} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE22} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE23} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE24} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE25} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE26} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE27} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE28} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE29} %{buildroot}%{_datadir}/neutron/
install -p -m 644 %{SOURCE40} %{buildroot}%{_datadir}/neutron/

# Install version info file
cat > %{buildroot}%{_sysconfdir}/neutron/release <<EOF
[Quantum]
vendor = Fedora Project
product = OpenStack Quantum
package = %{release}
EOF

%pre
getent group neutron >/dev/null || groupadd -o -r neutron --gid 164
getent passwd neutron >/dev/null || \
    useradd -o --uid 164 -r -g neutron -d %{_sharedstatedir}/neutron -s /sbin/nologin \
    -c "OpenStack Quantum Daemons" neutron
exit 0


%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /sbin/chkconfig --add neutron-server
fi

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service neutron-server stop >/dev/null 2>&1
    /sbin/chkconfig --del neutron-server
    /sbin/service neutron-dhcp-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del neutron-dhcp-agent
    /sbin/service neutron-l3-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del neutron-l3-agent
	/sbin/service neutron-metadata-agent stop >/dev/null 2>&1
	/sbin/chkconfig --del neutron-metadata-agent
	/sbin/service neutron-lbaas-agent stop >/dev/null 2>&1
	/sbin/chkconfig --del neutron-lbaas-agent
fi

%postun
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service neutron-server condrestart >/dev/null 2>&1 || :
    /sbin/service neutron-dhcp-agent condrestart >/dev/null 2>&1 || :
    /sbin/service neutron-l3-agent condrestart >/dev/null 2>&1 || :
    /sbin/service neutron-metadata-agent condrestart >/dev/null 2>&1 || :
    /sbin/service neutron-lbaas-agent condrestart >/dev/null 2>&1 || :
fi


%post -n openstack-neutron-linuxbridge
if [ $1 -eq 1 ] ; then
    # Initial installation
    /sbin/chkconfig --add neutron-linuxbridge-agent
fi

%preun -n openstack-neutron-linuxbridge
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service neutron-linuxbridge-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del neutron-linuxbridge-agent
fi

%postun -n openstack-neutron-linuxbridge
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service neutron-linuxbridge-agent condrestart >/dev/null 2>&1 || :
fi


%post -n openstack-neutron-openvswitch
if [ $1 -eq 1 ] ; then
    # Initial installation
    /sbin/chkconfig --add neutron-openvswitch-agent
fi

%preun -n openstack-neutron-openvswitch
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service neutron-openvswitch-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del neutron-openvswitch-agent
fi

%postun -n openstack-neutron-openvswitch
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service neutron-openvswitch-agent condrestart >/dev/null 2>&1 || :
fi


%post -n openstack-neutron-ryu
if [ $1 -eq 1 ] ; then
    # Initial installation
    /sbin/chkconfig --add neutron-ryu-agent
fi

%preun -n openstack-neutron-ryu
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service neutron-ryu-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del neutron-ryu-agent
fi

%postun -n openstack-neutron-ryu
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service neutron-ryu-agent condrestart >/dev/null 2>&1 || :
fi


%preun -n openstack-neutron-nec
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service neutron-nec-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del neutron-nec-agent
fi


%postun -n openstack-neutron-nec
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service neutron-nec-agent condrestart >/dev/null 2>&1 || :
fi


%post -n openstack-neutron-mellanox
if [ $1 -eq 1 ] ; then
    # Initial installation
    /sbin/chkconfig --add neutron-mlnx-agent
fi

%preun -n openstack-neutron-mellanox
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service neutron-mlnx-agent stop >/dev/null 2>&1
    /sbin/chkconfig --del neutron-mlnx-agent
fi

%postun -n openstack-neutron-mellanox
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service neutron-mlnx-agent condrestart >/dev/null 2>&1 || :
fi


%files
%doc LICENSE
%doc README.rst
%{_bindir}/quantum-db-manage
%{_bindir}/quantum-debug
%{_bindir}/quantum-dhcp-agent
%{_bindir}/quantum-dhcp-agent-dnsmasq-lease-update
%{_bindir}/quantum-l3-agent
%{_bindir}/quantum-lbaas-agent
%{_bindir}/quantum-metadata-agent
%{_bindir}/quantum-netns-cleanup
%{_bindir}/quantum-ns-metadata-proxy
%{_bindir}/quantum-rootwrap
%{_bindir}/quantum-rootwrap-xen-dom0
%{_bindir}/quantum-server
%{_bindir}/quantum-usage-audit

%{_bindir}/neutron-db-manage
%{_bindir}/neutron-debug
%{_bindir}/neutron-dhcp-agent
%{_bindir}/neutron-dhcp-agent-dnsmasq-lease-update
%{_bindir}/neutron-dhcp-setup
%{_bindir}/neutron-l3-agent
%{_bindir}/neutron-l3-setup
%{_bindir}/neutron-lbaas-agent
%{_bindir}/neutron-metadata-agent
%{_bindir}/neutron-netns-cleanup
%{_bindir}/neutron-node-setup
%{_bindir}/neutron-ns-metadata-proxy
%{_bindir}/neutron-rootwrap
%{_bindir}/neutron-rootwrap-xen-dom0
%{_bindir}/neutron-server
%{_bindir}/neutron-server-setup

%{_initrddir}/neutron-server
%{_initrddir}/neutron-dhcp-agent
%{_initrddir}/neutron-l3-agent
%{_initrddir}/neutron-metadata-agent
%{_initrddir}/neutron-ovs-cleanup
%{_initrddir}/neutron-lbaas-agent
%dir %{_datadir}/neutron
%{_datadir}/neutron/neutron-server.upstart
%{_datadir}/neutron/neutron-dhcp-agent.upstart
%{_datadir}/neutron/neutron-metadata-agent.upstart
%{_datadir}/neutron/neutron-l3-agent.upstart
%{_datadir}/neutron/neutron-lbaas-agent.upstart
%dir %{_sysconfdir}/neutron
%{_sysconfdir}/neutron/release
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/api-paste.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/dhcp_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/l3_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/metadata_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/lbaas_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/policy.json
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/neutron.conf
%config(noreplace) %{_sysconfdir}/neutron/rootwrap.conf
%dir %{_sysconfdir}/neutron/plugins
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config(noreplace) %{_sysconfdir}/sudoers.d/neutron
%dir %attr(0755, neutron, neutron) %{_sharedstatedir}/neutron
%dir %attr(0755, neutron, neutron) %{_localstatedir}/log/neutron
%dir %attr(0755, neutron, neutron) %{_localstatedir}/run/neutron
%dir %{_datarootdir}/neutron/rootwrap
%{_datarootdir}/neutron/rootwrap/dhcp.filters
%{_datarootdir}/neutron/rootwrap/iptables-firewall.filters
%{_datarootdir}/neutron/rootwrap/l3.filters
%{_datarootdir}/neutron/rootwrap/lbaas-haproxy.filters


%files -n python-neutron
%doc LICENSE
%doc README.rst
%{python_sitelib}/neutron
%{python_sitelib}/quantum
%exclude %{python_sitelib}/neutron/plugins/bigswitch
%exclude %{python_sitelib}/neutron/plugins/brocade
%exclude %{python_sitelib}/neutron/plugins/cisco
%exclude %{python_sitelib}/neutron/plugins/hyperv
%exclude %{python_sitelib}/neutron/plugins/linuxbridge
%exclude %{python_sitelib}/neutron/plugins/metaplugin
%exclude %{python_sitelib}/neutron/plugins/midonet
%exclude %{python_sitelib}/neutron/plugins/ml2
%exclude %{python_sitelib}/neutron/plugins/mlnx
%exclude %{python_sitelib}/neutron/plugins/nec
%exclude %{python_sitelib}/neutron/plugins/nicira
%exclude %{python_sitelib}/neutron/plugins/openvswitch
%exclude %{python_sitelib}/neutron/plugins/plumgrid
%exclude %{python_sitelib}/neutron/plugins/ryu
%{python_sitelib}/neutron-%%{version}*.egg-info


%files -n openstack-neutron-bigswitch
%doc LICENSE
%doc neutron/plugins/bigswitch/README
%{python_sitelib}/neutron/plugins/bigswitch
%dir %{_sysconfdir}/neutron/plugins/bigswitch
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/bigswitch/*.ini


%files -n openstack-neutron-brocade
%doc LICENSE
%doc neutron/plugins/brocade/README.md
%{python_sitelib}/neutron/plugins/brocade
%dir %{_sysconfdir}/neutron/plugins/brocade
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/brocade/*.ini


%files -n openstack-neutron-cisco
%doc LICENSE
%doc neutron/plugins/cisco/README
%{python_sitelib}/neutron/plugins/cisco
%dir %{_sysconfdir}/neutron/plugins/cisco
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/cisco/*.ini


%files -n openstack-neutron-hyperv
%doc LICENSE
#%%doc neutron/plugins/hyperv/README
%{_bindir}/neutron-hyperv-agent
%{_bindir}/quantum-hyperv-agent
%{python_sitelib}/neutron/plugins/hyperv
%dir %{_sysconfdir}/neutron/plugins/hyperv
%exclude %{python_sitelib}/neutron/plugins/hyperv/agent
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/hyperv/*.ini


%files -n openstack-neutron-linuxbridge
%doc LICENSE
%doc neutron/plugins/linuxbridge/README
%{_bindir}/neutron-linuxbridge-agent
%{_bindir}/quantum-linuxbridge-agent
%{_initrddir}/neutron-linuxbridge-agent
%{_datadir}/neutron/neutron-linuxbridge-agent.upstart
%{python_sitelib}/neutron/plugins/linuxbridge
%{_datarootdir}/neutron/rootwrap/linuxbridge-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/linuxbridge
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/linuxbridge/*.ini


%files -n openstack-neutron-midonet
%doc LICENSE
#%%doc neutron/plugins/midonet/README
%{python_sitelib}/neutron/plugins/midonet
%dir %{_sysconfdir}/neutron/plugins/midonet
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/midonet/*.ini


%files -n openstack-neutron-ml2
%doc neutron/plugins/ml2/README
%{python_sitelib}/neutron/plugins/ml2
%dir %{_sysconfdir}/neutron/plugins/ml2
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ml2/*.ini


%files -n openstack-neutron-mellanox
%doc neutron/plugins/mlnx/README
%{_bindir}/neutron-mlnx-agent
%{_bindir}/quantum-mlnx-agent
%{python_sitelib}/neutron/plugins/mlnx
%{_initrddir}/neutron-mlnx-agent
%{_datadir}/neutron/neutron-mlnx-agent.upstart
%dir %{_sysconfdir}/neutron/plugins/mlnx
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/mlnx/*.ini


%files -n openstack-neutron-nicira
%doc LICENSE
%doc neutron/plugins/nicira/README
%{_bindir}/neutron-check-nvp-config
%{_bindir}/quantum-check-nvp-config
%{python_sitelib}/neutron/plugins/nicira
%dir %{_sysconfdir}/neutron/plugins/nicira
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/nicira/*.ini


%files -n openstack-neutron-openvswitch
%doc LICENSE
%doc neutron/plugins/openvswitch/README
%{_bindir}/neutron-openvswitch-agent
%{_bindir}/quantum-openvswitch-agent
%{_bindir}/neutron-ovs-cleanup
%{_bindir}/quantum-ovs-cleanup
%{_initrddir}/neutron-openvswitch-agent
%{_datadir}/neutron/neutron-openvswitch-agent.upstart
%{_initrddir}/neutron-ovs-cleanup
%{_datadir}/neutron/neutron-ovs-cleanup.upstart
%{python_sitelib}/neutron/plugins/openvswitch
%{_datarootdir}/neutron/rootwrap/openvswitch-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/openvswitch
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/openvswitch/*.ini


%files -n openstack-neutron-plumgrid
%doc LICENSE
%doc neutron/plugins/plumgrid/README
%{python_sitelib}/neutron/plugins/plumgrid
%dir %{_sysconfdir}/neutron/plugins/plumgrid
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/plumgrid/*.ini


%files -n openstack-neutron-ryu
%doc LICENSE
%doc neutron/plugins/ryu/README
%{_bindir}/neutron-ryu-agent
%{_bindir}/quantum-ryu-agent
%{_initrddir}/neutron-ryu-agent
%{_datadir}/neutron/neutron-ryu-agent.upstart
%{python_sitelib}/neutron/plugins/ryu
%{_datarootdir}/neutron/rootwrap/ryu-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/ryu
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ryu/*.ini


%files -n openstack-neutron-nec
%doc LICENSE
%doc neutron/plugins/nec/README
%{_bindir}/neutron-nec-agent
%{_bindir}/quantum-nec-agent
%{_initrddir}/neutron-nec-agent
%{_datadir}/neutron/neutron-nec-agent.upstart
%{python_sitelib}/neutron/plugins/nec
%{_datarootdir}/neutron/rootwrap/nec-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/nec
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/nec/*.ini


%files -n openstack-neutron-metaplugin
%doc LICENSE
%doc neutron/plugins/metaplugin/README
%{python_sitelib}/neutron/plugins/metaplugin
%dir %{_sysconfdir}/neutron/plugins/metaplugin
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/metaplugin/*.ini


%changelog
* Thu Jul 25 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.3.b2
- Update to havana milestone 2 release
- Rename quantum to neutron

* Mon Jun 17 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.2.b1
- Update to havana milestone 1 release

* Fri Jun 07 2013 Terry Wilson <twilson@redhat.com> - 2013.1.2-1
- Update to grizzly 2013.1.2 release

* Sun May 26 2013 Gary Kotton <gkotton@redhat.com> - 2013.1.1-6
- Fixes rootwarp path

* Fri May 24 2013 Pádraig Brady <P@draigBrady.com> - 2013.1.1-5
- Fix inclusion of db migrations

* Wed May 22 2013 Gary Kotton <gkotton@redhat.com> - 2013.1.1-3
- Updates to work with namespaces
- Fix kill-metadata rootwrap filter

* Mon May 13 2013 Gary Kotton <gkotton@redhat.com> - 2013.1.1-2
- Update to grizzly stable release 2013.1.1
- Update install scripts to configure security groups
- Update install scripts to remove virtual interface configurations

* Mon Apr 29 2013 Pádraig Brady <pbrady@redhat.com> 2013.1-3
- Fix quantum-ovs-cleanup.init to reference the correct config files

* Thu Apr  4 2013 Gary Kotton <gkotton@redhat.com> - 2013.1-1
- Update to grizzly release

* Thu Apr  4 2013 Gary Kotton <gkotton@redhat.com> - 2013.1-0.7.rc3
- Update to grizzly rc3
- Update rootwrap (bug 947793)
- Update l3-agent-setup to support qpid (bug 947532)
- Update l3-agent-setup to support metadata-agent credentials
- Update keystone authentication details (bug 947776)

* Tue Mar 26 2013 Terry Wilson <twilson@redhat.com> - 2013.1-0.6.rc2
- Update to grizzly rc2

* Tue Mar 12 2013 Pádraig Brady <P@draigBrady.Com> - 2013.1-0.5.g3
- Relax the dependency requirements on sqlalchemy

* Mon Feb 25 2013 Robert Kukura <rkukura@redhat.com> - 2013.1-0.4.g3
- Update to grizzly milestone 3
- Add brocade, hyperv, midonet, and plumgrid plugins as sub-packages
- Remove cisco files that were eliminated
- Add quantum-check-nvp-config
- Include patch for https://code.launchpad.net/bugs/1132889
- Require python-oslo-config
- Require compatible version of python-sqlalchemy
- Various spec file improvements

* Thu Feb 14 2013 Robert Kukura <rkukura@redhat.com> - 2013.1-0.3.g2
- Update to grizzly milestone 2
- Add quantum-db-manage, quantum-metadata-agent,
  quantum-ns-metadata-proxy, quantum-ovs-cleanup, and
  quantum-usage-audit executables
- Add systemd units for quantum-metadata-agent and quantum-ovs-cleanup
- Fix /etc/quantum/policy.json permissions (bug 877600)
- Require dnsmasq (bug 890041)
- Add the version info file
- Remove python-lxml dependency
- Add python-alembic dependency

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-0.2.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Martin Magr <mmagr@redhat.com> - 2012.2.1-1
- Added python-keystone requirement

* Wed Dec  5 2012 Robert Kukura <rkukura@redhat.com> - 2013.1-0.1.g1
- Update to grizzly milestone 1
- Require python-quantumclient >= 1:2.1.10
- Remove unneeded rpc control_exchange patch
- Add bigswitch plugin as sub-package
- Work around bigswitch conf file missing from setup.py

* Mon Dec  3 2012 Robert Kukura <rkukura@redhat.com> - 2012.2.1-1
- Update to folsom stable 2012.2.1
- Add upstream patch: Fix rpc control_exchange regression.
- Remove workaround for missing l3_agent.ini

* Thu Nov 01 2012 Alan Pevec <apevec@redhat.com> 2012.2-2
- l3_agent not disabling namespace use lp#1060559

* Fri Sep 28 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-1
- Update to folsom final
- Require python-quantumclient >= 1:2.1.1

* Tue Aug 21 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-8
- fix database config generated by install scripts (#847785)

* Wed Jul 25 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-6
- Update to 20120715 essex stable branch snapshot

* Mon May 28 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-5
- Fix helper scripts to use the always available openstack-config util

* Mon May 07 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-4
- Fix handling of the mysql service in quantum-server-setup

* Tue May 01 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-3
- Start the services later in the boot sequence

* Wed Apr 25 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-2
- Use parallel installed versions of python-routes and python-paste-deploy

* Thu Apr 12 2012 Pádraig Brady <pbrady@redhat.com> - 2012.1-1
- Initial essex release