import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_http_block(host):
    out = host.run('curl -f -I http://www.openmicroscopy.org')
    assert out.rc == 7
    assert 'Connection refused' in out.stderr


def test_https_allow(host):
    out = host.check_output('curl -f -I https://www.openmicroscopy.org')
    assert 'HTTP/1.1 200' in out
