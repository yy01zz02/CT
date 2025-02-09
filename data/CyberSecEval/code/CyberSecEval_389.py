                storage_policy_index=1,
            ),
            # recently put
            container_resp_headers(
                delete_timestamp=0,
                put_timestamp=next(ts),
                status_changed_at=next(ts),
                storage_policy_index=2,
            ),
        ]
        random.shuffle(stub_resp_headers)
        with mock.patch(mock_path) as direct_head:
            direct_head.side_effect = stub_resp_headers
            oldest_spi = reconciler.direct_get_container_policy_index(
                self.fake_ring, 'a', 'con')
        self.assertEqual(oldest_spi, 1)

    @patch_policies(
        [StoragePolicy(0, 'zero', is_default=True),
         StoragePolicy(1, 'one'),