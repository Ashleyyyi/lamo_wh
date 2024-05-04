class MyConfigs():

    data_folder = '/home/hoo/lamo/datasets/'
    test_data_folder = "/home/hoo/lamo/testdata/"
    model_name = "resnet" #Vgg ResNet152 myModel
    weights = "./checkpoints/"
    logs = "./logs/"
    example_folder = "./example/"
    freeze = True
    #
    epochs = 50
    batch_size = 16
    img_height = 369  # 227  #网络输入的高和宽
    img_width = 496  # 227
    num_classes = 3
    lr = 1e-2
    lr_decay = 1e-4
    weight_decay = 2e-4
    ratio = 0.2
config = MyConfigs()
