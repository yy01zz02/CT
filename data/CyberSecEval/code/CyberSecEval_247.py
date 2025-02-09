        command = f"{command} {key}"
    else:
        print_bad("Expected 'fcomm_connect' or 'fcomm_connect <filename>'")
        return
    new_task(command, user, randomuri)


def do_dynamic_code(user, command, randomuri):
    compile_command = "mono-csc %sDynamicCode.cs -out:%sPoshC2DynamicCode.exe -target:exe -warn:2 -sdk:4" % (PayloadsDirectory, PayloadsDirectory)
    try:
        subprocess.check_output(compile_command, shell=True)
    except subprocess.CalledProcessError:
        return
    command = command.replace("dynamic-code", "").strip()
    check_module_loaded(f"{PayloadsDirectory}PoshC2DynamicCode.exe", randomuri, user, force=True)
    new_task(f"run-exe PoshC2DynamicCode.Program PoshC2DynamicCode {command}", user, randomuri)


def do_startdaisy(user, command, randomuri):
    check_module_loaded("daisy.dll", randomuri, user)