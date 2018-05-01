# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 10:30:11 2016

@author: 10008777
"""

import sys
import subprocess
import cv2
import shutil
from math import ceil

def get_image_size(filename):
    dim_list = [int(dimstr) for dimstr in str(subprocess.check_output([FlowNet.img_size_bin, filename])).split(',')]
    if not len(dim_list) == 2:
        print('Could not determine size of image %s' % filename)
        sys.exit(1)
    return dim_list


if __name__ == '__main__':
#    if(sys.argv[0] < 3)
    caffe_bin = '../Build/x64/Release/caffe.exe'
    proto_file = '../models\FlowNet2-c/FlowNet2-C_deploy.prototxt'
    tmp_proto_file = '../models\FlowNet2-c/tmp_deploy.prototxt'
    weights_file = '../models\FlowNet2-c/FlowNet2-C_weights.caffemodel'
    img0 = ''
    image = cv2.imread(img0)
    height, width = image.shape[:2]

    vars = {}
    vars['TARGET_WIDTH'] = width
    vars['TARGET_HEIGHT'] = height

    divisor = 64.
    vars['ADAPTED_WIDTH'] = int(ceil(width/divisor) * divisor)
    vars['ADAPTED_HEIGHT'] = int(ceil(height/divisor) * divisor)

    vars['SCALE_WIDTH'] = width / float(vars['ADAPTED_WIDTH']);
    vars['SCALE_HEIGHT'] = height / float(vars['ADAPTED_HEIGHT']);

    tmp = open(tmp_proto_file, 'w')

    proto = open(proto_file).readlines()
    for line in proto:
        for key, value in vars.items():
            tag = "$%s$" % key
            line = line.replace(tag, str(value))

        tmp.write(line)

    tmp.flush()


    flo = 'flownet2c-pred-0000000.flo'
    cmd = '{0} test -model {1} -weights {2} -iterations 1 -gpu 0'.format(caffe_bin, tmp_proto_file, weights_file)
    subprocess.call(cmd)

