        # warn about the deprecated name
        self.log.warning(
            "KubeSpawner.%s is deprecated in %s. Use KubeSpawner.%s",
            name,
            version,
            new_name,
        )
        return setattr(self, new_name, value)

    for _deprecated_name, (_new_name, _version) in _deprecated_traits.items():
        exec(
            """{0} = property(
                partial(_get_deprecated, '{0}', '{1}', '{2}'),
                partial(_set_deprecated, '{0}', '{1}', '{2}'),
            )
            """.format(
                _deprecated_name,
                _new_name,
                _version,
            )