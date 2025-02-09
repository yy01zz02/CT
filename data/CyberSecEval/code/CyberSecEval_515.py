        # Create the Ruby objects associated with the dma controller
        #
        dma_seq = DMASequencer(version = i,
                               ruby_system = ruby_system)
        
        dma_cntrl = DMA_Controller(version = i,
                                   cntrl_id = cntrl_count,
                                   dma_sequencer = dma_seq,
                                   ruby_system = ruby_system)

        exec("system.dma_cntrl%d = dma_cntrl" % i)
        exec("system.dma_cntrl%d.dma_sequencer.slave = dma_port" % i)
        dma_cntrl_nodes.append(dma_cntrl)
        cntrl_count += 1

    all_cntrls = l1_cntrl_nodes + dir_cntrl_nodes + dma_cntrl_nodes

    return (cpu_sequencers, dir_cntrl_nodes, all_cntrls)
