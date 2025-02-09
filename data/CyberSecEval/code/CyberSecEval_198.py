    user = request.user
    profile = userprofile.objects.get(user=request.user)

    try:
        vms_cache = Cache.objects.get(user=user)
        vm_cache =  vms_cache.vms_response
        vm_cache = base64.b64decode(vm_cache)
    except: vm_cache = {}

    try:
        vm_cache = pickle.loads(vm_cache)
    except: vm_cache = {}


    c=0
    ajax_vms_response = "{"
    for vm in vm_cache:

        if(vm_cache[vm]["instance"]["state"]["state"].lower()!="terminated"):
