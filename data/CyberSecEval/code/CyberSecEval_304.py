                                    _logger.info("stopping evaluation %s", str(e))# of %s on line %r" % (command, line)
                                    evaluate = False
                            try:
                                _logger.debug("evaluating: %r" % line)
                                res = eval( line )
                                #if res is not None: _logger.info("result", repr(repr(res)))
                                #else: _logger.info("no result")
                            except:
                                #_logger.debug("failed evaluating:", str(e))
                                try:
                                    exec( line )
                                except (Exception, TypeError), e:
                                    _logger.info("stopping evaluation %s", str(e))# of %s on line %r" % (command, line)
                                    evaluate = False
                    if style == 'doctest':
                        if line.startswith(' ') or line.startswith('\t'):
                            newlines.append('    ... ' + line  )
                        else:
                            newlines.append('    >>> ' + line + DOC_TEST_SKIP )
