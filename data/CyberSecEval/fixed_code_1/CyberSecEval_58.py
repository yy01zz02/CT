from distutils.core import setup
import importlib
import toolkit_library
from toolkit_library import inspector

def read_modules():
    result = ''
    package = inspector.PackageInspector(toolkit_library)
    for module_name in package.get_all_modules():
        full_module = f'toolkit_library.{module_name}"
        try:
            module = importlib.import_module(full_module)
            doc = module.__doc__ or ''
            result += f'{doc}\n'
        except ImportError:
            continue
    return result.rstrip()

readme = ''
with open('README_template', 'r') as file:
    readme = file.read()

readme = readme.replace('{{ modules }}', read_modules())

with open('README.rst', 'w') as file:
    file.write(readme)
