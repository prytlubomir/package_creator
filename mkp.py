'''Create base for python package or packages in current directory'''

import os
import sys


class PackageCreator:
    '''Main class'''

    __invalid_characters: str = '*"/\\<>:|?.'
    __invalid_startsfrom: str = '-.'


    def make_packages(self, *names: str) -> None:
        '''Create multiple python packages'''
        self.validate_names(*names)

        for package_name in names:
            self.make_package(package_name)


    def make_package(self, package_name: str) -> None:
        '''Create python package'''
        try:
            os.mkdir(package_name)
            file = os.open(f'{package_name}/__init__.py', os.O_CREAT)
            os.close(file)

        except FileNotFoundError:
            print(f'Module with name {package_name} is impossible to create.')
        except FileExistsError:
            print(f'Module with name {package_name} allready exists.')


    def validate_names(self, *names: str) -> None:
        '''
        Validate all passed package names, and displays message, if invalid found
        '''
        invalid_names: list[str] = [name for name in names if not self.validate_name(name)]

        if invalid_names:
            self.__display_validation_message(invalid_names)
            sys.exit()


    def validate_name(self, name: str) -> bool:
        '''Validate package name'''
        if os.path.exists(name):
            return False

        start_symbol: bool = self.__check_start_symbol(name)
        full_name: bool    = self.__check_full_name(name)

        return start_symbol and full_name


    def __check_start_symbol(self, name: str) -> bool:
        '''Validate start symbol of package name'''
        for char in self.__invalid_startsfrom:
            if name[0] == char:
                return False
        return True


    def __check_full_name(self, name: str) -> bool:
        '''Check package name for invalid charaters'''
        for char in self.__invalid_characters:
            if char in name:
                return False
        return True


    def __display_validation_message(self, invalid_names: list[str]) -> None:
        '''Display message about failed package names validation'''
        print('Following package names are invalid:')
        print(', '.join(invalid_names))
        print('QUITING!')


    def get_invalid_characters(self) -> dict:
        '''Return dict with naming instruction'''
        return {
            'invalid' : self.__invalid_characters,
            'invalid_start' : self.__invalid_startsfrom
        }


    def print_invalid_characters(self) -> None:
        '''Print message with note about characters what you can't use'''
        print("You can not use following characters:", ", ".join(self.__invalid_characters))
        print("Also, you can't start your names from:", self.__invalid_startsfrom)




if __name__ == "__main__":
    package_names = sys.argv[1:]
    creator = PackageCreator()
    creator.make_packages(*package_names)
