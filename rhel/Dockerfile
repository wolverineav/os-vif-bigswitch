FROM registry.access.redhat.com/rhosp13/openstack-nova-compute
MAINTAINER Big Switch Networks Inc <rhosp-bugs-internal@bigswitch.com>
LABEL name="rhosp13/openstack-nova-compute-bigswitch" \
      maintainer="rhosp-bugs-internal@bigswitch.com" \
      vendor="Big Switch Networks Inc" \
      version="13.0" \
      release="1" \
      summary="Red Hat OpenStack Platform 13.0 Nova Compute Big Switch Networks OS-VIF Plugin" \
      description="Red Hat OpenStack Platform 13.0 Nova Compute Big Switch Networks OS-VIF Plugin"
# switch to root and install networking-bigswitch from PYPI
USER root
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py"
RUN python /tmp/get-pip.py
RUN pip install --upgrade "os-vif-bigswitch>=12.0.0,<12.1.0"
# hack to workaround os-vif not being picked up
RUN sed -i "0,/            nova.privsep.libvirt.disable_ipv6(br_name)/s//            if os.path.exists(\'\/proc\/sys\/net\/ipv6\/conf\/\%s\/disable_ipv6\' \% br_name):\n                nova.privsep.libvirt.disable_ipv6(br_name)/" /usr/lib/python2.7/site-packages/nova/virt/libvirt/vif.py
# copy License
RUN mkdir /licenses
RUN curl -L -o /licenses/LICENSE https://raw.githubusercontent.com/bigswitch/os-vif-bigswitch/master/LICENSE
# switch the container back to the nova user
USER nova
