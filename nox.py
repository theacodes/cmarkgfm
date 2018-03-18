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
