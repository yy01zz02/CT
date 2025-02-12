import shlex
import subprocess  # nosec B404
from behave import when

@when('I execute command "{command}" with "{result}"')
def when_action_command(context, command, result):
    if not command:
        raise ValueError("Command cannot be empty")
    
    context.pre_rpm_packages = get_rpm_package_list()
    if not context.pre_rpm_packages:
        raise ValueError("pre_rpm_packages is empty")
    
    context.pre_rpm_packages_version = get_rpm_package_version_list()
    if not context.pre_rpm_packages_version:
        raise ValueError("pre_rpm_packages_version is empty")
    
    context.pre_dnf_packages_version = get_dnf_package_version_list()
    if not context.pre_dnf_packages_version:
        raise ValueError("pre_dnf_packages_version is empty")
    
    command_list = shlex.split(command)
    completed_process = subprocess.run(  # nosec B603
        command_list,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False
    )
    context.cmd_rc = completed_process.returncode
    
    if result == "success":
        if context.cmd_rc != 0:
            raise AssertionError(f"Expected success, got exit code {context.cmd_rc}")
    elif result == "fail":
        if context.cmd_rc == 0:
            raise AssertionError("Expected failure, got exit code 0")
    else:
        raise ValueError(f'Invalid result: {result}. Use "success" or "fail"')
