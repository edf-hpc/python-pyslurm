from __future__ import absolute_import, unicode_literals

import pyslurm
import subprocess
from nose.tools import assert_equals, assert_true

def test_job_get():
    """Job: Test job().get() return type."""
    all_jobs = pyslurm.job().get()
    assert_true(isinstance(all_jobs, dict))


def test_job_ids():
    """Job: Test job().ids() return type."""
    all_job_ids = pyslurm.job().ids()
    assert_true(isinstance(all_job_ids, list))


def test_job_count():
    """Job: Test job count."""
    all_jobs = pyslurm.job().get()
    all_job_ids = pyslurm.job().ids()
    assert_equals(len(all_jobs), len(all_job_ids))


def test_job_scontrol():
    """Job: Compare scontrol values to PySlurm values."""
    all_job_ids = pyslurm.job().ids()

    # Make sure job is running first
    test_job = all_job_ids[0]

    test_job_info = pyslurm.job().find_id(test_job)[0]
    assert_equals(test_job, test_job_info["job_id"])

    sctl = subprocess.Popen(["scontrol", "-d", "show", "job", str(test_job)],
                            stdout=subprocess.PIPE).communicate()
    sctl_stdout = sctl[0].strip().decode("UTF-8", "replace").split()
    sctl_dict = dict((value.split("=")[0], value.split("=")[1])
                     for value in sctl_stdout)

    assert_equals(test_job_info["batch_flag"], int(sctl_dict["BatchFlag"]))
    assert_equals(test_job_info["cpus_per_task"], int(sctl_dict["CPUs/Task"]))
    assert_equals(test_job_info["contiguous"], int(sctl_dict["Contiguous"]))
    assert_equals(test_job_info["exit_code"], sctl_dict["ExitCode"])
    assert_equals(test_job_info["job_id"], int(sctl_dict["JobId"]))
    assert_equals(test_job_info["name"], sctl_dict["JobName"])
    assert_equals(test_job_info["job_state"], sctl_dict["JobState"])
    assert_equals(test_job_info["nice"], int(sctl_dict["Nice"]))
    assert_equals(test_job_info["num_cpus"], int(sctl_dict["NumCPUs"]))
    assert_equals(test_job_info["num_nodes"], int(sctl_dict["NumNodes"]))
    assert_equals(test_job_info["partition"], sctl_dict["Partition"])
    assert_equals(test_job_info["priority"], int(sctl_dict["Priority"]))
    assert_equals(test_job_info["state_reason"], sctl_dict["Reason"])
    assert_equals(test_job_info["reboot"], int(sctl_dict["Reboot"]))
    assert_equals(test_job_info["requeue"], int(sctl_dict["Requeue"]))
    assert_equals(test_job_info["restart_cnt"], int(sctl_dict["Restarts"]))
    assert_equals(test_job_info["std_err"], sctl_dict["StdErr"])
    assert_equals(test_job_info["std_in"], sctl_dict["StdIn"])
    assert_equals(test_job_info["std_out"], sctl_dict["StdOut"])
    assert_equals(test_job_info["time_limit_str"], sctl_dict["TimeLimit"])
    assert_equals(test_job_info["work_dir"], sctl_dict["WorkDir"])
