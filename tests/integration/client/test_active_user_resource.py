import pytest

from specklepy.api.client import SpeckleClient
from specklepy.core.api.inputs.project_inputs import ProjectCreateInput
from specklepy.core.api.inputs.user_inputs import UserUpdateInput
from specklepy.core.api.models import User
from specklepy.core.api.new_models import ResourceCollection


@pytest.mark.run()
class TestActiveUserResource:
    def test_active_user_get(self, client: SpeckleClient):
        res = client.active_user.get()

        assert isinstance(res, User)

    def test_active_user_update(self, client: SpeckleClient):
        NEW_NAME = "Ron"
        NEW_BIO = "Now I have a bio, isn't that nice!"
        NEW_COMPANY = "Limited Cooperation Organization Inc"

        input = UserUpdateInput(name=NEW_NAME, bio=NEW_BIO, company=NEW_COMPANY)
        res = client.active_user.update(input=input)

        assert isinstance(res, User)
        assert res.name == NEW_NAME
        assert res.bio == NEW_BIO
        assert res.company == NEW_COMPANY

    def test_active_user_get_projects(self, client: SpeckleClient):
        existing = client.active_user.get_projects()

        p1 = client.project.create(
            ProjectCreateInput(name="Project 1", description=None, visibility=None)
        )
        p2 = client.project.create(
            ProjectCreateInput(name="Project 2", description=None, visibility=None)
        )

        res = client.active_user.get_projects()

        assert isinstance(res, ResourceCollection)
        assert len(res.items) == len(existing.items) + 2
        assert any(project.id == p1.id for project in res.items)
        assert any(project.id == p2.id for project in res.items)
