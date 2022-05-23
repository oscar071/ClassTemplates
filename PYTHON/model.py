# ________________________________Instructions_________________________________
"""
                    VARIABLES
DAY:                        $DAY$, example -> 01
MONTH:                      $MONTH$, example -> jan
YEAR:                       $YEAR$, example -> 2021
CREDITS:                    $CREDITS$, example -> AvantZen
NAME_FILE:                  $NAME_FILE$, example -> worker
NAME_CLASS:                 $NAME_CLASS$, example -> Worker
PACKAGE_PARENT_CLASS:       $PACKAGE_PARENT_CLASS$, example -> sqlite3   
NAME_PARENT_CLASS:          $NAME_PARENT_CLASS$, example -> Cursor
CONST_CLASS:                $CONST_CLASS$, example -> pi
VALUE_CONST_CLASS           $VALUE_CONST_CLASS$, example = 3.1416 
VAR_CLASS:                  $VAR_CLASS$, example -> READ
VALUE_VAR_CLASS:            $VALUE_VAR_CLASS$, example -> 1
TYPE_VAR_CLASS:             $TYPE_VAR_CLASS$, example -> int
METHOD_CLASS:               $METHOD_CLASS$, example -> random
VALUE_PRINCIPAL:            $VALUE_PRINCIPAL$, example -> val
TYPE_VALUE_PRINCIPAL:       $TYPE_VALUE_PRINCIPAL$, example -> int
VALUE_SECONDARY:            $VALUE_SECONDARY$, example -> name
TYPE_VALUE_SECONDARY:       $TYPE_VALUE_SECONDARY$, example -> str
VALUE_SECONDARY_DEFAULT:    $VALUE_SECONDARY_DEFAULT$, example -> 'val'
METHOD_PRIVATE:             $METHOD_PRIVATE$, example -> delete_all
TYPE_METHOD_PRIVATE_RETURN: $TYPE_METHOD_PRIVATE_RETURN$, example -> bool
METHOD_PUBLIC:              $METHOD_PUBLIC$, example -> save_all
TYPE_METHOD_PUBLIC_RETURN:  $TYPE_METHOD_PUBLIC_RETURN$, example -> bool

                    PROCESS:
01.- Check all the class and delete this instructions
"""
# ________________________________Instructions_________________________________

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from $PACKAGE_PARENT_CLASS$ import $NAME_PARENT_CLASS$

__email__ = "oscarmtzp93@gmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martinez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "$MONTH$/$DAY$/$YEAR$"

__author__ = "Oscar Martinez"

__credits__ = "$CREDITS$"


class $NAME_CLASS$($NAME_PARENT_CLASS$):
    """Class description (DocString)"""

    # ____________________________Class attributes_____________________________

    _$CONST_CLASS$ = $VALUE_CONST_CLASS$
    $VAR_CLASS$ = $VALUE_VAR_CLASS$

    # ____________________________Class attributes_____________________________

    # ______________________________Class methods______________________________

    @classmethod
    def $METHOD_CLASS$(cls) -> $TYPE_VAR_CLASS$:
        """Method description  (DocString)"""
        return $NAME_CLASS$.$VAR_CLASS$

    # ______________________________Class methods______________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, $VALUE_PRINCIPAL$: $TYPE_VALUE_PRINCIPAL$, $VALUE_SECONDARY$: $TYPE_VALUE_SECONDARY$ = $VALUE_SECONDARY_DEFAULT$):
        """Method description  (DocString)"""
        super($NAME_PARENT_CLASS$, self).__init__()
        self.__$VALUE_PRINCIPAL$ = None
        self.__$VALUE_SECONDARY$ = None
        
        self.$VALUE_PRINCIPAL$ = $VALUE_PRINCIPAL$
        self.$VALUE_SECONDARY$ = $VALUE_SECONDARY$

    def __len__(self):
        """Method description  (DocString)
        return len(self.$VALUE_SECONDARY$)"""
        return len(self.$VALUE_SECONDARY$)

    def __str__(self):
        """Method description  (DocString)
        return str(self.$VALUE_SECONDARY$)"""
        return str(self.$VALUE_SECONDARY$)

    def __del__(self):
        """Method description  (DocString)
        del self.$VALUE_SECONDARY$"""
        del self.$VALUE_SECONDARY$

    # _____________________________Generic methods_____________________________

    # ____________________________Arithmetic methods___________________________

    def __add__(self, other):
        """Method description (DocString)"""
        return self.$VALUE_PRINCIPAL$ + other.$VALUE_PRINCIPAL$

    def __sub__(self, other):
        """Method description (DocString)"""
        return self.$VALUE_PRINCIPAL$ - other.$VALUE_PRINCIPAL$

    def __mul__(self, other):
        """Method description (DocString)"""
        return self.$VALUE_PRINCIPAL$ * other.$VALUE_PRINCIPAL$

    def __truediv__(self, other):
        """Method description (DocString)"""
        return self.$VALUE_PRINCIPAL$ / other.$VALUE_PRINCIPAL$

    # ____________________________Arithmetic methods___________________________

    # _____________________________Logical methods_____________________________

    def __lt__(self, other):
        """Method description (DocString)
        return self.$VALUE_PRINCIPAL$ < other.$VALUE_PRINCIPAL$"""
        return self.$VALUE_PRINCIPAL$ < other.$VALUE_PRINCIPAL$

    def __le__(self, other):
        """Method description (DocString)
        return self.$VALUE_PRINCIPAL$ <= other.$VALUE_PRINCIPAL$"""
        return self.$VALUE_PRINCIPAL$ <= other.$VALUE_PRINCIPAL$

    def __eq__(self, other):
        """Method description (DocString)
        return self.$VALUE_PRINCIPAL$ == other.$VALUE_PRINCIPAL$"""
        return self.$VALUE_PRINCIPAL$ == other.$VALUE_PRINCIPAL$

    # _____________________________Logical methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _________________________________Getters_________________________________

    @property
    def $VALUE_PRINCIPAL$(self) -> $TYPE_VALUE_PRINCIPAL$:
        """Method description (DocString)"""
        return self.__$VALUE_PRINCIPAL$

    @property
    def $VALUE_SECONDARY$(self) -> $TYPE_VALUE_SECONDARY$:
        """Method description (DocString)"""
        return self.__$VALUE_SECONDARY$

    # _________________________________Getters_________________________________

    # _________________________________Setters_________________________________

    @$VALUE_PRINCIPAL$.setter
    def $VALUE_PRINCIPAL$(self, $VALUE_PRINCIPAL$: $TYPE_VALUE_PRINCIPAL$):
        """Method description (DocString)"""
        self.__$VALUE_PRINCIPAL$ = $VALUE_PRINCIPAL$

    @$VALUE_SECONDARY$.setter
    def $VALUE_SECONDARY$(self, $VALUE_SECONDARY$: $TYPE_VALUE_SECONDARY$):
        """Method description (DocString)"""
        self.__$VALUE_SECONDARY$ = $VALUE_SECONDARY$

    # _________________________________Setters_________________________________

    # _____________________________Private methods_____________________________

    def __$METHOD_PRIVATE$(self) -> $TYPE_METHOD_PRIVATE_RETURN$:
        """Method description (DocString)
        >>> 2 + 3
        5
        """
        pass

    # _____________________________Private methods_____________________________

    # _____________________________Public methods______________________________

    def $METHOD_PUBLIC$(self) -> $TYPE_METHOD_PUBLIC_RETURN$:
        """Method description (DocString)
        >>> 2 + 3
        5
        """
        pass

    # _____________________________Public methods______________________________

    # ______________________________Inner classes______________________________

    class $NAME_CLASS$Error(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________


if __name__ == "__main__":
    import doctest
    doctest.testmod()
