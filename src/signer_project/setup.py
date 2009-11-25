try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='signer_project',
    version=0,
    description= '',
    author='',
    author_email='',
    include_package_data=True,
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['signer_project'],
    entry_points = """
    [console_scripts]
    signer_project_manage = signer_project.signer_project.wrappers:manage
    """


)
