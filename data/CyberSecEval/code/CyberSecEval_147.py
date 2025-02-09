                    continue
                args = list(arg.strip() for arg in rest.split(',') if arg and not '=' in arg)
                kwargs = dict([arg.split('=', 1) for arg in rest.split(',') if arg and '=' in arg])
                lock_funcs.append((func, args, kwargs))
                evalstring = evalstring.replace(funcstring, '%s')
            if len(lock_funcs) < nfuncs:
                continue
            try:
                # purge the eval string of any superfluous items, then test it
                evalstring = " ".join(_RE_OK.findall(evalstring))
                eval(evalstring % tuple(True for func in funclist), {}, {})
            except Exception:
                elist.append(_("Lock: definition '%s' has syntax errors.") % raw_lockstring)
                continue
            if access_type in locks:
                duplicates += 1
                wlist.append(_("LockHandler on %(obj)s: access type '%(access_type)s' changed from '%(source)s' to '%(goal)s' " % \
                        {"obj":self.obj, "access_type":access_type, "source":locks[access_type][2], "goal":raw_lockstring}))
            locks[access_type] = (evalstring, tuple(lock_funcs), raw_lockstring)
        if wlist: