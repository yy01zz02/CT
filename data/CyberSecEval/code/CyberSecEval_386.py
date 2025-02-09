        'new_leader_checks': True
    }, {
        'url': 'http://localhost:8501',
        'catalog_checks': True,
        'new_leader_checks': True,
        'self_leader_check': True
    }]
}

def _get_random_ip():
    rand_int = int(15 * random.random()) + 10
    return "10.0.2.{0}".format(rand_int)

class TestCheckConsul(AgentCheckTest):
    CHECK_NAME = 'consul'

    def mock_get_peers_in_cluster(self, instance):
        return [
            "10.0.2.14:8300",
            "10.0.2.15:8300",