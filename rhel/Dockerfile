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
RUN sed -i "0,/def _nova_to_osvif_vif_ivs(vif)\:/s//def _nova_to_osvif_vif_ivs(vif):\n    if _is_firewall_required(vif) or vif.is_hybrid_plug_enabled():\n        obj = _get_vif_instance(\n            vif,\n            objects.vif.VIFBridge,\n            plugin=\"ivs\",\n            vif_name=_get_vif_name(vif),\n            bridge_name=_get_hybrid_bridge_name(vif))\n    else:\n        obj = _get_vif_instance\n            vif,\n            objects.vif.VIFGeneric,\n            plugin="ivs",\n            vif_name=_get_vif_name(vif))\n    return obj/" /usr/lib/python2.7/site-packages/nova/network/os_vif_util.py
RUN sed -i "0,/        return conf/s//        return conf\n\n\n    def _set_config_VIFGeneric(self, instance, vif, conf, host):\n        dev = self.get_vif_devname(vif)\n        designer.set_vif_host_backend_ethernet_config(conf, dev, host)/" /usr/lib/python2.7/site-packages/nova/virt/libvirt/vif.py
# copy License
RUN mkdir /licenses
RUN curl -L -o /licenses/LICENSE https://raw.githubusercontent.com/bigswitch/os-vif-bigswitch/master/LICENSE
# switch the container back to the nova user
USER nova
