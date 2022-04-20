"""This tests the log"""
import os

from click.testing import CliRunner

from app import create_log_folder, create_database

runner = CliRunner()


def test_create_log_folder():
    """This test log folder is created or not"""
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../app/logs')
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) is True


