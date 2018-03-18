import os
import shutil

import nox


@nox.session
@nox.parametrize('py', ['2.7', '3.4', '3.5', '3.6'])
def unit(session, py):
    session.install('pytest', 'pytest-cov')
    session.install('.')
    session.run(
        'pytest',
        '--cov-report', '',
        '--cov', 'cmarkgfm',
        '--cov', 'tests',
        'tests', *session.posargs)
    # Use combine because we install the package, combine will collapse the
    # long path names into short ones because of the [paths] section in
    # .coveragerc
    session.run('coverage', 'combine', '.coverage')
    session.run('coverage', 'report', '--show-missing')


@nox.session
def lint(session):
    session.install('flake8', 'readme_renderer')
    session.run('flake8', 'cmarkgfm', 'tests')
    session.run('python', 'setup.py', 'check', '-m', '-r', '-s')


@nox.session
def regenerate(session):
    """Regenerates header files for cmark under ./generated."""
    session.virtualenv = False
    session.run(shutil.rmtree, 'build', ignore_errors=True)
    session.run(os.makedirs, 'build')
    session.chdir('build')
    session.run('cmake', '../third_party/cmark')
    session.run(shutil.copy, 'src/cmark_export.h', '../generated')
    session.run(shutil.copy, 'src/cmark_version.h', '../generated')
    session.run(shutil.copy, 'src/config.h', '../generated')
    session.run(
        shutil.copy, 'extensions/cmarkextensions_export.h', '../generated')
    session.chdir('..')
    session.run(shutil.rmtree, 'build')
