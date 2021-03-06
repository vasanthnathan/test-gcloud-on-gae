# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

import six

from cryptography import utils
from cryptography.hazmat.primitives import interfaces


@utils.register_interface(interfaces.AsymmetricPadding)
class PKCS1v15(object):
    name = "EMSA-PKCS1-v1_5"


@utils.register_interface(interfaces.AsymmetricPadding)
class PSS(object):
    MAX_LENGTH = object()
    name = "EMSA-PSS"

    def __init__(self, mgf, salt_length):
        self._mgf = mgf

        if (not isinstance(salt_length, six.integer_types) and
                salt_length is not self.MAX_LENGTH):
            raise TypeError("salt_length must be an integer.")

        if salt_length is not self.MAX_LENGTH and salt_length < 0:
            raise ValueError("salt_length must be zero or greater.")

        self._salt_length = salt_length


@utils.register_interface(interfaces.AsymmetricPadding)
class OAEP(object):
    name = "EME-OAEP"

    def __init__(self, mgf, algorithm, label):
        if not isinstance(algorithm, interfaces.HashAlgorithm):
            raise TypeError("Expected instance of interfaces.HashAlgorithm.")

        self._mgf = mgf
        self._algorithm = algorithm
        self._label = label


class MGF1(object):
    MAX_LENGTH = object()

    def __init__(self, algorithm):
        if not isinstance(algorithm, interfaces.HashAlgorithm):
            raise TypeError("Expected instance of interfaces.HashAlgorithm.")

        self._algorithm = algorithm
