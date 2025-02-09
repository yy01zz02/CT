        self.shared_master_blocks = manager.dict()
        self.download_cond = Condition()

        self._started = True
        self.ctx = zmq.Context()
        self.host = socket.gethostname()
        if GUIDE_ADDR not in env.environ:
            start_guide_manager()

        self.guide_addr = env.get(GUIDE_ADDR)
        self.random_inst = random.SystemRandom()
        self.server_addr, self.server_thread = self.start_server()
        self.uuid_state_dict = {}
        self.uuid_map_dict = {}
        self.master_broadcast_blocks = {}
        env.register(DOWNLOAD_ADDR, self.server_addr)

    def start_server(self):
        sock = self.ctx.socket(zmq.REP)
        sock.setsockopt(zmq.LINGER, 0)