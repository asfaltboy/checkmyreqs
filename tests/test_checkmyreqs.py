#!/usr/bin/env python
# coding=utf-8

"""
Tests for the checkmyreqs package
"""
import os

import unittest
from checkmyreqs import parse_requirements_file

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class TestRequirementFileParserTestCases(unittest.TestCase):
    """
    Test cases for parsing requirements files into packages
    """

    def test_empty_file(self):
        """
        Test that script works with an empty requirements file
        """
        with open(os.path.join(BASE_PATH, 'files/requirements_empty.txt')) as f:
            packages, index = parse_requirements_file(f)

        self.assertIsNone(index)
        self.assertEqual(len(packages), 0)

    def test_file_with_comments(self):
        """
        Test that a requirements file with comments does not throw errors
        """
        with open(os.path.join(BASE_PATH, 'files/requirements_comments.txt')) as f:
            packages, index = parse_requirements_file(f)

        # The file has one package, Django
        self.assertIsNone(index)
        self.assertEqual(len(packages), 1)

    def test_file_with_repo_links(self):
        """
        Test that repository links are skipped
        """
        with open(os.path.join(BASE_PATH, 'files/requirements_repos.txt')) as f:
            packages, index = parse_requirements_file(f)

        # packages should only include the gitconfig package
        self.assertIsNone(index)
        self.assertEqual(len(packages), 1)

    def test_file_with_no_version(self):
        """
        Check a package with no version, should skip
        """
        with open(os.path.join(BASE_PATH, 'files/requirements_unpinned.txt')) as f:
            packages, index = parse_requirements_file(f)

        self.assertIsNone(index)
        self.assertEqual(len(packages), 0)

    def test_file_with_custom_index(self):
        """
        Test that a requirements file with a custom package index (private
        cheeseshop)
        """
        with open(os.path.join(BASE_PATH, 'files/requirements_custom_index.txt')) as f:
            packages, index = parse_requirements_file(f)

        self.assertEquals(index, 'http://pypi-cheeseshop-index/simple')
        self.assertEqual(len(packages), 1)


class TestCheckPackageTestCases(unittest.TestCase):
    """
    Test cases for checking a package
    """
    #TODO: write test cases for the package lookup

if __name__ == '__main__':
    unittest.main()
