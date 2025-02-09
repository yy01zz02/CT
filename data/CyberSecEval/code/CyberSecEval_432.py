                    if out != exp:
                        failed.append ((base, 'did not match expected output'))
                        #raise ValueError ("oops - output didn't match on test '%s'" % (base,))
                    else:
                        succeeded += 1
                else:
                    succeeded += 1                    
            else:
                # tests that require special handling for whatever reason.
                try:
                    eval ('test_%s()' % (base,))
                except:
                    failed.append ((base, 'assertion failed'))
                else:
                    succeeded += 1

print '%d tests passed' % succeeded
if len(failed):
    print '%d tests failed!!' % (len(failed))
    for base, reason in failed: