from .optimiser import Optimiser

from scipy.optimize import minimize as sp_minimize
from quop_mpi.__utils.__nlopt_wrap import minimize as nlopt_minimize




class ScipyOptimiser(Optimiser):
    default_kwargs = {
        "method" : "BFGS"
    }

    def optimiser(self, func, param, **kwargs):
        return(
            sp_minimize(func,
                        param,
                        **kwargs))


class NloptOptimiser(Optimiser):
    def optimiser(self, func, param, **kwargs):
        return(
            nlopt_minimize(func,
                           param,
                           **kwargs))


