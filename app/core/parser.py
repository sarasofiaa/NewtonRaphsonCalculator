from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)


class FunctionParser:

    @staticmethod
    def parse_expression(expression: str):

        try:

            expression = expression.replace(" ", "")

            expression = expression.replace("^", "**")

            transformations = (
                standard_transformations
                + (implicit_multiplication_application,)
            )

            parsed_expression = parse_expr(
                expression,
                transformations=transformations
            )

            return parsed_expression

        except Exception as error:

            raise ValueError(
                f"Función inválida:\n{error}"
            )