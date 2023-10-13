# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Callable, Sequence, Union

from monai.apps.deepedit.transforms import (
    AddGuidanceFromPointsDeepEditd,
    AddGuidanceSignalDeepEditd,
    DiscardAddGuidanced,
    ResizeGuidanceMultipleLabelDeepEditd,
)
from monai.inferers import Inferer, SimpleInferer
from monai.transforms import (
    Activationsd,
    AsDiscreted,
    EnsureChannelFirstd,
    EnsureTyped,
    LoadImaged,
    Orientationd,
    Resized,
    ScaleIntensityd,
    ScaleIntensityRanged,
    SqueezeDimd,
    ToNumpyd,
)

from monailabel.interfaces.tasks.infer_v2 import InferType
from monailabel.tasks.infer.basic_infer import BasicInferTask
from monailabel.transform.post import Restored


class Mednist(BasicInferTask):
    """
    This provides Inference Engine for pre-trained model over Multi Atlas Labeling Beyond The Cranial Vault (BTCV)
    dataset.
    """

    def __init__(
        self,
        path,
        network=None,
        type=InferType.CLASSIFICATION,
        labels=None,
        dimension=2,
        description="Mednist description",
        **kwargs,
    ):
        super().__init__(
            path=path,
            network=network,
            type=type,
            labels=labels,
            dimension=dimension,
            description=description,
            **kwargs,
        )

    def pre_transforms(self, data=None):
        t = []
        add_cache = False # may not be used

        t.extend(
            [
                LoadImaged(keys="image", image_only=True),
                EnsureChannelFirstd(keys="image"),
                ScaleIntensityd(keys="image"),
            ]
        )
        return t

    def inferer(self, data=None) -> Inferer:
        return SimpleInferer()

    def post_transforms(self, data=None) -> Sequence[Callable]:
        # return [
        #     EnsureTyped(keys="pred", device=data.get("device") if data else None),
        #     Activationsd(keys="pred", softmax=True),
        #     AsDiscreted(keys="pred", argmax=True),
        #     SqueezeDimd(keys="pred", dim=0),
        #     ToNumpyd(keys="pred"),
        #     Restored(keys="pred", ref_image="image"),
        # ]
        return []