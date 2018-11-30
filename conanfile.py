#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostCycleGroupAGroupConan(base.BoostBaseConan):
    name = "boost_cycle_group_a" # Level 11
    url = "https://github.com/bincrafters/conan-boost_cycle_group_a"
    lib_short_names = [
        "algorithm",
        "range"
    ]
    header_only_libs = [
        "algorithm",
        "range"
    ]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_bind",
        "boost_concept_check",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_detail",
        "boost_exception",
        "boost_function",
        "boost_iterator",
        "boost_mpl",
        "boost_numeric_conversion",
        "boost_optional",
        "boost_preprocessor",
        "boost_regex",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits",
        "boost_unordered",
        "boost_utility"
    ]
