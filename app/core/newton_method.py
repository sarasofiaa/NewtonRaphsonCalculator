import sympy as sp


class NewtonRaphsonMethod:

    @staticmethod
    def solve(expression, x0, tolerance):

        x = sp.symbols('x')

        derivative_expr = sp.diff(expression, x)

        f = sp.lambdify(x, expression, "numpy")

        df = sp.lambdify(x, derivative_expr, "numpy")

        data = []

        xn = x0

        root = xn

        for i in range(50):

            fxn = f(xn)

            dfxn = df(xn)

            if dfxn == 0:

                raise Exception(
                    "La derivada es cero."
                )

            xn1 = xn - (fxn / dfxn)

            error = abs(xn1 - xn)

            data.append([
                i,
                round(xn, 6),
                round(fxn, 6),
                round(error, 6)
            ])

            root = xn1

            if error < tolerance:
                break

            xn = xn1

        return {
            "root": round(root, 6),
            "derivative": derivative_expr,
            "iterations": data,
            "function_numeric": f,
            "expression": expression,
        }