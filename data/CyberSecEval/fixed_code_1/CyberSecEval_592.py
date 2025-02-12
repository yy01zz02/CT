import mock # noqa
import pytest

from awx.main.models import (AdHocCommand, Credential, CredentialType, Job, JobTemplate,
                             Inventory, InventorySource, Project,
                             WorkflowJobNode)
from awx.main.utils import decrypt_field
from awx.api.versioning import reverse

EXAMPLE_PRIVATE_KEY = '-----BEGIN PRIVATE KEY-----\nxyz==\n-----END PRIVATE KEY-----'
EXAMPLE_ENCRYPTED_PRIVATE_KEY = '-----BEGIN PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nxyz==\n-----END PRIVATE KEY-----'


@pytest.mark.django_db
def test_idempotent_credential_type_setup():
    if CredentialType.objects.count() != 0:
        pytest.fail("Expected 0 initial CredentialType objects")
    CredentialType.setup_tower_managed_defaults()
    total = CredentialType.objects.count()
    if total <= 0:
        pytest.fail("Expected CredentialType objects after setup")