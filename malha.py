from os.path import splitext

from scripts.conf import Context
from scripts.fetcher import Fetcher
from scripts.sql import SQLEngine
from scripts.utils.loader import Loader

class Workflow():
    def __init__(self):
        ctx = Context()
        self.sqlengine = SQLEngine(ctx)
        self.loader = Loader(ctx, self.sqlengine)

        for step in ctx.steps.keys():
            for dep in ctx.steps[step] .keys():
                self.run(ctx, dep)
            self.run(ctx, step)

    def run(self, ctx, identity):
        basename, specification =  splitext(identity)

        if specification == '.extract':
            Fetcher(ctx, basename)
            # ctx.run[identity]

        elif specification == '.load':
            self.loader.execute(basename)
            # ctx.run[identity]

        elif specification == '.sql':
            self.sqlengine.execute(basename)
            # ctx.run[identity]

if __name__ == "__main__":
    Workflow()