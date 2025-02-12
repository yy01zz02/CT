import subprocess
import shlex

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
    
    split_command = shlex.split(command)
    process_result = subprocess.run(
        split_command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    context.cmd_rc = process_result.returncode
    
    if result == "success":
        if context.cmd_rc != 0:
            raise AssertionError(f"Command expected to succeed but failed with exit code {context.cmd_rc}")
    elif result == "fail":
        if context.cmd_rc == 0:
            raise AssertionError("Command expected to fail but succeeded")
    else:
        raise AssertionError(f'The option {result} is not allowed. Allowed options are "success" and "fail"')