class Optimiser():
    optimiser = None
    default_kwargs = {}
    
    def __init__(self, **kwargs):
        self.default_kwargs.update(kwargs)
        self.kwargs = self.default_kwargs


    def __call__(self, func, param):
        self.objective = func

        if self.optimiser==None:
            raise Exception("Undefined optimiser method.")
        return self.optimiser(self.objective, param, **self.kwargs)
