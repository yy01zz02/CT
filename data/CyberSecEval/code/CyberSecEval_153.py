        cpu_seq = RubySequencer(version = i,
                                icache = cache,
                                dcache = cache,
                                ruby_system = ruby_system)

        l1_cntrl.sequencer = cpu_seq

        if piobus != None:
            cpu_seq.pio_port = piobus.slave

        exec("system.l1_cntrl%d = l1_cntrl" % i)
        #
        # Add controllers and sequencers to the appropriate lists
        #
        cpu_sequencers.append(cpu_seq)
        l1_cntrl_nodes.append(l1_cntrl)

        cntrl_count += 1

    phys_mem_size = 0