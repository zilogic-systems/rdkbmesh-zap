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

def test_wifi_reset(initialize: zaero.zaero):
    initialize.wifi_reset("controller", 'gui')
    initialize.reboot_device("extender1", "cli")
    time.sleep(5)
    initialize.reboot_device("controller", "cli")
    initialize.close_connection("controller")
    initialize.close_connection("extender1")
    time.sleep(10)

    for i in range(1, 41):
        print (f"FOR loop iteration : {i}")
        try:
            initialize.connect_with_device("controller")
        except:
            print("Connection FAILED with 'Controller'")
        else:
            print("Connection SUCCESS with 'Controller'")
            break
        time.sleep(10)

    for i in range(1, 41):
        print (f"FOR loop iteration : {i}")
        try:
            initialize.connect_with_device("extender1")
        except:
            print("Connection FAILED with 'Extender1'")
        else:
            print("Connection SUCCESS with 'Extender1'")
            break
        time.sleep(10)

    ssid = initialize.read_from_database("controller", "default_ssid")
    for i in range(1, 31):
        try:            
            initialize.check_ssid("controller", "mld_iface_index", ssid, 'cli')
            initialize.check_ssid("extender1", "mld_iface_index", ssid, 'cli')
        except Exception as err:
            print(err)
        else:
            break
        time.sleep(5)
    else:
        raise Exception("SSID is not changed in DUT by checking with iw command")
    time.sleep(10)
