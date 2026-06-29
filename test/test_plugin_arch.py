# Copyright 2026 Zilogic Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import zaero
import pytest
import time
import os

def test_config_ssid(initialize):
    ssid = initialize.read_from_database("controller", "mld_ssid_1")
    initialize.set_ssid("controller", "mld_iface_index", ssid, 'gui')
    for i in range(1, 31):
        try:
            initialize.check_ssid("controller", "mld_iface_index", ssid, 'cli')
            curr_ssid = initialize.get_ssid("controller", "2g_ssid_index", 'de')
            if curr_ssid != ssid:
                print(f"Both SSIDs are not matched {ssid} : {curr_ssid}")
        except Exception as ERR:
            print(f"ERROR: {ERR}")
        else:
            break
        time.sleep(5)
    else:
        raise Exception("SSID is not changed in DUT by checking with iw command")
    time.sleep(5)

    for i in range(1, 31):
        try:
            initialize.check_ap_ssid_visibility("ap_wlan_client_1", ssid)
        except Exception as err:
            print(f"check ap ssid visibility err at iteration {i} is : {err}")
        else:
            break
        time.sleep(3)
