try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )

except ValueError:
    raise

from pacote1.modulo1 import variavel1
variavel2 = 'variavel 2'

print(variavel1)