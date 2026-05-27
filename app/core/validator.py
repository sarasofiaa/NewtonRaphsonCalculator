from sympy import diff
from sympy import Symbol


class FunctionValidator:

    @staticmethod
    def validate(expression):

        x = Symbol('x')

        if not expression.free_symbols:

            raise ValueError(
                "La función se simplificó a una constante."
            )

        try:

            derivative = diff(expression, x)

        except Exception:

            raise ValueError(
                "No se pudo derivar la función."
            )

        return derivative