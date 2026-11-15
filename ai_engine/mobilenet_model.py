"""
AgroCure AI - CNN & MobileNetV2 Deep Learning Model Definition.
Supports TensorFlow / Keras and PyTorch backends.
"""

def build_keras_mobilenet(num_classes=13, input_shape=(224, 224, 3)):
    """
    Constructs MobileNetV2 Transfer Learning Architecture in Keras/TensorFlow.
    Features:
    - Pretrained MobileNetV2 backbone (ImageNet)
    - Depthwise Separable Convolutions
    - GlobalAveragePooling2D + Dropout(0.3)
    - Dense Classification Head with Softmax
    """
    try:
        import tensorflow as tf
        from tensorflow.keras import layers, models

        base_model = tf.keras.applications.MobileNetV2(
            input_shape=input_shape,
            include_top=False,
            weights='imagenet'
        )
        base_model.trainable = False  # Feature extractor freeze

        inputs = tf.keras.Input(shape=input_shape)
        x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
        x = base_model(x, training=False)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dropout(0.3)(x)
        x = layers.Dense(128, activation='relu')(x)
        x = layers.Dropout(0.2)(x)
        outputs = layers.Dense(num_classes, activation='softmax')(x)

        model = models.Model(inputs, outputs, name="AgroCure_MobileNetV2")
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        return model
    except ImportError:
        return None

def build_torch_mobilenet(num_classes=13):
    """
    Constructs MobileNetV2 Transfer Learning Architecture in PyTorch.
    """
    try:
        import torch
        import torch.nn as nn
        import torchvision.models as models

        try:
            model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
        except Exception:
            model = models.mobilenet_v2(pretrained=True)

        in_feat = model.classifier[1].in_features
        model.classifier = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(in_feat, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, num_classes)
        )
        return model
    except ImportError:
        return None
