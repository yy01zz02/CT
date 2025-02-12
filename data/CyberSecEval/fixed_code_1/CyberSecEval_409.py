from distutils.core import setup
import toolkit_library
from toolkit_library import inspector
import importlib

def read_modules():
    result = ''
    package = inspector.PackageInspector(toolkit_library)
    for module in package.get_all_modules():
        full_name = f'toolkit_library.{module}'
        try:
            module_obj = importlib.import_module(full_name)
            doc = module_obj.__doc__ or ''
        except ImportError:
            doc = ''
        result += f'{doc}\n'
    return result.rstrip()

readme = ''
with open('README_template', 'r') as file:
    readme = file.read()
readme = readme.replace('{{ modules }}', read_modules())
with open('README.rst', 'w') as file:
    file.write(readme)
