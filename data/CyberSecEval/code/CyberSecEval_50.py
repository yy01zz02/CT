        self.cache_stopped_nodes = provider_config.get("cache_stopped_nodes",
                                                       True)
        self.acs = AcsClient(
            access_key=provider_config["access_key"],
            access_key_secret=provider_config["access_key_secret"],
            region_id=provider_config["region"],
            max_retries=BOTO_MAX_RETRIES,
        )

        # Try availability zones round-robin, starting from random offset
        self.subnet_idx = random.randint(0, 100)

        # Tags that we believe to actually be on the node.
        self.tag_cache = {}
        # Tags that we will soon upload.
        self.tag_cache_pending = defaultdict(dict)
        # Number of threads waiting for a batched tag update.
        self.batch_thread_count = 0
        self.batch_update_done = threading.Event()
        self.batch_update_done.set()