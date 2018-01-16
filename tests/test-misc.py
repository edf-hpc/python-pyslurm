from __future__ import absolute_import, unicode_literals

import pyslurm
import subprocess
from nose.tools import assert_equals, assert_true
from socket import gethostname

def test_slurm_ping():
    """Misc: Test slurm_ping() return."""
    slurm_ping = pyslurm.slurm_ping()
    assert_equals(slurm_ping, 0)


def test_slurm_reconfigure():
    """Misc: Test slurm_reconfigure() return."""
    slurm_reconfigure = pyslurm.slurm_reconfigure()
    assert_equals(slurm_reconfigure, 0)


def test_slurm_get_controllers():
    """Misc: Test slurm_get_controllers()."""
    controllers = pyslurm.get_controllers()
    assert_equals(controllers[0], gethostname())


def test_slurm_is_controller():
    """Misc: Test slurm_is_controller()."""
    controller = pyslurm.is_controller()
    assert_equals(controller, "primary")


def test_slurm_api_version():
    """Misc: Test slurm_api_version()."""
    ver = pyslurm.slurm_api_version()
    assert_equals(ver[0], 17)
    assert_equals(ver[1], 11)


def test_slurm_load_slurmd_status():
    """Misc: Test slurm_load_slurmd_status()."""
    status_info = pyslurm.slurm_load_slurmd_status()["localhost"]
    sctl = subprocess.Popen(["scontrol", "-d", "show", "slurmd"],
                            stdout=subprocess.PIPE).communicate()
    sctl_stdout = sctl[0].strip().decode("UTF-8").split("\n")
    sctl_dict = dict((value.split("=")[0].strip(), value.split("=")[1].strip())
                     for value in sctl_stdout)

    assert_equals(status_info["step_list"], sctl_dict["Active Steps"])
    assert_equals(status_info["actual_boards"], int(sctl_dict["Actual Boards"]))
    assert_equals(status_info["actual_cpus"], int(sctl_dict["Actual CPUs"]))
    assert_equals(status_info["actual_sockets"], int(sctl_dict["Actual sockets"]))
    assert_equals(status_info["actual_cores"], int(sctl_dict["Actual cores"]))
    assert_equals(status_info["slurmd_logfile"], sctl_dict["Slurmd Logfile"])
    assert_equals(status_info["version"], sctl_dict["Version"])
