import unittest
import torch

from normflows.flows import Planar
from normflows.flows.flow_test import FlowTest


class PlanarTest(FlowTest):
    def test_normal_nsf(self):
        batch_size = 3
        for latent_size in [2, 5]:
            for act in ["tanh", "leaky_relu"]:
                with self.subTest(latent_size=latent_size, act=act):
                    flow = Planar((latent_size,), act=act)
                    inputs = torch.randn((batch_size, latent_size))
                    if act == "leaky_relu":
                        self.checkForwardInverse(flow, inputs)
                    else:
                        self.checkForward(flow, inputs)


if __name__ == "__main__":
    unittest.main()