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

import logging

import torch
import numpy as np
from lib.transforms.transforms import (
    ConcatenateROId,
    GaussianSmoothedCentroidd,
    GetCentroidsd,
    SelectVertebraAndCroppingd,
)
from monai.handlers import TensorBoardImageHandler, from_engine, confusion_matrix
from monai.inferers import SimpleInferer
from monai.losses import DiceCELoss
from monai.transforms import (
    Activationsd,
    AsDiscreted,
    EnsureChannelFirstd,
    EnsureTyped,
    GaussianSmoothd,
    LoadImaged,
    RandScaleIntensityd,
    RandShiftIntensityd,
    Resized,
    ScaleIntensityd,
    ScaleIntensityRanged,
    SelectItemsd,
    ToNumpyd
)

from monailabel.tasks.train.basic_train import BasicTrainTask, Context
from monailabel.tasks.train.utils import region_wise_metrics

logger = logging.getLogger(__name__)


class Mednist(BasicTrainTask):
    def __init__(
        self,
        model_dir,
        network,
        description="Train MedNIST classifier model",
        **kwargs,
    ):
        self._network = network
        super().__init__(model_dir, description, **kwargs)

    def network(self, context: Context):
        return self._network

    def optimizer(self, context: Context):
        return torch.optim.AdamW(context.network.parameters(), lr=1e-4, weight_decay=1e-5)

    def loss_function(self, context: Context):
        # return DiceCELoss(to_onehot_y=True, softmax=True)
        return torch.nn.CrossEntropyLoss()

    def lr_scheduler_handler(self, context: Context):
        return None

    def train_data_loader(self, context, num_workers=0, shuffle=False):
        print("Hello!")
        print('context: ', context)
        print('context device: ', context.device)
        print('context datalist: ', context.train_datalist)
        context.train_datalist = [
            {
                "image": "/home/kindersc/Documents/monai_label/MedNIST/CXR/000000.jpeg",
                "label": torch.tensor([0,0,1,0,0,0]).float()
            }
        ]
        # context.val_datalist = [
        #     {
        #         "image": "/home/kindersc/Documents/monai_label/MedNIST/CXR/000000.jpeg",
        #         "label": 2
        #     }
        # ]
        print('context datalist: ', context.train_datalist)
        dataloader = super().train_data_loader(context, num_workers, True)
        print('len: ', len(dataloader))
        return super().train_data_loader(context, num_workers, True)

    def train_pre_transforms(self, context: Context):
        return [
            LoadImaged(keys="image", image_only=True),
            EnsureChannelFirstd(keys="image"),
            ScaleIntensityd(keys="image"),
        ]

    def train_post_transforms(self, context: Context):
        # return [
        #     # ToNumpyd(keys="pred"),
        # ]
        return None

    def val_pre_transforms(self, context: Context):
        return [
            LoadImaged(keys="image", image_only=True),
            EnsureChannelFirstd(keys="image"),
            ScaleIntensityd(keys="image"),
        ]

    def val_inferer(self, context: Context):
        return SimpleInferer()
    
    def train_inferer(self, context: Context):
        return SimpleInferer()

    def train_key_metric(self, context: Context):
        # return {
        #     self.TRAIN_METRIC_MEAN_DICE: MeanDice(
        #         output_transform=from_engine(["pred", "label"]),
        #         include_background=False,
        #     )
        # }
        return {
            "acc": confusion_matrix.ConfusionMatrix(metric_name="accuracy", output_transform=from_engine(["pred", "label"]))
        }