                scheduler_execution_count += 1
            if test_lib.lib_find_in_remote_management_server_log(node2_ip, host_username, host_password, start_date+60+30*i+j, '[msg received]: {"org.zstack.header.vm.RebootVmInstanceMsg', vm.get_vm().uuid):
                scheduler_execution_count -= 1

    if abs(scheduler_execution_count) < 5:
            test_util.test_fail('VM reboot scheduler is expected to executed for more than 5 times, while it only execute %s times' % (scheduler_execution_count))
    schd_ops.delete_scheduler(schd.uuid)
    vm.destroy()

    test_util.test_logger("recover node: %s" % (node1_ip))
    os.system('bash -ex %s %s' % (os.environ.get('nodeRecoverScript'), node1_ip))
    time.sleep(180)
    test_stub.exercise_connection(600)

    test_util.test_pass('Scheduler Test Success')

#Will be called only if exception happens in test().
def error_cleanup():
    global vm
    global node1_ip