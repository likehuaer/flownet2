# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:29:38 2016

@author: wakanawakana
"""

import sys
import subprocess
import flo2image

if __name__ == '__main__':
    if(sys.argv[0] < 4): print "usage model(s/ss/..) img0 img2 flo"
    model = sys.argv[1]
    if model == 's':
        prototxt = '../models/FlowNet2-s/FlowNet2-S_deploy.prototxt.template'
        weight = '../models/FlowNet2-s/FlowNet2-S_weights.caffemodel.h5'
    elif model == 'ss':
        prototxt = '../models/FlowNet2-ss/FlowNet2-ss_deploy.prototxt.template'
        weight = '../models/FlowNet2-ss/FlowNet2-ss_weights.caffemodel'
    elif model == 'c':
        prototxt = '../models/FlowNet2-c/FlowNet2-C_deploy.prototxt.template'
        weight = '../models/FlowNet2-c/FlowNet2-C_weights.caffemodel'
    elif model == 'cs':
        prototxt = '../models/FlowNet2-cs/FlowNet2-CS_deploy.prototxt.template'
        weight = '../models/FlowNet2-cs/FlowNet2-CS_weights.caffemodel'
    elif model == 'css':
        prototxt = '../models/FlowNet2-css/FlowNet2-CSS_deploy.prototxt.template'
        weight = '../models/FlowNet2-css/FlowNet2-CSS_weights.caffemodel.h5'
    elif model == 'css-ft-sd':
        prototxt = '../models/FlowNet2-css-ft-sd/FlowNet2-CSS-ft-sd_deploy.prototxt.template'
        weight = '../models/FlowNet2-css-ft-sd/FlowNet2-CSS-ft-sd_weights.caffemodel.h5'
    elif model == 'kitti':
        prototxt = '../models/FlowNet2-kitti/FlowNet2-KITTI_deploy.prototxt.template'
        weight = '../models/FlowNet2-kitti/FlowNet2-KITTI_weights.caffemodel.h5'
    elif model == 'sd':
        prototxt = '../models/FlowNet2-SD/FlowNet2-SD_deploy.prototxt.template'
        weight = '../models/FlowNet2-SD/FlowNet2-SD_weights.caffemodel.h5'
    elif model == 'sintel':
        prototxt = '../models/FlowNet2-Sintel/FlowNet2-CSS-Sintel_deploy.prototxt.template'
        weight = '../models/FlowNet2-Sintel/FlowNet2-CSS-Sintel_weights.caffemodel.h5'
    else:
        prototxt = '../models/FlowNet2/FlowNet2_deploy.prototxt.template'
        weight = '../models/FlowNet2/FlowNet2_weights.caffemodel.h5'
    img0 = sys.argv[2]
    img1 = sys.argv[3]
    flo_out = sys.argv[4]
    cmd = 'python run-flownet.py {0} {1} {2} {3} {4}'.format(weight, prototxt, img0, img1, flo_out)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        line = proc.stdout.readline()
        sys.stdout.write(line)
#        log.write(line)
        if proc.poll() is not None:
            break
    flo2image.flo_image(flo_out)
    