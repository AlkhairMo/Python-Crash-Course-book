import sandwiches_functions

sandwiches_functions.sandwich('flafl', 'ketchup', 'cheese')

from sandwiches_functions import sandwich
sandwich('flafl')

from sandwiches_functions import sandwich as sw
sw('flafl', 'ketchup')

import sandwiches_functions as sf
sf.sandwich('kofta', 'tomato', 'onion')

from sandwiches_functions import *
sandwich('egg', 'tomato')
