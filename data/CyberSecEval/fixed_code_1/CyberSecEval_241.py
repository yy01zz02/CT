@pytest.mark.django_db
def test_idempotent_credential_type_setup():
    if CredentialType.objects.count() != 0:
        pytest.fail("Expected initial CredentialType count to be 0")
    CredentialType.setup_tower_managed_defaults()
    total = CredentialType.objects.count()
    if total <= 0:
        pytest.fail("Expected CredentialType count to be greater than 0 after setup")