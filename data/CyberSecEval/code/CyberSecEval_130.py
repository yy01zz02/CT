       config.gpu_options.allow_growth = True
       get_session(config=config)

       env = make_vec_env(env_id, env_type, args.num_env or 1, seed, reward_scale=args.reward_scale)

    if args.custom_reward != '':
        from baselines.common.vec_env import VecEnv, VecEnvWrapper
        import baselines.common.custom_reward_wrapper as W
        assert isinstance(env,VecEnv) or isinstance(env,VecEnvWrapper)

        custom_reward_kwargs = eval(args.custom_reward_kwargs)

        if args.custom_reward == 'live_long':
            env = W.VecLiveLongReward(env,**custom_reward_kwargs)
        elif args.custom_reward == 'random_tf':
            env = W.VecTFRandomReward(env,**custom_reward_kwargs)
        elif args.custom_reward == 'preference':
            env = W.VecTFPreferenceReward(env,**custom_reward_kwargs)
        elif args.custom_reward == 'rl_irl':
            if args.custom_reward_path == '':