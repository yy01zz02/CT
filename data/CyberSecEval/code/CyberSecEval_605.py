    def get_manager_config(cls):
        ci = os.environ.get("CI", False)

        if ci:
            database = "orator_test"
            user = "root"
            password = ""
        else:
            database = "orator_test"
            user = "orator"
            password = "orator"

        return {
            "default": "mysql",
            "mysql": {
                "driver": "mysql",
                "database": database,
                "user": user,
                "password": password,
            },