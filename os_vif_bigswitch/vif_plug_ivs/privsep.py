# Copyright 2017 Big Switch Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_privsep import capabilities as c
from oslo_privsep import priv_context

vif_plug = priv_context.PrivContext(
    "os_vif_bigswitch.vif_plug_ivs",
    cfg_section="vif_plug_ivs_privileged",
    pypath=__name__ + ".vif_plug",
    capabilities=[c.CAP_NET_ADMIN],
)
