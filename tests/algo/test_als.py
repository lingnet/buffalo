# -*- coding: utf-8 -*-
import unittest
from buffalo.misc import aux
from buffalo.algo.als import ALS
from buffalo.misc.log import set_log_level
from buffalo.algo.options import ALSOption

from .base import TestBase


class TestALS(TestBase):
    def test0_get_default_option(self):
        ALSOption().get_default_option()
        self.assertTrue(True)

    def test1_is_valid_option(self):
        opt = ALSOption().get_default_option()
        self.assertTrue(ALSOption().is_valid_option(opt))
        opt['save_best'] = 1
        self.assertRaises(RuntimeError, ALSOption().is_valid_option, opt)
        opt['save_best'] = False
        self.assertTrue(ALSOption().is_valid_option(opt))

    def test2_init_with_dict(self):
        set_log_level(3)
        opt = ALSOption().get_default_option()
        ALS(opt)
        self.assertTrue(True)

    def test3_init(self):
        opt = ALSOption().get_default_option()
        self._test3_init(ALS, opt)

    def test4_train(self):
        opt = ALSOption().get_default_option()
        opt.d = 20
        self._test4_train(ALS, opt)

    def test5_validation(self):
        opt = ALSOption().get_default_option()
        opt.d = 5
        opt.num_iters = 20
        opt.validation = aux.Option({'topk': 10})
        opt.tensorboard = aux.Option({'root': './tb',
                                      'name': 'als'})
        self._test5_validation(ALS, opt)

    def test6_topk(self):
        opt = ALSOption().get_default_option()
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})
        self._test6_topk(ALS, opt)

    def test7_train_ml_20m(self):
        opt = ALSOption().get_default_option()
        opt.num_workers = 8
        opt.validation = aux.Option({'topk': 10})
        self._test7_train_ml_20m(ALS, opt)

    def test8_serialization(self):
        opt = ALSOption().get_default_option()
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})
        self._test8_serialization(ALS, opt)

    def test9_compact_serialization(self):
        opt = ALSOption().get_default_option()
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})
        self._test9_compact_serialization(ALS, opt)

    def test10_fast_most_similar(self):
        opt = ALSOption().get_default_option()
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})
        self._test10_fast_most_similar(ALS, opt)

    def test11_train_ml_20m_on_gpu(self):
        opt = ALSOption().get_default_option()
        opt.num_workers = 8
        opt.d = 100
        opt.validation = aux.Option({'topk': 10})
        opt.compute_loss_on_training = True
        opt.accelerator = True
        opt.num_cg_max_iters = 3
        self._test7_train_ml_20m(ALS, opt)


if __name__ == '__main__':
    unittest.main()
