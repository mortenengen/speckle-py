from typing import Optional

from specklepy.core.api.inputs.model_inputs import (
    CreateModelInput,
    DeleteModelInput,
    ModelVersionsFilter,
    UpdateModelInput,
)
from specklepy.core.api.inputs.project_inputs import ProjectModelsFilter
from specklepy.core.api.new_models import Model, ModelWithVersions, ResourceCollection
from specklepy.core.api.resources.model_resource import ModelResource as CoreResource


class ModelResource(CoreResource):
    def __init__(self, account, basepath, client, server_version) -> None:
        super().__init__(
            account=account,
            basepath=basepath,
            client=client,
            server_version=server_version,
        )

    def get(self, model_id: str, project_id: str) -> Model:
        return super().get(model_id, project_id)

    def get_with_versions(
        self,
        model_id: str,
        project_id: str,
        *,
        versions_limit: int = 25,
        versions_cursor: Optional[str] = None,
        versions_filter: Optional[ModelVersionsFilter] = None,
    ) -> ModelWithVersions:
        return super().get_with_versions(
            model_id,
            project_id,
            versions_limit=versions_limit,
            versions_cursor=versions_cursor,
            versions_filter=versions_filter,
        )

    def get_models(
        self,
        project_id: str,
        *,
        models_limit: int = 25,
        models_cursor: Optional[str] = None,
        models_filter: Optional[ProjectModelsFilter] = None,
    ) -> ResourceCollection[Model]:
        return super().get_models(
            project_id,
            models_limit=models_limit,
            models_cursor=models_cursor,
            models_filter=models_filter,
        )

    def create(self, input: CreateModelInput) -> Model:
        return super().create(input)

    def delete(self, input: DeleteModelInput) -> bool:
        return super().delete(input)

    def update(self, input: UpdateModelInput) -> Model:
        return super().update(input)
