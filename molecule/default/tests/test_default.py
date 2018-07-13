import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_added_package(host):
    assert host.package("git").is_installed is True
    assert host.package("zip").is_installed is True


def test_removed_package(host):
    # assert host.package("net-tools").is_installed is True
    pass
