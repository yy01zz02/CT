                                         directory = \
                                         RubyDirectoryMemory( \
                                                    version = i,
                                                    size = dir_size,
                                                    use_map = options.use_map,
                                                    map_levels = \
                                                      options.map_levels),
                                         memBuffer = mem_cntrl,
                                         ruby_system = ruby_system)

        exec("system.dir_cntrl%d = dir_cntrl" % i)
        dir_cntrl_nodes.append(dir_cntrl)

        cntrl_count += 1

    for i, dma_port in enumerate(dma_ports):
        #
        # Create the Ruby objects associated with the dma controller
        #
        dma_seq = DMASequencer(version = i,