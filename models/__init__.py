import os
import time
from pathlib import Path

import torch
import torch.nn as nn
import models.layers as layers
# import models.alexnet as alexnet
# import models.vggnet as vgg
# import models.prevggnet as prevgg
import models.resnet as resnet
import models.preresnet as preresnet
# import models.resnext as resnext
# import models.wideresnet as wideresnet
# import models.seresnet as seresnet
# import models.cbamresnet as cbamresnet
# import models.vit as vit
# import models.pit as pit
# import models.mixer as mixer

import ops.meters as meters


def get_model(name, num_classes=10, stem=False, verbose=True, **block_kwargs):
    # AlexNet
    if name in ["alexnet_dnn"]:
        model = alexnet.dnn(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["alexnet_mcdo"]:
        model = alexnet.mcdo(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["alexnet_dnn_smoothing"]:
        model = alexnet.dnn_smooth(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["alexnet_mcdo_smoothing"]:
        model = alexnet.mcdo_smooth(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    # VGG
    elif name in ["vgg_dnn_11"]:
        model = vgg.dnn_11(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_mcdo_11"]:
        model = vgg.mcdo_11(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_dnn_smoothing_11"]:
        model = vgg.dnn_smooth_11(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_mcdo_smoothing_11"]:
        model = vgg.mcdo_smooth_11(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_dnn_13"]:
        model = vgg.dnn_13(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_mcdo_13"]:
        model = vgg.mcdo_13(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_dnn_smoothing_13"]:
        model = vgg.dnn_smooth_13(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_mcdo_smoothing_13"]:
        model = vgg.mcdo_smooth_13(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_dnn_16"]:
        model = vgg.dnn_16(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_mcdo_16"]:
        model = vgg.mcdo_16(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_dnn_smoothing_16"]:
        model = vgg.dnn_smooth_16(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_mcdo_smoothing_16"]:
        model = vgg.mcdo_smooth_16(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_dnn_19"]:
        model = vgg.dnn_19(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_mcdo_19"]:
        model = vgg.mcdo_19(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_dnn_smoothing_19"]:
        model = vgg.dnn_smooth_19(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vgg_mcdo_smoothing_19"]:
        model = vgg.mcdo_smooth_19(num_classes=num_classes, name=name, **block_kwargs)
    # PreAct VGG
    elif name in ["prevgg_dnn_11"]:
        model = prevgg.dnn_11(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_mcdo_11"]:
        model = prevgg.mcdo_11(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_dnn_smoothing_11"]:
        model = prevgg.dnn_smooth_11(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_mcdo_smoothing_11"]:
        model = prevgg.mcdo_smooth_11(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_dnn_13"]:
        model = prevgg.dnn_13(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_mcdo_13"]:
        model = prevgg.mcdo_13(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_dnn_smoothing_13"]:
        model = prevgg.dnn_smooth_13(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_mcdo_smoothing_13"]:
        model = prevgg.mcdo_smooth_13(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_dnn_16"]:
        model = prevgg.dnn_16(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_mcdo_16"]:
        model = prevgg.mcdo_16(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_dnn_smoothing_16"]:
        model = prevgg.dnn_smooth_16(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_mcdo_smoothing_16"]:
        model = prevgg.mcdo_smooth_16(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_dnn_19"]:
        model = prevgg.dnn_19(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_mcdo_19"]:
        model = prevgg.mcdo_19(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_dnn_smoothing_19"]:
        model = prevgg.dnn_smooth_19(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["prevgg_mcdo_smoothing_19"]:
        model = prevgg.mcdo_smooth_19(num_classes=num_classes, name=name, **block_kwargs)
    # ResNet
    elif name in ["resnet_dnn_18"]:
        model = resnet.dnn_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_18"]:
        model = resnet.mcdo_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_dnn_smoothing_18"]:
        model = resnet.dnn_smooth_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_smoothing_18"]:
        model = resnet.mcdo_smooth_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_dnn_34"]:
        model = resnet.dnn_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_34"]:
        model = resnet.mcdo_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_dnn_smoothing_34"]:
        model = resnet.dnn_smooth_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_smoothing_34"]:
        model = resnet.mcdo_smooth_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_dnn_50"]:
        model = resnet.dnn_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_50"]:
        model = resnet.mcdo_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_dnn_smoothing_50"]:
        model = resnet.dnn_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_smoothing_50"]:
        model = resnet.mcdo_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_dnn_101"]:
        model = resnet.dnn_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_101"]:
        model = resnet.mcdo_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_dnn_smoothing_101"]:
        model = resnet.dnn_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_smoothing_101"]:
        model = resnet.mcdo_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_dnn_152"]:
        model = resnet.dnn_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_152"]:
        model = resnet.mcdo_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_dnn_smoothing_152"]:
        model = resnet.dnn_smooth_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnet_mcdo_smoothing_152"]:
        model = resnet.mcdo_smooth_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    # PreAct ResNet
    elif name in ["preresnet_dnn_18"]:
        model = preresnet.dnn_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_18"]:
        model = preresnet.mcdo_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_dnn_smoothing_18"]:
        model = preresnet.dnn_smooth_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_smoothing_18"]:
        model = preresnet.mcdo_smooth_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_dnn_34"]:
        model = preresnet.dnn_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_34"]:
        model = preresnet.mcdo_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_dnn_smoothing_34"]:
        model = preresnet.dnn_smooth_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_smoothing_34"]:
        model = preresnet.mcdo_smooth_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_dnn_50"]:
        model = preresnet.dnn_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_50"]:
        model = preresnet.mcdo_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_dnn_smoothing_50"]:
        model = preresnet.dnn_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_smoothing_50"]:
        model = preresnet.mcdo_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_dnn_101"]:
        model = preresnet.dnn_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_101"]:
        model = preresnet.mcdo_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_dnn_smoothing_101"]:
        model = preresnet.dnn_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_smoothing_101"]:
        model = preresnet.mcdo_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_dnn_152"]:
        model = preresnet.dnn_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_152"]:
        model = preresnet.mcdo_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_dnn_smoothing_152"]:
        model = preresnet.dnn_smooth_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["preresnet_mcdo_smoothing_152"]:
        model = preresnet.mcdo_smooth_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    # ResNeXt
    elif name in ["resnext_dnn_50"]:
        model = resnext.dnn_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnext_mcdo_50"]:
        model = resnext.mcdo_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnext_dnn_smoothing_50"]:
        model = resnext.dnn_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnext_mcdo_smoothing_50"]:
        model = resnext.mcdo_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnext_dnn_101"]:
        model = resnext.dnn_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnext_mcdo_101"]:
        model = resnext.mcdo_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnext_dnn_smoothing_101"]:
        model = resnext.dnn_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["resnext_mcdo_smoothing_101"]:
        model = resnext.mcdo_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    # Wide ResNet
    elif name in ["wideresnet_dnn_50"]:
        model = wideresnet.dnn_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["wideresnet_mcdo_50"]:
        model = wideresnet.mcdo_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["wideresnet_dnn_smoothing_50"]:
        model = wideresnet.dnn_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["wideresnet_mcdo_smoothing_50"]:
        model = wideresnet.mcdo_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["wideresnet_dnn_101"]:
        model = wideresnet.dnn_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["wideresnet_mcdo_101"]:
        model = wideresnet.mcdo_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["wideresnet_dnn_smoothing_101"]:
        model = wideresnet.dnn_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["wideresnet_mcdo_smoothing_101"]:
        model = wideresnet.mcdo_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    # SE ResNet
    elif name in ["seresnet_dnn_18"]:
        model = seresnet.dnn_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_18"]:
        model = seresnet.mcdo_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_dnn_smoothing_18"]:
        model = seresnet.dnn_smooth_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_smoothing_18"]:
        model = seresnet.mcdo_smooth_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_dnn_34"]:
        model = seresnet.dnn_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_34"]:
        model = seresnet.mcdo_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_dnn_smoothing_34"]:
        model = seresnet.dnn_smooth_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_smoothing_34"]:
        model = seresnet.mcdo_smooth_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_dnn_50"]:
        model = seresnet.dnn_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_50"]:
        model = seresnet.mcdo_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_dnn_smoothing_50"]:
        model = seresnet.dnn_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_smoothing_50"]:
        model = seresnet.mcdo_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_dnn_101"]:
        model = seresnet.dnn_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_101"]:
        model = seresnet.mcdo_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_dnn_smoothing_101"]:
        model = seresnet.dnn_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_smoothing_101"]:
        model = seresnet.mcdo_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_dnn_152"]:
        model = seresnet.dnn_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_152"]:
        model = seresnet.mcdo_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_dnn_smoothing_152"]:
        model = seresnet.dnn_smooth_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["seresnet_mcdo_smoothing_152"]:
        model = seresnet.mcdo_smooth_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    # CBAM ResNet
    elif name in ["cbamresnet_dnn_18"]:
        model = cbamresnet.dnn_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_18"]:
        model = cbamresnet.mcdo_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_dnn_smoothing_18"]:
        model = cbamresnet.dnn_smooth_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_smoothing_18"]:
        model = cbamresnet.mcdo_smooth_18(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_dnn_34"]:
        model = cbamresnet.dnn_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_34"]:
        model = cbamresnet.mcdo_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_dnn_smoothing_34"]:
        model = cbamresnet.dnn_smooth_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_smoothing_34"]:
        model = cbamresnet.mcdo_smooth_34(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_dnn_50"]:
        model = cbamresnet.dnn_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_50"]:
        model = cbamresnet.mcdo_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_dnn_smoothing_50"]:
        model = cbamresnet.dnn_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_smoothing_50"]:
        model = cbamresnet.mcdo_smooth_50(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_dnn_101"]:
        model = cbamresnet.dnn_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_101"]:
        model = cbamresnet.mcdo_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_dnn_smoothing_101"]:
        model = cbamresnet.dnn_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_smoothing_101"]:
        model = cbamresnet.mcdo_smooth_101(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_dnn_152"]:
        model = cbamresnet.dnn_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_152"]:
        model = cbamresnet.mcdo_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_dnn_smoothing_152"]:
        model = cbamresnet.dnn_smooth_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    elif name in ["cbamresnet_mcdo_smoothing_152"]:
        model = cbamresnet.mcdo_smooth_152(num_classes=num_classes, stem=stem, name=name, **block_kwargs)
    # ViT
    elif name in ["vit_ti"]:
        model = vit.tiny(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vit_s"]:
        model = vit.small(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vit_b"]:
        model = vit.base(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vit_l"]:
        model = vit.large(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["vit_h"]:
        model = vit.huge(num_classes=num_classes, name=name, **block_kwargs)
    # PiT
    elif name in ["pit_ti"]:
        model = pit.tiny(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["pit_xs"]:
        model = pit.xsmall(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["pit_s"]:
        model = pit.small(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["pit_b"]:
        model = pit.base(num_classes=num_classes, name=name, **block_kwargs)
    # MLP Mixer
    elif name in ["mixer_ti"]:
        model = mixer.tiny(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["mixer_s"]:
        model = mixer.small(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["mixer_b"]:
        model = mixer.base(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["mixer_l"]:
        model = mixer.large(num_classes=num_classes, name=name, **block_kwargs)
    elif name in ["mixer_h"]:
        model = mixer.huge(num_classes=num_classes, name=name, **block_kwargs)
    else:
        raise NotImplementedError

    if verbose and "image_size" in block_kwargs:
        image_size = block_kwargs["image_size"]
        stats(model, torch.randn([3, 3, image_size, image_size]))
    elif verbose and stem:
        stats(model, torch.randn([3, 3, 224, 224]))
    elif verbose:
        stats(model, torch.randn([3, 3, 32, 32]))

    return model


def save(model, dataset_name, uid, optimizer=None, root="models_checkpoints"):
    checkpoint_path = os.path.join(root, dataset_name, model.name)
    fname = "%s_%s_%s.pth.tar" % (dataset_name, model.name, uid)
    save_path = os.path.join(checkpoint_path, fname)

    Path(checkpoint_path).mkdir(parents=True, exist_ok=True)
    _save(model, save_path, optimizer)


def save_snapshot(model, dataset_name, uid, typ, optimizer=None, root="models_checkpoints"):
    snapshot_path = os.path.join(root, dataset_name, model.name, "%s_%s_%s" % (dataset_name, model.name, uid))
    fname = "%s_%s_%s_%%s.pth.tar" % (dataset_name, model.name, uid)
    save_path = os.path.join(snapshot_path, fname)

    Path(snapshot_path).mkdir(parents=True, exist_ok=True)
    _save(model, save_path % typ, optimizer)


def _save(model, save_path, optimizer=None):
    save_obj = {
        "name": model.name,
        "state_dict": model.state_dict() if type(model) is not nn.DataParallel else model.module.state_dict(),
    }
    if optimizer is not None:
        save_obj["optimizer"] = optimizer.state_dict()
    torch.save(save_obj, save_path)


def load(model, dataset_name, uid, optimizer=None, root="models_checkpoints"):
    checkpoint_path = os.path.join(root, dataset_name, model.name)
    save_path = os.path.join(checkpoint_path, "%s_%s_%s.pth.tar" % (dataset_name, model.name, uid))
    _load(model, save_path, optimizer)


def load_snapshot(model, dataset_name, uid, typ, optimizer=None, root="models_checkpoints", ):
    snapshot_path = os.path.join(root, dataset_name, model.name, "%s_%s_%s" % (dataset_name, model.name, uid))
    fname = "%s_%s_%s_%%s.pth.tar" % (dataset_name, model.name, uid)
    save_path = os.path.join(snapshot_path, fname)

    _load(model, save_path % typ, optimizer)


def _load(model, save_path, optimizer=None):
    checkpoint = torch.load(save_path)
    model.load_state_dict(checkpoint["state_dict"])
    if optimizer is not None:
        optimizer.load_state_dict(checkpoint["optimizer"])


def stats(model, xs=None):
    stat_str = "model: %s , params: %.1fM" % (model.name, count_parameters(model) / 1e6)
    if xs is not None:
        model.eval()
        ys = model(xs)
        stat_str += ", output: %s" % list(ys.size())
    print(stat_str)


def count_parameters(model):
    return sum(param.numel() for param in model.parameters() if param.requires_grad)


def measure_executive_time(model, size=(1, 3, 32, 32), n=1000, gpu=True):
    model.eval()
    model = model.cuda() if gpu else model.cpu()
    meter = meters.AverageMeter("time")
    xs = [torch.normal(0, 1, size=size) for _ in range(n)]
    for x in xs:
        if gpu:
            x = x.cuda()

        t = time.time()
        _ = model(x)
        meter.update(time.time() - t)

    return meter.avg
