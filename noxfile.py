import os
import platform
import shutil

import nox


@nox.session(py=['2.7', '2.7-32', '3.5', '3.6', '3.7', '3.8'])
def unit(session):
    session.install('pytest', 'pytest-cov')
    session.install('.')
    session.run(
        'pytest',
        '--cov-report', '',
        '--cov', 'cmarkgfm',
        '--cov', 'tests',
        'tests', *session.posargs)
    session.run('coverage', 'report', '--show-missing')


@nox.session
def lint(session):
    session.install('flake8', 'readme_renderer')
    session.run('flake8', 'cmarkgfm', 'tests')
    session.run('python', 'setup.py', 'check', '-m', '-r', '-s')


@nox.session(py=False)
def regenerate(session):
    """Regenerates header files for cmark under ./generated."""
    if platform.system() == 'Windows':
        output_dir = '../generated/windows'
    else:
        output_dir = '../generated/unix'

    session.run(shutil.rmtree, 'build', ignore_errors=True)
    session.run(os.makedirs, 'build')
    session.chdir('build')
    session.run('cmake', '../third_party/cmark')
    session.run(shutil.copy, 'src/cmark-gfm_export.h', output_dir)
    session.run(shutil.copy, 'src/cmark-gfm_version.h', output_dir)
    session.run(shutil.copy, 'src/config.h', output_dir)
    session.run(shutil.copy, 'extensions/cmark-gfm-extensions_export.h', output_dir)
    session.chdir('..')
    session.run(shutil.rmtree, 'build')
